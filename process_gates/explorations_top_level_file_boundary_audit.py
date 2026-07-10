#!/usr/bin/env python3
"""Audit loose top-level exploration notes.

Most exploration notes belong in topical subdirectories. This gate keeps the
few current top-level Markdown notes explicit, reviewed, and boundary-labeled
without moving them or judging their research content.
"""

from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPLORATIONS = ROOT / "explorations"

ALLOWED_TOP_LEVEL_NOTES = {
    "substrate-choice-thesis-computational-vs-smooth-2026-07-07.md": (
        "Exploration grade",
        "no claim movement",
        "This is a research POSTURE / generative hypothesis, not a result.",
    ),
    "transcript-carrier-b-evidence-2026-07-10.md": (
        "TRANSCRIPT-TIER EVIDENCE",
        "NOT a verdict",
        "No canon promotion, no verdict movement.",
    ),
    "twenty-lens-source-action-build-method-sweep-2026-07-09.md": (
        "GENERATION ONLY",
        "moves no verdict/canon/public-posture",
        "only compute->verify decides",
    ),
}


def top_level_markdown_notes() -> set[str]:
    return {
        path.name
        for path in EXPLORATIONS.glob("*.md")
        if path.name != "README.md" and path.is_file()
    }


class ExplorationsTopLevelFileBoundaryAudit(unittest.TestCase):
    def test_only_reviewed_top_level_exploration_notes_are_loose(self) -> None:
        self.assertEqual(set(ALLOWED_TOP_LEVEL_NOTES), top_level_markdown_notes())

    def test_loose_notes_keep_explicit_boundary_phrases(self) -> None:
        missing: list[str] = []
        for filename, phrases in ALLOWED_TOP_LEVEL_NOTES.items():
            text = (EXPLORATIONS / filename).read_text(encoding="utf-8")
            for phrase in phrases:
                if phrase not in text:
                    missing.append(f"{filename}: missing {phrase!r}")

        self.assertEqual([], missing)

    def test_top_level_explorations_readme_stays_lab_not_canon_boundary(self) -> None:
        readme = (EXPLORATIONS / "README.md").read_text(encoding="utf-8")
        required = (
            "the research lab, not the project canon",
            "the durable, reviewed results live in `canon/`",
            "Do not cite as a result",
        )
        missing = [phrase for phrase in required if phrase not in readme]
        self.assertEqual([], missing)


if __name__ == "__main__":
    unittest.main(verbosity=2)
