#!/usr/bin/env python3
"""Audit public-safe surfaces for absolute home-path leaks.

This is a publication hygiene gate, not a research-content check. It scans the
public entry, contributor/config, process-gate, and active-research owner
surfaces so public-facing materials do not carry local machine paths.
"""

from __future__ import annotations

import re
import unittest
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

SAFE_FILES = (
    ".gitattributes",
    ".gitignore",
    "AGENTS.md",
    "CONTRIBUTING.md",
    "LICENSE-CODE.md",
    "LICENSE-DOCS.md",
    "README.md",
    "lakefile.lean",
    "lean-toolchain",
)

SAFE_DIRECTORIES = (
    "lab/active-research",
    "process_gates",
)

FORBIDDEN_SCAN_PREFIXES = (
    "CANON.md",
    "DERIVATION-PROGRESS.md",
    "NEXT-STEPS.md",
    "RESEARCH-PROGRAM.md",
    "RESEARCH-POSTURE.md",
    "RESEARCH-STATUS.md",
    "canon/",
    "explorations/",
    "papers/",
    "tests/",
    "Lean/",
)

TEXT_SUFFIXES = {".lean", ".md", ".py", ".txt"}

HOME_PATH_PATTERNS = (
    ("windows_home", re.compile(r"[A-Za-z]:\\Users\\[A-Za-z0-9._-]+")),
    ("escaped_windows_home", re.compile(r"[A-Za-z]:\\\\Users\\\\[A-Za-z0-9._-]+")),
    ("posix_users_home", re.compile(r"/Users/[A-Za-z0-9._-]+")),
    ("posix_home", re.compile(r"/home/[A-Za-z0-9._-]+")),
)


@dataclass(frozen=True)
class HomePathLeak:
    relpath: str
    line: int
    kind: str
    match: str


def relpath(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def is_text_file(path: Path) -> bool:
    return path.is_file() and (path.suffix in TEXT_SUFFIXES or path.name in SAFE_FILES)


def scan_targets() -> list[Path]:
    targets: list[Path] = []
    for name in SAFE_FILES:
        path = ROOT / name
        if path.is_file():
            targets.append(path)

    for dirname in SAFE_DIRECTORIES:
        base = ROOT / dirname
        if not base.is_dir():
            continue
        targets.extend(path for path in sorted(base.rglob("*")) if is_text_file(path))

    return sorted(set(targets), key=lambda path: relpath(path))


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def find_home_path_leaks(path: Path) -> list[HomePathLeak]:
    text = path.read_text(encoding="utf-8")
    leaks: list[HomePathLeak] = []
    for kind, pattern in HOME_PATH_PATTERNS:
        for match in pattern.finditer(text):
            leaks.append(
                HomePathLeak(
                    relpath=relpath(path),
                    line=line_number(text, match.start()),
                    kind=kind,
                    match=match.group(0),
                )
            )
    return leaks


class PublicPathHygieneAudit(unittest.TestCase):
    def test_scan_scope_avoids_research_truth_and_dirty_residual_surfaces(self) -> None:
        scanned = [relpath(path) for path in scan_targets()]
        self.assertGreaterEqual(len(scanned), 1)
        self.assertIn("README.md", scanned)
        self.assertIn(
            "lab/active-research/README.md",
            scanned,
            "active-research owner surfaces should stay in the public path hygiene scope",
        )
        for path in scanned:
            for prefix in FORBIDDEN_SCAN_PREFIXES:
                self.assertFalse(path == prefix.rstrip("/") or path.startswith(prefix), path)

    def test_public_safe_surfaces_do_not_contain_absolute_home_paths(self) -> None:
        leaks: list[HomePathLeak] = []
        for path in scan_targets():
            leaks.extend(find_home_path_leaks(path))

        rendered = [
            f"{leak.relpath}:{leak.line}: {leak.kind}: {leak.match}"
            for leak in leaks
        ]
        self.assertEqual([], rendered)


if __name__ == "__main__":
    unittest.main(verbosity=2)
