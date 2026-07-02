#!/usr/bin/env python3
"""Audit current roadmap routing links.

This is a documentation-governance gate, not a mathematical check. It keeps the
front-door roadmap table from pointing contributors at nonexistent local files.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
ROADMAP = ROOT / "lab" / "roadmap" / "README.md"

MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def local_link_targets(text: str) -> list[str]:
    targets: list[str] = []
    for match in MARKDOWN_LINK.finditer(text):
        raw_target = match.group(1).strip()
        if not raw_target or raw_target.startswith("#"):
            continue
        parsed = urlparse(raw_target)
        if parsed.scheme or parsed.netloc:
            continue
        targets.append(unquote(parsed.path))
    return targets


class RoadmapCurrentRoutingLinksAudit(unittest.TestCase):
    def test_current_routing_relative_links_resolve(self) -> None:
        self.assertTrue(ROADMAP.is_file(), f"missing {ROADMAP}")
        text = ROADMAP.read_text(encoding="utf-8")
        links = local_link_targets(text)
        self.assertGreaterEqual(len(links), 1)

        missing: list[str] = []
        for target in links:
            resolved = (ROADMAP.parent / target).resolve()
            if not resolved.exists():
                missing.append(f"{target} -> {resolved}")

        self.assertEqual([], missing)


if __name__ == "__main__":
    unittest.main(verbosity=2)
