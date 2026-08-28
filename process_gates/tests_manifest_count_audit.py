#!/usr/bin/env python3
"""Audit organized-subdirectory counts in tests/README.md.

This is a publication-manifest hygiene gate, not a mathematical check. It keeps
the reproduction map's live directory counts aligned with the current test tree
without treating archived off-tree rows as load-bearing test inventory.
"""

from __future__ import annotations

import re
import unittest
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TESTS_DIR = ROOT / "tests"
MANIFEST = TESTS_DIR / "README.md"

COUNTED_ROW = re.compile(r"^\| `(?P<dirname>[^`]+/)` \((?P<count>\d+)\) \|")
MIXED_ROW = re.compile(
    r"^\| `(?P<dirname>[^`]+/)` \((?P<python>\d+) Python \+ (?P<sage>\d+) Sage\) \|"
)
ARCHIVED_OFF_TREE_ROW = re.compile(
    r"^\| `(?P<dirname>[^`]+/)` \(archived off-tree\) \|"
)


@dataclass(frozen=True)
class ManifestCount:
    dirname: str
    count: int
    line: int


@dataclass(frozen=True)
class ArchivedOffTreeRow:
    dirname: str
    line: int


@dataclass(frozen=True)
class MixedManifestCount:
    dirname: str
    python: int
    sage: int
    line: int


def parse_manifest_counts(
    text: str,
) -> tuple[list[ManifestCount], list[MixedManifestCount], list[ArchivedOffTreeRow]]:
    counts: list[ManifestCount] = []
    mixed_counts: list[MixedManifestCount] = []
    archived_rows: list[ArchivedOffTreeRow] = []

    for line_number, line in enumerate(text.splitlines(), start=1):
        mixed = MIXED_ROW.match(line)
        if mixed:
            mixed_counts.append(
                MixedManifestCount(
                    dirname=mixed.group("dirname"),
                    python=int(mixed.group("python")),
                    sage=int(mixed.group("sage")),
                    line=line_number,
                )
            )
            continue

        counted = COUNTED_ROW.match(line)
        if counted:
            counts.append(
                ManifestCount(
                    dirname=counted.group("dirname"),
                    count=int(counted.group("count")),
                    line=line_number,
                )
            )
            continue

        archived = ARCHIVED_OFF_TREE_ROW.match(line)
        if archived:
            archived_rows.append(
                ArchivedOffTreeRow(
                    dirname=archived.group("dirname"),
                    line=line_number,
                )
            )

    return counts, mixed_counts, archived_rows


def direct_manifest_file_count(directory: Path) -> int:
    return sum(
        1
        for path in directory.iterdir()
        if path.is_file() and path.name.lower() != "readme.md"
    )


class TestsManifestCountAudit(unittest.TestCase):
    def test_manifest_count_rows_match_direct_files(self) -> None:
        self.assertTrue(MANIFEST.is_file(), f"missing {MANIFEST}")
        counts, _, _ = parse_manifest_counts(MANIFEST.read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(counts), 1)

        mismatches: list[str] = []
        for row in counts:
            directory = TESTS_DIR / row.dirname.rstrip("/")
            if not directory.is_dir():
                mismatches.append(
                    f"line {row.line}: {row.dirname} declares {row.count} but directory is missing"
                )
                continue

            actual = direct_manifest_file_count(directory)
            if row.count != actual:
                mismatches.append(
                    f"line {row.line}: {row.dirname} declares {row.count}, actual {actual}"
                )

        self.assertEqual([], mismatches)

    def test_mixed_manifest_rows_match_direct_extensions(self) -> None:
        _, mixed_counts, _ = parse_manifest_counts(MANIFEST.read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(mixed_counts), 1)
        mismatches: list[str] = []
        for row in mixed_counts:
            directory = TESTS_DIR / row.dirname.rstrip("/")
            if not directory.is_dir():
                mismatches.append(f"line {row.line}: {row.dirname} directory is missing")
                continue
            python_count = sum(1 for path in directory.iterdir() if path.is_file() and path.suffix == ".py")
            sage_count = sum(1 for path in directory.iterdir() if path.is_file() and path.suffix == ".sage")
            if (row.python, row.sage) != (python_count, sage_count):
                mismatches.append(
                    f"line {row.line}: {row.dirname} declares "
                    f"{row.python} Python + {row.sage} Sage, actual "
                    f"{python_count} Python + {sage_count} Sage"
                )
        self.assertEqual([], mismatches)

    def test_archived_off_tree_rows_are_not_live_directories(self) -> None:
        _, _, archived_rows = parse_manifest_counts(MANIFEST.read_text(encoding="utf-8"))

        live_archives = [
            f"line {row.line}: {row.dirname} is marked archived off-tree but exists"
            for row in archived_rows
            if (TESTS_DIR / row.dirname.rstrip("/")).exists()
        ]
        self.assertEqual([], live_archives)


if __name__ == "__main__":
    unittest.main(verbosity=2)
