#!/usr/bin/env python3
"""Audit public reproduction docs for central-runner consistency.

This is a documentation/process gate, not a mathematical certificate. It keeps
the public reproduction map aligned with scripts/reproduce_all.py while
preserving the fact that each certificate remains directly runnable.
"""

from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPRODUCE = ROOT / "REPRODUCE.md"
TESTS_README = ROOT / "tests" / "README.md"
HARNESS = ROOT / "scripts" / "reproduce_all.py"

OBSOLETE_NO_RUNNER_PHRASES = {
    "there is no central runner",
    "no central runner",
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


class ReproductionDocsConsistencyAudit(unittest.TestCase):
    def test_tests_readme_names_central_runner_and_direct_script_mode(self) -> None:
        text = read(TESTS_README)

        self.assertIn("scripts/reproduce_all.py", text)
        self.assertIn("central runner", text)
        self.assertIn("standalone", text)
        self.assertIn("run it directly", text)

    def test_reproduce_guide_names_quick_and_full_harness_commands(self) -> None:
        text = read(REPRODUCE)

        self.assertIn("python scripts/reproduce_all.py", text)
        self.assertIn("python scripts/reproduce_all.py --quick", text)
        self.assertIn("`--list`", text)

    def test_harness_docstring_names_runner_without_obsolete_claim(self) -> None:
        text = read(HARNESS)

        self.assertIn("central", text)
        self.assertIn("runner", text)
        self.assertIn("directly runnable", text)
        self.assertIn("tests/README.md", text)

    def test_public_reproduction_docs_do_not_claim_no_central_runner(self) -> None:
        scanned = {
            "REPRODUCE.md": read(REPRODUCE),
            "tests/README.md": read(TESTS_README),
            "scripts/reproduce_all.py": read(HARNESS),
        }

        failures: list[str] = []
        for label, text in scanned.items():
            folded = text.casefold()
            for phrase in OBSOLETE_NO_RUNNER_PHRASES:
                if phrase in folded:
                    failures.append(f"{label} still says {phrase!r}")

        self.assertEqual([], failures)


if __name__ == "__main__":
    unittest.main(verbosity=2)
