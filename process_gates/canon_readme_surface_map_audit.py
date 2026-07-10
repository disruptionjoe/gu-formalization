#!/usr/bin/env python3
"""Audit the canon README pointer map.

This is a documentation/process gate, not a research-content check. It keeps
the `canon/README.md` owner pointers wired to live repo surfaces and preserves
the boundary that `CANON.md` owns authoritative grades and index state.
"""

from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CANON = ROOT / "canon"
README = CANON / "README.md"

EXPECTED_REFERENCES = {
    "RESEARCH-POSTURE.md": ROOT / "RESEARCH-POSTURE.md",
    "../CANON.md": ROOT / "CANON.md",
    "firewall-boundary-hypothesis.md": CANON / "firewall-boundary-hypothesis.md",
}

BOUNDARY_PHRASES = (
    "Stable public spine",
    "not proof claims",
    "The authoritative index and grades live in `../CANON.md`",
    "Canon here = citable spine",
    "the generation-count verdict stays OPEN and nothing derives three",
)


def readme_text() -> str:
    return README.read_text(encoding="utf-8")


class CanonReadmeSurfaceMapAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = readme_text()

    def test_canon_readme_frontmatter_preserves_role(self) -> None:
        self.assertIn("status: canon", self.text)
        self.assertIn("doc_type: overview", self.text)

    def test_canon_readme_references_resolve_to_owner_surfaces(self) -> None:
        missing_text = [reference for reference in EXPECTED_REFERENCES if reference not in self.text]
        self.assertEqual([], missing_text)

        missing_paths = [
            f"{reference} -> {path.relative_to(ROOT).as_posix()}"
            for reference, path in EXPECTED_REFERENCES.items()
            if not path.exists()
        ]
        self.assertEqual([], missing_paths)

    def test_canon_readme_preserves_boundary_language(self) -> None:
        missing = [phrase for phrase in BOUNDARY_PHRASES if phrase not in self.text]
        self.assertEqual([], missing)

    def test_canon_readme_results_cluster_pointer_has_live_targets(self) -> None:
        result_files = sorted(CANON.glob("*-RESULTS.md"))
        self.assertTrue(result_files, "canon README names a RESULTS-file cluster but none exist")
        self.assertIn("*-RESULTS.md", self.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
