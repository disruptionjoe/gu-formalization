#!/usr/bin/env python3
"""W189 -- machine-checkable verification of the hardening register's factual claims.

The register (explorations/W189-hardening-register-2026-07-14.md) asserts a small
set of checkable repo facts about the CURRENT tree. This gate verifies them so the
register's hygiene rows are not merely asserted:

  1. Exactly two process gates are RED, and they are the two the register names
     (explorations_readme_surface_map_audit, explorations_top_level_file_boundary_audit).
  2. The readme-surface-map gate is red specifically because `explorations/wave46`
     exists on disk but is not declared in explorations/README.md (H01).
  3. The top-level-file-boundary gate is red specifically because there are many
     more top-level dated exploration notes than the gate's 4-entry allow-list (H02).

Run:  python tests/W189_hardening_register_checks.py
"""
from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GATES = ROOT / "process_gates"
EXPL = ROOT / "explorations"

NAMED_RED = {
    "explorations_readme_surface_map_audit",
    "explorations_top_level_file_boundary_audit",
}


def _run_gate(name: str) -> int:
    proc = subprocess.run(
        [sys.executable, str(GATES / f"{name}.py")],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return proc.returncode


def _all_gate_names() -> list[str]:
    return sorted(
        p.stem
        for p in GATES.glob("*.py")
        if p.stem != "__init__"
    )


class W189RegisterChecks(unittest.TestCase):
    def test_exactly_the_two_named_gates_are_red(self) -> None:
        red = {name for name in _all_gate_names() if _run_gate(name) != 0}
        self.assertEqual(
            NAMED_RED,
            red,
            f"register claims exactly {sorted(NAMED_RED)} are red; actual red set: {sorted(red)}",
        )

    def test_wave46_exists_but_is_undeclared(self) -> None:
        self.assertTrue((EXPL / "wave46").is_dir(), "explorations/wave46 should exist on disk")
        readme = (EXPL / "README.md").read_text(encoding="utf-8")
        self.assertNotIn("wave46", readme, "H01: wave46 should be MISSING from the README surface map")
        # And wave45 (the last declared one) IS present, so the omission is isolated.
        self.assertIn("wave45", readme)

    def test_top_level_notes_far_exceed_allowlist(self) -> None:
        top = {p.name for p in EXPL.glob("*.md") if p.name != "README.md" and p.is_file()}
        # The gate's allow-list is 4; the arc has left ~200 dated notes at top level.
        self.assertGreater(
            len(top),
            50,
            "H02: the boundary gate's 4-entry allow-list is stale against the dated-note convention",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
