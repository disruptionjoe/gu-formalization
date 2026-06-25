#!/usr/bin/env python3
"""Audit the hourly Cycle 2 VZ actual 0/1 operator certificate gate.

This is a status and specification audit. It checks that the artifact requires
the ActualDGU01OperatorCertificate before FC-VZ-1 or FC-VZ-4 can close, keeps
Phi_d/Phi_F and order splits explicit, and refuses to treat typed-spine
candidates as the actual GU operator.
"""

from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = REPO_ROOT / "explorations" / "hourly-cycle2-vz-actual-operator-certificate-gate-2026-06-24.md"

EXPECTED_VERDICT = "UNDERDEFINED_BLOCKED__ACTUAL_DGU_01_OPERATOR_CERTIFICATE_MISSING_TYPED_SPINE_ONLY"

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Actual operator certificate fields",
    "## 3. What prior VZ files establish",
    "## 4. Strongest positive operator-certificate attempt",
    "## 5. First exact missing proof object",
    "## 6. Impact for FC-VZ-1/FC-VZ-4 and no-go map wording",
    "## 7. Rollback/falsification conditions",
    "## 8. Next meaningful computation",
    "## 9. Machine-readable JSON summary",
]

REQUIRED_CERTIFICATE_FIELDS = {
    "operator_source_primary_action_or_EL",
    "rolled_up_domain",
    "rolled_up_codomain",
    "chirality_domain_codomain",
    "signature_and_clifford_convention",
    "sigma_1_D_GU_0_1_sector",
    "coefficient_a_of_i_xi_psi",
    "coefficient_b_of_xi_tensor_u",
    "coefficient_lambda_d_of_Phi_d",
    "Phi_2_Phi_d_Phi_F_F_xi_order_split",
    "connection_Z_A_lower_order_ledger",
    "section_pullback_s_star_D_GU",
    "constraint_blocks_gamma_trace_K_mu_nu",
    "E_actual_source_P_Q_out_sigma_1_D_GU_I_Q_in",
    "Q_in_Q_out_projectors",
    "coordinate_convention_trace_or_embedded",
    "all_real_mixed_covectors",
    "extra_first_order_terms_absent_or_kernel_audited",
}

REQUIRED_FC_VZ_4_TERMS = {
    "A_s_full",
    "B_s_full",
    "C_s_full",
    "E_s_full",
    "E_s_inverse_Schur_corrections",
    "II_s_H_equals_s_star_theta",
    "curved_horizontal_normal_frame_derivatives",
    "Phi_F_zero_order_curvature_insertion",
    "Z_A_lower_order_ledger",
    "spin_gimmel_connection",
    "mass_and_gauge_fixing_terms",
    "Poisson_and_invariant_subprincipal_corrections",
    "constraint_blocks_gamma_trace_K_mu_nu",
    "coupled_RS_constraint_characteristic_matrix",
}

REQUIRED_ROLLBACKS = {
    "actual_D_GU_lacks_rolled_up_0_1_block",
    "coefficient_a_zero",
    "coefficient_b_zero",
    "actual_Q_sector_has_extra_first_order_component_with_non_null_kernel",
    "non_null_E_actual_kernel_found",
    "mixed_covectors_not_quantified",
    "spacelike_characteristic_found_for_actual_section_pulled_operator",
    "II_s_H_enters_effective_first_order_symbol",
    "K_mu_nu_constraint_source_changes_characteristic_cone",
    "gamma_trace_constraint_system_has_spacelike_characteristic",
}

FORBIDDEN_PROMOTIONS = [
    r"\bVERIFIED\b",
    r"\bFC-VZ-1\s*:\s*(?:closed|proved|established)\b",
    r"\bFC-VZ-4\s*:\s*(?:closed|proved|established)\b",
    r"\bactual GU RS operator\s+(?:is\s+)?(?:identified|proved|established)\b",
    r"\bfull VZ evasion\s+(?:is\s+)?(?:closed|proved|established)\b",
    r'"full_vz_evasion_claim"\s*:\s*true',
]


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing hourly Cycle 2 VZ operator certificate artifact: {DOC}") from exc


def load_summary(text: str) -> dict[str, Any]:
    match = re.search(
        r"## 9\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing fenced JSON summary after section 9")
    return json.loads(match.group(1))


