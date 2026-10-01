---
name: cover-copy-check
description: Check and fix short-video / Xiaohongshu cover copy (封面文案) against a cover-length rule — by default at most 10 counted characters in total and 5 per line, where each Chinese character counts 1, each English word or number counts 1 (3.5 is one number), punctuation, spaces and emoji count 0, the account signature is not counted, and the cover must not repeat the title. Use this whenever someone writes, reviews or shortens 封面文案 / 封面字 / cover text for 抖音, 小红书, 视频号 or similar platforms, asks "封面超字了吗", "帮我改个封面", or pastes cover lines together with a video title, even if they don't mention the rule.
---

# 封面文案检查

规则：封面文案**总共不超过 10 个字，每行不超过 5 个字**，而且不重复标题。封面在手机信息流里只有一眼的时间，字多了读不完；标题和封面同时出现，重复就等于少了一半信息。所以这两条比“写得漂亮”更优先。

上限、账号署名写在 `scripts/check_cover.py` 顶部的设置里（默认总共 10、每行 5，这是 LeoLiu 账号自己的规矩，不是平台规定；默认没有署名）。封面上印了账号名，或用户说了别的上限，就用 `--signature`、`--max-total`、`--max-line` 传进去，也可以直接改脚本顶部的设置。

## 怎么数

- 一个汉字算 1 个；一个英文单词或一个数算 1 个：`Skill` 算 1，`Claude Code` 算 2，`2026`、`3.5`、`1,000` 各算 1，`GPT-5.5` 算 2，`AI智能体` 算 4。
- 标点、空格、emoji、`%` 这类符号不算。
- 账号署名不计入，脚本会先去掉（多了空格、全角半角不同也认得出）。

人工数容易错，尤其是英文和数字混排，一律用脚本：

```bash
python3 scripts/check_cover.py --title "视频标题" "第一行" "第二行" "第三行"
```

每行单独传一个参数最清楚；用户把几行写在一起、用 `/` 或换行隔开也可以原样传，脚本会拆开。脚本输出逐行字数、合计和问题，退出码 0 表示通过，1 表示不通过。

## 不重复标题：脚本管字面，你管意思

脚本只报两种字面重复：

- 某一行（3 个字及以上）整行出自标题；
- 整个封面七成以上的字是从标题里成段照搬的。

标题和封面共用一两个关键词（产品名、Skill、Gems 这类）是正常的，脚本不报，只在“备注”里列出来，你也**不要**把它当成重复。关键词本来就该在封面上出现，读者靠它认出这条视频讲什么。

脚本看不出“换了说法、意思一样”的重复。所以脚本通过以后，你还要读一遍：封面有没有补充标题没说的东西，比如结论、数字、反差或一个疑问。只是把标题换个说法，就在“问题”里写出来。

## 输出

按这个格式回复：

```
结论：通过／不通过
逐行：第一行（N 字）｜第二行（N 字）｜合计 N 字
问题：……（没有就写“无”）
改法：给 2–3 个版本，每个都先用脚本验证通过，再写出来，并注明每行字数
```

原稿通过时，“改法”可以写“不用改”，想留余量再给备选。改写时保留原意和关键词（尤其是英文产品名），优先删虚词和重复信息，而不是换掉核心词；两行时让第一行立问题或对象，第二行给结论或数字。不知道标题时照常检查字数，并提醒用户对一下标题。
