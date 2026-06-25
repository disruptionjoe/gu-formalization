#!/usr/bin/env python3
"""Audit the hourly Cycle 1 VZ subprincipal characteristic contract.

This audit checks status discipline, not the Clifford algebra. It enforces that
the artifact keeps FC-VZ-1 and FC-VZ-4 visible, refuses a full VZ upgrade,
names the actual-operator/subprincipal/extrinsic-curvature proof objects, and
contains rollback conditions for spacelike characteristics.
"""

from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = REPO_ROOT / "explorations" / "hourly-cycle1-vz-subprincipal-characteristic-contract-2026-06-24.md"

EXPECTED_VERDICT = "UNDERDEFINED_CONDITIONAL__ACTUAL_OPERATOR_AND_FC_VZ_4_NOT_COMPUTABLE_YET"

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. What Prior VZ Files Establish",
    "## 3. Strongest Positive Construction Attempt",
    "## 4. First Exact Obstruction Or Missing Proof Object",
    "## 5. What Would Falsify Or Demote The VZ Evasion Route",
    "## 6. Impact For No-Go-Class-Relative Map Wording",
    "## 7. Next Meaningful Computation",
    "## 8. Machine-Readable JSON Summary",
]

REQUIRED_ACTUAL_OPERATOR_FIELDS = {
    "sigma_1_D_GU_0_1_sector",
    "coefficient_a_of_d_A_star_psi",
    "coefficient_b_of_d_A_u",
    "coefficient_lambda_d_of_Phi_d",
    "Phi_2_Phi_d_Phi_F_F_xi_order_separation",
    "chirality_domains",
    "Q_sector_projectors",
    "coordinate_convention_trace_or_embedded",
    "Z_A_lower_order_ledger",
    "all_real_mixed_horizontal_vertical_covectors",
}

REQUIRED_SUBPRINCIPAL_TERMS = {
    "A_s_0",
    "B_s_0",
    "C_s_0",
    "E_s_0",
    "E_s_1_inverse_Schur_corrections",
    "Poisson_bracket_corrections",
    "invariant_subprincipal_correction",
    "Phi_F_zero_order_curvature_insertion",
    "spin_gimmel_connection_terms",
    "mass_gauge_fixing_and_Z_A_terms",
    "gamma_trace_constraint_source_K_mu_nu",
}

REQUIRED_EXTRINSIC_TERMS = {
    "II_s_H_equals_s_star_theta",
    "curved_horizontal_normal_frame_derivatives",
    "K_mu_nu_constraint_source",
    "Codazzi_section_pullback_terms",
}

REQUIRED_SPACELIKE_ROLLBACKS = {
    "spacelike_characteristic_found_for_actual_section_pulled_operator",
    "II_s_H_enters_effective_first_order_symbol",
    "K_mu_nu_constraint_source_changes_characteristic_cone",
    "gamma_trace_constraint_system_has_spacelike_characteristic",
}

FORBIDDEN_PROMOTIONS = [
    r"\bVERIFIED\b",
    r"\bfull VZ evasion\s+(?:is\s+)?(?:closed|proved|established)\b",
    r'"full_vz_evasion_claim"\s*:\s*true',
    r"\bFC-VZ-1\s*:\s*(?:closed|proved|established)\b",
    r"\bFC-VZ-4\s*:\s*(?:closed|proved|established)\b",
]


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing hourly VZ characteristic contract artifact: {DOC}") from exc


def load_summary(text: str) -> dict[str, Any]:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing fenced JSON summary after section 8")
    return json.loads(match.group(1))


