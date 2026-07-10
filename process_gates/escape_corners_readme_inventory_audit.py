#!/usr/bin/env python3
"""Audit tests/escape-corners/README.md inventory and boundary wording.

This is a documentation/process gate. It does not run the escape-corners
certificates and does not evaluate or change their scientific verdicts.
"""

from __future__ import annotations

import re
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ESCAPE_CORNERS_DIR = ROOT / "tests" / "escape-corners"
README = ESCAPE_CORNERS_DIR / "README.md"

REQUIRED_BOUNDARY_TERMS = {
    "corner",
    "sg4",
    "source action",
    "field-space declaration",
    "story-shopping",
    "claim status",
    "canon",
    "verdicts",
    "public posture",
    "paper status",
    "proof status",
}


def tracked_direct_files(suffix: str) -> set[str]:
    result = subprocess.run(
        ["git", "ls-files", "tests/escape-corners"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    names: set[str] = set()
    for line in result.stdout.splitlines():
        path = Path(line)
        if path.parent.as_posix() == "tests/escape-corners" and path.suffix == suffix:
            names.add(path.name)
    return names


def documented_escape_corners_file_names(text: str, suffix: str) -> set[str]:
    """Return escape-corners file basenames documented in Markdown code spans."""
    names: set[str] = set()
    pattern = rf"`([^`]+{re.escape(suffix)})`"
    for match in re.finditer(pattern, text):
        raw = match.group(1).replace("\\", "/")
        if "/" in raw and not raw.startswith("tests/escape-corners/"):
            continue
        names.add(Path(raw).name)
    return names


def missing_boundary_terms(text: str) -> list[str]:
    folded = text.casefold()
    return sorted(term for term in REQUIRED_BOUNDARY_TERMS if term not in folded)


class EscapeCornersReadmeInventoryAudit(unittest.TestCase):
    def test_readme_names_every_tracked_direct_escape_corners_script(self) -> None:
        self.assertTrue(README.is_file(), f"missing {README}")
        text = README.read_text(encoding="utf-8")
        live = tracked_direct_files(".py")
        documented = documented_escape_corners_file_names(text, ".py")

        self.assertEqual([], sorted(live - documented))

    def test_readme_has_no_stale_direct_script_entries(self) -> None:
        text = README.read_text(encoding="utf-8")
        live = tracked_direct_files(".py")
        documented = documented_escape_corners_file_names(text, ".py")
        local_script_names = {
            name
            for name in documented
            if (ESCAPE_CORNERS_DIR / name).suffix == ".py"
        }

        self.assertEqual([], sorted(local_script_names - live))

    def test_readme_names_every_tracked_direct_escape_corners_analysis(self) -> None:
        text = README.read_text(encoding="utf-8")
        live = tracked_direct_files(".md") - {"README.md"}
        documented = documented_escape_corners_file_names(text, ".md")
        documented.discard("README.md")

        self.assertEqual([], sorted(live - documented))

    def test_readme_has_no_stale_direct_analysis_entries(self) -> None:
        text = README.read_text(encoding="utf-8")
        live = tracked_direct_files(".md") - {"README.md"}
        documented = documented_escape_corners_file_names(text, ".md")
        documented.discard("README.md")
        local_analysis_names = {
            name
            for name in documented
            if (ESCAPE_CORNERS_DIR / name).suffix == ".md"
        }

        self.assertEqual([], sorted(local_analysis_names - live))

    def test_readme_names_every_tracked_direct_escape_corners_log(self) -> None:
        text = README.read_text(encoding="utf-8")
        live = tracked_direct_files(".log")
        documented = documented_escape_corners_file_names(text, ".log")

        self.assertEqual([], sorted(live - documented))

    def test_readme_has_no_stale_direct_log_entries(self) -> None:
        text = README.read_text(encoding="utf-8")
        live = tracked_direct_files(".log")
        documented = documented_escape_corners_file_names(text, ".log")
        local_log_names = {
            name
            for name in documented
            if (ESCAPE_CORNERS_DIR / name).suffix == ".log"
        }

        self.assertEqual([], sorted(local_log_names - live))

    def test_readme_preserves_sg4_no_status_movement_boundary(self) -> None:
        text = README.read_text(encoding="utf-8")
        self.assertEqual([], missing_boundary_terms(text))

    def test_helpers_parse_basename_from_paths(self) -> None:
        text = (
            "`tests/escape-corners/foo.py` and `bar.py` "
            "and `tests/escape-corners/leg.md` and `note.md` "
            "and `tests/escape-corners/run.log` and `process_gates/gate.py`"
        )
        self.assertEqual(
            {"foo.py", "bar.py"},
            documented_escape_corners_file_names(text, ".py"),
        )
        self.assertEqual(
            {"leg.md", "note.md"},
            documented_escape_corners_file_names(text, ".md"),
        )
        self.assertEqual(
            {"run.log"},
            documented_escape_corners_file_names(text, ".log"),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
