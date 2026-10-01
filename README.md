# 做视频每一步，该装哪个 Skill

做一条短视频分五步：选题、文案、配音字幕、画面、封面和复盘。这里把每一步能装的 Skill 和工具列成一张表，每一项都写了装法、对 AI 说的那句话，以及我们自己装上试过的结果。

Skill 就是装给 AI 的一份做事说明书（一个带 `SKILL.md` 的文件夹）。Claude Code、Codex、TRAE 等都支持这种格式，见 [agentskills.io](https://agentskills.io/)。

> 数字是 2026-10-01 采集的：GitHub 星数来自 GitHub API，下载量来自 ClawHub。它们每天在变，以链接里的页面为准。

## 怎么装

最简单的办法：跟你的 AI 说“帮我装这个 Skill”，后面贴上 GitHub 地址。

也可以用命令（需要 Node.js）：

```bash
npx skills add <作者>/<仓库>                     # 装整个仓库里的 Skill
npx skills add <作者>/<仓库> --skill <名字>       # 只装其中一个
npx skills add <作者>/<仓库> --list               # 先看看里面有哪些，不安装
```

Skill 本身免费。花钱的是运行它的 AI，以及它要调用的接口（比如云端大模型、素材库）。

## 一张表

| 步骤 | 名字 | 星数／下载（2026-10-01） | 许可 | 装法 | 对 AI 说 | 我们的结论 |
|---|---|---|---|---|---|---|
| 选题 | [content-strategy](https://github.com/coreyhaines31/marketingskills/tree/main/skills/content-strategy) | 仓库 5.2 万星 | MIT | `npx skills add coreyhaines31/marketingskills --skill content-strategy` | 帮我定一下接下来的内容方向 | 开工前先问：做什么生意、给谁看、手上有什么内容、能不能拍视频，再定内容支柱。一大半讲搜索关键词和博客，短视频拿它定方向就够 |
| 文案 | [humanizer](https://github.com/blader/humanizer) | 5.3 万星 | MIT | `npx skills add blader/humanizer` | 用 humanizer 改一下这段口播 | **实测**：中文口播初稿标出 8 处，改 6 处，按它自己的例外规则留 2 处（[记录](docs/humanizer-run.md)）。规则照英文写，说明书写明各语言同类句式一样处理 |
| 文案 | [copywriting](https://github.com/coreyhaines31/marketingskills/tree/main/skills/copywriting) | 仓库 5.2 万星 | MIT | `npx skills add coreyhaines31/marketingskills --skill copywriting` | — | 不是单独的仓库，是 marketingskills 50 个 Skill 里的一个。说明书第一句：给**网页**写营销文案（首页、落地页、定价页）。写短视频钩子用下一行的 social |
| 文案 | [social](https://github.com/coreyhaines31/marketingskills/tree/main/skills/social) | 仓库 5.2 万星 | MIT | `npx skills add coreyhaines31/marketingskills --skill social` | 给这条短视频写三个开头 | 说明书写着 short-form video、video hook。有一组钩子公式（数字、反常识、经历）。**实测**：本期开头用它的“数字＋反常识”写成（[记录](docs/social-hooks-run.md)） |
| 配音字幕 | [Whisper](https://github.com/openai/whisper) | 11 万星 | MIT | `pip install -U openai-whisper` | — | 工具，不是 Skill。我们用它把配音逐字对到时间轴，再按拼音和稿子比对，标出可能读错的地方 |
| 配音字幕 | [pyVideoTrans](https://github.com/jianchang512/pyvideotrans) | 1.9 万星 | GPL-3.0 | 按仓库 README 安装 | — | 识别、翻译、配音、字幕一站式，每一步都能停下来人工改。GPL 许可，做商用产品前先看清条款 |
| 画面 | [HyperFrames](https://github.com/heygen-com/hyperframes) | 5.5 万星 | Apache-2.0 | `npx skills add heygen-com/hyperframes --skill hyperframes` | 把这段文字做成一分钟讲解视频 | 用网页代码写画面再渲染成视频。marketingskills 的 video Skill 给 AI 做视频推荐的第一个就是它。我们的讲解片用它做 |
| 画面 | [Remotion](https://github.com/remotion-dev/remotion) | 6.1 万星 | Remotion License | `npx skills add remotion-dev/skills --skill remotion-best-practices` | 做一个视频 | 用 React 写视频。个人和 3 人以内的公司免费，公司再大要买授权（见其 LICENSE.md） |
| 封面 | [cover-copy-check](skills/cover-copy-check)（本仓库） | — | MIT | `npx skills add xiaoliuxiansheng648648-afk/leoliu-video-skills --skill cover-copy-check` | 帮我看看这个封面行不行 | 查封面字数：默认总共 ≤10、每行 ≤5，英文单词和一个数各算 1，标点、emoji、账号名不算；还查和标题是否重复。规则可改。附 9 个测试 |
| 全流程 | [MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | 12.8 万星 | MIT | 按仓库 README | — | **先别急着装**。给主题就出短视频；用云端大模型、在线素材前要先填各家 API Key。适合看懂一条视频怎么拼起来，直接发就跳过了每一步的检查 |
| 全流程 | [OpenMontage](https://github.com/calesthio/OpenMontage) | 6.2 万星 | AGPL-3.0 | 按仓库 README | — | **先别急着装**。12 条生产线。AGPL 许可，拿去做对外服务前先看清条款 |
| 装机必备 | [skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) | 仓库 17.9 万星 | Apache-2.0 | `npx skills add anthropics/skills --skill skill-creator` | 把我每期都重复的这几步写成 Skill | Anthropic 官方。会出测试题，带／不带 Skill 各跑一遍。本仓库的 cover-copy-check 就是用它写的 |
| 装机必备 | [self-improving-agent](https://clawhub.ai/pskoett/skills/self-improving-agent) | ClawHub 48 万次下载 | MIT-0 | `openclaw skills install @pskoett/self-improving-agent` | — | AI 出错、被你纠正时记进 `.learnings/` 笔记，下次先看。**同名的有 5 个作者**；这个热门版本写明只适配 OpenClaw，其他 AI 用作者的原仓库 [pskoett-ai-skills](https://github.com/pskoett/pskoett-ai-skills) |
| 装机必备 | [skill-vetter](https://clawhub.ai/spclaudehome/skills/skill-vetter) | ClawHub 27.5 万次下载 | MIT-0 | `openclaw skills install @spclaudehome/skill-vetter` | 装这个 Skill 之前先帮我查一下 | 装别人的 Skill 前，查会不会乱联网、读密钥、要高权限。**同名的有 4 个作者**，认准作者再装。**实测**：查 humanizer，14 个文件、1 个脚本、不联网、不碰密钥，结论可以装（[报告](docs/skill-vetter-humanizer.md)） |

## 装之前看三样

1. **认准作者**：同一个名字可能有好几个作者，看下载量、星数和最近更新时间。
2. **读说明书第一段**：它是干什么的，跟你要做的事对不对得上；要不要登录别家、填密钥。
3. **拿一个真活试一次**：Skill 拿的是 AI 的全部权限，不好用就删。

## 实测记录的条件

`docs/` 里的实测，都由 Claude Opus 5.5 在一次对话里读完对应的 `SKILL.md` 后照做，单次结果，不代表这个 Skill 在别的模型、别的输入上的表现。

## 关于

整理：LeoLiu｜AI智能体落地（抖音、小红书、视频号同名）。本仓库内容按 [MIT](LICENSE) 开源；表里列出的第三方项目各自遵守它们自己的许可证。
