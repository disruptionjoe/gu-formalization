#!/usr/bin/env python3
"""Audit tests/pati-salam/README.md inventory and boundary wording.

This is a documentation/process gate. It does not run the Pati-Salam
harness and does not evaluate or change the active-research verdict.
"""

from __future__ import annotations

import re
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PATI_SALAM_DIR = ROOT / "tests" / "pati-salam"
README = PATI_SALAM_DIR / "README.md"

REQUIRED_BOUNDARY_TERMS = {
    "pati-salam",
    "active-research",
    "reproduction harness",
    "owner scripts",
    "success markers",
    "physical generation count",
    "claim status",
    "verdicts",
    "public posture",
}


def tracked_pati_salam_scripts() -> set[str]:
    result = subprocess.run(
        ["git", "ls-files", "tests/pati-salam/*.py"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return {
        Path(raw).name
        for raw in result.stdout.splitlines()
        if raw.endswith(".py")
    }


def documented_pati_salam_script_names(text: str) -> set[str]:
    """Return Pati-Salam harness script basenames documented in Markdown code spans."""
    names: set[str] = set()
    for match in re.finditer(r"`([^`]+\.py)`", text):
        raw = match.group(1).replace("\\", "/")
        if raw.startswith("tests/pati-salam/"):
            names.add(Path(raw).name)
        elif "/" in raw:
            continue
        else:
            names.add(raw)
    return names


def missing_boundary_terms(text: str) -> list[str]:
    folded = text.casefold()
    return sorted(term for term in REQUIRED_BOUNDARY_TERMS if term not in folded)


class PatiSalamReadmeInventoryAudit(unittest.TestCase):
    def test_readme_names_every_tracked_pati_salam_script(self) -> None:
        self.assertTrue(README.is_file(), f"missing {README}")
        text = README.read_text(encoding="utf-8")
        tracked = tracked_pati_salam_scripts()
        documented = documented_pati_salam_script_names(text)

        self.assertEqual([], sorted(tracked - documented))

    def test_readme_has_no_stale_pati_salam_script_entries(self) -> None:
        text = README.read_text(encoding="utf-8")
        tracked = tracked_pati_salam_scripts()
        documented = documented_pati_salam_script_names(text)
        local_script_names = {
            name
            for name in documented
            if (PATI_SALAM_DIR / name).suffix == ".py"
        }

        self.assertEqual([], sorted(local_script_names - tracked))

    def test_readme_preserves_active_research_boundary(self) -> None:
        text = README.read_text(encoding="utf-8")
        self.assertEqual([], missing_boundary_terms(text))

    def test_helpers_parse_basename_from_paths(self) -> None:
        text = (
            "`tests/pati-salam/foo.py` and `bar.py` "
            "and `lab/active-research/owner.py`"
        )
        self.assertEqual(
            {"foo.py", "bar.py"},
            documented_pati_salam_script_names(text),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
