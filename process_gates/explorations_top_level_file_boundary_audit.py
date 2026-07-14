#!/usr/bin/env python3
"""Audit loose top-level exploration notes.

Top-level exploration Markdown falls into two intended, boundary-labeled kinds:

1. A small set of explicitly curated conversation/posture stubs, each of which
   must carry its own boundary phrases (the ``ALLOWED_TOP_LEVEL_NOTES`` map).
2. Dated arc notes -- the live lab record of the W-wave / dated-exploration
   runs, named ``<slug>-YYYY-MM-DD.md``. These are the working record, not
   canon; the README's top-level boundary language marks the whole surface as
   "the research lab, not the project canon."

This gate keeps that convention explicit without moving files or judging their
research content. Any top-level note that is neither a curated stub nor a dated
arc note still fails, preserving the lab-vs-canon boundary.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPLORATIONS = ROOT / "explorations"

# Dated arc notes are the live lab record: any slug suffixed with an ISO date,
# e.g. ``W191-projected-i1b-source-block-2026-07-14.md``. Matching notes are an
# accepted top-level kind and are not required to carry per-file boundary
# phrases; the README-level boundary language covers the surface.
DATED_ARC_NOTE = re.compile(r"-\d{4}-\d{2}-\d{2}\.md$")

ALLOWED_TOP_LEVEL_NOTES = {
    "godelian-initial-conditions-boundary-axiom-stub-2026-07-10.md": (
        "CONVERSATION CAPTURE",
        "VERIFY-BEFORE-USE",
        "Curiosity capture only. No claim promotion, no canon movement, no public posture.",
    ),
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


def is_dated_arc_note(filename: str) -> bool:
    return DATED_ARC_NOTE.search(filename) is not None


class ExplorationsTopLevelFileBoundaryAudit(unittest.TestCase):
    def test_only_recognized_top_level_exploration_notes_are_loose(self) -> None:
        # Every top-level note must be a curated stub or a dated arc note.
        # Anything else (an undated, non-allow-listed loose file) trips the
        # boundary: it has neither a per-file boundary label nor the dated
        # lab-record convention.
        unrecognized = sorted(
            name
            for name in top_level_markdown_notes()
            if name not in ALLOWED_TOP_LEVEL_NOTES and not is_dated_arc_note(name)
        )
        self.assertEqual([], unrecognized)

    def test_curated_stubs_are_still_present(self) -> None:
        present = top_level_markdown_notes()
        missing = sorted(set(ALLOWED_TOP_LEVEL_NOTES) - present)
        self.assertEqual([], missing)

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
