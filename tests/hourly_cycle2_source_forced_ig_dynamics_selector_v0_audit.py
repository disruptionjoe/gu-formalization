#!/usr/bin/env python3
"""Audit the hourly Cycle 2 source-forced IG dynamics selector gate.

This is a structural selector/provenance audit, not a physics computation. It
checks that the artifact distinguishes a legitimate Branch 3 action template
from source-forced selection, exposes all required selector fields, keeps target
comparison quarantined, and forbids derivation claims for dark energy, Lambda,
Z_theta, C_Rtheta, or xi_eff.
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
    / "hourly-cycle2-source-forced-ig-dynamics-selector-v0-2026-06-24.md"
)

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Candidate selector input/output signature",
    "## 3. What current sources actually fix",
    "## 4. Strongest positive selector construction attempt",
    "## 5. First exact obstruction or missing source datum",
    "## 6. Impact for Branch 3 and theta coefficient packet",
    "## 7. Rollback/falsification conditions",
    "## 8. Next meaningful proof/computation step",
    "## 9. Machine-readable JSON summary",
]

SELECTOR_FIELDS = {
    "K_IG",
    "Q_IG",
    "Z_U",
    "V_src",
    "S_cross_src",
    "field_degrees",
    "boundary_data",
}

REQUIRED_TEXT_TERMS = [
    "SourceForcedIGDynamicsSelector_V0",
    "K_IG",
    "Q_IG",
    "Z_U",
    "V_src",
    "S_cross_src",
    "field_degrees",
    "boundary_data",
    "target_inputs_seen = []",
    "target quarantine",
]

REQUIRED_ROLLBACKS = {
    "K_IG_chosen_by_simplicity_not_source",
    "K_IG_not_unique_under_allowed_source_rules",
    "field_degrees_not_source_selected",
    "Q_IG_not_selected",
    "Z_U_target_fitted",
    "V_src_target_fitted",
    "S_cross_src_chosen_after_residual_or_target",
    "boundary_data_chosen_after_target",
    "S_IG_dyn_template_promoted_without_selector",
    "J_IG_not_derived_from_delta_A",
    "theta_eff_missing_total_current_terms",
    "Noether_identity_not_written",
    "total_current_conservation_not_proved",
    "bare_theta_source_retained_in_Branch_3",
    "bare_Lambda_inserted",
    "bare_Rtheta_inserted",
    "Z_theta_or_C_Rtheta_claimed_without_FLRW_reduction",
    "xi_eff_fitted_not_generated",
    "dark_energy_derivation_claimed_before_selector_closes",
    "DESI_Rubin_window_used_upstream",
    "xi_eff_threshold_used_upstream",
    "xi_eff_target_value_used_upstream",
    "replacement_or_withheld_target_check_changes_selector",
}

FORBIDDEN_POSITIVE_DERIVATION_PATTERNS = [
    r"\bGU\s+(currently\s+)?derives\s+(dark energy|Lambda|Z_theta|C_Rtheta|xi_eff)\b",
    r"\bBranch 3\s+(currently\s+)?derives\s+(dark energy|Lambda|Z_theta|C_Rtheta|xi_eff)\b",
    r"\bselector\s+(currently\s+)?derives\s+(dark energy|Lambda|Z_theta|C_Rtheta|xi_eff)\b",
    r"\b(dark energy|Lambda|Z_theta|C_Rtheta|xi_eff)\s+(is|are)\s+(currently\s+)?derived\b",
    r'"GU_derives_dark_energy"\s*:\s*true',
    r'"GU_derives_Lambda"\s*:\s*true',
    r'"GU_derives_Z_theta"\s*:\s*true',
    r'"GU_derives_C_Rtheta"\s*:\s*true',
    r'"GU_derives_xi_eff"\s*:\s*true',
]


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing selector gate artifact: {DOC}") from exc


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 9\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class SourceForcedIGDynamicsSelectorV0Audit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_required_sections_are_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_required_selector_terms_are_present(self) -> None:
        for term in REQUIRED_TEXT_TERMS:
            if term == "target quarantine":
                self.assertIn(term, self.text.lower())
            else:
                self.assertIn(term, self.text)

    def test_verdict_blocks_selector_emission(self) -> None:
        self.assertEqual(self.summary["mission_posture"], "Mission_A_constructive_obstruction")
        self.assertEqual(self.summary["verdict"], "underdefined")
        self.assertEqual(self.summary["selector_name"], "SourceForcedIGDynamicsSelector_V0")
        self.assertFalse(self.summary["selector_emitted_by_repo_sources"])
        self.assertTrue(self.summary["legitimate_action_template_exists"])
        self.assertFalse(self.summary["source_forced_selection_exists"])
        self.assertFalse(self.summary["target_comparison_permitted"])

    def test_selector_fields_are_required_and_unselected(self) -> None:
        fields = self.summary["selector_fields"]
        self.assertTrue(SELECTOR_FIELDS.issubset(fields.keys()))

        for field_name in SELECTOR_FIELDS:
            field = fields[field_name]
            self.assertTrue(field["required"], field_name)
            self.assertFalse(field["selected"], field_name)
            self.assertTrue(field["status"].strip(), field_name)

        self.assertEqual(fields["K_IG"]["candidate"], "D_A U")
        self.assertIn("candidate_only", fields["field_degrees"]["status"])

    def test_first_missing_source_datum_is_k_ig_selector(self) -> None:
        missing = self.summary["first_exact_missing_source_datum"]
        self.assertEqual(missing["id"], "K_IG_selector")
        self.assertEqual(missing["candidate"], "K_IG(U)=D_A U")
        self.assertEqual(
            missing["candidate_status"],
            "natural_gauge_covariant_template_not_source_selected",
        )
        self.assertIn("Q_IG", missing["blocks"])
        self.assertIn("FLRW_coefficient_packet", missing["blocks"])

    def test_template_is_not_promoted_to_source_forced_selection(self) -> None:
        construction = self.summary["strongest_positive_construction"]
        self.assertEqual(construction["branch"], "Branch_3_dynamical_IG_total_current")
        self.assertEqual(construction["candidate_K_IG"], "D_A U")
        self.assertEqual(construction["candidate_source_law"], "D_A^*F_A=theta_eff")
        self.assertEqual(
            construction["construction_status"],
            "coherent_template_not_source_forced",
        )
        self.assertIn("K_IG", self.summary["current_sources_do_not_fix"])
        self.assertIn("source_forced_S_IG_dyn", self.summary["current_sources_do_not_fix"])

    def test_target_quarantine_is_machine_readable(self) -> None:
        quarantine = self.summary["target_quarantine"]
        self.assertTrue(quarantine["required"])
        self.assertEqual(quarantine["target_inputs_seen"], [])
        self.assertTrue(quarantine["replacement_target_check_required"])
        quarantined = set(quarantine["known_targets_quarantined_until_after_selector_and_coefficients"])
        self.assertIn("DESI_Rubin_windows", quarantined)
        self.assertIn("xi_eff_less_than_minus_0_319", quarantined)
        self.assertIn("Schwarzschild_Kerr_residuals", quarantined)
        self.assertEqual(self.summary["target_inputs_seen_before_selector"], [])

    def test_no_forbidden_derivation_claims(self) -> None:
        claims = self.summary["derived_claims"]
        for key in [
            "GU_derives_dark_energy",
            "GU_derives_Lambda",
            "GU_derives_Z_theta",
            "GU_derives_C_Rtheta",
            "GU_derives_xi_eff",
            "Branch_3_derives_dark_energy",
            "selector_derives_theta_FLRW_packet",
        ]:
            self.assertFalse(claims[key], key)

        for pattern in FORBIDDEN_POSITIVE_DERIVATION_PATTERNS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                pattern,
            )

    def test_theta_flrw_packet_requirements_are_downstream_only(self) -> None:
        requirements = set(self.summary["theta_flrw_packet_requirements_later"])
        self.assertIn("SourceForcedIGDynamicsSelector", requirements)
        self.assertIn("Z_theta", requirements)
        self.assertIn("C_Rtheta", requirements)
        self.assertIn("xi_eff_equals_C_Rtheta_over_Z_theta", requirements)
        self.assertIn("target_inputs_seen_empty_before_coefficient_emission", requirements)

        not_fixed = set(self.summary["current_sources_do_not_fix"])
        self.assertIn("Z_theta", not_fixed)
        self.assertIn("C_Rtheta", not_fixed)
        self.assertIn("xi_eff", not_fixed)

    def test_rollback_conditions_are_complete(self) -> None:
        rollbacks = set(self.summary["rollback_conditions"])
        missing = REQUIRED_ROLLBACKS - rollbacks
        self.assertFalse(missing, f"missing rollback conditions: {sorted(missing)}")
        self.assertIn("Rollback conditions", self.text)

    def test_next_step_targets_source_selection_not_cosmology(self) -> None:
        next_step = self.summary["next_meaningful_step"]
        self.assertEqual(next_step["id"], "K_IGSourceSelectionTest_V0")
        self.assertTrue(next_step["do_next"])
        self.assertEqual(
            next_step["avoid_next"],
            "cosmology_target_comparison_before_source_selector",
        )
        required = set(next_step["required_outputs"])
        self.assertIn("operator_list", required)
        self.assertIn("replacement_target_check", required)
        self.assertIn("boundary_data_decision", required)


if __name__ == "__main__":
    unittest.main(verbosity=2)
