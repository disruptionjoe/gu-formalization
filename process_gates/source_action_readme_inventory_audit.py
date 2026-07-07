#!/usr/bin/env python3
"""Audit tests/source-action/README.md inventory and boundary wording.

This is a documentation/process gate. It does not run the source-action
certificates and does not evaluate or change their scientific verdicts.
"""

from __future__ import annotations

import re
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_ACTION_DIR = ROOT / "tests" / "source-action"
README = SOURCE_ACTION_DIR / "README.md"

REQUIRED_BOUNDARY_TERMS = {
    "frozen",
    "paper-adjacent",
    "source-action wall",
    "source action",
    "integer-extraction",
    "claim status",
    "verdicts",
    "public posture",
}


def tracked_source_action_scripts() -> set[str]:
    result = subprocess.run(
        ["git", "ls-files", "tests/source-action/*.py"],
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


def documented_source_action_script_names(text: str) -> set[str]:
    """Return source-action script basenames documented in Markdown code spans."""
    names: set[str] = set()
    for match in re.finditer(r"`([^`]+\.py)`", text):
        raw = match.group(1).replace("\\", "/")
        if raw.startswith("tests/source-action/"):
            names.add(Path(raw).name)
        elif "/" in raw:
            continue
        else:
            names.add(raw)
    return names


def missing_boundary_terms(text: str) -> list[str]:
    folded = text.casefold()
    return sorted(term for term in REQUIRED_BOUNDARY_TERMS if term not in folded)


class SourceActionReadmeInventoryAudit(unittest.TestCase):
    def test_readme_names_every_tracked_source_action_script(self) -> None:
        self.assertTrue(README.is_file(), f"missing {README}")
        text = README.read_text(encoding="utf-8")
        tracked = tracked_source_action_scripts()
        documented = documented_source_action_script_names(text)

        self.assertEqual([], sorted(tracked - documented))

    def test_readme_has_no_stale_source_action_script_entries(self) -> None:
        text = README.read_text(encoding="utf-8")
        tracked = tracked_source_action_scripts()
        documented = documented_source_action_script_names(text)
        local_script_names = {
            name
            for name in documented
            if (SOURCE_ACTION_DIR / name).suffix == ".py"
        }

        self.assertEqual([], sorted(local_script_names - tracked))

    def test_readme_preserves_frozen_source_action_wall_boundary(self) -> None:
        text = README.read_text(encoding="utf-8")
        self.assertEqual([], missing_boundary_terms(text))

    def test_helpers_parse_basename_from_paths(self) -> None:
        text = (
            "`tests/source-action/foo.py` and `bar.py` "
            "and `process_gates/gate.py`"
        )
        self.assertEqual(
            {"foo.py", "bar.py"},
            documented_source_action_script_names(text),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
