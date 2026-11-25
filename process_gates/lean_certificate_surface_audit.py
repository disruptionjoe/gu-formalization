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


def proof_placeholder_locations(text: str) -> list[tuple[int, str]]:
    """Locate forbidden source tokens after removing comments and strings.

    This is a source-text check, not Lean parsing or a transitive axiom audit.
    Theorem-level ``#print axioms`` receipts remain a separate check.
    """
    surface = lean_without_comments_or_strings(text)
    return [
        (surface.count("\n", 0, match.start()) + 1, match.group())
        for match in FORBIDDEN_PROOF_PLACEHOLDER.finditer(surface)
    ]


class LeanCertificateSurfaceAudit(unittest.TestCase):
    def test_no_lean_source_carries_proof_placeholders(self) -> None:
        """Use the same lexical check for every library and standalone source."""
        sources = set((ROOT / "Lean").rglob("*.lean")) | set(STANDALONE_LEAN_CERTIFICATES)
        self.assertTrue(sources, "no Lean source files found")
        offenders = []
        for source in sorted(sources):
            self.assertTrue(source.is_file(), f"missing {source}")
            for number, token in proof_placeholder_locations(source.read_text(encoding="utf-8")):
                offenders.append(f"{source.relative_to(ROOT)}:{number}: {token}")
        self.assertEqual([], offenders, "Lean source proof placeholders:\n  " + "\n  ".join(offenders))

    def test_placeholder_scanner_controls(self) -> None:
        clean = (
            '-- sorry axiom\n'
            '/- multiline\n sorry /- nested axiom -/\n-/\n'
            'def message := "sorry axiom -- /-"\n'
            'def escaped := "a \\"quoted\\" sorry"\n'
            'theorem sound : True := by trivial\n'
        )
        self.assertEqual([], proof_placeholder_locations(clean))
        self.assertEqual([(2, "sorry")], proof_placeholder_locations('-- harmless\ntheorem bad : True := by sorry\n'))
        self.assertEqual([(1, "axiom")], proof_placeholder_locations('axiom invented : False\n'))
        self.assertEqual([(1, "sorry")], proof_placeholder_locations('/- no `sorry` -/ theorem bad : True := by sorry\n'))
        self.assertEqual([], proof_placeholder_locations('def sorryCount := 0\n'))
        for malformed in ['/- unfinished', 'def bad := "unfinished']:
            with self.subTest(source=malformed), self.assertRaises(ValueError):
                proof_placeholder_locations(malformed)

    def test_lake_scaffold_exists(self) -> None:
        self.assertTrue((ROOT / "lean-toolchain").is_file())
        self.assertTrue((ROOT / "lakefile.lean").is_file())
        self.assertIn("mathlib", (ROOT / "lakefile.lean").read_text(encoding="utf-8"))

    def test_declared_lean_files_exist(self) -> None:
        certificate_paths = (
            [DEFAULT_TARGET_ENTRYPOINT]
            + default_target_certificates()
            + MANUAL_NON_DEFAULT_CERTIFICATES
            + STANDALONE_LEAN_CERTIFICATES
        )
        for path in certificate_paths:
            with self.subTest(path=path):
                self.assertTrue(path.is_file(), f"missing {path}")

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
