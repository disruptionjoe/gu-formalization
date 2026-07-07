#!/usr/bin/env python3
"""Audit tests/enum-completeness/README.md inventory and boundary wording.

This is a documentation/process gate. It does not run the enum-completeness
certificates and does not evaluate or change their scientific verdicts.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ENUM_COMPLETENESS_DIR = ROOT / "tests" / "enum-completeness"
README = ENUM_COMPLETENESS_DIR / "README.md"

REQUIRED_BOUNDARY_TERMS = {
    "delimited class c",
    "engine finds no escape",
    "boundary sharp",
    "no canon.md promotion",
    "physics derivation of gu",
    "forces or forbids three",
    "computed + independently re-verified",
    "inherited, not recomputed",
    "prior art",
}


def live_enum_completeness_scripts() -> set[str]:
    return {
        path.relative_to(ENUM_COMPLETENESS_DIR).as_posix()
        for path in ENUM_COMPLETENESS_DIR.rglob("*.py")
        if "__pycache__" not in path.parts and path.name != "__init__.py"
    }


def documented_enum_completeness_script_paths(text: str) -> set[str]:
    """Return enum-completeness script paths documented in Markdown code spans."""
    names: set[str] = set()
    for match in re.finditer(r"`([^`]+\.py)`", text):
        raw = match.group(1).replace("\\", "/")
        if raw.startswith("tests/enum-completeness/"):
            names.add(raw.removeprefix("tests/enum-completeness/"))
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


class EnumCompletenessReadmeInventoryAudit(unittest.TestCase):
    def test_readme_names_every_live_enum_completeness_script(self) -> None:
        self.assertTrue(README.is_file(), f"missing {README}")
        text = README.read_text(encoding="utf-8")
        live = live_enum_completeness_scripts()
        documented = documented_enum_completeness_script_paths(text)

        self.assertEqual([], sorted(live - documented))

    def test_readme_has_no_stale_enum_completeness_script_entries(self) -> None:
        text = README.read_text(encoding="utf-8")
        live = live_enum_completeness_scripts()
        documented = documented_enum_completeness_script_paths(text)
        local_script_paths = {
            path
            for path in documented
            if path.endswith(".py") and (ENUM_COMPLETENESS_DIR / path).suffix == ".py"
        }

        self.assertEqual([], sorted(local_script_paths - live))

    def test_readme_preserves_delimited_no_promotion_boundary(self) -> None:
        text = README.read_text(encoding="utf-8")
        self.assertEqual([], missing_boundary_terms(text))

    def test_helpers_parse_relative_and_repo_relative_paths(self) -> None:
        text = (
            "`tests/enum-completeness/foo.py` and `verify/bar.py` "
            "and `process_gates/gate.py` and `loose.py`"
        )
        self.assertEqual(
            {"foo.py", "verify/bar.py", "loose.py"},
            documented_enum_completeness_script_paths(text),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
