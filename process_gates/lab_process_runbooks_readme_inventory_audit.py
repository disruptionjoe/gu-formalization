#!/usr/bin/env python3
"""Audit the lab/process/runbooks README inventory.

This is a process/navigation gate, not a research-content check. It keeps the
runbooks map synchronized with the live repo-local workflow runbooks and verifies
local Markdown links resolve from `lab/process/runbooks/README.md`.
"""

from __future__ import annotations

import re
import unittest
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
RUNBOOKS = ROOT / "lab" / "process" / "runbooks"
README = RUNBOOKS / "README.md"

MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")

BOUNDARY_PHRASES = (
    "does not change claim status",
    "canon verdicts",
    "public posture",
    "proof status",
    "research verdicts",
    "does not run Lean",
    "does not run Lean, typecheck proofs, or validate any research claim",
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


def live_runbook_files() -> set[str]:
    return {
        path.name
        for path in RUNBOOKS.iterdir()
        if path.is_file() and path.suffix == ".md" and path.name != "README.md"
    }


def linked_runbook_files(text: str) -> set[str]:
    linked: set[str] = set()
    for link in local_links(text):
        target = Path(link.target.strip())
        if target.parent != Path("."):
            continue
        if target.suffix == ".md" and target.name != "README.md":
            linked.add(target.name)
    return linked


def display_path(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


class LabProcessRunbooksReadmeInventoryAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = readme_text()

    def test_runbook_links_match_live_runbooks(self) -> None:
        live = live_runbook_files()
        self.assertEqual(live, linked_runbook_files(self.text))
        for runbook_name in live:
            with self.subTest(runbook_name=runbook_name):
                self.assertEqual(1, self.text.count(f"]({runbook_name})"))

    def test_runbook_readme_links_resolve_from_runbooks_readme(self) -> None:
        missing: list[str] = []
        for link in local_links(self.text):
            target = Path(link.target)
            self.assertFalse(
                target.is_absolute(),
                f"line {link.line}: runbooks README links must be relative, not {link.target}",
            )
            resolved = (README.parent / target).resolve()
            if not resolved.exists():
                missing.append(f"line {link.line}: {link.target} -> {display_path(resolved)}")

        self.assertEqual([], missing)

    def test_runbook_readme_preserves_process_boundary(self) -> None:
        normalized = " ".join(self.text.split())
        missing = [phrase for phrase in BOUNDARY_PHRASES if phrase not in normalized]
        self.assertEqual([], missing)
        self.assertIn("Lean verification", self.text)
        self.assertIn("claim-status consistency workflow", self.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
