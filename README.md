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

| 步骤 | 名字 | 星数／下载（2026-10-01） | 许可 | 一句话结论 |
|---|---|---|---|---|
| 选题 | [content-strategy](#content-strategy) | 仓库 5.2 万星 | MIT | 定方向够用；一大半讲搜索和博客 |
| 文案 | [humanizer](#humanizer) | 5.3 万星 | MIT | 去 AI 味；实测标出 8 处、改 6 处 |
| 文案 | [copywriting](#copywriting) | 仓库 5.2 万星 | MIT | 写**网页**文案的，写短视频钩子用 social |
| 文案 | [social](#social) | 仓库 5.2 万星 | MIT | 有短视频钩子公式 |
| 配音字幕 | [Whisper](#whisper) | 11 万星 | MIT | 工具；把配音逐字对到时间轴 |
| 配音字幕 | [pyVideoTrans](#pyvideotrans) | 1.9 万星 | GPL-3.0 | 一站式，每步可停下来改；商用先看条款 |
| 画面 | [HyperFrames](#hyperframes) | 5.5 万星 | Apache-2.0 | 网页代码写画面，可商用 |
| 画面 | [Remotion](#remotion) | 6.1 万星 | Remotion License | 3 人以上的公司要买授权 |
| 封面 | [cover-copy-check](#cover-copy-check) | 本仓库 | MIT | 查封面字数和是否重复标题 |
| 全流程 | [MoneyPrinterTurbo](#moneyprinterturbo) | 12.8 万星 | MIT | 先别急着装：要先填各家 API Key |
| 全流程 | [OpenMontage](#openmontage) | 6.2 万星 | AGPL-3.0 | 先别急着装：做对外服务先看条款 |
| 装机必备 | [skill-creator](#skill-creator) | 仓库 17.9 万星 | Apache-2.0 | 官方；把反复做的事写成 Skill 并自测 |
| 装机必备 | [self-improving-agent](#self-improving-agent) | ClawHub 48 万次 | MIT-0 | 同名 5 个作者；热门版只适配 OpenClaw |
| 装机必备 | [skill-vetter](#skill-vetter) | ClawHub 27.5 万次 | MIT-0 | 装前安全检查；同名一长串，认准作者 |

## 逐项说明

### content-strategy

- 仓库：[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills/tree/main/skills/content-strategy)
- 装：`npx skills add coreyhaines31/marketingskills --skill content-strategy`
- 对 AI 说：帮我定一下接下来的内容方向
- 结论：开工前先问做什么生意、给谁看、手上有什么内容、能不能拍视频，再定内容支柱。一大半讲搜索关键词和博客，短视频拿它定方向就够。

### humanizer

- 仓库：[blader/humanizer](https://github.com/blader/humanizer)
- 装：`npx skills add blader/humanizer`
- 对 AI 说：用 humanizer 改一下这段口播
- 实测：中文口播初稿标出 8 处，改 6 处，按它自己的例外规则留 2 处（[记录](docs/humanizer-run.md)）。规则照英文写，说明书写明各语言的同类句式一样处理。

### copywriting

- 仓库：[marketingskills/skills/copywriting](https://github.com/coreyhaines31/marketingskills/tree/main/skills/copywriting)（不是单独的仓库，是 marketingskills 50 个 Skill 里的一个）
- 装：`npx skills add coreyhaines31/marketingskills --skill copywriting`
- 结论：说明书第一句写的是给**网页**写营销文案（首页、落地页、定价页），开写前先问“这是什么页面”。写短视频钩子用 social。

### social

- 仓库：[marketingskills/skills/social](https://github.com/coreyhaines31/marketingskills/tree/main/skills/social)
- 装：`npx skills add coreyhaines31/marketingskills --skill social`
- 对 AI 说：给这条短视频写三个开头
- 实测：说明书写着 short-form video、video hook，有一组钩子公式（数字、反常识、经历）。本期视频开头用它的“数字＋反常识”写成（[记录](docs/social-hooks-run.md)）。

### Whisper

- 仓库：[openai/whisper](https://github.com/openai/whisper)（工具，不是 Skill）
- 装：`pip install -U openai-whisper`
- 我们怎么用：把配音逐字对到时间轴，再按拼音和稿子比对，标出可能读错的地方，人去听，不对就重配那一句。

### pyVideoTrans

- 仓库：[jianchang512/pyvideotrans](https://github.com/jianchang512/pyvideotrans)，按 README 安装
- 结论：识别、翻译、配音、字幕一站式，每一步都能停下来人工改。GPL-3.0，做商用产品前先看清条款。

### HyperFrames

- 仓库：[heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)
- 装：`npx skills add heygen-com/hyperframes --skill hyperframes`
- 对 AI 说：把这段文字做成一分钟讲解视频
- 结论：用网页代码写画面再渲染成视频，Apache-2.0。marketingskills 的 video Skill 给 AI 做视频推荐的第一个就是它。我们的讲解片用它做。

### Remotion

- 仓库：[remotion-dev/remotion](https://github.com/remotion-dev/remotion)
- 装：`npx skills add remotion-dev/skills --skill remotion-best-practices`
- 结论：用 React 写视频。个人和 3 人以内的公司免费，公司再大要买授权（见其 LICENSE.md）。

### cover-copy-check

- 位置：本仓库 [skills/cover-copy-check](skills/cover-copy-check)
- 装：`npx skills add xiaoliuxiansheng648648-afk/leoliu-video-skills --skill cover-copy-check`
- 对 AI 说：帮我看看这个封面行不行
- 规则：默认总共 ≤10 字、每行 ≤5；英文单词和一个数各算 1，标点、emoji、账号名不算；还查和标题是否重复。规则写在脚本顶部，可改成你自己的。附 9 个测试：`python3 -m unittest discover skills/cover-copy-check/tests`

### MoneyPrinterTurbo

- 仓库：[harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo)，按 README 安装
- 结论：先别急着装。给主题就出短视频；用云端大模型、在线素材前要先填各家 API Key。适合看懂一条视频怎么拼起来，直接发就跳过了每一步的检查。

### OpenMontage

- 仓库：[calesthio/OpenMontage](https://github.com/calesthio/OpenMontage)，按 README 安装
- 结论：先别急着装。12 条生产线；AGPL-3.0，拿去做对外服务前先看清条款。

### skill-creator

- 仓库：[anthropics/skills/skills/skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator)
- 装：`npx skills add anthropics/skills --skill skill-creator`
- 对 AI 说：把我每期都重复的这几步写成 Skill
- 结论：Anthropic 官方，会出测试题，带／不带 Skill 各跑一遍。本仓库的 cover-copy-check 就是用它写的。

### self-improving-agent

- 页面：[ClawHub @pskoett/self-improving-agent](https://clawhub.ai/pskoett/skills/self-improving-agent)
- 装：`openclaw skills install @pskoett/self-improving-agent`
- 结论：AI 出错、被你纠正时记进 `.learnings/` 笔记，下次先看。同名的有 5 个作者；这个热门版本写明只适配 OpenClaw，其他 AI 用作者的原仓库 [pskoett-ai-skills](https://github.com/pskoett/pskoett-ai-skills)。

### skill-vetter

- 页面：[ClawHub @spclaudehome/skill-vetter](https://clawhub.ai/spclaudehome/skills/skill-vetter)
- 装：`openclaw skills install @spclaudehome/skill-vetter`
- 对 AI 说：装这个 Skill 之前先帮我查一下
- 实测：查 humanizer，14 个文件、1 个脚本；搜联网命令只命中说明书里一句讲弯引号的英文（auto-curl），不碰密钥，结论可以装（[报告](docs/skill-vetter-humanizer.md)）。ClawHub 上同名的一长串，认准作者再装。

## 装之前看三样

1. **认准作者**：同一个名字可能有好几个作者，看下载量、星数和最近更新时间。
2. **读说明书第一段**：它是干什么的，跟你要做的事对不对得上；要不要登录别家、填密钥。
3. **拿一个真活试一次**：Skill 拿的是 AI 的全部权限，不好用就删。

## 实测记录的条件

`docs/` 里的实测，都由 Claude Opus 5.5 在一次对话里读完对应的 `SKILL.md` 后照做，单次结果，不代表这个 Skill 在别的模型、别的输入上的表现。

## 关于

整理：LeoLiu｜AI智能体落地（抖音、小红书、视频号同名）。本仓库内容按 [MIT](LICENSE) 开源；表里列出的第三方项目各自遵守它们自己的许可证。
