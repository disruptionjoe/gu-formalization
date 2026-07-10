#!/usr/bin/env python3
"""Audit the lab/process README surface map.

This is a documentation/process gate, not a research-content check. It keeps
the `lab/process/` map synchronized with the live process directories and
direct process files while preserving the boundary around status-changing work.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROCESS = ROOT / "lab" / "process"
README = PROCESS / "README.md"

BACKTICK_PATH = re.compile(r"`([^`]+)`")

EXPECTED_PROCESS_DIRS = {
    "dialectics",
    "hegelian-method",
    "persona-passes",
    "public-surface-refresh-2026-05-31",
    "runbooks",
    "syntheses",
    "templates",
}

BOUNDARY_PHRASES = (
    "process navigation",
    "does not change claim status",
    "canon verdicts",
    "proof status",
    "research verdicts",
    "public posture",
    "claim-status consistency workflow",
)


def readme_text() -> str:
    return README.read_text(encoding="utf-8")


def live_process_directories() -> set[str]:
    return {
        path.name
        for path in PROCESS.iterdir()
        if path.is_dir() and not path.name.startswith((".", "__"))
    }


def live_direct_process_files() -> set[str]:
    return {
        path.name
        for path in PROCESS.iterdir()
        if path.is_file() and path.name != "README.md"
    }


def listed_process_directories(text: str) -> set[str]:
    listed: set[str] = set()
    for raw_path in BACKTICK_PATH.findall(text):
        normalized = raw_path.replace("\\", "/")
        if normalized.endswith("/") and "/" not in normalized[:-1]:
            listed.add(normalized.rstrip("/"))
    return listed


def listed_direct_process_files(text: str) -> set[str]:
    listed: set[str] = set()
    for raw_path in BACKTICK_PATH.findall(text):
        normalized = raw_path.replace("\\", "/")
        if "/" in normalized or "\\" in raw_path:
            continue
        if normalized.endswith((".md", ".py")) and normalized != "README.md":
            listed.add(normalized)
    return listed


class LabProcessReadmeSurfaceMapAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = readme_text()

    def test_process_directories_match_live_surface(self) -> None:
        self.assertEqual(EXPECTED_PROCESS_DIRS, live_process_directories())
        self.assertEqual(EXPECTED_PROCESS_DIRS, listed_process_directories(self.text))

        for directory_name in EXPECTED_PROCESS_DIRS:
            with self.subTest(directory_name=directory_name):
                self.assertEqual(1, self.text.count(f"`{directory_name}/`"))

    def test_direct_process_files_match_live_surface(self) -> None:
        live_files = live_direct_process_files()
        listed_files = listed_direct_process_files(self.text)

        self.assertEqual(live_files, listed_files)
        for file_name in live_files:
            with self.subTest(file_name=file_name):
                self.assertEqual(1, self.text.count(f"`{file_name}`"))

    def test_process_readme_preserves_status_change_boundary(self) -> None:
        normalized = " ".join(self.text.split())
        missing = [phrase for phrase in BOUNDARY_PHRASES if phrase not in normalized]
        self.assertEqual([], missing)


if __name__ == "__main__":
    unittest.main(verbosity=2)
