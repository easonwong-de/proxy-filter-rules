# 仓库迁移记录

## quantumultX_filter

- 旧仓库：`LceAn/quantumultX_filter`（GitHub 当前已不存在）
- 最后已知提交：`0576d2c3f353672ee95c693a9e961fd4c4706e45`
- 最后提交日期：2025-07-02
- 本地证据来源：2026-03-04 GitHub 仓库快照

2026-07-28 对旧仓库全部实质文件与本仓库做 SHA-256 比对：

| 旧文件 | 当前文件 | SHA-256 | 结果 |
| --- | --- | --- | --- |
| `AI.list` | `rules/AI.qx.list` | `6c185c383e86324278fe97f49b17a68b563dde893803dec085bc23f8ab4b191e` | 完全相同 |
| `WeChat.list` | `rules/WeChat.qx.list` | `7d5349fecabf5d1289b92e3ebd60103bb54569715291b58e7dd6cdfb317d5ce4` | 完全相同 |
| `Work_local_filter.list` | `rules/Work_local_filter.qx.list` | `74610e0b5e35dfada4e2dc188fbc99662e335483d1227cf54342d5d20210b7ef` | 完全相同 |
| `LICENSE` | `LICENSE` | `c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4` | 完全相同 |

当前仓库还保留持续演进的 Surge 格式版本和更多规则，因此旧仓库已被完全吸收。旧仓库不在当前 GitHub 账户中，无法执行归档；无需重新创建。

哈希证明的是迁移时内容一致。后续正常更新 `*.qx.list` 时哈希可以变化，不代表迁移失效；旧版本仍可通过上述提交和本地快照追溯。
