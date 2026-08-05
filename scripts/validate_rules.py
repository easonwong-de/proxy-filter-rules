#!/usr/bin/env python3
"""Validate rule syntax and paired Surge/Quantumult X rule sets."""

from __future__ import annotations

import argparse
import ipaddress
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


PAIR_STEMS = (
    "AI",
    "CDN_Direct",
    "ChinaBank",
    "Taobao",
    "TencentQQ",
    "WeChat",
    "Work_local_filter",
)

TYPE_ALIASES = {
    "HOST": "DOMAIN",
    "HOST-SUFFIX": "DOMAIN-SUFFIX",
    "HOST-KEYWORD": "DOMAIN-KEYWORD",
}

DOMAIN_TYPES = {
    "DOMAIN",
    "DOMAIN-SUFFIX",
    "DOMAIN-KEYWORD",
    "DOMAIN-WILDCARD",
    "HOST",
    "HOST-SUFFIX",
    "HOST-KEYWORD",
}
IP_TYPES = {"IP-CIDR", "IP-CIDR6", "IP6-CIDR"}
SIMPLE_TYPES = {"PROCESS-NAME", "USER-AGENT", "URL-REGEX"}
ALLOWED_TYPES = DOMAIN_TYPES | IP_TYPES | SIMPLE_TYPES | {"IP-ASN", "OR"}
DOMAIN_VALUE = re.compile(r"^[A-Za-z0-9_*?.+:-]+(?:\.[A-Za-z0-9_*?+:-]+)*$")


@dataclass(frozen=True)
class ValidationResult:
    files: int
    records: int
    errors: tuple[str, ...]


def _error(path: Path, line_number: int, message: str) -> str:
    return f"{path}:{line_number}: {message}"


def _validate_field_count(
    path: Path, line_number: int, fields: list[str], is_qx: bool
) -> str | None:
    rule_type = fields[0]
    count = len(fields)

    if rule_type == "OR":
        return None if count >= 2 else _error(path, line_number, "OR rule is empty")

    if is_qx:
        valid_counts = {3, 4} if rule_type in IP_TYPES | {"IP-ASN"} else {3}
    elif rule_type in IP_TYPES | {"IP-ASN"}:
        valid_counts = {2, 3}
    else:
        valid_counts = {2}

    if count not in valid_counts:
        expected = " or ".join(str(value) for value in sorted(valid_counts))
        return _error(
            path,
            line_number,
            f"{rule_type} has {count} fields; expected {expected}",
        )

    if count > 2 and not is_qx and fields[-1] != "no-resolve":
        return _error(path, line_number, "only no-resolve is allowed as a flag")
    if count == 4 and fields[-1] != "no-resolve":
        return _error(path, line_number, "fourth field must be no-resolve")
    return None


def _validate_value(
    path: Path, line_number: int, rule_type: str, value: str
) -> str | None:
    if rule_type in DOMAIN_TYPES:
        if not DOMAIN_VALUE.fullmatch(value):
            return _error(path, line_number, f"invalid domain value: {value!r}")
    elif rule_type in IP_TYPES:
        try:
            network = ipaddress.ip_network(value, strict=False)
        except ValueError:
            return _error(path, line_number, f"invalid CIDR: {value!r}")
        expected_version = 6 if rule_type in {"IP-CIDR6", "IP6-CIDR"} else 4
        if network.version != expected_version:
            return _error(
                path,
                line_number,
                f"{rule_type} requires IPv{expected_version}: {value!r}",
            )
    elif rule_type == "IP-ASN" and (not value.isdigit() or int(value) <= 0):
        return _error(path, line_number, f"invalid ASN: {value!r}")
    elif rule_type == "OR":
        if not (value.startswith("(") and value.endswith(")")):
            return _error(path, line_number, "OR expression must be parenthesized")
    elif not value:
        return _error(path, line_number, f"{rule_type} value is empty")
    return None


