#!/usr/bin/env python3
"""Surface audit for the Lean robustness layer.

This is not a substitute for `lake build`. It checks that the repo-local Lean
certificate files and owner-surface references are present, and that certified
Lean proof bodies do not contain `sorry` or `axiom` placeholders.
"""

from __future__ import annotations

from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]

LEAN_ENTRYPOINTS = [
    ROOT / "Lean" / "GUFormalization.lean",
]

LEAN_LIBRARY_CERTIFICATES = [
    ROOT / "Lean" / "GUFormalization" / "Status.lean",
    ROOT / "Lean" / "GUFormalization" / "K3IndexArithmetic.lean",
    ROOT / "Lean" / "GUFormalization" / "W2Polynomial.lean",
    ROOT / "Lean" / "GUFormalization" / "LocatedNotForcedLegs.lean",
]

STANDALONE_LEAN_CERTIFICATES = [
    ROOT / "tests" / "big-swing" / "R4_TwoArena.lean",
]

OWNER_REFERENCES = {
    ROOT / "Lean" / "README.md": [
        "GUFormalization/LocatedNotForcedLegs.lean",
        "tests/big-swing/R4_TwoArena.lean",
    ],
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
    ROOT / "canon" / "two-arena-rep-theory-core-RESULTS.md": [
        "tests/big-swing/R4_TwoArena.lean",
        "Finset.card_sdiff_of_subset",
        "AddMonoid.addOrderOf_eq_one_iff",
    ],
}

FORBIDDEN_PROOF_PLACEHOLDER = re.compile(r"\b(?:sorry|axiom)\b")


def lean_without_comments_or_strings(text: str) -> str:
    """Return Lean source with comments and string literals blanked out."""
    out: list[str] = []
    i = 0
    block_depth = 0
    in_string = False
    escaped = False

    while i < len(text):
        char = text[i]
        nxt = text[i : i + 2]

        if block_depth:
            if nxt == "/-":
                block_depth += 1
                out.extend("  ")
                i += 2
            elif nxt == "-/":
                block_depth -= 1
                out.extend("  ")
                i += 2
            else:
                out.append("\n" if char == "\n" else " ")
                i += 1
            continue

        if in_string:
            out.append("\n" if char == "\n" else " ")
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                in_string = False
            i += 1
            continue

        if nxt == "/-":
            block_depth = 1
            out.extend("  ")
            i += 2
            continue

        if nxt == "--":
            out.extend("  ")
            i += 2
            while i < len(text) and text[i] != "\n":
                out.append(" ")
                i += 1
            continue

        if char == '"':
            in_string = True
            out.append(" ")
            i += 1
            continue

        out.append(char)
        i += 1

    if block_depth:
        raise ValueError("unterminated Lean block comment")
    if in_string:
        raise ValueError("unterminated Lean string literal")

    return "".join(out)


class LeanCertificateSurfaceAudit(unittest.TestCase):
    def test_lake_scaffold_exists(self) -> None:
        self.assertTrue((ROOT / "lean-toolchain").is_file())
        self.assertTrue((ROOT / "lakefile.lean").is_file())
        self.assertIn("mathlib", (ROOT / "lakefile.lean").read_text(encoding="utf-8"))

    def test_lean_files_exist_and_are_placeholder_free(self) -> None:
        for path in LEAN_ENTRYPOINTS + LEAN_LIBRARY_CERTIFICATES + STANDALONE_LEAN_CERTIFICATES:
            with self.subTest(path=path):
                self.assertTrue(path.is_file(), f"missing {path}")
                text = path.read_text(encoding="utf-8")
                proof_surface = lean_without_comments_or_strings(text)
                self.assertIsNone(FORBIDDEN_PROOF_PLACEHOLDER.search(proof_surface))

    def test_library_entrypoint_imports_certificates(self) -> None:
        text = (ROOT / "Lean" / "GUFormalization.lean").read_text(encoding="utf-8")
        for module in [
            "GUFormalization.Status",
            "GUFormalization.K3IndexArithmetic",
            "GUFormalization.W2Polynomial",
            "GUFormalization.LocatedNotForcedLegs",
        ]:
            with self.subTest(module=module):
                self.assertIn(f"import {module}", text)

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
