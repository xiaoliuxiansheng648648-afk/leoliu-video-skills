# skill-vetter 实跑：检查 humanizer（2026-10-01）

- Skill：ClawHub @spclaudehome/skill-vetter（2026-10-01：下载 275,225；同名 slug 另有 3 个作者）。说明书原文从 https://clawhub.ai/spclaudehome/skills/skill-vetter 页面读取。
- 执行方：Claude Opus 5.5 在本会话按其 Vetting Protocol 四步执行；被检对象 blader/humanizer 提交 225a6f3。单次结果。

SKILL VETTING REPORT
Skill: humanizer ｜ Source: GitHub blader/humanizer ｜ Author: blader ｜ Version: 3.1.0
METRICS: Stars 53,168（2026-10-01）｜ Last updated 2026-09-27 ｜ Files reviewed 14（1,094 行）
RED FLAGS: None。逐文件 grep curl/wget/requests/urlopen/fetch/base64/eval/exec/subprocess/os.system/.ssh/.aws/cookie/sudo/api key/token：唯一的整词命中是 SKILL.md 第 307 行 “Most editors auto-curl”（讲弯引号的英文说明，误报）；另有 SKILL.md 英文例句里的 “tokens”。脚本里一处都没有。
PERMISSIONS NEEDED: Files 无（纯文字说明书）｜ Network 无 ｜ Commands：scripts/validate-package.py 只读取本仓库的 SKILL.md、README、CHANGELOG、plugin.json 做格式校验，仅 import json/re/pathlib。
RISK LEVEL: LOW ｜ VERDICT: SAFE TO INSTALL
NOTES: 是否联网取决于你用的 AI 本身，不取决于这个 Skill。
