#!/usr/bin/env python3
"""Audit the lab/specifications README surface map.

This is a specification-navigation gate, not a research-content check. It keeps
the `lab/specifications/` map synchronized with live direct specification
directories and preserves the role of specifications as comparable,
falsifiable research-object machinery.
"""

from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPECIFICATIONS = ROOT / "lab" / "specifications"
README = SPECIFICATIONS / "README.md"

EXPECTED_SPECIFICATION_DIRS = {
    "six-axis",
    "type-ii1-spectral-sm",
}

BOUNDARY_PHRASES = (
    "Reusable specification templates",
    "typed format",
    "under-specified physical proposal",
    "comparable, falsifiable research object",
    "machinery behind the Six-Axis Testability white paper",
)


def readme_text() -> str:
    return README.read_text(encoding="utf-8")


def live_specification_directories() -> set[str]:
    return {
        path.name
        for path in SPECIFICATIONS.iterdir()
        if path.is_dir() and not path.name.startswith((".", "__"))
    }


def listed_specification_directories(text: str) -> set[str]:
    listed: set[str] = set()
    for name in EXPECTED_SPECIFICATION_DIRS:
        if f"`{name}/`" in text:
            listed.add(name)
    return listed


def bullet_for_directory(text: str, directory_name: str) -> str:
    marker = f"- `{directory_name}/`"
    start = text.find(marker)
    if start == -1:
        return ""
    next_bullet = text.find("\n- `", start + len(marker))
    if next_bullet == -1:
        return text[start:]
    return text[start:next_bullet]


class LabSpecificationsReadmeSurfaceMapAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = readme_text()

    def test_specification_directories_match_live_surface(self) -> None:
        self.assertEqual(EXPECTED_SPECIFICATION_DIRS, live_specification_directories())
        self.assertEqual(EXPECTED_SPECIFICATION_DIRS, listed_specification_directories(self.text))
        for directory_name in EXPECTED_SPECIFICATION_DIRS:
            with self.subTest(directory_name=directory_name):
                self.assertEqual(1, self.text.count(f"`{directory_name}/`"))

    def test_listed_specification_directories_have_readmes(self) -> None:
        for directory_name in EXPECTED_SPECIFICATION_DIRS:
            with self.subTest(directory_name=directory_name):
                self.assertTrue((SPECIFICATIONS / directory_name / "README.md").is_file())
                bullet = bullet_for_directory(self.text, directory_name)
                self.assertIn("README.md", bullet)

    def test_specifications_readme_preserves_specification_boundary(self) -> None:
        normalized = " ".join(self.text.split())
        missing = [phrase for phrase in BOUNDARY_PHRASES if phrase not in normalized]
        self.assertEqual([], missing)
        self.assertIn("Six-Axis Testability", self.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
