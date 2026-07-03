#!/usr/bin/env python3
"""Audit that internal CapacityOS ops records stay local and untracked."""

from __future__ import annotations

import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GITIGNORE = ROOT / ".gitignore"
RUN_RECORD_DIR = "steward/runs/"
IGNORE_PROBE = "steward/runs/__capacityos_ignore_probe__.md"


def run_git(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def active_gitignore_lines() -> list[str]:
    lines: list[str] = []
    for raw_line in GITIGNORE.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        lines.append(line)
    return lines


class InternalOpsGitignoreAudit(unittest.TestCase):
    def test_steward_run_records_have_visible_gitignore_rule(self) -> None:
        self.assertTrue(GITIGNORE.is_file(), "missing .gitignore")
        lines = active_gitignore_lines()

        self.assertIn(RUN_RECORD_DIR, lines)
        self.assertNotIn(f"!{RUN_RECORD_DIR}", lines)
        self.assertNotIn("!steward/runs", lines)

    def test_git_ignores_steward_run_records(self) -> None:
        result = run_git("check-ignore", "-v", "--", IGNORE_PROBE)
        self.assertEqual(
            0,
            result.returncode,
            result.stderr.strip() or f"{IGNORE_PROBE} is not ignored",
        )

        output = result.stdout.strip()
        self.assertIn(".gitignore:", output)
        self.assertIn(RUN_RECORD_DIR, output)

    def test_no_steward_run_records_are_tracked(self) -> None:
        result = run_git("ls-files", "--", "steward/runs")
        self.assertEqual(0, result.returncode, result.stderr.strip())

        tracked = [line for line in result.stdout.splitlines() if line.strip()]
        self.assertEqual([], tracked)


if __name__ == "__main__":
    unittest.main(verbosity=2)
