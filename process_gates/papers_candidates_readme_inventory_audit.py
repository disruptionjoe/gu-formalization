#!/usr/bin/env python3
"""Audit the papers/candidates README staged-candidate inventory.

This is a documentation/process gate, not a publication-status or research
content check. It keeps the candidate staging map synchronized with live
candidate folders while preserving the Joe-confirmed boundaries around
candidate and published status.
"""

from __future__ import annotations

import re
import unittest
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / "papers" / "candidates"
README = CANDIDATES / "README.md"

MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")

BOUNDARY_PHRASES = (
    "not yet public",
    "explicitly said he wants to publish it",
    "does not mean it has been submitted or posted",
    "only after Joe informs that it has actually been published",
    "This table is inventory only",
    "does not publish, submit, reclassify, or advance a paper",
)

MISSING_NOTE_MARKER = "not present; staging-note cleanup debt"


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


def live_candidate_directories() -> set[str]:
    return {
        path.name
        for path in CANDIDATES.iterdir()
        if path.is_dir() and not path.name.startswith((".", "__"))
    }


def candidate_directory_link_counts(text: str) -> dict[str, int]:
    counts = {candidate: 0 for candidate in live_candidate_directories()}
    for link in local_links(text):
        normalized = link.target.rstrip("/")
        if normalized in counts:
            counts[normalized] += 1
    return counts


def candidates_with_staging_notes() -> set[str]:
    return {
        path.name
        for path in CANDIDATES.iterdir()
        if path.is_dir() and (path / "STAGING-NOTES.md").exists()
    }


def candidates_without_staging_notes() -> set[str]:
    return live_candidate_directories() - candidates_with_staging_notes()


def display_path(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


class PapersCandidatesReadmeInventoryAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = readme_text()

    def test_staged_candidate_rows_match_live_directories(self) -> None:
        counts = candidate_directory_link_counts(self.text)
        self.assertEqual(
            {candidate: 1 for candidate in live_candidate_directories()},
            counts,
        )

    def test_staging_note_state_is_explicit(self) -> None:
        for candidate in candidates_with_staging_notes():
            with self.subTest(candidate=candidate):
                self.assertIn(f"{candidate}/STAGING-NOTES.md", self.text)

        missing_marker_count = self.text.count(MISSING_NOTE_MARKER)
        self.assertEqual(len(candidates_without_staging_notes()), missing_marker_count)

        for candidate in candidates_without_staging_notes():
            with self.subTest(candidate=candidate):
                row_prefix = f"| [`{candidate}/`]({candidate}/)"
                rows = [line for line in self.text.splitlines() if line.startswith(row_prefix)]
                self.assertEqual(1, len(rows))
                self.assertIn(MISSING_NOTE_MARKER, rows[0])

    def test_candidate_readme_links_resolve_from_candidate_readme(self) -> None:
        missing: list[str] = []
        for link in local_links(self.text):
            target = Path(link.target)
            self.assertFalse(
                target.is_absolute(),
                f"line {link.line}: candidate README links must be relative, not {link.target}",
            )
            resolved = (README.parent / target).resolve()
            if not resolved.exists():
                missing.append(f"line {link.line}: {link.target} -> {display_path(resolved)}")

        self.assertEqual([], missing)

    def test_candidate_readme_preserves_publication_boundaries(self) -> None:
        normalized = " ".join(self.text.replace("**", "").split())
        missing = [phrase for phrase in BOUNDARY_PHRASES if phrase not in normalized]
        self.assertEqual([], missing)


if __name__ == "__main__":
    unittest.main(verbosity=2)
