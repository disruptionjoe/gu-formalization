#!/usr/bin/env python3
"""Audit the Cycle 1 Branch 3 dynamical IG total-current gate.

This is a structural proof-contract audit, not a physics computation. It checks
that the artifact keeps Mission A posture, avoids Lambda/dark-energy promotion,
states the Branch 3 S_IG_dyn/theta_eff/total-current contract, names the exact
missing proof object, records rollback/falsification conditions, and exposes a
machine-readable summary.
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
    / "cycle-gates-and-audits" / "cycle1-branch3-dynamical-ig-current-gate-2026-06-24.md"
)

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. What Was Derived Directly From Repo Sources",
    "## 3. Strongest Positive Branch 3 Construction Possible Now",
    "## 4. First Exact Obstruction Or Missing Proof Object",
    "## 5. Constructive Next Object That Would Remove Or Test The Obstruction",
    "## 6. What This Means For Lambda/Dark Energy And Source-Geometry Claims",
    "## 7. Next Meaningful Proof Or Computation Step",
    "## 8. Machine-Readable JSON Summary",
]

REQUIRED_CONTRACT_TERMS = [
    "S_IG_dyn",
    "theta_eff",
    "Theorem_B3_TotalCurrentConservation",
    "D_A^* theta_eff = 0",
    "DynamicIGActionPacket_B3",
    "Branch3TotalCurrentPacket_V0",
]

REQUIRED_ROLLBACKS = {
    "S_IG_dyn_absent",
    "S_IG_dyn_not_source_forced",
    "Z_U_or_V_target_fitted",
    "J_IG_omitted_from_source_law",
    "bare_theta_claimed_conserved_in_Branch_3",
    "Noether_identity_does_not_imply_total_current_conservation",
    "no_FLRW_scalar_mode",
    "Z_theta_nonpositive_without_gauge_removal",
    "C_Rtheta_inserted_by_hand",
    "xi_eff_fitted_not_generated",
    "DESI_Rubin_window_used_upstream",
    "exact_GR_residual_hidden_as_dark_energy",
}


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing Branch 3 gate artifact: {DOC}") from exc


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class Branch3DynamicalIGCurrentAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_required_deliverable_sections_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_mission_a_posture_and_verdict_are_explicit(self) -> None:
        self.assertIn("Mission A posture applies", self.text)
        self.assertEqual(self.summary["mission_posture"], "Mission_A_constructive_obstruction")
        self.assertEqual(self.summary["verdict"], "underdefined")
        promotion = self.summary["promotion_decision"]
        self.assertFalse(promotion["promoted"])
        self.assertEqual(promotion["reason"], "source_forced_S_IG_dyn_is_missing")

    def test_no_lambda_or_dark_energy_promotion_claims(self) -> None:
        non_claims = self.summary["explicit_non_claims"]
        self.assertFalse(non_claims["GU_derives_Lambda"])
        self.assertFalse(non_claims["GU_cancels_Lambda"])
        self.assertFalse(non_claims["GU_derives_dark_energy"])
        self.assertFalse(non_claims["GU_derives_xi_eff_window"])
        self.assertFalse(non_claims["bare_Lambda_source_derived"])
        self.assertIn("claim that GU derives Lambda", self.text)
        self.assertIn("GU_has_derived_or_cancelled_Lambda_or_dark_energy", self.text)

    def test_s_ig_dyn_theta_eff_and_conservation_contract_are_explicit(self) -> None:
        for term in REQUIRED_CONTRACT_TERMS:
            self.assertIn(term, self.text)
        construction = self.summary["strongest_positive_construction"]
        self.assertEqual(construction["source_law_contract"], "D_A^*F_A=theta_eff")
        self.assertIn("theta_eff", construction["theta_eff_contract"])
        theorem_reqs = self.summary["proof_object_contract"]["total_current_theorem_requires"]
        self.assertIn("complete_E_A_current_decomposition", theorem_reqs)
        self.assertIn("route_to_D_A_star_theta_eff_conservation", theorem_reqs)

    def test_first_missing_object_and_ordered_dependencies(self) -> None:
        self.assertEqual(
            self.summary["first_missing_object"],
            "source_forced_S_IG_dyn_action_term",
        )
        ordered = self.summary["missing_objects_ordered"]
        self.assertEqual(ordered[0], "S_IG_dyn")
        self.assertLess(ordered.index("S_IG_dyn"), ordered.index("theta_eff"))
        self.assertLess(ordered.index("theta_eff"), ordered.index("Z_theta"))
        self.assertLess(ordered.index("Z_theta"), ordered.index("xi_eff_provenance"))

    def test_rollback_and_falsification_conditions_are_machine_readable(self) -> None:
        rollbacks = set(self.summary["rollback_falsification_conditions"])
        missing = REQUIRED_ROLLBACKS - rollbacks
        self.assertFalse(missing, f"missing rollback conditions: {sorted(missing)}")
        self.assertIn("Fail or rollback conditions", self.text)

    def test_flrw_coefficient_packet_blocks_xi_eff_promotion(self) -> None:
        flrw = self.summary["proof_object_contract"]["flrw_packet_requires"]
        self.assertIn("Z_theta", flrw)
        self.assertIn("C_Rtheta", flrw)
        self.assertIn("xi_eff_equals_C_Rtheta_over_Z_theta", flrw)
        self.assertIn("Z_theta_C_Rtheta_xi_eff_are_required_but_undefined", self.summary["derived_from_repo_sources"])


if __name__ == "__main__":
    unittest.main()
