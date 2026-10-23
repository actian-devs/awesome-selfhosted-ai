"""Tests for scripts/validate.py and scripts/build_readme.py.

Run: python3 -m unittest discover tests
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from build_readme import anchor, render_entry  # noqa: E402
from validate import check  # noqa: E402

CATEGORIES = [{"id": "vector-databases", "title": "Vector databases"}]


def entry(**overrides):
    data = {
        "name": "Example DB",
        "url": "https://github.com/example/example-db",
        "category": "vector-databases",
        "description": "Vector database for local development.",
        "license": "Apache-2.0",
        "proprietary": False,
        "added": "2026-10-23",
    }
    data.update(overrides)
    data = {k: v for k, v in data.items() if v is not None}
    data["_path"] = Path(f"{data.get('_file', 'example-db')}.yml")
    data.pop("_file", None)
    return data


def errors_for(*entries):
    return check(list(entries), CATEGORIES)


class ValidateTest(unittest.TestCase):
    def test_valid_entry_passes(self):
        self.assertEqual(errors_for(entry()), [])

    def test_description_must_end_with_period(self):
        self.assertTrue(errors_for(entry(description="Vector database for local development")))

    def test_description_rejects_double_period(self):
        self.assertTrue(errors_for(entry(description="Vector database for local development..")))

    def test_rejects_utm_link(self):
        self.assertTrue(errors_for(entry(url="https://example.com/db?utm_source=list")))

    def test_rejects_bki_tracking_link(self):
        self.assertTrue(errors_for(entry(url="https://bki.sh/abc123")))

    def test_rejects_referral_link(self):
        self.assertTrue(errors_for(entry(url="https://example.com/db?ref=list")))

    def test_non_open_license_needs_proprietary(self):
        errs = errors_for(entry(license="BUSL-1.1"))
        self.assertTrue(any("proprietary" in e for e in errs))
        self.assertEqual(errors_for(entry(license="BUSL-1.1", proprietary=True)), [])

    def test_proprietary_conflicts_with_open_license(self):
        self.assertTrue(errors_for(entry(proprietary=True)))

    def test_proprietary_tag_not_written_in_description(self):
        self.assertTrue(errors_for(entry(description="Vector database (`⊘ Proprietary`).")))

    def test_rejects_marketing_language(self):
        self.assertTrue(errors_for(entry(description="The best vector database for local development.")))

    def test_requires_proprietary_field(self):
        data = entry()
        del data["proprietary"]
        self.assertTrue(errors_for(data))

    def test_unknown_category(self):
        self.assertTrue(errors_for(entry(category="nope")))

    def test_kind_must_be_known(self):
        self.assertEqual(errors_for(entry(kind="model")), [])
        self.assertTrue(errors_for(entry(kind="tool")))

    def test_unknown_field(self):
        self.assertTrue(errors_for(entry(stars=100)))

    def test_file_name_must_match_name(self):
        self.assertTrue(errors_for(entry(_file="something-else")))

    def test_duplicate_url(self):
        other = entry(name="Other DB", _file="other-db", url="https://github.com/example/example-db/")
        self.assertTrue(any("duplicate URL" in e for e in errors_for(entry(), other)))


class BuildTest(unittest.TestCase):
    def test_render_plain_entry(self):
        self.assertEqual(
            render_entry(entry()),
            "- [Example DB](https://github.com/example/example-db) - Vector database for local development.",
        )

    def test_render_proprietary_entry(self):
        rendered = render_entry(entry(license=None, proprietary=True))
        self.assertTrue(rendered.endswith("local development (`⊘ Proprietary`)."))

    def test_anchor_matches_github(self):
        self.assertEqual(anchor("Agents & memory"), "agents--memory")
        self.assertEqual(anchor("UIs"), "uis")


if __name__ == "__main__":
    unittest.main()
