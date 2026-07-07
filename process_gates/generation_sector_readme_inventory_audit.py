#!/usr/bin/env python3
"""Audit tests/generation-sector/README.md inventory and boundary wording.

This is a documentation/process gate. It does not run the generation-sector
certificates and does not evaluate or change their scientific verdicts.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GENERATION_SECTOR_DIR = ROOT / "tests" / "generation-sector"
README = GENERATION_SECTOR_DIR / "README.md"

REQUIRED_BOUNDARY_TERMS = {
    "paper-cited",
    "frozen",
    "do not move",
    "do not rename",
    "generation count",
    "source-action",
    "integer-extraction",
    "claim status",
    "verdicts",
    "public posture",
}


def live_direct_scripts() -> set[str]:
    return {
        path.name
        for path in GENERATION_SECTOR_DIR.glob("*.py")
        if path.name != "__init__.py"
    }


def documented_generation_sector_script_names(text: str) -> set[str]:
    """Return generation-sector script basenames documented in Markdown code spans."""
    names: set[str] = set()
    for match in re.finditer(r"`([^`]+\.py)`", text):
        raw = match.group(1).replace("\\", "/")
        if "/" in raw and not raw.startswith("tests/generation-sector/"):
            continue
        names.add(Path(raw).name)
    return names


def missing_boundary_terms(text: str) -> list[str]:
    folded = text.casefold()
    return sorted(term for term in REQUIRED_BOUNDARY_TERMS if term not in folded)


class GenerationSectorReadmeInventoryAudit(unittest.TestCase):
    def test_readme_names_every_live_direct_generation_sector_script(self) -> None:
        self.assertTrue(README.is_file(), f"missing {README}")
        text = README.read_text(encoding="utf-8")
        live = live_direct_scripts()
        documented = documented_generation_sector_script_names(text)

        self.assertEqual([], sorted(live - documented))

    def test_readme_has_no_stale_direct_script_entries(self) -> None:
        text = README.read_text(encoding="utf-8")
        live = live_direct_scripts()
        documented = documented_generation_sector_script_names(text)
        local_script_names = {
            name
            for name in documented
            if (GENERATION_SECTOR_DIR / name).suffix == ".py"
        }

        self.assertEqual([], sorted(local_script_names - live))

    def test_readme_preserves_frozen_not_verdict_changing_boundary(self) -> None:
        text = README.read_text(encoding="utf-8")
        self.assertEqual([], missing_boundary_terms(text))

    def test_helpers_parse_basename_from_paths(self) -> None:
        text = (
            "`tests/generation-sector/foo.py` and `bar.py` "
            "and `process_gates/gate.py`"
        )
        self.assertEqual(
            {"foo.py", "bar.py"},
            documented_generation_sector_script_names(text),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
