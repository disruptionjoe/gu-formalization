#!/usr/bin/env python3
"""Audit tests/rs-function-space/README.md inventory and boundary wording.

This is a documentation/process gate. It does not run the RS function-space
certificates and does not evaluate or change their scientific verdicts.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RS_FUNCTION_SPACE_DIR = ROOT / "tests" / "rs-function-space"
README = RS_FUNCTION_SPACE_DIR / "README.md"

REQUIRED_BOUNDARY_TERMS = {
    "rs function-space",
    "family-index",
    "boundary-eta",
    "2-primary",
    "source action",
    "target-import",
    "open crux",
    "claim status",
    "verdicts",
    "public posture",
}


def live_rs_function_space_scripts() -> set[str]:
    return {
        path.relative_to(RS_FUNCTION_SPACE_DIR).as_posix()
        for path in RS_FUNCTION_SPACE_DIR.rglob("*.py")
        if "__pycache__" not in path.parts and path.name != "__init__.py"
    }


def documented_rs_function_space_script_paths(text: str) -> set[str]:
    """Return RS function-space script paths documented in Markdown code spans."""
    names: set[str] = set()
    for match in re.finditer(r"`([^`]+\.py)`", text):
        raw = match.group(1).replace("\\", "/")
        if raw.startswith("tests/rs-function-space/"):
            names.add(raw.removeprefix("tests/rs-function-space/"))
        elif raw.startswith(("verify/", "order3-rho/", "rho-38-adjudication/")):
            names.add(raw)
        elif "/" in raw:
            continue
        else:
            names.add(raw)
    return names


def missing_boundary_terms(text: str) -> list[str]:
    folded = text.casefold()
    return sorted(term for term in REQUIRED_BOUNDARY_TERMS if term not in folded)


class RsFunctionSpaceReadmeInventoryAudit(unittest.TestCase):
    def test_readme_names_every_live_rs_function_space_script(self) -> None:
        self.assertTrue(README.is_file(), f"missing {README}")
        text = README.read_text(encoding="utf-8")
        live = live_rs_function_space_scripts()
        documented = documented_rs_function_space_script_paths(text)

        self.assertEqual([], sorted(live - documented))

    def test_readme_has_no_stale_rs_function_space_script_entries(self) -> None:
        text = README.read_text(encoding="utf-8")
        live = live_rs_function_space_scripts()
        documented = documented_rs_function_space_script_paths(text)
        local_script_paths = {
            path
            for path in documented
            if path.endswith(".py") and (RS_FUNCTION_SPACE_DIR / path).suffix == ".py"
        }

        self.assertEqual([], sorted(local_script_paths - live))

    def test_readme_preserves_open_crux_no_target_import_boundary(self) -> None:
        text = README.read_text(encoding="utf-8")
        self.assertEqual([], missing_boundary_terms(text))

    def test_helpers_parse_relative_and_repo_relative_paths(self) -> None:
        text = (
            "`tests/rs-function-space/foo.py` and `verify/bar.py` "
            "and `order3-rho/baz.py` and `rho-38-adjudication/qux.py` "
            "and `process_gates/gate.py` and `loose.py`"
        )
        self.assertEqual(
            {
                "foo.py",
                "verify/bar.py",
                "order3-rho/baz.py",
                "rho-38-adjudication/qux.py",
                "loose.py",
            },
            documented_rs_function_space_script_paths(text),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
