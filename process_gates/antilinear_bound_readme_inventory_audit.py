#!/usr/bin/env python3
"""Audit tests/antilinear-bound/README.md inventory and boundary wording.

This is a documentation/process gate. It does not run the antilinear-bound
certificates and does not evaluate or change their scientific verdicts.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ANTILINEAR_BOUND_DIR = ROOT / "tests" / "antilinear-bound"
README = ANTILINEAR_BOUND_DIR / "README.md"

REQUIRED_BOUNDARY_TERMS = {
    "antilinear-bound",
    "null-eigenspace",
    "krein",
    "index-nullity",
    "not load-bearing",
    "physics derivation of gu",
    "claim status",
    "verdicts",
    "public posture",
}


def live_antilinear_bound_scripts() -> set[str]:
    return {
        path.relative_to(ANTILINEAR_BOUND_DIR).as_posix()
        for path in ANTILINEAR_BOUND_DIR.rglob("*.py")
        if "__pycache__" not in path.parts and path.name != "__init__.py"
    }


def documented_antilinear_bound_script_paths(text: str) -> set[str]:
    """Return antilinear-bound script paths documented in Markdown code spans."""
    names: set[str] = set()
    for match in re.finditer(r"`([^`]+\.py)`", text):
        raw = match.group(1).replace("\\", "/")
        if raw.startswith("tests/antilinear-bound/"):
            names.add(raw.removeprefix("tests/antilinear-bound/"))
        elif raw.startswith("verify/"):
            names.add(raw)
        elif "/" in raw:
            continue
        else:
            names.add(raw)
    return names


def missing_boundary_terms(text: str) -> list[str]:
    folded = text.casefold()
    return sorted(term for term in REQUIRED_BOUNDARY_TERMS if term not in folded)


class AntilinearBoundReadmeInventoryAudit(unittest.TestCase):
    def test_readme_names_every_live_antilinear_bound_script(self) -> None:
        self.assertTrue(README.is_file(), f"missing {README}")
        text = README.read_text(encoding="utf-8")
        live = live_antilinear_bound_scripts()
        documented = documented_antilinear_bound_script_paths(text)

        self.assertEqual([], sorted(live - documented))

    def test_readme_has_no_stale_antilinear_bound_script_entries(self) -> None:
        text = README.read_text(encoding="utf-8")
        live = live_antilinear_bound_scripts()
        documented = documented_antilinear_bound_script_paths(text)
        local_script_paths = {
            path
            for path in documented
            if path.endswith(".py") and (ANTILINEAR_BOUND_DIR / path).suffix == ".py"
        }

        self.assertEqual([], sorted(local_script_paths - live))

    def test_readme_preserves_admissibility_not_derivation_boundary(self) -> None:
        text = README.read_text(encoding="utf-8")
        self.assertEqual([], missing_boundary_terms(text))

    def test_helpers_parse_relative_and_repo_relative_paths(self) -> None:
        text = (
            "`tests/antilinear-bound/foo.py` and `verify/bar.py` "
            "and `process_gates/gate.py` and `loose.py`"
        )
        self.assertEqual(
            {"foo.py", "verify/bar.py", "loose.py"},
            documented_antilinear_bound_script_paths(text),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
