from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from scripts.validate_rules import PAIR_STEMS, validate_repository


class RuleValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.root = Path(self.temporary_directory.name)
        rules = self.root / "rules"
        rules.mkdir()
        for stem in PAIR_STEMS:
            (rules / f"{stem}.list").write_text(
                "DOMAIN-SUFFIX,example.com\n", encoding="utf-8"
            )
            (rules / f"{stem}.qx.list").write_text(
                "HOST-SUFFIX,example.com,Test\n", encoding="utf-8"
            )

    def write_rule(self, name: str, content: str) -> None:
        (self.root / "rules" / name).write_text(content, encoding="utf-8")

    def assert_has_error(self, fragment: str) -> None:
        result = validate_repository(self.root)
        self.assertTrue(
            any(fragment in error for error in result.errors),
            f"expected {fragment!r} in {result.errors!r}",
        )

    def test_valid_repository(self) -> None:
        result = validate_repository(self.root)
        self.assertEqual(result.errors, ())

    def test_rejects_unknown_rule_type(self) -> None:
        self.write_rule("extra.list", "NOT-A-RULE,example.com\n")
        self.assert_has_error("unsupported rule type")

    def test_rejects_duplicate_active_line(self) -> None:
        self.write_rule(
            "extra.list",
            "DOMAIN,example.com\n# comment\nDOMAIN,example.com\n",
        )
        self.assert_has_error("duplicate of active line")

    def test_rejects_malformed_cidr(self) -> None:
        self.write_rule("extra.list", "IP-CIDR,999.1.1.1/24\n")
        self.assert_has_error("invalid CIDR")

    def test_detects_pair_mismatch(self) -> None:
        self.write_rule("AI.qx.list", "HOST-SUFFIX,different.example,AI\n")
        self.assert_has_error("paired rules differ for AI")


if __name__ == "__main__":
    unittest.main()
