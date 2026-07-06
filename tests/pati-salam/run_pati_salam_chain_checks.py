#!/usr/bin/env python3
"""Run the Pati-Salam active-research verification scripts as tests."""

from __future__ import annotations

import subprocess
import sys
import unittest
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


@dataclass(frozen=True)
class ScriptCheck:
    relpath: str
    success_marker: str

    @property
    def path(self) -> Path:
        return ROOT / self.relpath


CHECKS = (
    ScriptCheck(
        relpath="lab/active-research/pati_salam_chain_verification.py",
        success_marker="VERDICT: every checked step holds.",
    ),
    ScriptCheck(
        relpath="lab/active-research/verify_clifford_explicit.py",
        success_marker="CROSS-CHECK PASSED",
    ),
)


def run_script(check: ScriptCheck) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(check.path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


class PatiSalamChainChecks(unittest.TestCase):
    def test_active_research_scripts_still_pass(self) -> None:
        for check in CHECKS:
            with self.subTest(script=check.relpath):
                self.assertTrue(check.path.is_file(), f"missing {check.relpath}")
                result = run_script(check)
                self.assertEqual(
                    0,
                    result.returncode,
                    result.stderr or result.stdout,
                )
                self.assertIn(check.success_marker, result.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
