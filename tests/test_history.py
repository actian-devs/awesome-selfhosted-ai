"""Tests for scripts/snapshot.py and scripts/changelog.py (no network).

Run: python3 -m unittest discover tests
"""
import datetime
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from changelog import pick_pair, section  # noqa: E402
from listdata import github_repo  # noqa: E402
from snapshot import apply_renames, find_issues  # noqa: E402

NOW = datetime.datetime(2026, 10, 23, tzinfo=datetime.timezone.utc)


def gh(**overrides):
    data = {
        "canonical_url": "https://github.com/example/tool",
        "stars": 100,
        "pushed_at": "2026-10-01T00:00:00Z",
        "archived": False,
    }
    data.update(overrides)
    return data


class SnapshotTest(unittest.TestCase):
    def setUp(self):
        self.entry = {"slug": "tool", "name": "Tool", "url": "https://github.com/example/tool",
                      "_path": Path("tool.yml")}

    def issues(self, result):
        return find_issues([self.entry], {"tool": result}, NOW)

    def test_healthy_repo_has_no_issues(self):
        self.assertFalse(any(self.issues(gh()).values()))

    def test_archived(self):
        self.assertEqual(len(self.issues(gh(archived=True))["archived"]), 1)

    def test_stale(self):
        self.assertEqual(len(self.issues(gh(pushed_at="2026-01-01T00:00:00Z"))["stale"]), 1)

    def test_non_software_is_never_stale(self):
        for kind in ("model", "dataset", "learning", "community"):
            self.entry["kind"] = kind
            self.assertEqual(self.issues(gh(pushed_at="2023-01-01T00:00:00Z"))["stale"], [])

    def test_archived_applies_to_every_kind(self):
        self.entry["kind"] = "model"
        self.assertEqual(len(self.issues(gh(archived=True))["archived"]), 1)

    def test_renamed(self):
        renamed = self.issues(gh(canonical_url="https://github.com/new-org/tool"))["renamed"]
        self.assertEqual(renamed[0][1], "https://github.com/new-org/tool")

    def test_missing(self):
        self.assertEqual(len(self.issues({"error": "not_found"})["missing"]), 1)

    def test_apply_renames_rewrites_url_line_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "tool.yml"
            path.write_text("name: Tool\nurl: https://github.com/example/tool\ndescription: A tool.\n")
            self.entry["_path"] = path
            apply_renames([(self.entry, "https://github.com/new-org/tool")])
            self.assertEqual(path.read_text(),
                             "name: Tool\nurl: https://github.com/new-org/tool\ndescription: A tool.\n")

    def test_github_repo_parsing(self):
        self.assertEqual(github_repo("https://github.com/ollama/ollama"), ("ollama", "ollama"))
        self.assertIsNone(github_repo("https://huggingface.co/microsoft/phi-4"))
        self.assertIsNone(github_repo("https://github.com/sindresorhus/awesome/blob/main/x.md"))


def snap(day, entries):
    return {"_taken": datetime.datetime(2026, 10, day, tzinfo=datetime.timezone.utc), "entries": entries}


def item(name, stars=None, url=None):
    return {"name": name, "url": url or f"https://github.com/x/{name.lower()}",
            **({"github": {"stars": stars}} if stars is not None else {})}


class ChangelogTest(unittest.TestCase):
    def test_needs_three_weeks_of_history(self):
        self.assertIsNone(pick_pair([snap(1, {}), snap(15, {})]))
        self.assertIsNotNone(pick_pair([snap(1, {}), snap(29, {})]))

    def test_section_lists_changes(self):
        old = snap(1, {"a": item("A", 10), "b": item("B", 5), "c": item("C", 1)})
        new = snap(29, {"a": item("A", 40), "b": item("B", 5, url="https://github.com/y/b"), "d": item("D")})
        month, body = section(old, new, top=10)
        self.assertEqual(month, "October 2026")
        self.assertIn("### Added\n\n- [D]", body)
        self.assertIn("### Removed\n\n- C", body)
        self.assertIn("- B: https://github.com/x/b → https://github.com/y/b", body)
        self.assertIn("- [A](https://github.com/x/a) +30", body)


if __name__ == "__main__":
    unittest.main()
