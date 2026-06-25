#!/usr/bin/env python3
"""Audit the Cycle 2 ActualDGU01OperatorCertificate schema artifact.

This is a structural contract audit, not a proof of VZ closure. It checks that
the artifact supplies a machine-checkable schema with source, projection,
finality, loss, accept/fail decisions, and rollback conditions while forbidding
promotion to actual operator identification, FC-VZ closure, VZ evasion,
hyperbolicity, causality, or absence of spacelike characteristics.
"""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = (
    REPO_ROOT
    / "explorations"
    / "hourly-cycle2-actual-dgu-operator-certificate-schema-2026-06-25.md"
)

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. What Was Derived Directly From Repo Sources",
    "## 3. Strongest Positive Construction Attempt",
    "## 4. First Exact Obstruction Or Missing Proof Object",
    "## 5. Constructive Next Object",
    "## 6. Impact On GU Claim",
    "## 7. Next Meaningful Proof Or Computation Step",
    "## 8. Machine-Readable JSON Summary",
]

REQUIRED_SOURCE_FIELDS = {
    "operator_source_primary_action_or_EL",
    "actual_operator_formula",
    "rolled_up_domain",
    "rolled_up_codomain",
    "base_and_cone",
    "signature_and_clifford_convention",
    "chirality_domain_codomain",
    "coordinate_convention",
    "sigma_1_D_GU_0_1_sector",
    "coefficient_a_nonzero",
    "coefficient_b_nonzero",
    "coefficient_lambda_d_nonzero",
}

REQUIRED_PROJECTION_FIELDS = {
    "Q_in_Q_out_projectors",
    "spin_3_2_projector",
    "E_actual_definition",
    "Schur_blocks",
    "all_real_mixed_covector_domain",
}

REQUIRED_LOSS_FIELDS = {
    "Phi_2_Phi_d_Phi_F_order_split",
    "extra_order_one_terms",
    "lower_order_Z_A_ledger",
    "section_pullback_rule",
    "constraint_blocks_gamma_trace_K_mu_nu",
}

REQUIRED_ROLLBACKS = {
    "ActualDGU01OperatorCertificate_missing",
    "operator_source_primary_action_or_EL_missing",
    "actual_operator_differs_from_D_roll_typed_spine",
    "actual_D_GU_0_1_block_absent",
    "rolled_up_domain_or_codomain_mismatch",
    "trace_coordinate_and_embedded_coordinate_conventions_mixed",
    "coefficient_a_zero",
    "coefficient_b_zero",
    "coefficient_lambda_d_zero",
    "Phi_d_not_present_as_order_one_source_of_F_xi",
    "Phi_F_used_as_F_xi_principal_block",
    "Q_in_Q_out_projectors_missing_or_unnormalized",
    "proof_checks_only_pure_horizontal_or_pure_vertical_covectors",
    "hidden_first_order_terms_placed_in_Z_A_without_projection_or_kernel_audit",
    "extra_first_order_Q_or_R_term_has_non_null_kernel",
    "non_null_E_actual_kernel_found",
    "actual_R_sector_Schur_block_differs_and_has_non_null_kernel",
    "section_pullback_payload_missing",
    "II_s_H_enters_effective_first_order_symbol",
    "K_mu_nu_constraint_source_changes_characteristic_cone",
    "gamma_trace_constraint_system_has_spacelike_characteristic",
    "spacelike_characteristic_found_for_actual_section_pulled_operator",
    "standalone_GU_RS_Lagrangian_has_VZ_spacelike_roots",
}

