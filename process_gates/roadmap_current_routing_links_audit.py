#!/usr/bin/env python3
"""Audit current roadmap routing links.

This is a documentation-governance gate, not a mathematical check. It keeps the
front-door roadmap table from pointing contributors at nonexistent local files.
"""

from __future__ import annotations

import re
import unittest
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
ROADMAP = ROOT / "lab" / "roadmap" / "README.md"

MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


@dataclass(frozen=True)
class LocalLink:
    target: str
    line: int


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def local_link_targets(text: str) -> list[LocalLink]:
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


def display_path(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


class RoadmapCurrentRoutingLinksAudit(unittest.TestCase):
    def test_current_routing_relative_links_resolve(self) -> None:
        self.assertTrue(ROADMAP.is_file(), f"missing {ROADMAP}")
        text = ROADMAP.read_text(encoding="utf-8")
        links = local_link_targets(text)
        self.assertGreaterEqual(len(links), 1)

        missing: list[str] = []
        for link in links:
            target = Path(link.target)
            self.assertFalse(
                target.is_absolute(),
                f"line {link.line}: local roadmap links must be repository-relative, not {link.target}",
            )
            resolved = (ROADMAP.parent / target).resolve()
            if not resolved.exists():
                missing.append(f"line {link.line}: {link.target} -> {display_path(resolved)}")

        self.assertEqual([], missing)


if __name__ == "__main__":
    unittest.main(verbosity=2)