class HourlyCycle1VzSubprincipalCharacteristicContractAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = load_summary(cls.text)

    def test_required_sections_are_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_fc_vz_1_and_fc_vz_4_are_visible(self) -> None:
        for gate_id in ["FC-VZ-1", "FC-VZ-4"]:
            self.assertIn(gate_id, self.text)
            self.assertIn(gate_id, self.summary["gates"])

    def test_no_full_vz_upgrade_or_verified_wording(self) -> None:
        self.assertFalse(self.summary.get("full_vz_evasion_claim"))
        self.assertFalse(self.summary.get("spacelike_characteristic_absence_computable_now"))
        self.assertEqual(self.summary["verdict"], EXPECTED_VERDICT)

        for pattern in FORBIDDEN_PROMOTIONS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE if pattern != r"\bVERIFIED\b" else 0),
                f"forbidden promotion pattern present: {pattern}",
            )

    def test_actual_operator_subprincipal_and_extrinsic_fields_exist(self) -> None:
        for key in ["actual_operator", "subprincipal", "extrinsic_curvature"]:
            self.assertIn(key, self.summary)
            self.assertIsInstance(self.summary[key], dict)
            self.assertIn("status", self.summary[key])

    def test_actual_operator_contract_names_required_fields(self) -> None:
        actual = self.summary["actual_operator"]
        self.assertEqual(actual["status"], "missing_source_closed_certificate")
        fields = set(actual["required_fields"])
        missing = REQUIRED_ACTUAL_OPERATOR_FIELDS - fields
        self.assertFalse(missing, f"missing actual-operator fields: {sorted(missing)}")
        self.assertIn("first_missing_operator", actual)
        self.assertIn("D_GU", actual["first_missing_operator"])

    def test_subprincipal_contract_names_required_terms(self) -> None:
        subprincipal = self.summary["subprincipal"]
        self.assertEqual(subprincipal["status"], "missing_actual_section_pulled_invariant_subprincipal_symbol")
        self.assertEqual(subprincipal["required_object"], "sigma_0_inv(S_Rs_4D_full)(x,eta)")
        terms = set(subprincipal["required_terms"])
        missing = REQUIRED_SUBPRINCIPAL_TERMS - terms
        self.assertFalse(missing, f"missing subprincipal terms: {sorted(missing)}")
        self.assertEqual(subprincipal["pass_condition"], "actual_coupled_characteristic_roots_confined_to_null_cone")

    def test_extrinsic_curvature_contract_names_required_terms(self) -> None:
        extrinsic = self.summary["extrinsic_curvature"]
        self.assertEqual(extrinsic["status"], "not_computed_for_actual_operator")
        terms = set(extrinsic["required_terms"])
        missing = REQUIRED_EXTRINSIC_TERMS - terms
        self.assertFalse(missing, f"missing extrinsic-curvature terms: {sorted(missing)}")
        self.assertIn("II_s_H", extrinsic["first_missing_term"])

    def test_spacelike_characteristic_rollback_conditions_are_present(self) -> None:
        fc_vz_4_rollbacks = set(self.summary["gates"]["FC-VZ-4"]["rollback_conditions"])
        subprincipal_rollbacks = set(self.summary["subprincipal"]["rollback_conditions"])
        extrinsic_rollbacks = set(
            self.summary["extrinsic_curvature"]["rollback_conditions_if_spacelike_characteristics_appear"]
        )
        combined = fc_vz_4_rollbacks | subprincipal_rollbacks | extrinsic_rollbacks
        missing = REQUIRED_SPACELIKE_ROLLBACKS - combined
        self.assertFalse(missing, f"missing spacelike rollback conditions: {sorted(missing)}")

        self.assertIn("spacelike", self.summary["exact_falsification_condition"])
        self.assertIn("nontrivial kernel", self.summary["exact_falsification_condition"])

    def test_no_go_map_wording_is_capped_not_upgraded(self) -> None:
        wording = self.summary["no_go_map_wording"]
        self.assertEqual(wording["status_cap"], "conditional_14D_and_4D_principal_symbol_only")
        self.assertIn("FC-VZ-1_actual_operator_E_block_open", wording["must_keep_visible"])
        self.assertIn("FC-VZ-4_actual_subprincipal_extrinsic_curvature_gate_open", wording["must_keep_visible"])
        self.assertIn("FC-VZ-1_closed_for_actual_D_GU", wording["forbidden_upgrade_until"])
        self.assertIn("FC-VZ-4_closed_for_actual_section_pulled_operator", wording["forbidden_upgrade_until"])

    def test_next_computation_is_an_extraction_and_characteristic_audit(self) -> None:
        next_steps = set(self.summary["next_meaningful_computation"])
        self.assertIn("source_closed_actual_D_GU_0_1_operator_certificate", next_steps)
        self.assertIn("E_actual_extraction_and_non_null_kernel_audit", next_steps)
        self.assertIn("sigma_0_inv_S_Rs_4D_full_with_II_s_H_Z_A_Poisson_and_K_mu_nu", next_steps)
        self.assertIn("coupled_RS_constraint_characteristic_matrix_non_null_kernel_test", next_steps)


if __name__ == "__main__":
    unittest.main(argv=sys.argv, verbosity=2)
