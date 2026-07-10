#!/usr/bin/env python3
"""Audit the lab/deep-research README surface map.

This is a provenance/navigation gate, not a research-content check. It keeps
the `lab/deep-research/` brief map synchronized with live direct Markdown
files while preserving the boundary that external deep-research reports are
source/adversarial-hardening context, not status movement by themselves.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEEP_RESEARCH = ROOT / "lab" / "deep-research"
README = DEEP_RESEARCH / "README.md"

BACKTICK_MARKDOWN_FILE = re.compile(r"`([^`]+\.md)`")

BOUNDARY_PHRASES = (
    "External deep-research briefs",
    "adversarial-hardening passes",
    "prompts sent to web-enabled deep-research models",
    "reports that came back",
    "verify prior art",
    "stress-test the lead paper",
    "hostile-referee prompts",
)

ADJACENT_SURFACE_REFERENCES = (
    "papers/candidates/located-not-forced/",
    "papers/drafts/",
)


def readme_text() -> str:
    return README.read_text(encoding="utf-8")


def live_deep_research_files() -> set[str]:
    return {
        path.name
        for path in DEEP_RESEARCH.iterdir()
        if path.is_file() and path.suffix == ".md" and path.name != "README.md"
    }


def directly_listed_deep_research_files(text: str) -> set[str]:
    listed: set[str] = set()
    for raw_target in BACKTICK_MARKDOWN_FILE.findall(text):
        if "/" in raw_target or "\\" in raw_target or raw_target == "README.md":
            continue
        listed.add(raw_target)
    return listed


class LabDeepResearchReadmeSurfaceMapAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = readme_text()

    def test_listed_deep_research_files_resolve_once(self) -> None:
        listed = directly_listed_deep_research_files(self.text)
        missing = [name for name in sorted(listed) if not (DEEP_RESEARCH / name).is_file()]
        self.assertEqual([], missing)

        for name in listed:
            with self.subTest(name=name):
                self.assertEqual(1, self.text.count(f"`{name}`"))

    def test_no_deep_research_files_are_missing_from_the_readme(self) -> None:
        self.assertEqual(live_deep_research_files(), directly_listed_deep_research_files(self.text))

    def test_adjacent_paper_surfaces_still_exist(self) -> None:
        missing: list[str] = []
        for reference in ADJACENT_SURFACE_REFERENCES:
            if reference not in self.text:
                missing.append(reference)
                continue
            if not (ROOT / reference).exists():
                missing.append(reference)

        self.assertEqual([], missing)

    def test_deep_research_readme_preserves_provenance_boundary(self) -> None:
        normalized = " ".join(self.text.split())
        missing = [phrase for phrase in BOUNDARY_PHRASES if phrase not in normalized]
        self.assertEqual([], missing)


if __name__ == "__main__":
    unittest.main(verbosity=2)
