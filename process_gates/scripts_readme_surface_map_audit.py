#!/usr/bin/env python3
"""Audit the scripts README surface map.

This is a contributor-tooling/process gate, not a research-content check. It keeps
the public `scripts/` map synchronized with live repo tooling and verifies local
Markdown links resolve from `scripts/README.md`.
"""

from __future__ import annotations

import re
import unittest
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
README = SCRIPTS / "README.md"

MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")

EXPECTED_SCRIPT_FILES = {"reproduce_all.py"}
BOUNDARY_PHRASES = (
    "do not validate research claims",
    "does not change claim status",
    "canon verdicts",
    "research truth",
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


def live_script_files() -> set[str]:
    return {
        path.name
        for path in SCRIPTS.iterdir()
        if path.is_file() and path.suffix == ".py" and path.name != "__init__.py"
    }


def linked_script_files(text: str) -> set[str]:
    linked: set[str] = set()
    for link in local_links(text):
        target = link.target.strip()
        if "/" in target or "\\" in target:
            continue
        if target.endswith(".py"):
            linked.add(target)
    return linked


def display_path(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


class ScriptsReadmeSurfaceMapAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = readme_text()

    def test_script_links_match_live_tools(self) -> None:
        self.assertEqual(EXPECTED_SCRIPT_FILES, live_script_files())
        self.assertEqual(EXPECTED_SCRIPT_FILES, linked_script_files(self.text))
        for script_name in EXPECTED_SCRIPT_FILES:
            with self.subTest(script_name=script_name):
                self.assertEqual(1, self.text.count(f"]({script_name})"))

    def test_scripts_readme_links_resolve_from_scripts_readme(self) -> None:
        missing: list[str] = []
        for link in local_links(self.text):
            target = Path(link.target)
            self.assertFalse(
                target.is_absolute(),
                f"line {link.line}: scripts README links must be relative, not {link.target}",
            )
            resolved = (README.parent / target).resolve()
            if not resolved.exists():
                missing.append(f"line {link.line}: {link.target} -> {display_path(resolved)}")

        self.assertEqual([], missing)

    def test_scripts_readme_preserves_tooling_boundary(self) -> None:
        normalized = " ".join(self.text.split())
        missing = [phrase for phrase in BOUNDARY_PHRASES if phrase not in normalized]
        self.assertEqual([], missing)
        self.assertIn("--tracked-only", self.text)
        self.assertIn("--list", self.text)
        self.assertIn("-k SUBSTR", self.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
