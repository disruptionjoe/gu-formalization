#!/usr/bin/env python3
"""Audit the Cycle 2 actual-operator VZ E-block certificate.

This is a status and specification audit. It does not prove the Clifford
algebra. It checks that the artifact separates the formal typed-spine inverse
from the actual GU E-block, keeps FC-VZ-1 explicit and open, names the
domain/codomain/cone/signature requirements, and exposes verdict and rollback
conditions in machine-readable JSON.
"""

from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = REPO_ROOT / "explorations" / "cycle-gates-and-audits" / "cycle2-vz-actual-operator-e-block-certificate-2026-06-24.md"

EXPECTED_VERDICT = "ACTUAL_OPERATOR_E_BLOCK_CERTIFICATE_OPEN__TYPED_SPINE_FORMAL_BLOCK_TESTED_ONLY"

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. What current E-block tests prove",
    "## 3. Actual-operator E-block certificate definition",
    "## 4. Cone, signature, domain/codomain, and typed-spine requirements",
    "## 5. Failure modes that would kill FC-VZ-1",
    "## 6. Impact for VZ evasion and what remains for FC-VZ-4",
    "## 7. Next meaningful computation",
    "## 8. Machine-readable JSON summary",
]

REQUIRED_SPEC_TERMS = [
    "domain",
    "codomain",
    "cone",
    "signature",
    "signature(g_Y) = (9,5)",
    "Clifford convention",
    "G^2 = q Id",
    "Q_in^epsilon",
    "Q_out^epsilon",
    "sigma_1(D_GU^epsilon)",
]

REQUIRED_MATRIX_DATA = {
    "actual_sigma_1_D_GU_0_1_sector",
    "coefficient_a_of_i_xi_psi",
    "coefficient_b_of_xi_tensor_u",
    "coefficient_lambda_d_of_Phi_2_d_A_psi",
    "Phi_2_Phi_d_Phi_F_F_xi_order_separation",
    "chiral_Gamma_j_P_Q_in_P_Q_out_normalizations",
    "one_coordinate_convention_trace_or_embedded",
    "all_extra_first_order_Q_block_terms_or_proof_absent",
    "all_real_mixed_horizontal_vertical_covectors_quantified",
}

REQUIRED_ROLLBACKS = {
    "actual_operator_E_block_has_non_null_kernel",
    "coefficient_a_of_d_A_star_vanishes",
    "coefficient_b_of_d_A_u_vanishes",
    "actual_Q_sector_not_S_plus_Im_j_or_has_extra_principal_component",
    "signature_or_Clifford_convention_not_G_squared_equals_q_Id",
    "mixed_horizontal_vertical_non_null_covector_not_covered",
    "hidden_first_order_Z_A_or_gauge_fixing_terms_modify_Q_block",
    "determinant_circularity_used_instead_of_direct_E_actual_kernel_proof",
}

FORBIDDEN_FULL_VZ_PROMOTIONS = [
    r"\bfull VZ evasion\s+(?:is\s+)?(?:closed|proved|verified|established)\b",
    r"\bVZ verified\b",
    r"\bproof-grade VZ causality\b",
    r'"full_vz_evasion_claim"\s*:\s*true',
    r"\bFC-VZ-1\s*:\s*(?:closed|proved|verified)\b",
]


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing Cycle 2 VZ E-block artifact: {DOC}") from exc


def load_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing fenced JSON summary after section 8")
    return json.loads(match.group(1))


class Cycle2VzActualOperatorEBlockAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = load_summary(cls.text)

    def test_required_sections_are_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_no_full_vz_evasion_claim_or_fc_vz_1_promotion(self) -> None:
        self.assertFalse(self.summary.get("full_vz_evasion_claim"))
        self.assertEqual(self.summary["fc_vz_1_status"], "open_actual_operator_E_block_certificate_not_closed")
        self.assertNotIn("CLOSED", self.summary["fc_vz_1_status"].upper().replace("NOT_CLOSED", ""))

        for pattern in FORBIDDEN_FULL_VZ_PROMOTIONS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                f"forbidden promotion pattern present: {pattern}",
            )

    def test_fc_vz_1_is_explicit_in_text_and_json(self) -> None:
        self.assertIn("FC-VZ-1", self.text)
        self.assertTrue(self.summary["fc_vz_1_explicit"])
        self.assertIn("fc_vz_1_status", self.summary)

    def test_actual_vs_toy_e_block_status_is_separated(self) -> None:
        self.assertTrue(self.summary["actual_vs_toy_separated"])
        actual = self.summary["actual_operator_e_block_status"]
        toy = self.summary["toy_or_embedded_e_block_status"]

        self.assertEqual(actual["status"], "open_not_proved")
        self.assertEqual(toy["status"], "tested_formal_typed_spine_block_only")
        self.assertNotEqual(actual["status"], toy["status"])
        self.assertIn("does_not_prove", toy)
        self.assertIn("actual_D_GU_has_this_E_block", toy["does_not_prove"])

    def test_domain_codomain_cone_and_signature_are_present(self) -> None:
        for term in REQUIRED_SPEC_TERMS:
            self.assertIn(term, self.text)

        actual = self.summary["actual_operator_e_block_status"]
        for key in ["domain", "codomain", "cone", "signature", "definition"]:
            self.assertIn(key, actual)
            self.assertTrue(actual[key])

        self.assertIn("signature(g_Y)=(9,5)", actual["signature"])
        self.assertIn("q=g_Y^{-1}(xi,xi)!=0", actual["cone"])

    def test_verdict_and_rollback_conditions_are_machine_readable(self) -> None:
        self.assertEqual(self.summary["verdict"], EXPECTED_VERDICT)
        rollbacks = set(self.summary["rollback_conditions"])
        missing = REQUIRED_ROLLBACKS - rollbacks
        self.assertFalse(missing, f"missing rollback conditions: {sorted(missing)}")
        self.assertGreaterEqual(len(rollbacks), 8)

    def test_required_matrix_operator_data_is_named(self) -> None:
        matrix_data = set(self.summary["required_matrix_operator_data"])
        missing = REQUIRED_MATRIX_DATA - matrix_data
        self.assertFalse(missing, f"missing required matrix/operator data: {sorted(missing)}")

    def test_certificate_matrix_keeps_coordinate_conventions_separate(self) -> None:
        target = self.summary["certificate_target_matrix"]
        self.assertIn("trace_coordinate", target)
        self.assertIn("embedded_coordinate", target)
        self.assertIn("13/7", target["trace_coordinate"])
        self.assertIn("13/98", target["embedded_coordinate"])
        self.assertIn("one chosen convention", self.text)

    def test_fc_vz_4_remains_open_with_concrete_remaining_work(self) -> None:
        self.assertEqual(self.summary["fc_vz_4_status"], "open_subprincipal_section_pulled_gate_not_closed")
        remaining = set(self.summary["fc_vz_4_remaining"])
        self.assertIn("compute_sigma_0_inv_S_Rs_4D_full", remaining)
        self.assertIn("include_II_s_H", remaining)
        self.assertIn("prove_no_effective_first_order_spacelike_characteristic", remaining)


if __name__ == "__main__":
    unittest.main(argv=sys.argv, verbosity=2)
