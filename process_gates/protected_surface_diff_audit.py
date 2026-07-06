#!/usr/bin/env python3
"""Audit current local diffs for protected research/status surfaces.

This is a scheduled-run guard, not a mathematical certificate. It fails when
the current working tree, staged diff, or untracked file set touches surfaces
that require explicit review in unattended Progress runs.
"""

from __future__ import annotations

import subprocess
import unittest
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

PROTECTED_EXACT_PATHS = {
    "CANON.md",
    "DERIVATION-PROGRESS.md",
    "RESEARCH-PROGRAM.md",
    "RESEARCH-POSTURE.md",
    "RESEARCH-STATUS.md",
    "LICENSE-CODE.md",
    "LICENSE-DOCS.md",
    "lakefile.lean",
    "lean-toolchain",
    "lab/process/runbooks/claim-status-consistency-quality-workflow.md",
    "lab/sources/claim-ledger.md",
    "lab/sources/claim-ledger-v1-draft.md",
}

PROTECTED_PREFIXES = {
    "canon/",
    "papers/",
    "Lean/",
    "lab/active-research/",
    "absorbed/gu-source-action/",
}

PROTECTED_SUFFIXES = {
    ".lean",
}


@dataclass(frozen=True)
class ProtectedTouch:
    relpath: str
    reason: str


def normalize_path(path: str) -> str:
    return path.strip().replace("\\", "/").lstrip("./")


def protection_reason(relpath: str) -> str | None:
    path = normalize_path(relpath)

    if path in PROTECTED_EXACT_PATHS:
        return "protected exact path"

    for prefix in sorted(PROTECTED_PREFIXES):
        if path.startswith(prefix):
            return f"protected prefix {prefix}"

    suffix = Path(path).suffix
    if suffix in PROTECTED_SUFFIXES:
        return f"protected suffix {suffix}"

    return None


def is_protected_path(path: str) -> bool:
    return protection_reason(path) is not None


def run_git(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def git_path_lines(*args: str) -> list[str]:
    result = run_git(*args)
    if result.returncode != 0:
        command = "git " + " ".join(args)
        raise AssertionError(result.stderr.strip() or f"{command} failed")

    return [normalize_path(line) for line in result.stdout.splitlines() if line.strip()]


def locally_changed_paths() -> list[str]:
    paths = set(git_path_lines("diff", "--name-only", "HEAD", "--"))
    paths.update(git_path_lines("ls-files", "--others", "--exclude-standard"))
    return sorted(paths)


def protected_touches(paths: list[str]) -> list[ProtectedTouch]:
    touches: list[ProtectedTouch] = []
    for path in paths:
        reason = protection_reason(path)
        if reason is not None:
            touches.append(ProtectedTouch(relpath=path, reason=reason))
    return touches


class ProtectedSurfaceDiffAudit(unittest.TestCase):
    def test_classifier_marks_governed_surfaces(self) -> None:
        protected_examples = {
            "CANON.md",
            "RESEARCH-STATUS.md",
            "LICENSE-CODE.md",
            "canon/firewall-boundary-hypothesis.md",
            "papers/candidates/located-not-forced/example.md",
            "Lean/GUFormalization.lean",
            "tests/big-swing/R4_TwoArena.lean",
            "lab/active-research/anomaly/example.md",
            "absorbed/gu-source-action/RS-BRST-CARRIER-PACKET-2026-07-05.md",
            "lab/sources/claim-ledger.md",
        }

        for relpath in protected_examples:
            with self.subTest(relpath=relpath):
                self.assertTrue(is_protected_path(relpath), relpath)

    def test_classifier_allows_process_and_local_ops_surfaces(self) -> None:
        allowed_examples = {
            "process_gates/protected_surface_diff_audit.py",
            "process_gates/README.md",
            "tests/README.md",
            "tests/pati-salam/run_pati_salam_chain_checks.py",
            "REPRODUCE.md",
            "steward/memory-log.md",
            "steward/runs/2026-07-06-progress-fanout-193.md",
        }

        for relpath in allowed_examples:
            with self.subTest(relpath=relpath):
                self.assertFalse(is_protected_path(relpath), relpath)

    def test_current_local_diff_does_not_touch_protected_surfaces(self) -> None:
        touches = protected_touches(locally_changed_paths())
        rendered = [f"{touch.relpath}: {touch.reason}" for touch in touches]
        self.assertEqual([], rendered)


if __name__ == "__main__":
    unittest.main(verbosity=2)
