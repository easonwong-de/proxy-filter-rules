# Proxy Filter Rules

[![Validate rules](https://github.com/LceAn/proxy-filter-rules/actions/workflows/validate.yml/badge.svg)](https://github.com/LceAn/proxy-filter-rules/actions/workflows/validate.yml)
[![License](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](LICENSE)

面向 Surge 和 Quantumult X 的分流规则集合。仓库目前包含 59 个 `.list` 和 5 个上游 `.conf` 文件；使用前请按客户端和文件格式选择规则，不要假定所有文件可跨客户端直接使用。

## 使用方式

### Surge

未带 `.qx` 的自维护规则使用 Surge 规则集格式：

```ini
[Rule]
RULE-SET,https://raw.githubusercontent.com/LceAn/proxy-filter-rules/main/rules/AI.list,AI
RULE-SET,https://raw.githubusercontent.com/LceAn/proxy-filter-rules/main/rules/WeChat.list,WeChat
```

### Quantumult X

明确以 `.qx.list` 结尾的文件包含策略字段，可作为 Quantumult X 远程规则引用：

```ini
[filter_remote]
https://raw.githubusercontent.com/LceAn/proxy-filter-rules/main/rules/AI.qx.list, tag=AI, enabled=true
https://raw.githubusercontent.com/LceAn/proxy-filter-rules/main/rules/WeChat.qx.list, tag=WeChat, enabled=true
```

目前维护以下七组成对版本：

| 规则 | Surge | Quantumult X |
| --- | --- | --- |
| AI | `AI.list` | `AI.qx.list` |
| CDN direct | `CDN_Direct.list` | `CDN_Direct.qx.list` |
| China banks | `ChinaBank.list` | `ChinaBank.qx.list` |
| Taobao | `Taobao.list` | `Taobao.qx.list` |
| Tencent QQ | `TencentQQ.list` | `TencentQQ.qx.list` |
| WeChat | `WeChat.list` | `WeChat.qx.list` |
| Work local | `Work_local_filter.list` | `Work_local_filter.qx.list` |

其余 `.list` 主要是 Surge 格式或保留的上游格式。其他客户端可能只兼容其中一部分规则类型；本仓库不承诺 Clash、Loon 或 Shadowrocket 的完整兼容性。

## 校验

提交前运行：

```bash
python3 scripts/validate_rules.py
python3 -m unittest discover -s tests -v
```

校验器检查 UTF-8、NUL 字节、空字段、未知规则类型、字段数量、CIDR、ASN、同文件重复记录，以及七组成对规则在格式转换后的语义一致性。GitHub Actions 会在 push 和 pull request 时执行相同检查。

## 来源与维护

- 文件头标注 `blackmatrix7/ios_rule_script` 的规则来自对应上游项目。
- `rules/*.conf` 来自 Sukka's Ruleset，文件头保留来源、更新时间及 AGPL-3.0 声明。
- 自维护规则与上游数据可能随服务域名变化；更新时应保留来源说明并通过校验器。
- `Work_local_filter` 是工作环境专用规则。公开复用前请先确认其中的域名和网段适用于自己的环境。

旧仓库 `quantumultX_filter` 的内容已经迁入本仓库，提交和 SHA-256 证据见 [MIGRATIONS.md](MIGRATIONS.md)。该迁移关系不表示两个仍需并行维护的仓库。

## 许可证

仓库自有内容使用 [Apache License 2.0](LICENSE)。带独立来源或许可证头的第三方规则继续受各自声明约束，尤其是 `rules/*.conf` 中标注的 AGPL-3.0；根许可证不会覆盖或替代这些上游条款。

---

## 文档

- [CHANGELOG.md](CHANGELOG.md) — 更新日志
- [ROADMAP.md](ROADMAP.md) — 未来更新计划
- [MIGRATIONS.md](MIGRATIONS.md) — 规则迁移记录
