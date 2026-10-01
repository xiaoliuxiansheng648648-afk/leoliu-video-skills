#!/usr/bin/env python3
"""Check cover copy: length (default 10 in total, 5 per line) and repetition of the title.

Counting: a CJK character is 1, an English word or a number is 1 (3.5 and 1,000 are one
number), punctuation, spaces and emoji are 0. The account signature is not counted.

Usage: check_cover.py [--title T] [--signature S] [--max-total N] [--max-line N] LINE [LINE ...]
A LINE may hold several lines separated by "/", "／" or a newline. Exit code 0 = pass, 1 = fail.
"""
import argparse, re, sys, unicodedata

# Settings: change these to your own account's rule.
SIGNATURE = ""  # e.g. "你的账号名"; text equal to it is removed before counting
MAX_TOTAL = 10
MAX_LINE = 5
# Share of cover characters copied from the title (in runs of 2+) that counts as
# repeating it. One or two shared keywords stay well below this.
OVERLAP_LIMIT = 0.7

HAN = re.compile(r"[㐀-鿿豈-﫿぀-ヿ]")
TOKEN = re.compile(r"[A-Za-z0-9]+(?:[.,][0-9]+)*")
LINE_BREAK = re.compile(r"\s*[/／\n]\s*")


def units(text: str) -> list[str]:
    """The counted characters of text in order: words, numbers and CJK characters."""
    text, out, i = unicodedata.normalize("NFKC", text), [], 0
    while i < len(text):
        m = TOKEN.match(text, i)
        if m:
            out.append(m.group().lower())
            i = m.end()
            continue
        if HAN.match(text[i]):
            out.append(text[i])
        i += 1
    return out


def count(text: str) -> int:
    return len(units(text))


def strip_signature(text: str, signature: str) -> str:
    """Remove the signature, tolerating extra spaces and full/half-width variants."""
    def either_width(c: str) -> str:
        full = chr(ord(c) + 0xFEE0) if "!" <= c <= "~" else c
        return "[" + re.escape(c) + re.escape(full) + "]"
    chars = [either_width(c) for c in unicodedata.normalize("NFKC", signature) if not c.isspace()]
    return re.sub(r"\s*".join(chars), "", text) if chars else text


def split_lines(args: list[str], signature: str) -> list[str]:
    parts = (p.strip() for a in args for p in LINE_BREAK.split(strip_signature(a, signature)))
    return [p for p in parts if p]


def contains(seq: list[str], sub: list[str]) -> bool:
    return any(seq[i:i + len(sub)] == sub for i in range(len(seq) - len(sub) + 1))


def copied_from_title(cover: list[str], title: list[str]) -> int:
    """How many cover characters sit in a run of 2+ characters that also appears in the title."""
    covered = [False] * len(cover)
    for start in range(len(cover)):
        end = start + 2
        while end <= len(cover) and contains(title, cover[start:end]):
            covered[start:end] = [True] * (end - start)
            end += 1
    return sum(covered)


def check(lines, title="", max_total=MAX_TOTAL, max_line=MAX_LINE):
    """Return (issues, notes, per-line descriptions, total)."""
    issues, notes, parts = [], [], []
    title_units = units(title)
    for line in lines:
        n = count(line)
        parts.append(f"{line}（{n} 字）")
        if n > max_line:
            issues.append(f"“{line}”一行 {n} 字，超过 {max_line} 字")
        # A whole line lifted from the title repeats it; one shared keyword does not.
        if title_units and n >= 3 and contains(title_units, units(line)):
            issues.append(f"“{line}”整行和标题重复")
    total = sum(count(l) for l in lines)
    if total > max_total:
        issues.insert(0, f"合计 {total} 字，超过 {max_total} 字")
    cover = [u for l in lines for u in units(l)]
    if title_units and len(cover) >= 3 and not any("标题重复" in i for i in issues):
        copied = copied_from_title(cover, title_units)
        if copied / len(cover) >= OVERLAP_LIMIT:
            issues.append(f"封面 {len(cover)} 个字里有 {copied} 个照搬标题，和标题重复")
    shared = sorted({u for u in cover if TOKEN.fullmatch(u) and u in title_units})
    if shared:
        notes.append("和标题共用关键词 " + "、".join(shared) + "，单个关键词相同不算重复")
    return issues, notes, parts, total


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--title", default="", help="video title, for the repetition check")
    ap.add_argument("--signature", default=SIGNATURE, help="account signature; not counted")
    ap.add_argument("--max-total", type=int, default=MAX_TOTAL)
    ap.add_argument("--max-line", type=int, default=MAX_LINE)
    ap.add_argument("lines", nargs="+")
    a = ap.parse_args()
    lines = split_lines(a.lines, a.signature)
    if not lines:
        print("结论：不通过\n逐行：无｜合计 0 字\n问题：去掉署名后没有封面文字")
        return 1
    issues, notes, parts, total = check(lines, a.title, a.max_total, a.max_line)
    print("结论：" + ("通过" if not issues else "不通过"))
    print("逐行：" + "｜".join(parts) + f"｜合计 {total} 字")
    print("问题：" + ("；".join(issues) if issues else "无"))
    for note in notes:
        print("备注：" + note)
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
