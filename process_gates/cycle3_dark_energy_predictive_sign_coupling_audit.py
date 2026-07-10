#!/usr/bin/env python3
"""Audit the Cycle 3 dark-energy predictive sign/nonminimal-coupling gate.

This is a structural provenance audit, not a cosmology simulation. It checks
that the artifact keeps the minimal w_a > 0 sign, nonminimal xi window,
DESI/Rubin anti-fitting rule, and source-provenance gate separate. It also
checks that no positive GU prediction of DESI/dark energy is claimed.
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
    / "cycle-gates-and-audits" / "cycle3-dark-energy-predictive-sign-coupling-gate-2026-06-24.md"
)

OQ3A = REPO_ROOT / "explorations" / "dark-energy-cosmology" / "dark-energy-oq3a-slow-roll-ic-sign-2026-06-23.md"
WINDOW = REPO_ROOT / "explorations" / "dark-energy-cosmology" / "dark-energy-w-window-mechanism-2026-06-23.md"
BRANCH = REPO_ROOT / "explorations" / "dark-energy-cosmology" / "flrw-theta-xi-branch-reduction-2026-06-24.md"
CYCLE2 = REPO_ROOT / "explorations" / "cycle-gates-and-audits" / "cycle2-source-forced-s-ig-dyn-action-gate-2026-06-24.md"
MISSION = REPO_ROOT / "explorations" / "dark-energy-cosmology" / "mission-a-lambda-dark-energy-provenance-2026-06-24.md"

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Minimal theta-field sign status",
    "## 3. Nonminimal `xi R theta^2` window status",
    "## 4. Source provenance needed for `xi`",
    "## 5. DESI/Rubin anti-fitting protocol",
    "## 6. First exact obstruction or falsifier",
    "## 7. Impact for GU empirical usefulness",
    "## 8. Next meaningful computation",
    "## 9. Machine-readable JSON summary",
]

REQUIRED_TEXT = [
    "w_a > 0",
    "xi_eff < -0.319",
    "xi_eff ~= -0.6",
    "DESI/Rubin",
    "anti-fitting",
    "source provenance",
    "ThetaXiSourceCoefficientCertificate",
    "xi_eff = C_Rtheta / Z_theta",
]

FORBIDDEN_POSITIVE_CLAIMS = [
    "GU predicts the DESI dark-energy sign",
    "GU predicts DESI",
    "GU predicts dark energy",
    "GU derives dark energy",
    "GU has derived dark energy",
    "DESI is predicted by GU",
    "dark energy is predicted by GU",
]

REQUIRED_ROLLBACKS = {
    "target_leakage_into_source_construction",
    "source_forced_xi_missing",
    "bare_Rtheta_inserted",
    "no_FLRW_scalar_mode",
    "Z_theta_nonpositive_unresolved",
    "theta_eff_not_conserved",
    "xi_generated_above_negative_window",
    "DESI_Rubin_fit_used_as_input",
}

REQUIRED_FALSIFIERS = {
    "minimal_route_falsified_if_robust_same_convention_data_require_w_a_negative",
    "DESI_sign_route_killed_if_all_source_forced_scalar_branches_have_xi_eff_greater_equal_minus_0_319",
    "theta_KG_route_killed_if_s_star_theta_is_not_scalar_or_is_constrained_away",
    "nonminimal_route_demoted_if_negative_xi_requires_target_selected_Rtheta2",
    "future_source_generated_route_falsified_if_locked_w0_wa_region_excluded_by_joint_DESI_Rubin_likelihood",
}


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing required file: {path}") from exc


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 9\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary")
    return json.loads(match.group(1))


class DarkEnergyPredictiveSignCouplingAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read(DOC)
        cls.summary = extract_summary(cls.text)

    def test_source_anchors_still_support_gate_values(self) -> None:
        oq3a = read(OQ3A)
        window = read(WINDOW)
        branch = read(BRANCH)
        cycle2 = read(CYCLE2)
        mission = read(MISSION)

        self.assertIn("predicts w_a > 0", oq3a)
        self.assertIn("xi < xi_c1 = -0.319", window)
        self.assertIn("xi ~ -0.6", window)
        self.assertIn("supply the sign or magnitude", window)
        self.assertIn("No currently written viable action branch generates negative", branch)
        self.assertIn("xi_eff = C_Rtheta / Z_theta", branch)
        self.assertIn("SourceForcedIGDynamicsSelector", cycle2)
        self.assertIn("does not claim that GU derives Lambda", cycle2)
        self.assertIn("no fitted xi_eff", mission)
        self.assertIn("no DESI/Rubin target window may be used upstream", mission)

    def test_required_deliverable_sections_and_terms_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)
        for term in REQUIRED_TEXT:
            self.assertIn(term, self.text)

    def test_no_positive_gu_prediction_claim(self) -> None:
        self.assertFalse(self.summary["gu_predicts_desi_dark_energy"])
        self.assertEqual(self.summary["gu_dark_energy_prediction_status"], "not_established")
        self.assertEqual(
            self.summary["verdict"],
            "target_sensitive_fit_window_for_DESI_not_GU_prediction",
        )
        lower_text = self.text.lower()
        for claim in FORBIDDEN_POSITIVE_CLAIMS:
            self.assertNotIn(claim.lower(), lower_text, claim)

    def test_minimal_theta_sign_is_machine_readable(self) -> None:
        minimal = self.summary["minimal_theta_field_sign"]
        self.assertEqual(minimal["wa_sign"], "positive")
        self.assertEqual(minimal["wa_expression"], "w_a > 0")
        self.assertEqual(
            minimal["predictive_status"],
            "conditional_minimal_scalar_model_prediction",
        )
        self.assertEqual(minimal["DESI_sign_status"], "discordant_with_repo_DESI_target")
        self.assertFalse(minimal["full_GU_provenance"])
        self.assertIn("xi_equals_0", minimal["assumptions"])
        self.assertIn("slow_roll_attractor_initial_conditions", minimal["assumptions"])

    def test_nonminimal_xi_window_is_not_promoted(self) -> None:
        xi_window = self.summary["nonminimal_xi_window"]
        self.assertEqual(xi_window["canonical_formula"], "xi_eff = C_Rtheta / Z_theta")
        self.assertEqual(xi_window["negative_wa_threshold"], -0.319)
        self.assertEqual(xi_window["DESI_ratio_match"], -0.6)
        self.assertEqual(xi_window["window_status"], "reaches_DESI_sign_as_FLRW_mechanism")
        self.assertEqual(xi_window["prediction_status"], "not_predicted_currently")
        self.assertFalse(xi_window["xi_generated_by_current_branch"])
        self.assertEqual(xi_window["minimal_xi_status"], "wrong_sign")
        self.assertEqual(xi_window["conformal_xi_status"], "wrong_sign")

    def test_source_provenance_object_is_exact_and_upstream_of_prediction(self) -> None:
        provenance = self.summary["source_provenance_needed"]
        self.assertEqual(provenance["exact_object"], "ThetaXiSourceCoefficientCertificate")
        self.assertEqual(provenance["branch3_first_subobject"], "SourceForcedIGDynamicsSelector")
        for required in [
            "written_source_forced_action_or_operator_action_pair",
            "Noether_conservation_proof",
            "FLRW_scalar_mode_u0",
            "Z_theta",
            "C_Rtheta",
            "xi_eff",
            "anti_fitting_log",
        ]:
            self.assertIn(required, provenance["required_outputs"])
        self.assertIn("before_DESI_Rubin_targets", provenance["makes_xi_predicted_if"])

    def test_anti_fitting_protocol_mentions_desi_rubin_and_target_lock(self) -> None:
        protocol = set(self.summary["DESI_Rubin_anti_fitting_protocol"])
        self.assertIn("branch_freeze", protocol)
        self.assertIn("target_quarantine", protocol)
        self.assertIn("coefficient_lock", protocol)
        self.assertIn("replacement_withheld_target_check", protocol)
        self.assertIn("rollback_on_target_leakage", protocol)
        self.assertIn("Target quarantine", self.text)
        self.assertIn("DESI/Rubin CPL windows", self.text)

    def test_verdict_rollback_and_falsification_are_machine_readable(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["id"], "missing_ThetaXiSourceCoefficientCertificate")
        self.assertEqual(
            obstruction["branch3_subobstruction"],
            "missing_SourceForcedIGDynamicsSelector",
        )
        self.assertEqual(obstruction["current_DESI_compatibility"], "fit_window")

        rollbacks = set(self.summary["rollback_conditions"])
        self.assertTrue(REQUIRED_ROLLBACKS.issubset(rollbacks))

        falsifiers = set(self.summary["falsification_conditions"])
        self.assertTrue(REQUIRED_FALSIFIERS.issubset(falsifiers))

    def test_empirical_usefulness_and_next_computation_are_not_overstated(self) -> None:
        impact = self.summary["impact_for_GU_empirical_usefulness"]
        self.assertFalse(impact["current_positive_evidence"])
        self.assertEqual(impact["current_usefulness"], "sharp_falsification_and_coefficient_gate")
        self.assertEqual(
            impact["promotion_requires"],
            "source_generated_xi_eff_before_target_comparison",
        )

        next_step = self.summary["next_meaningful_computation"]
        self.assertEqual(next_step["id"], "ThetaXiSourceCoefficientPacket_V0")
        self.assertTrue(next_step["do_next"])
        self.assertEqual(next_step["avoid_next"], "another_unproven_cosmology_scan")


if __name__ == "__main__":
    unittest.main(verbosity=2)
