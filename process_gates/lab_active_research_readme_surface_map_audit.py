#!/usr/bin/env python3
"""Audit the lab/active-research README current-thread map.

This is a documentation/process gate, not a research-content check. It keeps
the declared active-research front door wired to live local surfaces while
preserving the boundary around status-changing work.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ACTIVE_RESEARCH = ROOT / "lab" / "active-research"
README = ACTIVE_RESEARCH / "README.md"

CURRENT_THREAD_ROW = re.compile(
    r"^\|\s*`(?P<path>[^`]+)`\s*\|\s*(?P<status>[^|]+?)\s*\|\s*(?P<note>[^|]+?)\s*\|$",
    re.MULTILINE,
)

EXPECTED_CURRENT_THREADS = {
    "signed-readout/": {
        "status": "active_research",
        "note": "Boundary/readout theorem program.",
        "target": ACTIVE_RESEARCH / "signed-readout" / "README.md",
    },
    "calm-gw-boundary/": {
        "status": "active_research",
        "note": "CALM/Ginsparg-Wilson boundary program.",
        "target": ACTIVE_RESEARCH / "calm-gw-boundary" / "README.md",
    },
    "lab/active-research/topological-generation-count-families-k3-chi-gate-2026-06-26.md": {
        "status": "active_research / open gate",
        "note": "Steel Man 2 topological generation-count route; families/K3 chi pushforward is live but not closed.",
        "target": ACTIVE_RESEARCH / "topological-generation-count-families-k3-chi-gate-2026-06-26.md",
    },
}

BOUNDARY_PHRASES = (
    "Frontstage theorem work",
    "promising but not yet canon",
    "Current Threads",
)


def readme_text() -> str:
    return README.read_text(encoding="utf-8")


def current_thread_rows(text: str) -> dict[str, dict[str, str]]:
    rows: dict[str, dict[str, str]] = {}
    for match in CURRENT_THREAD_ROW.finditer(text):
        path = match.group("path").replace("\\", "/")
        rows[path] = {
            "status": " ".join(match.group("status").split()),
            "note": " ".join(match.group("note").split()),
        }
    return rows


class LabActiveResearchReadmeSurfaceMapAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = readme_text()
        cls.rows = current_thread_rows(cls.text)

    def test_current_thread_rows_match_declared_front_door(self) -> None:
        self.assertEqual(set(EXPECTED_CURRENT_THREADS), set(self.rows))

        for path, expected in EXPECTED_CURRENT_THREADS.items():
            with self.subTest(path=path):
                self.assertEqual(expected["status"], self.rows[path]["status"])
                self.assertEqual(expected["note"], self.rows[path]["note"])
                self.assertEqual(1, self.text.count(f"`{path}`"))

    def test_current_thread_targets_resolve(self) -> None:
        for path, expected in EXPECTED_CURRENT_THREADS.items():
            with self.subTest(path=path):
                target = expected["target"]
                self.assertTrue(target.exists(), f"missing active-research target: {target}")
                if path.endswith("/"):
                    self.assertTrue(target.is_file(), f"directory thread lacks README: {target}")

    def test_front_door_preserves_active_research_boundary(self) -> None:
        normalized = " ".join(self.text.split())
        missing = [phrase for phrase in BOUNDARY_PHRASES if phrase not in normalized]
        self.assertEqual([], missing)

        for row in self.rows.values():
            with self.subTest(status=row["status"]):
                self.assertNotIn("canon", row["status"].lower())
                self.assertNotIn("resolved", row["status"].lower())


if __name__ == "__main__":
    unittest.main(verbosity=2)
