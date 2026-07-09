#!/usr/bin/env python3
"""Audit the explorations README surface map.

This is a documentation/process gate, not a research-content check. It keeps
the public `explorations/` map synchronized with the live top-level exploration
directories and preserves the distinction between lab record and reviewed
canon or publication surfaces.
"""

from __future__ import annotations

import re
import unittest
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
EXPLORATIONS = ROOT / "explorations"
README = EXPLORATIONS / "README.md"

MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")

BOUNDARY_PHRASES = (
    "the research lab, not the project canon",
    "the durable, reviewed results live in `canon/` and the papers under",
    "Do not cite as a result",
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


def live_exploration_directories() -> set[str]:
    return {
        path.name
        for path in EXPLORATIONS.iterdir()
        if path.is_dir() and not path.name.startswith((".", "__"))
    }


def linked_exploration_directories(text: str) -> Counter[str]:
    linked: Counter[str] = Counter()
    live_dirs = live_exploration_directories()
    for link in local_links(text):
        normalized = link.target.strip().strip("/")
        if not normalized:
            continue
        first_segment = normalized.split("/", 1)[0]
        if first_segment in live_dirs:
            linked[first_segment] += 1
    return linked


def display_path(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


class ExplorationsReadmeSurfaceMapAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = readme_text()

    def test_exploration_directory_links_match_live_directories(self) -> None:
        live = live_exploration_directories()
        linked = linked_exploration_directories(self.text)

        self.assertEqual(live, set(linked))
        duplicates = sorted(name for name, count in linked.items() if count != 1)
        self.assertEqual([], duplicates)

    def test_explorations_readme_links_resolve_from_readme(self) -> None:
        missing: list[str] = []
        for link in local_links(self.text):
            target = Path(link.target)
            self.assertFalse(
                target.is_absolute(),
                f"line {link.line}: explorations README links must be relative, not {link.target}",
            )
            resolved = (README.parent / target).resolve()
            if not resolved.exists():
                missing.append(f"line {link.line}: {link.target} -> {display_path(resolved)}")

        self.assertEqual([], missing)

    def test_explorations_readme_preserves_boundary_language(self) -> None:
        missing = [phrase for phrase in BOUNDARY_PHRASES if phrase not in self.text]
        self.assertEqual([], missing)


if __name__ == "__main__":
    unittest.main(verbosity=2)
