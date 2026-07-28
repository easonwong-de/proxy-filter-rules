# Proxy Filter Rules

[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](LICENSE)
[![Quantumult X](https://img.shields.io/badge/Quantumult%20X-Supported-007AFF?style=flat-square&logo=apple)](https://apps.apple.com/app/id1443988620)
[![Surge](https://img.shields.io/badge/Surge-Supported-FF6900?style=flat-square&logo=surge)](https://nssurge.com/)
[![Updates](https://img.shields.io/badge/Updates-On%20demand-green?style=flat-square)](https://github.com/LceAn/proxy-filter-rules/commits/main)
[![Stars](https://img.shields.io/github/stars/LceAn/proxy-filter-rules?style=flat-square)](https://github.com/LceAn/proxy-filter-rules/stargazers)
[![Issues](https://img.shields.io/github/issues/LceAn/proxy-filter-rules?style=flat-square)](https://github.com/LceAn/proxy-filter-rules/issues)

> 📦 适用于 Quantumult X / Surge 的分流规则集合 | Proxy Filter Rules for Quantumult X & Surge

---

## 📖 简介 | Introduction

本仓库收集了适用于 **Quantumult X** 和 **Surge** 的分流规则，帮助精准控制网络流量，提升上网体验。

**特点 | Features:**
- ✅ **双平台支持** — Quantumult X & Surge
- ✅ **精准分流** — 针对特定网站和服务的精细规则
- ✅ **持续更新** — 按需校验和更新规则
- ✅ **易于使用** — 一键订阅，自动更新
- ✅ **开源免费** — MIT 许可，完全免费使用

---

## 🚀 快速开始 | Quick Start

### Quantumult X

#### 远程订阅

在配置文件的 `[filter_remote]` 部分添加：

```ini
[filter_remote]
https://raw.githubusercontent.com/LceAn/proxy-filter-rules/main/rules/AI.qx.list, tag=🤖 AI 服务, enabled=true
https://raw.githubusercontent.com/LceAn/proxy-filter-rules/main/rules/WeChat.qx.list, tag=💬 微信, enabled=true
```

#### 本地引用

```ini
[filter_local]
include-filter=rules/AI.qx.list
include-filter=rules/WeChat.qx.list
```

### Surge

```ini
[Rule]
RULE-SET,https://raw.githubusercontent.com/LceAn/proxy-filter-rules/main/rules/AI.list,🤖 AI 服务
RULE-SET,https://raw.githubusercontent.com/LceAn/proxy-filter-rules/main/rules/WeChat.list,💬 微信
```

---

## 📁 目录结构 | Directory Structure

```
proxy-filter-rules/
├── rules/                  # 全部分流规则文件
├── README.md               # 本文件
└── LICENSE
```

旧仓库 `quantumultX_filter` 的三份规则已逐字节迁入对应 `*.qx.list`，迁移提交和 SHA-256 证据见 [`MIGRATIONS.md`](MIGRATIONS.md)。

---

## 📋 规则列表 | Rule Files

### 🤖 AI 服务

| 文件 | 说明 | 规则数 | 来源 |
|------|------|--------|------|
| AI.list | AI 服务（OpenAI/Claude/Gemini 等） | 50+ | 原创 |
| Claude.list | Claude / Anthropic | — | blackmatrix7 |
| Gemini.list | Google Gemini | — | blackmatrix7 |
| OpenAI.list | OpenAI / ChatGPT | — | blackmatrix7 |

### 💬 社交通讯

| 文件 | 说明 | 规则数 | 来源 |
|------|------|--------|------|
| WeChat.list | 微信国际版 | 60+ | 原创 |
| TencentQQ.list | QQ / 微信 / 腾讯社交 | 2500+ | 原创 |
| Telegram.list | Telegram | — | blackmatrix7 |
| Twitter.list | X / Twitter | — | blackmatrix7 |
| Weibo.list | 新浪微博 | — | blackmatrix7 |
| DingTalk.list | 钉钉 | — | blackmatrix7 |

### 🛒 购物支付

| 文件 | 说明 | 规则数 | 来源 |
|------|------|--------|------|
| Taobao.list | 淘宝 / 天猫 / 阿里系电商 | 1300+ | 原创 |
| ChinaBank.list | 中国银行服务（工建农中交招邮储平安光大） | 190+ | 原创 |
| AliPay.list | 支付宝 | — | blackmatrix7 |
| JingDong.list | 京东 | — | blackmatrix7 |
| Pinduoduo.list | 拼多多 | — | blackmatrix7 |
| PayPal.list | PayPal | — | blackmatrix7 |
| UnionPay.list | 银联 | — | blackmatrix7 |

### 🎬 流媒体

| 文件 | 说明 | 来源 |
|------|------|------|
| BiliBili.list | 哔哩哔哩 | blackmatrix7 |
| DouYin.list | 抖音 | blackmatrix7 |
| iQIYI.list | 爱奇艺 | blackmatrix7 |
| Netflix.list | Netflix | blackmatrix7 |
| Spotify.list | Spotify | blackmatrix7 |
| TencentVideo.list | 腾讯视频 | blackmatrix7 |
| YouTube.list | YouTube | blackmatrix7 |
| Youku.list | 优酷 | blackmatrix7 |
| Disney.list | Disney+ | blackmatrix7 |
| Himalaya.list | 喜马拉雅 | blackmatrix7 |
| XiaoHongShu.list | 小红书 | blackmatrix7 |
| Zhihu.list | 知乎 | blackmatrix7 |
| DouBan.list | 豆瓣 | blackmatrix7 |

### 💼 办公工具

| 文件 | 说明 | 来源 |
|------|------|------|
| Work_local_filter.list | 工作本地分流 | 原创 |
| Mail.list | 邮件服务 | blackmatrix7 |
| Microsoft.list | 微软服务 | blackmatrix7 |
| Google.list | Google 服务 | blackmatrix7 |
| Apple.list | Apple 服务 | blackmatrix7 |
| GitHub.list | GitHub | blackmatrix7 |
| GitLab.list | GitLab | blackmatrix7 |
| Kingsoft.list | 金山（WPS） | blackmatrix7 |
| Python.list | Python 相关 | blackmatrix7 |
| Docker.list | Docker | blackmatrix7 |
| BaiDuTieBa.list | 百度贴吧 | blackmatrix7 |

### 🎮 游戏

| 文件 | 说明 | 来源 |
|------|------|------|
| Steam.list | Steam | blackmatrix7 |
| Epic.list | Epic Games | blackmatrix7 |
| Nintendo.list | Nintendo | blackmatrix7 |
| PlayStation.list | PlayStation | blackmatrix7 |
| Xbox.list | Xbox | blackmatrix7 |

### 🌍 地区 & 其他

| 文件 | 说明 | 来源 |
|------|------|------|
| China.list | 中国大陆 | blackmatrix7 |
| 115.list | 115 网盘 | blackmatrix7 |

### ⚙️ 配置文件

| 文件 | 说明 |
|------|------|
| download.conf | 下载分流配置 |
| global.conf | 全局规则配置 |
| reject.conf | 广告拦截配置 |
| speedtest.conf | 测速分流配置 |
| telegram.conf | Telegram 专用配置 |

---

## ⚙️ 配置指南 | Configuration Guide

### Quantumult X

```ini
[filter_remote]
https://raw.githubusercontent.com/LceAn/proxy-filter-rules/main/rules/AI.qx.list, tag=🤖 AI 服务, enabled=true
https://raw.githubusercontent.com/LceAn/proxy-filter-rules/main/rules/WeChat.qx.list, tag=💬 微信, enabled=true
https://raw.githubusercontent.com/LceAn/proxy-filter-rules/main/rules/Telegram.list, tag=✈️ Telegram, enabled=true
https://raw.githubusercontent.com/LceAn/proxy-filter-rules/main/rules/YouTube.list, tag=📺 YouTube, enabled=true
```

### Surge

```ini
[Proxy Group]
🤖 AI 服务 = select, 美国节点, 主力高速, 节点选择
💬 微信 = select, 香港节点, 新加坡节点, DIRECT
✈️ Telegram = select, 美国节点, 香港节点, 节点选择

[Rule]
RULE-SET,https://raw.githubusercontent.com/LceAn/proxy-filter-rules/main/rules/AI.list,🤖 AI 服务
RULE-SET,https://raw.githubusercontent.com/LceAn/proxy-filter-rules/main/rules/WeChat.list,💬 微信
RULE-SET,https://raw.githubusercontent.com/LceAn/proxy-filter-rules/main/rules/Telegram.list,✈️ Telegram
```

---

## 🔧 常见问题 | FAQ

**Q: 规则不生效怎么办？**
1. 确认规则 URL 正确
2. 执行「刷新所有资源」
3. 重启代理工具
4. 检查策略组名称是否匹配

**Q: 如何更新规则？**
- 自动更新：代理工具会自动更新远程规则
- 手动更新：点击「刷新所有资源」

**Q: 支持其他代理工具吗？**
- ✅ Clash — 规则格式通用
- ✅ Shadowrocket — 部分兼容
- ✅ Loon — 部分兼容

---

## 📊 统计 | Statistics

| 指标 | 数值 |
|------|------|
| 规则文件 | 64 个 |
| 规则总数 | 4000+ 条 |
| 支持平台 | Quantumult X, Surge |
| 数据来源 | 原创 + blackmatrix7 + skk.moe |

---

## 🤝 贡献 | Contributing

欢迎提交新的分流规则或改进建议！

- **Issue**: https://github.com/LceAn/proxy-filter-rules/issues
- **Pull Request**: Fork → 修改 → 提交 PR

---

## 📄 许可证 | License

[MIT License](LICENSE)

---

<div align="center">

**🛡️ 持续更新中 · 欢迎 Star 支持**

Made with ❤️ by LceAn

</div>

---

<!-- repo-readme-standard:v1 -->
## 仓库维护信息

- 项目类型：资料/集合
- 当前状态：本轮已整理（2026-07-28）
- 可见性：public
- 维护节奏：按季度补索引、许可和去重证据
- 相关仓库：已记录 quantumultX_filter 规则迁移证据
- 维护边界：普通文档和代码更新可直接提交；归档、删除、历史重写或强制推送需单独确认。
