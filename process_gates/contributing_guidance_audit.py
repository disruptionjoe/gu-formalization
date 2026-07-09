#!/usr/bin/env python3
"""Audit contributor guidance against live process surfaces.

This is a documentation/process gate, not a research-content check. It keeps
the public contributor guide wired to the repo's claim-grading discipline,
claim-status workflow, placement conventions, and validation surfaces without
changing contributor policy.
"""

from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTRIBUTING = ROOT / "CONTRIBUTING.md"

CLAIM_DISCIPLINE_REFERENCES = (
    "[verified]",
    "[reconstruction]",
    "[speculation]",
    "lab/process/runbooks/claim-status-consistency-quality-workflow.md",
)

PLACEMENT_REFERENCES = (
    "explorations/",
    "tests/",
    "tests/README.md",
    "canon/",
    "papers/drafts/",
    "papers/candidates/",
    "papers/published/",
    "papers/published/README.md",
)

LICENSE_REFERENCES = (
    "LICENSE-DOCS.md",
    "LICENSE-CODE.md",
)

LIVE_PATH_REFERENCES = (
    "lab/process/runbooks/claim-status-consistency-quality-workflow.md",
) + PLACEMENT_REFERENCES + LICENSE_REFERENCES


def read_contributing() -> str:
    return CONTRIBUTING.read_text(encoding="utf-8")


class ContributingGuidanceAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_contributing()

    def test_contributor_guide_names_claim_grading_discipline(self) -> None:
        missing = [
            reference
            for reference in CLAIM_DISCIPLINE_REFERENCES
            if reference not in self.text
        ]
        self.assertEqual([], missing)
        self.assertIn("If the change promotes, downgrades, or re-scopes a claim", self.text)

    def test_contributor_guide_keeps_repo_placement_map(self) -> None:
        missing = [reference for reference in PLACEMENT_REFERENCES if reference not in self.text]
        self.assertEqual([], missing)
        self.assertIn("Archived automation output", self.text)
        self.assertIn("not load-bearing", self.text)

    def test_contributor_guide_names_licensing_boundaries(self) -> None:
        missing = [reference for reference in LICENSE_REFERENCES if reference not in self.text]
        self.assertEqual([], missing)
        self.assertIn("CC-BY-4.0", self.text)
        self.assertIn("MIT", self.text)

    def test_referenced_repo_paths_exist(self) -> None:
        missing: list[str] = []
        for reference in LIVE_PATH_REFERENCES:
            if reference.endswith(".md"):
                target = ROOT / reference
            else:
                target = ROOT / reference.strip("/")
            if not target.exists():
                missing.append(reference)

        self.assertEqual([], missing)


if __name__ == "__main__":
    unittest.main(verbosity=2)
