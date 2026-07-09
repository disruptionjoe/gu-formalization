#!/usr/bin/env python3
"""Audit the docs README surface map.

This is a documentation/process gate, not a research-content check. It keeps
the second-tier `docs/` map synchronized with live docs files and preserves the
distinction between explanatory context and owner status/canon/publication
surfaces.
"""

from __future__ import annotations

import re
import unittest
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
README = DOCS / "README.md"

MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")

OWNER_SURFACE_REFERENCES = (
    "README.md",
    "RESEARCH-PROGRAM.md",
    "RESEARCH-POSTURE.md",
    "../CANON.md",
    "../RESEARCH-STATUS.md",
    "../canon/",
    "../papers/README.md",
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


def live_docs_files() -> set[str]:
    return {
        path.name
        for path in DOCS.iterdir()
        if path.is_file() and path.suffix == ".md" and path.name != "README.md"
    }


def linked_docs_files(text: str) -> set[str]:
    linked: set[str] = set()
    for link in local_links(text):
        normalized = link.target.strip()
        if "/" in normalized or normalized == "README.md":
            continue
        if normalized.endswith(".md"):
            linked.add(normalized)
    return linked


def display_path(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


class DocsReadmeSurfaceMapAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = readme_text()

    def test_docs_file_links_match_live_documents(self) -> None:
        self.assertEqual(live_docs_files(), linked_docs_files(self.text))

    def test_docs_readme_links_resolve_from_docs_readme(self) -> None:
        missing: list[str] = []
        for link in local_links(self.text):
            target = Path(link.target)
            self.assertFalse(
                target.is_absolute(),
                f"line {link.line}: docs README links must be relative, not {link.target}",
            )
            resolved = (README.parent / target).resolve()
            if not resolved.exists():
                missing.append(f"line {link.line}: {link.target} -> {display_path(resolved)}")

        self.assertEqual([], missing)

    def test_docs_readme_preserves_owner_boundary(self) -> None:
        missing = [reference for reference in OWNER_SURFACE_REFERENCES if reference not in self.text]
        self.assertEqual([], missing)
        self.assertIn("Do not treat `docs/` as the owner of claim grades", self.text)
        self.assertIn("If this folder's older context disagrees", self.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
