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

DEFAULT_TARGET_ENTRYPOINT = ROOT / "Lean" / "GUFormalization.lean"
LOCAL_MODULE_PREFIX = "GUFormalization."
IMPORT_LINE = re.compile(r"^import\s+([A-Za-z0-9_.]+)\s*$", re.MULTILINE)

# Manual `#print axioms` receipt: not in the default lake target (run via
# `lake env lean`), but its source is still in scope for the placeholder scan.
MANUAL_NON_DEFAULT_CERTIFICATES = [
    ROOT / "Lean" / "GUFormalization" / "ResidualSelectionAxioms.lean",
]

STANDALONE_LEAN_CERTIFICATES = [
    ROOT / "tests" / "big-swing" / "R4_TwoArena.lean",
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
    ROOT / "lab" / "methods" / "claim-status-consistency.md": [
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


def local_import_modules(entrypoint: Path = DEFAULT_TARGET_ENTRYPOINT) -> list[str]:
    """Return local modules imported by the default target in source order."""
    return [
        module
        for module in IMPORT_LINE.findall(entrypoint.read_text(encoding="utf-8"))
        if module.startswith(LOCAL_MODULE_PREFIX)
    ]


def module_source(module: str) -> Path:
    return ROOT / "Lean" / (module.replace(".", "/") + ".lean")


def default_target_certificates() -> list[Path]:
    return [module_source(module) for module in local_import_modules()]


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
    def test_no_lean_source_carries_sorry_or_undeclared_axiom(self) -> None:
        """Enforce the precondition the LEAN-VERIFIED label already asserts.

        Added 2026-08-08, register P-H5.  The lane ledger defines LEAN-VERIFIED as
        "default or named target typechecks, with no `sorry` or unreported axioms,
        and the owner cites it".  As of 2026-08-08 the tree genuinely carries no
        `sorry` -- the only textual hits are docstrings stating their own absence --
        so this gate fixes no present defect.  What it fixes is that the label's
        precondition was unenforced: nothing would have caught a `sorry` being
        introduced under a row already marked LEAN-VERIFIED.

        Note this is a SOURCE-TEXT check, not a kernel check.  A real guarantee is
        `#print axioms` on the built target; that receipt lives in
        ResidualSelectionAxioms.lean and is deliberately outside the default
        target, informational and non-enforcing, as the ledger states.  This test
        does not upgrade that receipt and must not be cited as if it had.
        """
        lean_root = Path(__file__).resolve().parent.parent / "Lean"
        if not lean_root.is_dir():
            self.skipTest("no Lean/ tree")

        offenders = []
        for source in sorted(lean_root.rglob("*.lean")):
            for number, line in enumerate(source.read_text(errors="ignore").splitlines(), 1):
                stripped = line.strip()
                if stripped.startswith("--") or stripped.startswith("/-"):
                    continue
                # a docstring line that merely says "there is no sorry" is prose
                if re.search(r"\bsorry\b", line) and "no `sorry`" not in line and "No `sorry`" not in line:
                    offenders.append(f"{source.name}:{number}: {stripped[:80]}")

        self.assertEqual(
            [], offenders,
            "Lean sources carrying `sorry` while the lane ledger defines "
            "LEAN-VERIFIED as requiring none:\n  " + "\n  ".join(offenders),
        )

    def test_lake_scaffold_exists(self) -> None:
        self.assertTrue((ROOT / "lean-toolchain").is_file())
        self.assertTrue((ROOT / "lakefile.lean").is_file())
        self.assertIn("mathlib", (ROOT / "lakefile.lean").read_text(encoding="utf-8"))

    def test_lean_files_exist_and_are_placeholder_free(self) -> None:
        certificate_paths = (
            [DEFAULT_TARGET_ENTRYPOINT]
            + default_target_certificates()
            + MANUAL_NON_DEFAULT_CERTIFICATES
            + STANDALONE_LEAN_CERTIFICATES
        )
        for path in certificate_paths:
            with self.subTest(path=path):
                self.assertTrue(path.is_file(), f"missing {path}")
                text = path.read_text(encoding="utf-8")
                proof_surface = lean_without_comments_or_strings(text)
                self.assertIsNone(FORBIDDEN_PROOF_PLACEHOLDER.search(proof_surface))

    def test_library_inventory_is_derived_from_default_entrypoint(self) -> None:
        modules = local_import_modules()
        self.assertEqual(len(modules), len(set(modules)), "duplicate local imports")

        imported = set(default_target_certificates())
        manual = set(MANUAL_NON_DEFAULT_CERTIFICATES)
        library = set((ROOT / "Lean" / "GUFormalization").glob("*.lean"))
        self.assertEqual(
            library,
            imported | manual,
            "every library certificate must be imported by the default target or "
            "declared as a manual non-default certificate",
        )
        self.assertFalse(imported & manual, "manual receipts must stay outside the default target")

    def test_default_target_inventory_is_mapped_by_owner_surfaces(self) -> None:
        readme = (ROOT / "Lean" / "README.md").read_text(encoding="utf-8")
        ledger = (ROOT / "lab" / "process" / "lean-verification-lane-LEDGER.md").read_text(
            encoding="utf-8"
        )
        for path in default_target_certificates() + MANUAL_NON_DEFAULT_CERTIFICATES:
            relative = path.relative_to(ROOT).as_posix()
            readme_relative = path.relative_to(ROOT / "Lean").as_posix()
            with self.subTest(path=relative):
                self.assertIn(f"`{readme_relative}`", readme)
                self.assertIn(f"`{relative}`", ledger)

        for path in STANDALONE_LEAN_CERTIFICATES:
            relative = path.relative_to(ROOT).as_posix()
            with self.subTest(path=relative):
                self.assertIn(f"`{relative}`", readme)

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
