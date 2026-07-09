#!/usr/bin/env python3
"""Audit the lab automation README surface map.

This is a documentation/process gate, not a research-content check. It keeps
the `lab/automation/` operational-provenance map synchronized with the live
direct entries while preserving the boundary that automation records are not
load-bearing research.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUTOMATION = ROOT / "lab" / "automation"
README = AUTOMATION / "README.md"

CODE_SPAN = re.compile(r"`([^`]+)`")

EXPECTED_AUTOMATION_ENTRIES = (
    "check-lean.ps1",
    "runs",
    "evidence",
    "logs",
    "tmp",
)

BOUNDARY_PHRASES = (
    "operational record, not load-bearing research",
    "outsider can safely skip it",
    "research outputs",
    "durable, reviewed results live in `canon/`",
    "papers under `papers/published/`",
)


def readme_text() -> str:
    return README.read_text(encoding="utf-8")


def live_direct_entries() -> set[str]:
    return {
        path.name
        for path in AUTOMATION.iterdir()
        if path.name != "README.md" and not path.name.startswith((".", "__"))
    }


def documented_local_entries(text: str) -> set[str]:
    entries: set[str] = set()
    expected = set(EXPECTED_AUTOMATION_ENTRIES)
    for match in CODE_SPAN.finditer(text):
        raw = match.group(1).strip().replace("\\", "/")
        normalized = raw.strip("/")
        if "/" in normalized or not normalized:
            continue
        if normalized in expected:
            entries.add(normalized)
    return entries


def missing_boundary_phrases(text: str) -> list[str]:
    folded = text.casefold()
    return sorted(phrase for phrase in BOUNDARY_PHRASES if phrase.casefold() not in folded)


class LabAutomationReadmeSurfaceMapAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = readme_text()

    def test_automation_entries_match_live_direct_entries(self) -> None:
        expected = set(EXPECTED_AUTOMATION_ENTRIES)
        self.assertEqual(expected, live_direct_entries())
        self.assertEqual(expected, documented_local_entries(self.text) & expected)

    def test_documented_automation_entries_resolve(self) -> None:
        missing: list[str] = []
        documented = documented_local_entries(self.text)
        for name in sorted(set(EXPECTED_AUTOMATION_ENTRIES) & documented):
            if not (AUTOMATION / name).exists():
                missing.append(name)

        self.assertEqual([], missing)

    def test_readme_preserves_operational_provenance_boundary(self) -> None:
        self.assertEqual([], missing_boundary_phrases(self.text))

    def test_helper_ignores_nonlocal_code_spans(self) -> None:
        sample = "`runs/` `check-lean.ps1` `canon/` `papers/published/`"
        self.assertEqual({"runs", "check-lean.ps1"}, documented_local_entries(sample))


if __name__ == "__main__":
    unittest.main(verbosity=2)
