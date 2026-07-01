#!/usr/bin/env python3
"""Audit the hourly Cycle 1 effect-typed witness VZ operator contract.

This is a status and contract audit. It parses the artifact JSON and checks that
the transport interface keeps the actual-operator certificate as the first
obstruction, names source/projection/finality/loss fields, and refuses VZ,
hyperbolicity, causality, or spacelike-characteristic overclaims.
"""

from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = REPO_ROOT / "explorations" / "hourly-cycle1-effect-typed-witness-vz-operator-2026-06-25.md"

EXPECTED_VERDICT = (
    "BLOCKED_CONDITIONAL__EFFECT_TYPED_WITNESS_TRANSPORT_REDUCES_OBLIGATIONS_BUT_"
    "ACTUAL_DGU_01_OPERATOR_CERTIFICATE_MISSING"
)

REQUIRED_HEADINGS = [
    "## 1. Verdict: blocked / conditional",
    "## 2. What was derived directly from repo sources",
    "## 3. The strongest positive result",
    "## 4. The first exact obstruction or missing proof object",
    "## 5. The constructive next object that would remove or test the obstruction",
    "## 6. What this means for the relevant GU claim",
    "## 7. Next meaningful proof or computation step",
    "## 8. Machine-readable JSON summary",
]

REQUIRED_STAGES = {"source", "projection", "finality", "loss"}

REQUIRED_SOURCE_FIELDS = {
    "operator_source_primary_action_or_EL",
    "actual_operator_formula",
    "rolled_up_domain",
    "rolled_up_codomain",
    "chirality_domain_codomain",
    "signature_and_clifford_convention",
    "trace_or_embedded_coordinate_convention",
    "sigma_1_D_GU_0_1_sector",
    "coefficient_a_nonzero",
    "coefficient_b_nonzero",
    "coefficient_lambda_d_nonzero",
    "Phi_2_Phi_d_Phi_F_order_split",
    "Q_in_Q_out_projectors",
    "spin_3_2_projector",
    "E_actual_definition",
    "all_real_mixed_covector_domain",
    "extra_first_order_terms_absent_or_audited",
    "lower_order_Z_A_ledger",
    "section_pullback_rule",
    "constraint_blocks_gamma_trace_K_mu_nu",
    "rollback_conditions",
}

REQUIRED_PROJECTORS = {
    "P_Q_in",
    "P_Q_out",
    "spin_3_2_projector",
    "section_pullback_s_star",
    "gamma_trace_constraint_projection",
}

REQUIRED_LOSS_TERMS = {
    "Phi_F_zero_order_curvature_insertion",
    "Z_A_lower_order_ledger",
    "II_s_H_equals_s_star_theta",
    "curved_horizontal_normal_frame_derivatives",
    "spin_gimmel_connection_terms",
    "mass_and_gauge_fixing_terms",
    "Poisson_and_invariant_subprincipal_corrections",
    "constraint_blocks_gamma_trace_K_mu_nu",
    "extra_first_order_Q_or_R_terms",
}

REQUIRED_FORBIDDEN_CLAIMS = {
    "actual_GU_RS_operator_identified_from_current_sources",
    "FC-VZ-1_closed_for_actual_D_GU",
    "FC-VZ-4_closed_for_actual_section_pulled_operator",
    "full_VZ_evasion_closed",
    "hyperbolicity_established",
    "causality_established",
    "absence_of_spacelike_characteristics_proved",
    "Phi_F_supplies_F_xi_principal_block",
}

REQUIRED_ROLLBACKS = {
    "ActualDGU01OperatorCertificate_missing",
    "actual_operator_differs_from_D_roll_typed_spine",
    "coefficient_lambda_d_zero",
    "Phi_d_not_present_as_order_one_source_of_F_xi",
    "Phi_F_used_as_F_xi_principal_block",
    "extra_first_order_Q_or_R_term_has_non_null_kernel",
    "non_null_E_actual_kernel_found",
    "spacelike_characteristic_found_for_actual_section_pulled_operator",
    "II_s_H_enters_effective_first_order_symbol",
    "K_mu_nu_constraint_source_changes_characteristic_cone",
    "gamma_trace_constraint_system_has_spacelike_characteristic",
}

