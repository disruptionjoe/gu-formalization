#!/usr/bin/env python3
"""Audit SourceDefinedLocalPhysicalFieldEquivalenceRelationAndDescentData_V1.

The audit parses the embedded JSON summary and enforces the cycle 2 QFT
schema-gate contract: required quotient/descent/naturality fields are explicit,
no finite extraction or proof restart is valid until they are source-defined,
and no target-imported QFT state claims are promoted.
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
    / "hourly-20260625-0803-cycle2-qft-source-equivalence-descent-schema-gate.md"
)

EXPECTED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Specific GU claim or bridge under test",
    "## 3. Sources read first",
    "## 4. Equivalence/descent/naturality schema",
    "## 5. Strongest positive construction attempt",
    "## 6. First exact obstruction or missing object",
    "## 7. Impact if closed",
    "## 8. Falsification/demotion condition",
    "## 9. Next meaningful proof/source step",
    "## 10. Machine-readable JSON summary",
]

REQUIRED_SCHEMA_FIELDS = {
    "branch_context",
    "raw_local_field_object",
    "source_generators",
    "equations_constraints_policy",
    "gauge_action_policy",
    "observer_change_policy",
    "physical_equivalence_relation",
    "physical_quotient",
    "restriction_functoriality",
    "finite_codomain",
    "representative_extraction_rule",
    "descent_proof",
    "descended_extraction",
    "naturality_squares",
    "non_import_guard",
}

REQUIRED_SQUARES = {
    "restriction_square",
    "observation_pullback_square",
    "gauge_action_square",
    "observer_change_square",
    "quotient_descent_square",
}

FORBIDDEN_TARGET_CLAIM_PATTERNS = [
    r"\brho_AB\s+is\s+derived\b",
    r"\bderived\s+rho_AB\b",
    r"\bCHSH\s+is\s+derived\b",
    r"\bderived\s+CHSH\b",
    r"\bBell\s+violation\s+is\s+derived\b",
    r"\bproves\s+Bell\s+violation\b",
    r"\bQFT\s+recovery\s+is\s+promoted\b",
    r"\bvalid\s+QFT\s+state\s+restart\b",
]


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing schema gate artifact: {DOC}") from exc


def extract_summary(text: str) -> dict[str, Any]:
    match = re.search(
        r"## 10\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class SourceEquivalenceDescentSchemaGateAudit(unittest.TestCase):
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
            "SourceDefinedLocalPhysicalFieldEquivalenceRelationAndDescentData_V1",
        )
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0803")
        self.assertEqual(self.summary["cycle"], 2)
        self.assertEqual(self.summary["lane"], 5)
        self.assertEqual(
            self.summary["verdict"], "BLOCKED_SCHEMA_SPECIFIED_SOURCE_DATA_ABSENT"
        )
        self.assertEqual(self.summary["verdict_class"], "blocked")

    def test_decision_state_blocks_all_downstream_restart(self) -> None:
        state = self.summary["decision_state"]
        self.assertTrue(state["schema_defined"])
        for key in [
            "schema_inhabited_by_source_data",
            "source_defined_equivalence_relation",
            "source_defined_descent_data",
            "source_defined_naturality_data",
            "source_defined_F_phys_b_O",
            "source_defined_K_b",
            "P_fin_b_defined",
            "valid_finite_extraction_restart",
            "valid_qft_state_restart",
            "local_mode_image_work_allowed",
            "rho_AB_work_allowed",
            "CHSH_work_allowed",
            "Bell_work_allowed",
            "target_import_detected",
            "global_no_go_promoted",
        ]:
            self.assertIs(state[key], False, key)

    def test_required_schema_fields_and_statuses(self) -> None:
        fields = self.summary["required_schema_fields"]
        self.assertEqual(set(fields), REQUIRED_SCHEMA_FIELDS)
        self.assertEqual(fields["branch_context"]["status"], "partial_shell")
        self.assertEqual(fields["raw_local_field_object"]["status"], "shell_only")
        self.assertEqual(fields["physical_equivalence_relation"]["status"], "missing")
        self.assertEqual(fields["physical_quotient"]["status"], "not_defined")
        self.assertEqual(
            fields["finite_codomain"]["status"], "representation_carrier_only"
        )
        self.assertEqual(fields["descent_proof"]["status"], "missing")
        self.assertEqual(fields["descended_extraction"]["status"], "missing")
        self.assertEqual(fields["naturality_squares"]["status"], "missing")
        self.assertEqual(fields["non_import_guard"]["status"], "specified_guard_only")

    def test_schema_requires_exact_quotient_descent_and_naturality_data(self) -> None:
        fields = self.summary["required_schema_fields"]
        self.assertIn(
            "source_defined_congruence_generators_for_tilde_phys_b_O",
            fields["physical_equivalence_relation"]["required_data"],
        )
        self.assertIn(
            "F_phys_b_O_equals_R_raw_b_O_mod_tilde_phys_b_O",
            fields["physical_quotient"]["required_data"],
        )
        self.assertIn("quotient_map_q_O", fields["physical_quotient"]["required_data"])
        self.assertIn(
            "phi_tilde_phys_psi_implies_P_raw_phi_equals_P_raw_psi",
            fields["descent_proof"]["required_data"],
        )
        self.assertIn(
            "P_fin_b_O_from_F_phys_b_O_to_K_b",
            fields["descended_extraction"]["required_data"],
        )
        self.assertEqual(set(self.summary["required_naturality_squares"]), REQUIRED_SQUARES)

    def test_strongest_positive_attempt_is_schema_shell_only(self) -> None:
        attempt = self.summary["strongest_positive_construction_attempt"]
        self.assertEqual(attempt["id"], "SourceFacingEquivalenceDescentSchemaShell_V1")
        self.assertEqual(attempt["classification"], "schema_shell_not_source_inhabited")
        self.assertTrue(attempt["does_not_use_target_data"])
        self.assertIn("required_fields", attempt["positive_result"])
        self.assertIn("source_congruence_generators", attempt["why_not_closed"])
        for source_piece in [
            "Y14_X4_separation",
            "observation_pullback_from_Y_to_X",
            "zero_form_and_one_form_field_context",
            "inhomogeneous_gauge_group_context",
        ]:
            self.assertIn(source_piece, attempt["uses_source_machinery"])

    def test_first_obstruction_blocks_fphys_pfin_kb_and_bell_side_work(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(
            obstruction["id"], "source_defined_congruence_generators_for_tilde_phys_b_O"
        )
        self.assertEqual(
            obstruction["parent_missing_object"],
            "SourceDefinedLocalPhysicalFieldEquivalenceRelationAndDescentData_V1",
        )
        self.assertTrue(obstruction["missing"])
        self.assertIn("F_phys_b_O_is_not_a_mathematical_object", obstruction["why_first"])
        blocked = set(obstruction["blocks_before"])
        for item in [
            "F_phys^b(O)",
            "P_fin^b",
            "K_b_as_source_codomain",
            "local_mode_images",
            "rho_AB",
            "CHSH",
            "Bell_work",
        ]:
            self.assertIn(item, blocked)

    def test_restart_policy_requires_source_defined_fields(self) -> None:
        policy = self.summary["restart_policy"]
        self.assertFalse(policy["finite_extraction_restart_allowed"])
        self.assertFalse(policy["qft_state_restart_allowed"])
        required = set(policy["required_before_restart"])
        for item in [
            "source_defined_physical_equivalence_relation",
            "F_phys_b_O_quotient",
            "restriction_functoriality",
            "source_defined_K_b",
            "P_raw_b_O",
            "descent_proof",
            "naturality_squares",
            "non_import_proof",
        ]:
            self.assertIn(item, required)

    def test_non_import_guard_blocks_target_imported_qft_state_claims(self) -> None:
        forbidden = set(self.summary["non_import_condition"]["forbidden_selectors"])
        for item in [
            "target_Hilbert_state",
            "target_covariance",
            "rho_AB",
            "CHSH_value",
            "Bell_state",
            "Bell_violation_target",
            "Pauli_observables",
            "free_or_Fock_or_Hadamard_vacuum",
            "Gram_matrix_selected_by_target_fit",
            "ordinary_QFT_recovery_target",
        ]:
            self.assertIn(item, forbidden)

    def test_impact_and_next_step_do_not_skip_to_qft_state_work(self) -> None:
        impact = self.summary["impact_if_closed"]
        self.assertEqual(
            impact["current_branch_status"],
            "blocked_at_source_equivalence_descent_and_naturality_data",
        )
        for item in ["QFT_recovery", "vacuum_selection", "rho_AB", "CHSH", "Bell_violation"]:
            self.assertIn(item, impact["does_not_unlock_directly"])

        next_step = self.summary["next_meaningful_proof_or_source_step"]
        self.assertEqual(
            next_step["id"],
            "CandidateCongruenceGeneratorsForLocalGUPhysicalFieldEquivalence_V1",
        )
        for item in ["F_phys^b(O)", "P_fin^b", "rho_AB", "CHSH", "Bell_work"]:
            self.assertIn(item, next_step["required_before"])
        self.assertIn("blocked_missing_congruence_generators", next_step["expected_outcomes"])
        self.assertIn("import_control", next_step["expected_outcomes"])

    def test_falsification_and_demotion_conditions_are_exact(self) -> None:
        condition = self.summary["falsification_or_demotion_condition"]
        self.assertIn("R_raw_tilde_phys_F_phys_q_O", condition["falsified_by"])
        self.assertIn("descent", condition["falsified_by"])
        self.assertIn("naturality", condition["falsified_by"])
        self.assertIn("non_import_proof", condition["falsified_by"])
        self.assertIn("imports_target_QFT_structures", condition["demote_to_fail_if"])
        self.assertIn("fails_descent", condition["demote_to_fail_if"])
        self.assertIn("fails_required_naturality_squares", condition["demote_to_fail_if"])
        self.assertFalse(condition["global_no_go_promoted"])

    def test_no_target_imported_qft_state_derivation_claims(self) -> None:
        for pattern in FORBIDDEN_TARGET_CLAIM_PATTERNS:
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
        "schema_defined": summary["decision_state"]["schema_defined"],
        "schema_inhabited_by_source_data": summary["decision_state"][
            "schema_inhabited_by_source_data"
        ],
        "valid_finite_extraction_restart": summary["decision_state"][
            "valid_finite_extraction_restart"
        ],
        "valid_qft_state_restart": summary["decision_state"]["valid_qft_state_restart"],
        "first_exact_obstruction": summary["first_exact_obstruction"]["id"],
        "next_step": summary["next_meaningful_proof_or_source_step"]["id"],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Audit the QFT source equivalence/descent schema gate."
    )
    parser.add_argument("--json", action="store_true", help="Print audit summary as JSON.")
    args, _remaining = parser.parse_known_args(argv)

    if args.json:
        print(json.dumps(audit_summary(), indent=2, sort_keys=True))
        return 0

    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(
            SourceEquivalenceDescentSchemaGateAudit
        )
    )
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
