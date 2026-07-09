#!/usr/bin/env python3
"""Audit the lab README surface map.

This is a documentation/process gate, not a research-content check. It keeps
the second-level `lab/` map synchronized with the live lab directories and
preserves the distinction between working lab material and reviewed front-door
surfaces.
"""

from __future__ import annotations

import re
import unittest
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
LAB = ROOT / "lab"
README = LAB / "README.md"

MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")

EXPECTED_LAB_SURFACES = (
    "active-research",
    "roadmap",
    "process",
    "deep-research",
    "literature",
    "sources",
    "specifications",
    "automation",
    "archive",
)

FRONT_DOOR_REFERENCES = (
    "README.md",
    "RESEARCH-PROGRAM.md",
    "canon/",
    "papers/",
)


@dataclass(frozen=True)
class LocalLink:
    target: str
    line: int


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def readme_text() -> str:
    return README.read_text(encoding="utf-8")


def local_links(text: str) -> list[LocalLink]:
    links: list[LocalLink] = []
    for match in MARKDOWN_LINK.finditer(text):
        raw_target = match.group(1).strip()
        if not raw_target or raw_target.startswith("#"):
            continue
        parsed = urlparse(raw_target)
        if parsed.scheme or parsed.netloc:
            continue
        links.append(
            LocalLink(target=unquote(parsed.path), line=line_number(text, match.start(1)))
        )
    return links


def live_lab_directories() -> set[str]:
    return {
        path.name
        for path in LAB.iterdir()
        if path.is_dir() and not path.name.startswith((".", "__"))
    }


def linked_lab_directories(text: str) -> set[str]:
    linked: set[str] = set()
    for link in local_links(text):
        normalized = link.target.strip().strip("/")
        if "/" in normalized or not normalized:
            continue
        linked.add(normalized)
    return linked


def display_path(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


class LabReadmeSurfaceMapAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = readme_text()

    def test_lab_surface_links_match_live_directories(self) -> None:
        expected = set(EXPECTED_LAB_SURFACES)
        self.assertEqual(expected, live_lab_directories())
        self.assertEqual(expected, linked_lab_directories(self.text))

    def test_lab_surface_links_resolve_from_lab_readme(self) -> None:
        missing: list[str] = []
        for link in local_links(self.text):
            target = Path(link.target)
            self.assertFalse(
                target.is_absolute(),
                f"line {link.line}: lab README links must be relative, not {link.target}",
            )
            resolved = (README.parent / target).resolve()
            if not resolved.exists():
                missing.append(f"line {link.line}: {link.target} -> {display_path(resolved)}")

        self.assertEqual([], missing)

    def test_lab_readme_preserves_front_door_boundary(self) -> None:
        missing = [reference for reference in FRONT_DOOR_REFERENCES if reference not in self.text]
        self.assertEqual([], missing)
        self.assertIn("working program", self.text)
        self.assertIn("durable, reviewed results live in `canon/` and `papers/`", self.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