FORBIDDEN_PROMOTIONS = [
    r"\bVERIFIED\b",
    r"\bFC-VZ-1\s*:\s*(?:closed|proved|established)\b",
    r"\bFC-VZ-4\s*:\s*(?:closed|proved|established)\b",
    r"\bfull VZ evasion\s+(?:is\s+)?(?:closed|proved|established)\b",
    r"\bhyperbolicity\s+(?:is\s+)?(?:closed|proved|established)\b",
    r"\bcausality\s+(?:is\s+)?(?:closed|proved|established)\b",
    r"\babsence of spacelike characteristics\s+(?:is\s+)?(?:closed|proved|established)\b",
    r'"full_vz_evasion_claim"\s*:\s*true',
    r'"hyperbolicity_claim"\s*:\s*true',
    r'"causality_claim"\s*:\s*true',
    r'"spacelike_characteristic_absence_claim"\s*:\s*true',
]


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing effect-typed witness artifact: {DOC}") from exc


def load_summary(text: str) -> dict[str, Any]:
    match = re.search(
        r"## 8\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing fenced JSON summary after section 8")
    return json.loads(match.group(1))


class HourlyCycle1EffectTypedWitnessVzOperatorAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = load_summary(cls.text)

    def test_required_sections_are_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_verdict_and_top_level_anti_overclaim_flags(self) -> None:
        self.assertEqual(self.summary["verdict"], EXPECTED_VERDICT)
        self.assertFalse(self.summary["full_vz_evasion_claim"])
        self.assertFalse(self.summary["hyperbolicity_claim"])
        self.assertFalse(self.summary["causality_claim"])
        self.assertFalse(self.summary["spacelike_characteristic_absence_claim"])

    def test_no_forbidden_promotion_wording(self) -> None:
        for pattern in FORBIDDEN_PROMOTIONS:
            flags = 0 if pattern == r"\bVERIFIED\b" else re.IGNORECASE
            self.assertIsNone(
                re.search(pattern, self.text, flags=flags),
                f"forbidden promotion pattern present: {pattern}",
            )

    def test_transport_interface_is_specified_but_not_closing(self) -> None:
        transport = self.summary["effect_typed_witness_transport"]
        self.assertEqual(
            transport["status"],
            "interface_specified_transport_blocked_on_actual_operator_certificate",
        )
        self.assertTrue(transport["can_reduce_blocker_to_contract"])
        self.assertFalse(transport["can_close_vz_without_actual_operator_certificate"])
        self.assertEqual(transport["input_required_first"], "ActualDGU01OperatorCertificate")
        self.assertEqual(transport["typed_model_available"], "D_roll_typed_spine_candidate_only")
        self.assertFalse(transport["actual_operator_identified"])
        self.assertEqual(set(transport["stages"]), REQUIRED_STAGES)

    def test_source_contract_names_actual_operator_certificate_fields(self) -> None:
        source = self.summary["source_contract"]
        self.assertEqual(source["required_object"], "ActualDGU01OperatorCertificate")
        self.assertEqual(source["status"], "missing_source_closed_certificate")
        fields = set(source["required_fields"])
        missing = REQUIRED_SOURCE_FIELDS - fields
        self.assertFalse(missing, f"missing source fields: {sorted(missing)}")
        self.assertEqual(source["E_actual_definition"], "P_Q_out sigma_1(D_GU^epsilon) I_Q_in")

    def test_projection_contract_requires_projectors_and_actual_blocks(self) -> None:
        projection = self.summary["projection_contract"]
        self.assertEqual(projection["status"], "conditional_on_source_contract")
        missing_projectors = REQUIRED_PROJECTORS - set(projection["required_projectors"])
        self.assertFalse(missing_projectors, f"missing projectors: {sorted(missing_projectors)}")
        self.assertIn("E_actual", projection["required_blocks"])
        self.assertIn(
            "S_R_epsilon_equals_A_actual_minus_B_actual_E_actual_inverse_C_actual",
            projection["required_blocks"],
        )
        self.assertTrue(projection["all_real_mixed_covectors_required"])

    def test_finality_contract_keeps_fc_vz_1_and_fc_vz_4_open(self) -> None:
        finality = self.summary["finality_contract"]
        self.assertEqual(finality["status"], "conditional_not_closed")
        self.assertEqual(
            finality["FC-VZ-1"]["status"],
            "open_actual_operator_certificate_missing",
        )
        self.assertEqual(
            finality["FC-VZ-1"]["first_missing_proof_object"],
            "ActualDGU01OperatorCertificate",
        )
        self.assertEqual(
            finality["FC-VZ-4"]["status"],
            "open_actual_section_pulled_subprincipal_characteristic_certificate_missing",
        )
        self.assertEqual(
            finality["FC-VZ-4"]["required_object"],
            "ActualSectionPulledSubprincipalCharacteristicCertificate",
        )
        self.assertIn("null_cone", finality["FC-VZ-4"]["pass_condition"])

    def test_loss_contract_names_terms_and_harmlessness_condition(self) -> None:
        loss = self.summary["loss_contract"]
        self.assertEqual(loss["status"], "required_not_computed_for_actual_operator")
        missing = REQUIRED_LOSS_TERMS - set(loss["terms_to_classify"])
        self.assertFalse(missing, f"missing loss terms: {sorted(missing)}")
        self.assertIn("not_effective_first_order_characteristic_change", loss["harmless_only_if"])

    def test_strongest_positive_result_stays_conditional(self) -> None:
        positive = self.summary["strongest_positive_result"]
        self.assertTrue(positive["requires_actual_operator_certificate"])
        self.assertTrue(positive["requires_lambda_d_nonzero"])
        self.assertTrue(positive["requires_no_harmful_extra_first_order_loss_terms"])
        self.assertTrue(positive["does_not_close_full_vz"])

    def test_first_obstructions_and_relevant_claim_status_are_capped(self) -> None:
        self.assertEqual(self.summary["first_exact_obstruction"], "ActualDGU01OperatorCertificate")
        self.assertEqual(
            self.summary["second_obstruction"],
            "ActualSectionPulledSubprincipalCharacteristicCertificate",
        )
        self.assertEqual(
            self.summary["relevant_gu_claim_status"],
            "coherent_conditional_route_only_not_actual_vz_closure",
        )

    def test_forbidden_claims_and_rollbacks_are_machine_readable(self) -> None:
        forbidden = set(self.summary["forbidden_claims"])
        missing_forbidden = REQUIRED_FORBIDDEN_CLAIMS - forbidden
        self.assertFalse(missing_forbidden, f"missing forbidden claims: {sorted(missing_forbidden)}")

        rollbacks = set(self.summary["rollback_conditions"])
        missing_rollbacks = REQUIRED_ROLLBACKS - rollbacks
        self.assertFalse(missing_rollbacks, f"missing rollback conditions: {sorted(missing_rollbacks)}")

    def test_next_steps_are_certificate_then_projection_then_characteristic_audit(self) -> None:
        next_steps = self.summary["next_meaningful_proof_or_computation"]
        self.assertEqual(
            next_steps[0],
            "construct_ActualDGU01OperatorCertificate_from_primary_GU_action_or_EL_sources",
        )
        self.assertIn("project_E_actual_from_sigma_1_D_GU", next_steps)
        self.assertIn("run_all_real_mixed_covector_non_null_kernel_audit", next_steps)
        self.assertIn("compute_actual_section_pulled_sigma_0_inv_S_Rs_4D_full", next_steps)
        self.assertIn("classify_loss_terms_as_harmless_or_characteristic_changing", next_steps)


if __name__ == "__main__":
    unittest.main(argv=sys.argv, verbosity=2)
