#!/usr/bin/env python3
"""Audit tests/forcing-slot/README.md inventory and boundary wording.

This is a documentation/process gate. It does not run the forcing-slot
certificates and does not evaluate or change their scientific verdicts.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FORCING_SLOT_DIR = ROOT / "tests" / "forcing-slot"
README = FORCING_SLOT_DIR / "README.md"

REQUIRED_BOUNDARY_TERMS = {
    "forcing-slot",
    "toy",
    "stabilized-source",
    "source action",
    "integer-extraction",
    "frame charge",
    "net chirality",
    "not-a-gu-derivation",
    "not-a-verdict-change",
    "claim status",
    "verdicts",
    "public posture",
}


def live_direct_scripts() -> set[str]:
    return {
        path.name
        for path in FORCING_SLOT_DIR.glob("*.py")
        if path.name != "__init__.py"
    }


def documented_forcing_slot_script_names(text: str) -> set[str]:
    """Return forcing-slot script basenames documented in Markdown code spans."""
    names: set[str] = set()
    for match in re.finditer(r"`([^`]+\.py)`", text):
        raw = match.group(1).replace("\\", "/")
        if "/" in raw and not raw.startswith("tests/forcing-slot/"):
            continue
        names.add(Path(raw).name)
    return names


def missing_boundary_terms(text: str) -> list[str]:
    folded = text.casefold()
    return sorted(term for term in REQUIRED_BOUNDARY_TERMS if term not in folded)


class ForcingSlotReadmeInventoryAudit(unittest.TestCase):
    def test_readme_names_every_live_direct_forcing_slot_script(self) -> None:
        self.assertTrue(README.is_file(), f"missing {README}")
        text = README.read_text(encoding="utf-8")
        live = live_direct_scripts()
        documented = documented_forcing_slot_script_names(text)

        self.assertEqual([], sorted(live - documented))

    def test_readme_has_no_stale_direct_script_entries(self) -> None:
        text = README.read_text(encoding="utf-8")
        live = live_direct_scripts()
        documented = documented_forcing_slot_script_names(text)
        local_script_names = {
            name
            for name in documented
            if (FORCING_SLOT_DIR / name).suffix == ".py"
        }

        self.assertEqual([], sorted(local_script_names - live))

    def test_readme_preserves_toy_not_derivation_boundary(self) -> None:
        text = README.read_text(encoding="utf-8")
        self.assertEqual([], missing_boundary_terms(text))

    def test_helpers_parse_basename_from_paths(self) -> None:
        text = (
            "`tests/forcing-slot/foo.py` and `bar.py` "
            "and `process_gates/gate.py`"
        )
        self.assertEqual(
            {"foo.py", "bar.py"},
            documented_forcing_slot_script_names(text),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
