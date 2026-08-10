#!/usr/bin/env python3
"""Frontmatter in canon/ and docs/ must parse as YAML.

Motivation (2026-08-10): canon/theta-field-flrw-dark-energy-eos.md sat in canon with frontmatter
yaml.safe_load could not parse (a correction key indented four spaces), so every tool reading
frontmatter silently saw nothing. Found by the canon-spine hostile sweep; fixed the same day.
This gate keeps the invariant: a canon/docs file either has no frontmatter or has parseable
frontmatter.
"""
from __future__ import annotations

import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SURFACES = ("canon", "docs")


def frontmatter_block(path: Path) -> str | None:
    text = path.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    return parts[1] if len(parts) >= 3 else None


class CanonDocsFrontmatterValidity(unittest.TestCase):
    def test_frontmatter_parses(self) -> None:
        bad: list[str] = []
        for surface in SURFACES:
            for path in sorted((ROOT / surface).glob("*.md")):
                block = frontmatter_block(path)
                if block is None:
                    continue
                try:
                    yaml.safe_load(block)
                except yaml.YAMLError as exc:
                    bad.append(f"{path.relative_to(ROOT)}: {exc}")
        self.assertEqual(
            bad, [], "Unparseable frontmatter (fix the YAML, do not remove the block):\n" + "\n".join(bad)
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
