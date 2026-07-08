#!/usr/bin/env python3
"""Audit tests/internal-paths/README.md inventory and boundary wording.

This is a documentation/process gate. It does not run the internal-path
certificates and does not evaluate or change their scientific verdicts.
"""

from __future__ import annotations

import re
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INTERNAL_PATHS_DIR = ROOT / "tests" / "internal-paths"
README = INTERNAL_PATHS_DIR / "README.md"

REQUIRED_BOUNDARY_TERMS = {
    "internal-path",
    "target-free",
    "source action",
    "non-compact",
    "2-primary",
    "not force",
    "claim status",
    "verdicts",
    "public posture",
}


def tracked_internal_paths_scripts() -> set[str]:
    result = subprocess.run(
        ["git", "ls-files", "tests/internal-paths/*.py"],
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


def documented_internal_paths_script_names(text: str) -> set[str]:
    """Return internal-path script basenames documented in Markdown code spans."""
    names: set[str] = set()
    for match in re.finditer(r"`([^`]+\.py)`", text):
        raw = match.group(1).replace("\\", "/")
        if raw.startswith("tests/internal-paths/"):
            names.add(Path(raw).name)
        elif "/" in raw:
            continue
        else:
            names.add(raw)
    return names


def missing_boundary_terms(text: str) -> list[str]:
    folded = text.casefold()
    return sorted(term for term in REQUIRED_BOUNDARY_TERMS if term not in folded)


class InternalPathsReadmeInventoryAudit(unittest.TestCase):
    def test_readme_names_every_tracked_internal_path_script(self) -> None:
        self.assertTrue(README.is_file(), f"missing {README}")
        text = README.read_text(encoding="utf-8")
        tracked = tracked_internal_paths_scripts()
        documented = documented_internal_paths_script_names(text)

        self.assertEqual([], sorted(tracked - documented))

    def test_readme_has_no_stale_internal_path_script_entries(self) -> None:
        text = README.read_text(encoding="utf-8")
        tracked = tracked_internal_paths_scripts()
        documented = documented_internal_paths_script_names(text)
        local_script_names = {
            name
            for name in documented
            if (INTERNAL_PATHS_DIR / name).suffix == ".py"
        }

        self.assertEqual([], sorted(local_script_names - tracked))

    def test_readme_preserves_internal_path_boundary(self) -> None:
        text = README.read_text(encoding="utf-8")
        self.assertEqual([], missing_boundary_terms(text))

    def test_helpers_parse_basename_from_paths(self) -> None:
        text = (
            "`tests/internal-paths/foo.py` and `bar.py` "
            "and `process_gates/gate.py`"
        )
        self.assertEqual(
            {"foo.py", "bar.py"},
            documented_internal_paths_script_names(text),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
