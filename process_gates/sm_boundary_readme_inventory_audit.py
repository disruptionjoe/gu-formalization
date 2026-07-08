#!/usr/bin/env python3
"""Audit tests/sm-boundary/README.md inventory and boundary wording.

This is a documentation/process gate. It does not run the SM-boundary
certificates and does not evaluate or change their scientific verdicts.
"""

from __future__ import annotations

import re
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM_BOUNDARY_DIR = ROOT / "tests" / "sm-boundary"
README = SM_BOUNDARY_DIR / "README.md"

REQUIRED_BOUNDARY_TERMS = {
    "sm-boundary",
    "local anomaly",
    "2-primary",
    "mod-3 selector",
    "external count",
    "generation count",
    "claim status",
    "verdicts",
    "public posture",
}


def tracked_sm_boundary_scripts() -> set[str]:
    result = subprocess.run(
        ["git", "ls-files", "tests/sm-boundary"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return {
        Path(raw).relative_to("tests/sm-boundary").as_posix()
        for raw in result.stdout.splitlines()
        if raw.endswith(".py")
    }


def documented_sm_boundary_script_paths(text: str) -> set[str]:
    """Return SM-boundary script paths documented in Markdown code spans."""
    names: set[str] = set()
    for match in re.finditer(r"`([^`]+\.py)`", text):
        raw = match.group(1).replace("\\", "/")
        if raw.startswith("tests/sm-boundary/"):
            names.add(raw.removeprefix("tests/sm-boundary/"))
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


class SmBoundaryReadmeInventoryAudit(unittest.TestCase):
    def test_readme_names_every_tracked_sm_boundary_script(self) -> None:
        self.assertTrue(README.is_file(), f"missing {README}")
        text = README.read_text(encoding="utf-8")
        tracked = tracked_sm_boundary_scripts()
        documented = documented_sm_boundary_script_paths(text)

        self.assertEqual([], sorted(tracked - documented))

    def test_readme_has_no_stale_sm_boundary_script_entries(self) -> None:
        text = README.read_text(encoding="utf-8")
        tracked = tracked_sm_boundary_scripts()
        documented = documented_sm_boundary_script_paths(text)
        local_script_paths = {
            path
            for path in documented
            if path.endswith(".py") and (SM_BOUNDARY_DIR / path).suffix == ".py"
        }

        self.assertEqual([], sorted(local_script_paths - tracked))

    def test_readme_preserves_local_anomaly_boundary(self) -> None:
        text = README.read_text(encoding="utf-8")
        self.assertEqual([], missing_boundary_terms(text))

    def test_helpers_parse_relative_and_repo_relative_paths(self) -> None:
        text = (
            "`tests/sm-boundary/foo.py` and `verify/bar.py` "
            "and `process_gates/gate.py` and `loose.py`"
        )
        self.assertEqual(
            {"foo.py", "verify/bar.py", "loose.py"},
            documented_sm_boundary_script_paths(text),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
