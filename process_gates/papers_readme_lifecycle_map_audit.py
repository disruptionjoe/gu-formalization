#!/usr/bin/env python3
"""Audit the papers README publication-lifecycle map.

This is a documentation/process gate, not a publication-status or research
content check. It keeps the root `papers/` map synchronized with the live
publication-stage directories and staged candidate folders while preserving the
Joe-confirmed boundaries around candidate and published status.
"""

from __future__ import annotations

import re
import unittest
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
PAPERS = ROOT / "papers"
README = PAPERS / "README.md"
CANDIDATES = PAPERS / "candidates"
PUBLISHED = PAPERS / "published"

MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
STAGE_DIRECTORIES = ("drafts", "candidates", "published")

BOUNDARY_PHRASES = (
    "A paper lives in exactly one of the three subfolders at a time",
    "explicitly said he wants to publish it",
    "only after Joe confirms it has actually been published",
    "append-mostly",
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


def live_stage_directories() -> set[str]:
    return {
        path.name
        for path in PAPERS.iterdir()
        if path.is_dir() and not path.name.startswith((".", "__"))
    }


def live_candidate_directories() -> set[str]:
    return {
        path.name
        for path in CANDIDATES.iterdir()
        if path.is_dir() and not path.name.startswith((".", "__"))
    }


def candidate_directory_reference_counts(text: str) -> dict[str, int]:
    return {
        candidate: text.count(f"candidates/{candidate}/")
        for candidate in live_candidate_directories()
    }


def published_payload_entries() -> list[str]:
    return sorted(
        path.name
        for path in PUBLISHED.iterdir()
        if path.name != "README.md" and not path.name.startswith((".", "__"))
    )


def display_path(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


class PapersReadmeLifecycleMapAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = readme_text()

    def test_publication_stage_directories_match_lifecycle_links(self) -> None:
        self.assertEqual(set(STAGE_DIRECTORIES), live_stage_directories())
        for stage in STAGE_DIRECTORIES:
            self.assertIn(f"{stage}/", self.text)

    def test_staged_candidate_references_match_live_candidate_directories(self) -> None:
        counts = candidate_directory_reference_counts(self.text)
        self.assertEqual(
            {candidate: 1 for candidate in live_candidate_directories()},
            counts,
        )
        self.assertIn("candidates/README.md", self.text)

    def test_papers_readme_links_resolve_from_papers_readme(self) -> None:
        missing: list[str] = []
        for link in local_links(self.text):
            target = Path(link.target)
            self.assertFalse(
                target.is_absolute(),
                f"line {link.line}: papers README links must be relative, not {link.target}",
            )
            resolved = (README.parent / target).resolve()
            if not resolved.exists():
                missing.append(f"line {link.line}: {link.target} -> {display_path(resolved)}")

        self.assertEqual([], missing)

    def test_papers_readme_preserves_publication_boundaries(self) -> None:
        normalized = " ".join(self.text.split())
        missing = [phrase for phrase in BOUNDARY_PHRASES if phrase not in normalized]
        self.assertEqual([], missing)

    def test_published_empty_marker_matches_empty_published_folder(self) -> None:
        self.assertEqual([], published_payload_entries())
        self.assertIn("Published:** none yet", self.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
