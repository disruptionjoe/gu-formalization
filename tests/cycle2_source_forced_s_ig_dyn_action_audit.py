#!/usr/bin/env python3
"""Audit the Cycle 2 source-forced S_IG_dyn action gate.

This is a structural source/anti-fitting audit, not a physics computation. It
checks that the artifact separates a legitimate formal Branch 3 action template
from a source-forced existence theorem, keeps Lambda/dark-energy non-claims
explicit, includes S_IG_dyn/J_IG/theta_eff/total-current conservation language,
and exposes machine-readable verdict and rollback conditions.
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
    / "cycle2-source-forced-s-ig-dyn-action-gate-2026-06-24.md"
)

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Candidate Action Functional And Allowed Source Terms",
    "## 3. Variation/Current Contract: `delta S_IG_dyn / delta A`, `J_IG`, `theta_eff`",
    "## 4. Conservation Identity Needed And What Proves It",
    "## 5. Why This Does Or Does Not Generate `Z_theta`, `C_Rtheta`, `xi_eff`",
    "## 6. First Exact Obstruction Or No-Go",
    "## 7. Impact For Branch 3/Dark Energy",
    "## 8. Next Meaningful Computation",
    "## 9. Machine-Readable JSON Summary",
]

REQUIRED_TEXT_TERMS = [
    "S_IG_dyn",
    "J_IG",
    "theta_eff",
    "D_A^* theta_eff = 0",
    "SourceForcedIGDynamicsSelector",
    "SourceForcedIGDynamicsPacket_V0",
    "Target-fitting exclusion",
    "Source-forcing rule",
]

REQUIRED_ROLLBACKS = {
    "S_IG_dyn_absent",
    "S_IG_dyn_template_only",
    "SourceForcedIGDynamicsSelector_missing",
    "K_IG_not_selected",
    "Z_U_or_V_src_target_fitted",
    "J_IG_not_derived_from_delta_A",
    "theta_eff_missing_total_current_terms",
    "bare_theta_source_retained_in_Branch_3",
    "Noether_identity_not_written",
    "total_current_conservation_not_proved",
    "Z_theta_or_C_Rtheta_claimed_without_FLRW_reduction",
    "xi_eff_fitted_not_generated",
    "bare_Lambda_inserted",
    "bare_Rtheta_inserted",
    "DESI_Rubin_window_used_upstream",
    "dark_energy_derivation_claimed_before_action_packet_closes",
}


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing Cycle 2 S_IG_dyn action artifact: {DOC}") from exc


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 9\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class SourceForcedSIGDynActionAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_required_deliverable_sections_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_required_source_current_terms_are_present(self) -> None:
        for term in REQUIRED_TEXT_TERMS:
            self.assertIn(term, self.text)
        contract = self.summary["variation_current_contract"]
        self.assertIn("J_IG", contract["delta_S_IG_dyn_delta_A"])
        self.assertEqual(contract["source_law"], "D_A^*F_A=theta_eff")
        self.assertIn("J_IG", contract["theta_eff"])

    def test_verdict_and_promotion_decision_are_machine_readable(self) -> None:
        self.assertEqual(self.summary["mission_posture"], "Mission_A_constructive_obstruction")
        self.assertEqual(self.summary["verdict"], "underdefined")
        self.assertFalse(self.summary["promotion_decision"]["promoted"])
        self.assertEqual(
            self.summary["promotion_decision"]["reason"],
            "SourceForcedIGDynamicsSelector_missing",
        )
        self.assertEqual(
            self.summary["first_exact_obstruction"]["id"],
            "SourceForcedIGDynamicsSelector",
        )

    def test_formal_template_is_not_promoted_to_source_forced_action(self) -> None:
        action = self.summary["candidate_action"]
        self.assertTrue(action["legitimate_formal_template"])
        self.assertFalse(action["source_forced"])
        self.assertIn("parent_kinetic_pairing", action["allowed_source_terms"])
        self.assertIn("bare_Lambda", action["excluded_target_fit_terms"])
        self.assertEqual(
            self.summary["first_exact_obstruction"]["candidate_operator_status"],
            "natural_but_not_source_selected_or_unique",
        )

    def test_source_forcing_and_target_fitting_are_separated(self) -> None:
        separation = self.summary["source_forcing_target_fitting_separation"]
        self.assertTrue(separation["replacement_target_check_required"])
        self.assertIn("K_IG_selected_before_targets", separation["source_forcing_requires"])
        forbidden = set(separation["target_fitting_forbidden_inputs"])
        self.assertIn("DESI_Rubin_window", forbidden)
        self.assertIn("xi_eff_target", forbidden)
        self.assertIn("Schwarzschild_Kerr_residual_after_evaluation", forbidden)

    def test_no_lambda_or_dark_energy_derivation_claim(self) -> None:
        non_claims = self.summary["explicit_non_claims"]
        for key in [
            "GU_derives_Lambda",
            "GU_cancels_Lambda",
            "GU_derives_dark_energy",
            "GU_derives_Z_theta",
            "GU_derives_C_Rtheta",
            "GU_derives_xi_eff",
            "bare_Lambda_source_derived",
            "bare_Rtheta_source_derived",
        ]:
            self.assertFalse(non_claims[key], key)
        impact = self.summary["branch3_impact"]
        self.assertEqual(
            impact["current_dark_energy_status"],
            "blocked_before_source_forced_action_and_coefficients",
        )

    def test_conservation_contract_is_total_current_not_bare_theta(self) -> None:
        conservation = self.summary["conservation_contract"]
        self.assertEqual(conservation["target"], "D_A^*theta_eff=0")
        self.assertEqual(conservation["proving_identity"], "source_sector_gauge_Noether_identity")
        self.assertIn("N_U(E_U)", conservation["identity_shape"])
        self.assertEqual(conservation["current_status"], "not_written_for_source_forced_action")
        self.assertIn("field_transformation_rules", conservation["requires"])

    def test_z_theta_c_rtheta_xi_eff_are_not_generated(self) -> None:
        coeffs = self.summary["coefficient_generation"]
        self.assertFalse(coeffs["Z_theta_generated"])
        self.assertFalse(coeffs["C_Rtheta_generated"])
        self.assertFalse(coeffs["xi_eff_generated"])
        self.assertEqual(coeffs["reason"], "FLRW_projection_packet_missing")
        self.assertIn("scalar_mode_u0", coeffs["needed_before_coefficients"])

    def test_ordered_missing_objects_and_obligations_are_precise(self) -> None:
        ordered = self.summary["ordered_missing_objects"]
        self.assertEqual(ordered[0], "SourceForcedIGDynamicsSelector")
        self.assertLess(ordered.index("K_IG"), ordered.index("J_IG"))
        self.assertLess(ordered.index("J_IG"), ordered.index("theta_eff"))
        self.assertLess(ordered.index("theta_eff"), ordered.index("source_sector_Noether_identity"))
        obligations = set(self.summary["source_obligations"])
        self.assertIn("derive_J_IG_and_theta_eff", obligations)
        self.assertIn("prove_D_A_star_theta_eff_conservation", obligations)

    def test_rollback_conditions_are_machine_readable(self) -> None:
        rollbacks = set(self.summary["rollback_conditions"])
        missing = REQUIRED_ROLLBACKS - rollbacks
        self.assertFalse(missing, f"missing rollback conditions: {sorted(missing)}")
        self.assertIn("Rollback conditions", self.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