class HourlyCycle2VzActualOperatorCertificateGateAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = load_summary(cls.text)

    def test_required_sections_are_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_verdict_and_actual_operator_status_are_not_promoted(self) -> None:
        self.assertEqual(self.summary["verdict"], EXPECTED_VERDICT)
        self.assertEqual(
            self.summary["actual_operator_status"],
            "typed_spine_candidates_only_actual_DGU_not_identified",
        )
        self.assertFalse(self.summary["full_vz_evasion_claim"])

        certificate = self.summary["actual_operator_certificate"]
        self.assertEqual(certificate["status"], "missing_source_closed_certificate")
        self.assertEqual(certificate["current_repo_identification"], "D_roll_typed_spine_candidate_only")
        self.assertFalse(certificate["decides_actual_operator"])

    def test_no_verified_or_full_vz_promotion_wording(self) -> None:
        for pattern in FORBIDDEN_PROMOTIONS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE if "VERIFIED" not in pattern else 0),
                f"forbidden promotion pattern present: {pattern}",
            )

    def test_certificate_names_required_actual_operator_fields(self) -> None:
        fields = set(self.summary["actual_operator_certificate"]["required_fields"])
        missing = REQUIRED_CERTIFICATE_FIELDS - fields
        self.assertFalse(missing, f"missing certificate fields: {sorted(missing)}")

        certificate = self.summary["actual_operator_certificate"]
        self.assertIn("E_roll^epsilon", certificate["rolled_up_domain"])
        self.assertIn("F_roll^epsilon", certificate["rolled_up_codomain"])
        self.assertIn("sigma_1(D_GU^epsilon)", certificate["E_actual_definition"])

    def test_phi_d_phi_f_and_order_split_are_explicit(self) -> None:
        phi = self.summary["phi_conventions"]
        self.assertTrue(phi["must_keep_separate"])
        self.assertEqual(phi["Phi_2"]["order"], 0)
        self.assertEqual(phi["Phi_d"]["order"], 1)
        self.assertEqual(phi["F_xi"]["order"], 1)
        self.assertEqual(phi["Phi_F"]["order"], 0)
        self.assertIn("not_source_of_F_xi", phi["Phi_F"]["role"])

        order_split = self.summary["order_split"]
        self.assertIn("Phi_d_principal_F_xi", order_split["principal_order_one_terms"])
        self.assertIn("Phi_F_zero_order_curvature_insertion", order_split["lower_order_Z_A_terms"])
        self.assertIn("constraint_blocks", self.text)

    def test_fc_vz_1_and_fc_vz_4_visibility_and_status(self) -> None:
        for gate_id in ["FC-VZ-1", "FC-VZ-4"]:
            self.assertIn(gate_id, self.text)
            self.assertIn(gate_id, self.summary)
            self.assertTrue(self.summary[gate_id]["visibility_required"])

        self.assertEqual(self.summary["FC-VZ-1"]["status"], "open_actual_operator_certificate_missing")
        self.assertEqual(
            self.summary["FC-VZ-4"]["status"],
            "open_actual_section_pulled_subprincipal_constraint_gate_missing",
        )

    def test_fc_vz_4_requires_section_pullback_subprincipal_and_constraints(self) -> None:
        fc_vz_4 = self.summary["FC-VZ-4"]
        self.assertEqual(fc_vz_4["required_object"], "sigma_0_inv(S_Rs_4D_full)(x,eta)")
        required_terms = set(fc_vz_4["required_terms"])
        missing = REQUIRED_FC_VZ_4_TERMS - required_terms
        self.assertFalse(missing, f"missing FC-VZ-4 terms: {sorted(missing)}")

    def test_rollback_conditions_cover_actual_operator_and_spacelike_failures(self) -> None:
        fc_vz_1_rollbacks = set(self.summary["FC-VZ-1"]["rollback_conditions"])
        fc_vz_4_rollbacks = set(self.summary["FC-VZ-4"]["rollback_conditions"])
        combined = fc_vz_1_rollbacks | fc_vz_4_rollbacks
        missing = REQUIRED_ROLLBACKS - combined
        self.assertFalse(missing, f"missing rollback conditions: {sorted(missing)}")

    def test_no_go_map_wording_is_capped(self) -> None:
        wording = self.summary["no_go_map_wording"]
        self.assertEqual(
            wording["status_cap"],
            "conditional_14D_gated_on_FC_VZ_1_and_4D_principal_symbol_only",
        )
        self.assertIn("FC-VZ-1_actual_operator_certificate_open", wording["must_keep_visible"])
        self.assertIn("FC-VZ-4_actual_subprincipal_constraint_gate_open", wording["must_keep_visible"])
        self.assertIn("actual_D_GU_0_1_operator_certificate_closed", wording["forbidden_until"])

    def test_forbidden_claims_record_no_actual_operator_or_full_vz_closure(self) -> None:
        forbidden = set(self.summary["forbidden_claims"])
        self.assertIn("actual_GU_RS_operator_identified_from_current_sources", forbidden)
        self.assertIn("FC-VZ-1_closed_for_actual_D_GU", forbidden)
        self.assertIn("FC-VZ-4_closed_for_actual_section_pulled_operator", forbidden)
        self.assertIn("full_VZ_evasion_closed", forbidden)
        self.assertIn("Phi_F_supplies_F_xi_principal_block", forbidden)

    def test_next_meaningful_computation_is_extraction_then_characteristic_audit(self) -> None:
        next_steps = set(self.summary["next_meaningful_computation"])
        self.assertIn("extract_source_closed_actual_D_GU_0_1_operator_certificate", next_steps)
        self.assertIn("project_E_actual_from_sigma_1_D_GU", next_steps)
        self.assertIn("run_all_real_mixed_covector_Clifford_kernel_audit", next_steps)
        self.assertIn("compute_actual_section_pulled_sigma_0_inv_S_Rs_4D_full", next_steps)
        self.assertIn("build_coupled_RS_constraint_characteristic_matrix", next_steps)


if __name__ == "__main__":
    unittest.main(argv=sys.argv, verbosity=2)
