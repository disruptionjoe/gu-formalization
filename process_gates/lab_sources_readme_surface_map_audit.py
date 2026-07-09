#!/usr/bin/env python3
"""Audit the lab/sources README surface map.

This is a provenance/navigation gate, not a research-content check. It keeps
the `lab/sources/` map from silently drifting and preserves the boundary that
media/source material is provenance, not mathematical evidence by itself.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "lab" / "sources"
README = SOURCES / "README.md"

BACKTICK_MARKDOWN_FILE = re.compile(r"`([^`]+\.md)`")

KNOWN_UNLISTED_SOURCE_FILES = {
    "gu-paper-reference-surfaces.md",
    "media-claim-and-insight-mining-v1.md",
}

BOUNDARY_PHRASES = (
    "not treated as mathematical evidence",
    "transcript, timestamp, or archived text fragment",
    "current verification status",
    "media/source items",
)


def readme_text() -> str:
    return README.read_text(encoding="utf-8")


def live_source_files() -> set[str]:
    return {
        path.name
        for path in SOURCES.iterdir()
        if path.is_file() and path.suffix == ".md" and path.name != "README.md"
    }


def directly_listed_source_files(text: str) -> set[str]:
    listed: set[str] = set()
    for raw_target in BACKTICK_MARKDOWN_FILE.findall(text):
        if "/" in raw_target or "\\" in raw_target or raw_target == "README.md":
            continue
        listed.add(raw_target)
    return listed


class LabSourcesReadmeSurfaceMapAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = readme_text()

    def test_listed_source_files_resolve(self) -> None:
        listed = directly_listed_source_files(self.text)
        missing = [name for name in sorted(listed) if not (SOURCES / name).is_file()]
        self.assertEqual([], missing)

        for name in listed:
            with self.subTest(name=name):
                self.assertEqual(1, self.text.count(f"`{name}`"))

    def test_no_new_source_files_are_missing_from_the_readme(self) -> None:
        unlisted = live_source_files() - directly_listed_source_files(self.text)
        self.assertEqual(KNOWN_UNLISTED_SOURCE_FILES, unlisted)

    def test_sources_readme_preserves_provenance_boundary(self) -> None:
        normalized = " ".join(self.text.split())
        missing = [phrase for phrase in BOUNDARY_PHRASES if phrase not in normalized]
        self.assertEqual([], missing)
        self.assertIn("Source and Media Index", self.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