def _read_active_lines(path: Path) -> tuple[list[tuple[int, str]], list[str]]:
    errors: list[str] = []
    try:
        data = path.read_bytes()
        text = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        return [], [f"{path}: invalid UTF-8: {exc}"]

    if b"\x00" in data:
        errors.append(f"{path}: contains a NUL byte")

    active = [
        (line_number, line.strip())
        for line_number, line in enumerate(text.splitlines(), start=1)
        if line.strip() and not line.lstrip().startswith("#")
    ]
    return active, errors


def _validate_file(path: Path) -> tuple[int, list[str]]:
    active, errors = _read_active_lines(path)
    seen: dict[str, int] = {}
    is_qx = path.name.endswith(".qx.list")
    is_conf = path.suffix == ".conf"

    for line_number, line in active:
        if line in seen:
            errors.append(
                _error(path, line_number, f"duplicate of active line {seen[line]}")
            )
        else:
            seen[line] = line_number

        fields = [field.strip() for field in line.split(",")]
        if any(not field for field in fields):
            errors.append(_error(path, line_number, "record contains an empty field"))
            continue

        if len(fields) == 1 and is_conf:
            if any(character.isspace() for character in fields[0]):
                errors.append(_error(path, line_number, "domain-set entry contains whitespace"))
            continue

        rule_type = fields[0]
        if rule_type not in ALLOWED_TYPES:
            errors.append(_error(path, line_number, f"unsupported rule type: {rule_type}"))
            continue

        count_error = _validate_field_count(path, line_number, fields, is_qx)
        if count_error:
            errors.append(count_error)
            continue

        value = ",".join(fields[1:]) if rule_type == "OR" else fields[1]
        value_error = _validate_value(path, line_number, rule_type, value)
        if value_error:
            errors.append(value_error)

    return len(active), errors


def _normalized_pair(path: Path) -> tuple[Counter[tuple[str, str]], list[str]]:
    active, errors = _read_active_lines(path)
    normalized: Counter[tuple[str, str]] = Counter()
    for line_number, line in active:
        fields = [field.strip() for field in line.split(",")]
        if len(fields) < 2:
            errors.append(_error(path, line_number, "paired rule has fewer than two fields"))
            continue
        normalized[(TYPE_ALIASES.get(fields[0], fields[0]), fields[1])] += 1
    return normalized, errors


def validate_repository(root: Path) -> ValidationResult:
    rules_dir = root / "rules"
    paths = sorted((*rules_dir.glob("*.list"), *rules_dir.glob("*.conf")))
    errors: list[str] = []
    records = 0

    if not paths:
        return ValidationResult(0, 0, (f"{rules_dir}: no rule files found",))

    for path in paths:
        count, file_errors = _validate_file(path)
        records += count
        errors.extend(file_errors)

    for stem in PAIR_STEMS:
        surge_path = rules_dir / f"{stem}.list"
        qx_path = rules_dir / f"{stem}.qx.list"
        if not surge_path.is_file() or not qx_path.is_file():
            errors.append(f"missing paired files for {stem}")
            continue

        surge_rules, surge_errors = _normalized_pair(surge_path)
        qx_rules, qx_errors = _normalized_pair(qx_path)
        errors.extend(surge_errors)
        errors.extend(qx_errors)
        if surge_rules != qx_rules:
            only_surge = list((surge_rules - qx_rules).elements())[:3]
            only_qx = list((qx_rules - surge_rules).elements())[:3]
            errors.append(
                f"paired rules differ for {stem}: "
                f"Surge-only={only_surge}, Quantumult-X-only={only_qx}"
            )

    return ValidationResult(len(paths), records, tuple(errors))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="repository root (defaults to the parent of scripts/)",
    )
    args = parser.parse_args()
    result = validate_repository(args.root.resolve())
    if result.errors:
        for error in result.errors:
            print(error, file=sys.stderr)
        print(
            f"validation failed: {len(result.errors)} error(s)", file=sys.stderr
        )
        return 1

    print(f"validated {result.files} files and {result.records} active records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
