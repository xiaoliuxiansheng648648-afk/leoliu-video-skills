"""Script-level tests for check_cover.py, one per case in evals/evals.json.

Run: python3 -m unittest discover skills/cover-copy-check/tests
These check the counting and repetition rules only; the evals check how an agent uses the Skill.
"""
import subprocess
import sys
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "check_cover.py"


def run(*args):
    result = subprocess.run([sys.executable, str(SCRIPT), *args], capture_output=True, text=True)
    return result.returncode, result.stdout


class CoverCheckTest(unittest.TestCase):
    def test_1_english_word_counts_one(self):
        code, out = run("--title", "谷歌要把Gems全改成Skill", "谷歌Gems", "全部改成Skill了")
        self.assertEqual(code, 1)
        self.assertIn("全部改成Skill了（6 字）", out)

    def test_2_words_and_numbers(self):
        code, out = run("Claude Code只用了30%能力？")
        self.assertEqual(code, 1)
        self.assertIn("（8 字）", out)

    def test_3_signature_not_counted(self):
        code, out = run("--signature", "LeoLiu｜AI智能体落地", "--title", "Skill写好了，怎么交给客户用？",
                        "LeoLiu｜AI智能体落地 / 零基础客户 / 做出宣传片")
        self.assertEqual(code, 0)
        self.assertIn("合计 10 字", out)

    def test_4_shared_keyword_is_not_repetition(self):
        code, out = run("--title", "我把封面检查做成了Skill", "Skill", "测了两轮")
        self.assertEqual(code, 0)
        self.assertIn("合计 5 字", out)
        self.assertIn("备注：", out)

    def test_5_all_english(self):
        code, out = run("--title", "封面字数别再手数了", "Stop Counting", "Use Skills")
        self.assertEqual(code, 0)
        self.assertIn("合计 4 字", out)

    def test_6_emoji_and_decimal(self):
        code, out = run("--title", "GPT-5.5实测：写代码比上一代强在哪", "🔥GPT-5.5", "真的值得换吗？")
        self.assertEqual(code, 1)
        self.assertIn("🔥GPT-5.5（2 字）", out)
        self.assertIn("真的值得换吗？（6 字）", out)

    def test_7_three_lines_in_one_string(self):
        code, out = run("别再手数 / 封面字数 / 交给Skill")
        self.assertEqual(code, 1)
        self.assertIn("合计 11 字", out)

    def test_8_copied_title_is_repetition(self):
        code, out = run("--title", "谷歌要把Gems全改成Skill", "谷歌Gems", "全改Skill")
        self.assertEqual(code, 1)
        self.assertIn("合计 6 字", out)
        self.assertIn("和标题重复", out)

    def test_this_episode_cover(self):
        code, out = run("--title", "做视频每一步，该装哪个Skill？", "一条视频", "装哪些Skill")
        self.assertEqual(code, 0, out)


if __name__ == "__main__":
    unittest.main()
