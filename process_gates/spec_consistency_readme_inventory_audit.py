#!/usr/bin/env python3
"""Audit tests/spec-consistency/README.md inventory and boundary wording.

This is a documentation/process gate. It does not run the spec-consistency
certificates and does not evaluate or change their scientific verdicts.
"""

from __future__ import annotations

import re
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC_CONSISTENCY_DIR = ROOT / "tests" / "spec-consistency"
README = SPEC_CONSISTENCY_DIR / "README.md"

REQUIRED_BOUNDARY_TERMS = {
    "consolidation",
    "not new physics",
    "not a source-action build",
    "source action",
    "claim status",
    "canon",
    "verdicts",
    "public posture",
    "paper status",
    "source-action wall",
}


def tracked_spec_consistency_scripts() -> set[str]:
    result = subprocess.run(
        ["git", "ls-files", "tests/spec-consistency/*.py"],
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


def documented_spec_consistency_script_names(text: str) -> set[str]:
    """Return spec-consistency script basenames documented in Markdown code spans."""
    names: set[str] = set()
    for match in re.finditer(r"`([^`]+\.py)`", text):
        raw = match.group(1).replace("\\", "/")
        if raw.startswith("tests/spec-consistency/"):
            names.add(Path(raw).name)
        elif "/" in raw:
            continue
        else:
            names.add(raw)
    return names


def missing_boundary_terms(text: str) -> list[str]:
    folded = text.casefold()
    return sorted(term for term in REQUIRED_BOUNDARY_TERMS if term not in folded)


class SpecConsistencyReadmeInventoryAudit(unittest.TestCase):
    def test_readme_names_every_tracked_spec_consistency_script(self) -> None:
        self.assertTrue(README.is_file(), f"missing {README}")
        text = README.read_text(encoding="utf-8")
        tracked = tracked_spec_consistency_scripts()
        documented = documented_spec_consistency_script_names(text)

        self.assertEqual([], sorted(tracked - documented))

    def test_readme_has_no_stale_spec_consistency_script_entries(self) -> None:
        text = README.read_text(encoding="utf-8")
        tracked = tracked_spec_consistency_scripts()
        documented = documented_spec_consistency_script_names(text)
        local_script_names = {
            name
            for name in documented
            if (SPEC_CONSISTENCY_DIR / name).suffix == ".py"
        }

        self.assertEqual([], sorted(local_script_names - tracked))

    def test_readme_preserves_consolidation_no_verdict_boundary(self) -> None:
        text = README.read_text(encoding="utf-8")
        self.assertEqual([], missing_boundary_terms(text))

    def test_helpers_parse_basename_from_paths(self) -> None:
        text = (
            "`tests/spec-consistency/foo.py` and `bar.py` "
            "and `process_gates/gate.py`"
        )
        self.assertEqual(
            {"foo.py", "bar.py"},
            documented_spec_consistency_script_names(text),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
