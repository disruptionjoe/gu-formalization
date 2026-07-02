#!/usr/bin/env python3
"""Surface audit for the Lean robustness layer.

This is not a substitute for `lake build`. It checks that the repo-local Lean
certificate files and owner-surface references are present, and that certified
Lean files do not contain `sorry`.
"""

from __future__ import annotations

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]

LEAN_FILES = [
    ROOT / "Lean" / "GUFormalization.lean",
    ROOT / "Lean" / "GUFormalization" / "Status.lean",
    ROOT / "Lean" / "GUFormalization" / "K3IndexArithmetic.lean",
    ROOT / "Lean" / "GUFormalization" / "W2Polynomial.lean",
]

OWNER_REFERENCES = {
    ROOT / "canon" / "w2-y14-spin-structure.md": [
        "GUFormalization.W2Polynomial",
        "w2Sym2Rank3_eq_e1_sq_add_e2",
        "w2TensorLineRank3_eq_e2_add_l_sq",
    ],
    ROOT
    / "lab"
    / "active-research"
    / "topological-generation-count-families-k3-chi-gate-2026-06-26.md": [
        "GUFormalization.K3IndexArithmetic",
        "brstStyle_is_raw_minus_two_spinor_ghosts",
    ],
    ROOT / "lab" / "process" / "runbooks" / "claim-status-consistency-quality-workflow.md": [
        "GUFormalization.Status",
        "AllowedByDeps",
    ],
}


class LeanCertificateSurfaceAudit(unittest.TestCase):
    def test_lake_scaffold_exists(self) -> None:
        self.assertTrue((ROOT / "lean-toolchain").is_file())
        self.assertTrue((ROOT / "lakefile.lean").is_file())
        self.assertIn("mathlib", (ROOT / "lakefile.lean").read_text(encoding="utf-8"))

    def test_lean_files_exist_and_are_sorry_free(self) -> None:
        for path in LEAN_FILES:
            with self.subTest(path=path):
                self.assertTrue(path.is_file(), f"missing {path}")
                text = path.read_text(encoding="utf-8")
                self.assertNotIn("sorry", text)

    def test_owner_surfaces_reference_certificates(self) -> None:
        for path, required in OWNER_REFERENCES.items():
            with self.subTest(path=path):
                text = path.read_text(encoding="utf-8")
                for needle in required:
                    self.assertIn(needle, text)

    def test_local_check_script_exists(self) -> None:
        script = ROOT / "lab" / "automation" / "check-lean.ps1"
        self.assertTrue(script.is_file())
        self.assertIn("lake build", script.read_text(encoding="utf-8"))

    def test_github_workflow_exists(self) -> None:
        workflow = ROOT / ".github" / "workflows" / "lean.yml"
        self.assertTrue(workflow.is_file())
        text = workflow.read_text(encoding="utf-8")
        self.assertIn("leanprover/lean-action@v1", text)
        self.assertIn("build: true", text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
