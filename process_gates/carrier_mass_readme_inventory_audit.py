#!/usr/bin/env python3
"""Audit tests/carrier-mass/README.md inventory and boundary wording.

This is a documentation/process gate. It does not run the carrier-mass
certificates and does not evaluate or change their scientific verdicts.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CARRIER_MASS_DIR = ROOT / "tests" / "carrier-mass"
README = CARRIER_MASS_DIR / "README.md"

REQUIRED_BOUNDARY_TERMS = {
    "vectorlike",
    "zero, not three",
    "action-gated",
    "source action",
    "chiral projection",
    "claim status",
    "verdicts",
    "public posture",
}


def live_direct_scripts() -> set[str]:
    return {
        path.name
        for path in CARRIER_MASS_DIR.glob("*.py")
        if path.name != "__init__.py"
    }


def live_direct_json_outputs() -> set[str]:
    return {path.name for path in CARRIER_MASS_DIR.glob("*.json")}


def documented_carrier_mass_file_names(text: str, suffix: str) -> set[str]:
    """Return carrier-mass file basenames documented in Markdown code spans."""
    names: set[str] = set()
    pattern = rf"`([^`]+{re.escape(suffix)})`"
    for match in re.finditer(pattern, text):
        raw = match.group(1).replace("\\", "/")
        if "/" in raw and not raw.startswith("tests/carrier-mass/"):
            continue
        names.add(Path(raw).name)
    return names


def missing_boundary_terms(text: str) -> list[str]:
    folded = text.casefold()
    return sorted(term for term in REQUIRED_BOUNDARY_TERMS if term not in folded)


class CarrierMassReadmeInventoryAudit(unittest.TestCase):
    def test_readme_names_every_live_direct_carrier_mass_script(self) -> None:
        self.assertTrue(README.is_file(), f"missing {README}")
        text = README.read_text(encoding="utf-8")
        live = live_direct_scripts()
        documented = documented_carrier_mass_file_names(text, ".py")

        self.assertEqual([], sorted(live - documented))

    def test_readme_has_no_stale_direct_script_entries(self) -> None:
        text = README.read_text(encoding="utf-8")
        live = live_direct_scripts()
        documented = documented_carrier_mass_file_names(text, ".py")
        local_script_names = {
            name
            for name in documented
            if (CARRIER_MASS_DIR / name).suffix == ".py"
        }

        self.assertEqual([], sorted(local_script_names - live))

    def test_readme_names_every_live_direct_json_output(self) -> None:
        text = README.read_text(encoding="utf-8")
        live = live_direct_json_outputs()
        documented = documented_carrier_mass_file_names(text, ".json")

        self.assertEqual([], sorted(live - documented))

    def test_readme_has_no_stale_direct_json_entries(self) -> None:
        text = README.read_text(encoding="utf-8")
        live = live_direct_json_outputs()
        documented = documented_carrier_mass_file_names(text, ".json")
        local_json_names = {
            name
            for name in documented
            if (CARRIER_MASS_DIR / name).suffix == ".json"
        }

        self.assertEqual([], sorted(local_json_names - live))

    def test_readme_preserves_not_forced_action_gated_boundary(self) -> None:
        text = README.read_text(encoding="utf-8")
        self.assertEqual([], missing_boundary_terms(text))

    def test_helpers_parse_basename_from_paths(self) -> None:
        text = (
            "`tests/carrier-mass/foo.py` and `bar.py` "
            "and `process_gates/gate.py` and `decoupling_results.json`"
        )
        self.assertEqual(
            {"foo.py", "bar.py"},
            documented_carrier_mass_file_names(text, ".py"),
        )
        self.assertEqual(
            {"decoupling_results.json"},
            documented_carrier_mass_file_names(text, ".json"),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
