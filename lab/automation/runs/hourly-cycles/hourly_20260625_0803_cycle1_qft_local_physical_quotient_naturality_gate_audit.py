#!/usr/bin/env python3
"""Audit LocalPhysicalFieldQuotientAndNaturalityLemma_V1.

The audit parses the embedded JSON summary and enforces that the artifact
keeps the QFT route source-facing: no proof restart, no target-imported
rho_AB/CHSH/Bell claims, and exact naming of the missing quotient/descent
object required before P_fin^b can be tested.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unittest
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0803-cycle1-qft-local-physical-quotient-naturality-gate.md"
)

EXPECTED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Specific GU claim or bridge under test",
    "## 3. Owned output path and sources read first",
    "## 4. What was derived directly from repo sources",
    "## 5. Strongest positive construction attempt",
    "## 6. First exact obstruction or missing object",
    "## 7. Impact if closed",
    "## 8. Falsification/demotion condition",
    "## 9. Next meaningful computation or proof/source step",
    "## 10. Machine-readable JSON summary",
]

MISSING_OBJECT = "SourceDefinedLocalPhysicalFieldEquivalenceRelationAndDescentData_V1"
REQUIRED_QFT_MAP = "P_fin^b: F_phys^b(O) -> K_b"

FORBIDDEN_TARGET_DERIVATION_PATTERNS = [
    r"\brho_AB\s+is\s+derived\b",
    r"\bderived\s+rho_AB\b",
    r"\bCHSH\s+is\s+derived\b",
    r"\bderived\s+CHSH\b",
    r"\bBell\s+violation\s+is\s+derived\b",
    r"\bproves\s+Bell\s+violation\b",
    r"\bproof\s+restart\s+allowed\b",
    r"\bQFT\s+recovery\s+promoted\b",
]


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing artifact: {DOC}") from exc


def extract_summary(text: str) -> dict[str, Any]:
    match = re.search(
        r"## 10\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class LocalPhysicalFieldQuotientNaturalityGateAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_required_sections_present(self) -> None:
        for heading in EXPECTED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_artifact_identity_and_verdict(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "LocalPhysicalFieldQuotientAndNaturalityLemma_V1",
        )
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0803")
        self.assertEqual(self.summary["cycle"], 1)
        self.assertEqual(self.summary["lane"], 5)
        self.assertEqual(self.summary["verdict_class"], "underdefined")
        self.assertEqual(
            self.summary["verdict"],
            "UNDERDEFINED_MISSING_SOURCE_PHYSICAL_QUOTIENT_AND_DESCENT_DATA",
        )

    def test_source_facing_requirements_are_not_defined_yet(self) -> None:
        state = self.summary["decision_state"]
        for key in [
            "source_facing_quotient_defined",
            "source_defined_F_phys_b_O",
            "P_fin_b_defined",
            "K_b_source_codomain_defined",
            "descent_naturality_defined",
            "valid_reconstruction_spec",
            "accepted_for_routing",
            "proof_restart_allowed",
            "qft_recovery_promoted",
            "target_import_detected",
            "global_no_go_promoted",
        ]:
            self.assertIs(state[key], False, key)

    def test_required_components_include_quotient_pfin_kb_and_naturality(self) -> None:
        components = self.summary["source_compatible_components"]
        self.assertEqual(
            components["physical_quotient"]["candidate_name"],
            "F_phys^b(O) = R_raw^b(O) / ~_phys^b(O)",
        )
        self.assertEqual(components["physical_quotient"]["status"], "missing")
        self.assertEqual(
            components["finite_codomain"]["status"],
            "representation_carrier_only_not_source_codomain",
        )
        self.assertEqual(components["finite_extraction"]["required_form"], REQUIRED_QFT_MAP)
        self.assertEqual(components["finite_extraction"]["status"], "missing")
        self.assertEqual(components["descent_naturality"]["status"], "missing")
        for square in [
            "local_restriction_square",
            "observation_pullback_square",
            "gauge_action_square",
            "observer_change_square",
            "quotient_descent_square",
        ]:
            self.assertIn(square, components["descent_naturality"]["required_squares"])

    def test_first_exact_obstruction_is_named_and_blocks_pfin_restart(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["id"], MISSING_OBJECT)
        self.assertTrue(obstruction["missing"])
        self.assertIn("F_phys^b(O)_is_not_an_object", obstruction["why_first"])
        required = set(obstruction["required_components"])
        for item in [
            "typed_R_raw_b_O",
            "source_defined_phys_equivalence_relation",
            "F_phys_b_O_quotient",
            "source_defined_K_b",
            "P_fin_b_representative_rule",
            "descent_proof",
            "naturality_under_restriction_pullback_gauge_observer_change_and_quotient",
        ]:
            self.assertIn(item, required)

        blocked = set(obstruction["blocks_before"])
        for item in [
            "SourceDefinedFiniteLocalExtractionOperation_V1",
            "one_local_mode_image_certificate",
            "H_raw",
            "Q_b",
            "H_phys",
            "rho_AB",
            "CHSH",
            "Bell_violation",
        ]:
            self.assertIn(item, blocked)

    def test_strongest_attempt_is_shell_not_closed_claim(self) -> None:
        attempt = self.summary["strongest_positive_construction_attempt"]
        self.assertEqual(attempt["id"], "LocalPhysicalFieldQuotientShell_V1")
        self.assertEqual(
            attempt["classification"],
            "source_facing_uninhabited_quotient_shell",
        )
        self.assertTrue(attempt["does_not_use_target_data"])
        self.assertIn("physical_equivalence_relation", attempt["why_not_closed"])
        for source_piece in [
            "Y14_X4_separation",
            "Observerse_or_section_pullback",
            "Y_native_field_content",
            "inhomogeneous_gauge_group_context",
        ]:
            self.assertIn(source_piece, attempt["uses_source_machinery"])

    def test_non_import_guard_blocks_target_qft_data(self) -> None:
        forbidden = set(self.summary["non_import_condition"]["forbidden_inputs"])
        for item in [
            "rho_AB",
            "CHSH_value",
            "Bell_state",
            "Pauli_observables",
            "Bell_violation_target",
            "free_or_Fock_or_Hadamard_vacuum",
            "Gram_matrix_selected_by_target_fit",
            "ordinary_QFT_recovery_target",
            "target_covariance_fit",
        ]:
            self.assertIn(item, forbidden)

    def test_impact_and_next_step_do_not_skip_to_qft_recovery(self) -> None:
        impact = self.summary["impact_if_closed"]
        self.assertEqual(
            impact["current_branch_status"],
            "open_but_underdefined_at_source_physical_quotient_and_descent",
        )
        for item in ["QFT_recovery", "vacuum_selection", "rho_AB", "CHSH", "Bell_violation"]:
            self.assertIn(item, impact["does_not_unlock_directly"])

        next_step = self.summary["next_meaningful_computation_or_proof_step"]
        self.assertEqual(next_step["id"], MISSING_OBJECT)
        for item in [
            "SourceDefinedFiniteLocalExtractionOperation_V1",
            "one_mode_image_certificate",
            "H_raw",
            "rho_AB",
            "CHSH",
        ]:
            self.assertIn(item, next_step["required_before"])
        self.assertIn("prove_descent_before_finite_image_tests", next_step["steps"])
        self.assertIn("import_control", next_step["expected_outcomes"])

    def test_falsification_and_demotion_conditions_are_exact(self) -> None:
        condition = self.summary["falsification_or_demotion_condition"]
        self.assertIn("R_raw_b_O_phys_equivalence_F_phys_b_O", condition["falsified_by"])
        self.assertIn("imports_target_QFT_data", condition["demote_to_fail_if"])
        self.assertIn("fails_descent", condition["demote_to_fail_if"])
        self.assertIn("fails_naturality", condition["demote_to_fail_if"])
        self.assertFalse(condition["global_no_go_promoted"])

    def test_no_target_imported_rho_chsh_bell_derivation_claims(self) -> None:
        for pattern in FORBIDDEN_TARGET_DERIVATION_PATTERNS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                f"forbidden target derivation phrase matched: {pattern}",
            )


def audit_summary() -> dict[str, Any]:
    text = read_doc()
    summary = extract_summary(text)
    return {
        "document": str(DOC.relative_to(REPO_ROOT)),
        "artifact": summary["artifact"],
        "verdict": summary["verdict"],
        "verdict_class": summary["verdict_class"],
        "proof_restart_allowed": summary["decision_state"]["proof_restart_allowed"],
        "target_import_detected": summary["decision_state"]["target_import_detected"],
        "first_exact_obstruction": summary["first_exact_obstruction"]["id"],
        "next_step": summary["next_meaningful_computation_or_proof_step"]["id"],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Audit the QFT local physical quotient and naturality gate."
    )
    parser.add_argument("--json", action="store_true", help="Print audit summary as JSON.")
    args, _remaining = parser.parse_known_args(argv)

    if args.json:
        print(json.dumps(audit_summary(), indent=2, sort_keys=True))
        return 0

    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(
            LocalPhysicalFieldQuotientNaturalityGateAudit
        )
    )
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