FORBIDDEN_POSITIVE_PATTERNS = [
    r"actual GU Rarita-Schwinger operator (is|has been) identified",
    r"FC-VZ-1 (is|has been) closed for actual",
    r"FC-VZ-4 (is|has been) closed",
    r"VZ evasion (is|has been) (closed|proved|established)",
    r"hyperbolicity (is|has been) established",
    r"causality (is|has been) established",
    r"absence of spacelike characteristics (is|has been) proved",
]


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing certificate schema artifact: {DOC}") from exc


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class ActualDGUOperatorCertificateSchemaAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_required_deliverable_sections_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_verdict_and_current_decision_are_machine_readable(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "HOURLY_CYCLE2_ACTUAL_DGU_OPERATOR_CERTIFICATE_SCHEMA",
        )
        self.assertEqual(
            self.summary["schema_version"],
            "ACTUAL_DGU_01_OPERATOR_CERTIFICATE_SCHEMA_V1",
        )
        self.assertEqual(self.summary["verdict_class"], "underdefined_blocked")
        self.assertEqual(
            self.summary["decision_for_current_sources"],
            "BLOCKED_MISSING_SOURCE_OBJECT",
        )
        self.assertEqual(
            self.summary["certificate"]["first_missing_field"],
            "source.operator_source_primary_action_or_EL",
        )

    def test_schema_groups_and_required_fields_are_present(self) -> None:
        groups = set(self.summary["certificate"]["required_groups"])
        self.assertTrue(
            {"source", "projection", "finality", "loss", "rollback_conditions"}
            <= groups
        )
        self.assertFalse(REQUIRED_SOURCE_FIELDS - set(self.summary["source_required_fields"]))
        self.assertFalse(
            REQUIRED_PROJECTION_FIELDS - set(self.summary["projection_required_fields"])
        )
        self.assertFalse(REQUIRED_LOSS_FIELDS - set(self.summary["loss_required_fields"]))

        for field in REQUIRED_SOURCE_FIELDS | REQUIRED_PROJECTION_FIELDS | REQUIRED_LOSS_FIELDS:
            self.assertIn(field, self.text)

    def test_accept_fail_decisions_are_explicit(self) -> None:
        for decision in [
            "ACCEPT_ACTUAL_OPERATOR_CERTIFICATE",
            "FAIL_SOURCE_PROVENANCE",
            "FAIL_OPERATOR_DIFFERENCE",
            "FAIL_COEFFICIENT_ZERO",
            "FAIL_E_KERNEL",
            "FAIL_LOSS_LEDGER",
            "BLOCKED_MISSING_SOURCE_OBJECT",
        ]:
            self.assertIn(decision, self.text)
        self.assertIn("accept_if", self.text)
        self.assertIn("fail_if", self.text)

    def test_finality_gates_remain_open_and_conditional(self) -> None:
        finality = self.summary["finality_required_fields"]
        self.assertEqual(
            finality["FC-VZ-1"]["status"],
            "open_actual_operator_certificate_missing",
        )
        self.assertEqual(
            finality["FC-VZ-4"]["status"],
            "open_actual_section_pulled_subprincipal_characteristic_certificate_missing",
        )
        construction = self.summary["strongest_positive_construction"]
        self.assertTrue(construction["requires_actual_operator_certificate"])
        self.assertTrue(construction["requires_lambda_d_nonzero"])
        self.assertTrue(construction["requires_no_harmful_extra_first_order_loss_terms"])
        self.assertTrue(construction["does_not_close_full_vz"])

    def test_forbidden_claims_are_false_and_not_promoted_in_text(self) -> None:
        non_claims = self.summary["explicit_non_claims"]
        for key, value in non_claims.items():
            self.assertIs(value, False, f"{key} should be false")

        for pattern in FORBIDDEN_POSITIVE_PATTERNS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                f"forbidden positive claim matched: {pattern}",
            )

    def test_required_rollback_conditions_are_machine_readable(self) -> None:
        rollbacks = set(self.summary["rollback_conditions"])
        missing = REQUIRED_ROLLBACKS - rollbacks
        self.assertFalse(missing, f"missing rollback conditions: {sorted(missing)}")

    def test_first_obstruction_and_next_object_are_exact(self) -> None:
        self.assertEqual(
            self.summary["first_exact_obstruction"],
            "ActualDGU01OperatorCertificate.source.operator_source_primary_action_or_EL",
        )
        self.assertEqual(
            self.summary["constructive_next_object"],
            "ActualDGU01OperatorCertificateInstance_V1",
        )
        self.assertIn("d_A u + lambda_d Phi_2(d_A psi)", self.text)
        self.assertIn("lambda_d != 0", self.text)

    def test_next_steps_are_computational_not_summary_only(self) -> None:
        steps = set(self.summary["next_meaningful_step"])
        self.assertIn("compute_E_actual_from_sigma_1_D_GU", steps)
        self.assertIn(
            "audit_E_actual_over_all_real_mixed_non_null_14D_covectors",
            steps,
        )
        self.assertIn("classify_extra_first_order_loss_terms", steps)


if __name__ == "__main__":
    unittest.main()
