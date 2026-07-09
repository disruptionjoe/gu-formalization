#!/usr/bin/env python3
"""Audit the public .github contributor-ops surface map.

This is a process/documentation gate, not a research-content check. It keeps
the public intake templates and lightweight CI workflow visible from
.github/README.md and verifies local Markdown links resolve from that file.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
GITHUB_DIR = ROOT / ".github"
README = GITHUB_DIR / "README.md"

EXPECTED_PULL_REQUEST_TEMPLATES = {"PULL_REQUEST_TEMPLATE.md"}
EXPECTED_ISSUE_TEMPLATES = {
    "media-claim-mining.yml",
    "open-problem.yml",
    "reference-pointer.yml",
    "specification-proposal.yml",
}
EXPECTED_WORKFLOWS = {"lean.yml"}


def readme_text() -> str:
    return README.read_text(encoding="utf-8")


def file_names(path: Path, pattern: str) -> set[str]:
    return {candidate.name for candidate in path.glob(pattern) if candidate.is_file()}


def local_markdown_targets(text: str) -> list[str]:
    targets: list[str] = []
    for match in re.finditer(r"\[[^\]]+\]\(([^)]+)\)", text):
        target = match.group(1).strip()
        if not target or target.startswith(("#", "http://", "https://", "mailto:")):
            continue
        targets.append(target.split("#", 1)[0])
    return targets


def resolve_target(target: str) -> Path:
    return (GITHUB_DIR / unquote(target)).resolve()


class GithubReadmeSurfaceMapAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = readme_text()

    def test_current_github_surface_is_accounted_for(self) -> None:
        self.assertEqual(EXPECTED_PULL_REQUEST_TEMPLATES, file_names(GITHUB_DIR, "*TEMPLATE.md"))
        self.assertEqual(
            EXPECTED_ISSUE_TEMPLATES,
            file_names(GITHUB_DIR / "ISSUE_TEMPLATE", "*.yml"),
        )
        self.assertEqual(EXPECTED_WORKFLOWS, file_names(GITHUB_DIR / "workflows", "*.yml"))

    def test_surface_map_links_every_live_intake_file_once(self) -> None:
        expected_targets = {
            "PULL_REQUEST_TEMPLATE.md",
            *{f"ISSUE_TEMPLATE/{name}" for name in EXPECTED_ISSUE_TEMPLATES},
            *{f"workflows/{name}" for name in EXPECTED_WORKFLOWS},
        }

        for target in sorted(expected_targets):
            with self.subTest(target=target):
                self.assertEqual(1, self.text.count(f"]({target})"))

    def test_local_markdown_links_resolve_from_github_readme(self) -> None:
        missing = [
            target
            for target in local_markdown_targets(self.text)
            if not resolve_target(target).exists()
        ]
        self.assertEqual([], missing)

    def test_boundary_keeps_intake_separate_from_research_status(self) -> None:
        normalized = " ".join(self.text.split())
        self.assertIn("do not validate research claims", normalized)
        self.assertIn("not instructions to change research truth", normalized)
        self.assertIn(
            "../lab/process/runbooks/claim-status-consistency-quality-workflow.md",
            self.text,
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
