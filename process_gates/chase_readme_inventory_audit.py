#!/usr/bin/env python3
"""Audit tests/chase/README.md inventory and boundary wording.

This is a documentation/process gate. It does not run the chase certificates
and does not evaluate or change their scientific verdicts.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHASE_DIR = ROOT / "tests" / "chase"
README = CHASE_DIR / "README.md"

REQUIRED_BOUNDARY_TERMS = {
    "terminal computational verdict",
    "independent re-verifier",
    "zero flips",
    "not a physics derivation",
    "source-action bottleneck",
    "claim status",
    "verdicts",
}


def live_chase_scripts() -> set[str]:
    return {
        path.relative_to(CHASE_DIR).as_posix()
        for path in CHASE_DIR.rglob("*.py")
        if "__pycache__" not in path.parts and path.name != "__init__.py"
    }


def documented_chase_script_paths(text: str) -> set[str]:
    """Return chase script paths documented in Markdown code spans."""
    names: set[str] = set()
    for match in re.finditer(r"`([^`]+\.py)`", text):
        raw = match.group(1).replace("\\", "/")
        if raw.startswith("tests/chase/"):
            names.add(raw.removeprefix("tests/chase/"))
        elif "/" in raw:
            first = raw.split("/", 1)[0]
            if first.startswith("MOVE-"):
                names.add(raw)
        else:
            names.add(raw)
    return names


def missing_boundary_terms(text: str) -> list[str]:
    folded = text.casefold()
    return sorted(term for term in REQUIRED_BOUNDARY_TERMS if term not in folded)


class ChaseReadmeInventoryAudit(unittest.TestCase):
    def test_readme_names_every_live_chase_script(self) -> None:
        self.assertTrue(README.is_file(), f"missing {README}")
        text = README.read_text(encoding="utf-8")
        live = live_chase_scripts()
        documented = documented_chase_script_paths(text)

        self.assertEqual([], sorted(live - documented))

    def test_readme_has_no_stale_chase_script_entries(self) -> None:
        text = README.read_text(encoding="utf-8")
        live = live_chase_scripts()
        documented = documented_chase_script_paths(text)
        local_script_paths = {
            path
            for path in documented
            if path.endswith(".py") and (CHASE_DIR / path).suffix == ".py"
        }

        self.assertEqual([], sorted(local_script_paths - live))

    def test_readme_preserves_chase_boundary(self) -> None:
        text = README.read_text(encoding="utf-8")
        self.assertEqual([], missing_boundary_terms(text))

    def test_helpers_parse_relative_and_repo_relative_paths(self) -> None:
        text = (
            "`tests/chase/MOVE-1/foo.py` and `MOVE-2/verify/bar.py` "
            "and `process_gates/gate.py` and `loose.py`"
        )
        self.assertEqual(
            {"MOVE-1/foo.py", "MOVE-2/verify/bar.py", "loose.py"},
            documented_chase_script_paths(text),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
