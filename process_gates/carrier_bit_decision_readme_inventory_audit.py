#!/usr/bin/env python3
"""Audit tests/carrier-bit-decision/README.md inventory and boundary wording.

This is a documentation/process gate. It does not run the carrier-bit
certificates and does not evaluate or change their scientific verdicts.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CARRIER_BIT_DIR = ROOT / "tests" / "carrier-bit-decision"
README = CARRIER_BIT_DIR / "README.md"

REQUIRED_BOUNDARY_TERMS = {
    "bit-narrowed-but-open",
    "sg4",
    "source action",
    "field-space declaration",
    "story-shopping",
    "claim status",
    "canon",
    "verdicts",
    "public posture",
}


def live_direct_files(suffix: str) -> set[str]:
    return {
        path.name
        for path in CARRIER_BIT_DIR.glob(f"*{suffix}")
        if path.name != "__init__.py"
    }


def documented_carrier_bit_file_names(text: str, suffix: str) -> set[str]:
    """Return carrier-bit file basenames documented in Markdown code spans."""
    names: set[str] = set()
    pattern = rf"`([^`]+{re.escape(suffix)})`"
    for match in re.finditer(pattern, text):
        raw = match.group(1).replace("\\", "/")
        if "/" in raw and not raw.startswith("tests/carrier-bit-decision/"):
            continue
        names.add(Path(raw).name)
    return names


def missing_boundary_terms(text: str) -> list[str]:
    folded = text.casefold()
    return sorted(term for term in REQUIRED_BOUNDARY_TERMS if term not in folded)


class CarrierBitDecisionReadmeInventoryAudit(unittest.TestCase):
    def test_readme_names_every_live_direct_carrier_bit_script(self) -> None:
        self.assertTrue(README.is_file(), f"missing {README}")
        text = README.read_text(encoding="utf-8")
        live = live_direct_files(".py")
        documented = documented_carrier_bit_file_names(text, ".py")

        self.assertEqual([], sorted(live - documented))

    def test_readme_has_no_stale_direct_script_entries(self) -> None:
        text = README.read_text(encoding="utf-8")
        live = live_direct_files(".py")
        documented = documented_carrier_bit_file_names(text, ".py")
        local_script_names = {
            name
            for name in documented
            if (CARRIER_BIT_DIR / name).suffix == ".py"
        }

        self.assertEqual([], sorted(local_script_names - live))

    def test_readme_names_every_live_direct_carrier_bit_analysis(self) -> None:
        text = README.read_text(encoding="utf-8")
        live = live_direct_files(".md") - {"README.md"}
        documented = documented_carrier_bit_file_names(text, ".md")
        documented.discard("README.md")

        self.assertEqual([], sorted(live - documented))

    def test_readme_has_no_stale_direct_analysis_entries(self) -> None:
        text = README.read_text(encoding="utf-8")
        live = live_direct_files(".md") - {"README.md"}
        documented = documented_carrier_bit_file_names(text, ".md")
        documented.discard("README.md")
        local_analysis_names = {
            name
            for name in documented
            if (CARRIER_BIT_DIR / name).suffix == ".md"
        }

        self.assertEqual([], sorted(local_analysis_names - live))

    def test_readme_preserves_bit_open_sg4_boundary(self) -> None:
        text = README.read_text(encoding="utf-8")
        self.assertEqual([], missing_boundary_terms(text))

    def test_helpers_parse_basename_from_paths(self) -> None:
        text = (
            "`tests/carrier-bit-decision/foo.py` and `bar.py` "
            "and `tests/carrier-bit-decision/leg.md` and `note.md` "
            "and `process_gates/gate.py`"
        )
        self.assertEqual(
            {"foo.py", "bar.py"},
            documented_carrier_bit_file_names(text, ".py"),
        )
        self.assertEqual(
            {"leg.md", "note.md"},
            documented_carrier_bit_file_names(text, ".md"),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
