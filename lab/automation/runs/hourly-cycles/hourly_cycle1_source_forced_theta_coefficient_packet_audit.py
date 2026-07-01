#!/usr/bin/env python3
"""Audit the hourly Cycle 1 source-forced theta/FLRW coefficient packet gate.

This is a structural provenance audit, not a cosmology computation. It checks
that the artifact has the required decision sections, exposes the coefficient
fields as machine-readable packet fields, blocks empirical-prediction promotion
while the fields are absent, and keeps target-fitting language in rollback form.
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
    / "hourly-cycle1-source-forced-theta-coefficient-packet-2026-06-24.md"
)

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. What was derived directly from repo sources",
    "## 3. The strongest positive result",
    "## 4. The first exact obstruction or missing proof object",
    "## 5. The constructive next object that would remove or test the obstruction",
    "## 6. What this means for the relevant GU claim",
    "## 7. Next meaningful proof or computation step",
    "## 8. Machine-readable JSON summary",
]

COEFFICIENT_FIELDS = {
    "scalar_theta_mode",
    "Z_theta",
    "C_Rtheta",
    "xi_eff",
}

REQUIRED_ROLLBACKS = {
    "DESI_Rubin_window_used_upstream",
    "xi_eff_threshold_used_upstream",
    "xi_eff_target_value_used_upstream",
    "bare_Rtheta_inserted",
    "S_IG_dyn_template_promoted_without_selector",
    "scalar_ansatz_chosen_to_get_negative_xi",
    "Z_theta_or_C_Rtheta_adjusted_after_target_comparison",
    "replacement_or_withheld_target_check_changes_packet",
}

FORBIDDEN_UNQUALIFIED_TARGET_FIT_CLAIMS = [
    "gu predicts desi",
    "gu predicts dark energy",
    "desi is predicted by gu",
    "dark energy is predicted by gu",
    "target-fitted coefficient is source-derived",
    "fitted xi_eff is source-derived",
    "choose xi_eff to match",
    "tune xi_eff to desi",
]


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing coefficient packet artifact: {DOC}") from exc


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-readable JSON summary\s*```json\s*(.*?)\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class SourceForcedThetaCoefficientPacketAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_required_sections_are_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_verdict_blocks_current_packet_emission(self) -> None:
        self.assertEqual(self.summary["verdict"], "blocked")
        self.assertEqual(
            self.summary["packet_name"],
            "SourceForcedThetaFLRWCoefficientPacket",
        )
        self.assertFalse(self.summary["packet_emitted_by_repo"])
        self.assertFalse(self.summary["source_action_locked_before_targets"])
        self.assertEqual(
            self.summary["current_C01_status"],
            "best_next_coefficient_gate_not_empirical_prediction",
        )

    def test_coefficient_fields_are_machine_readable_and_absent(self) -> None:
        fields = self.summary["coefficient_fields"]
        self.assertTrue(COEFFICIENT_FIELDS.issubset(fields.keys()))

        for field_name in COEFFICIENT_FIELDS:
            field = fields[field_name]
            self.assertTrue(field["required"], field_name)
            self.assertFalse(field["present"], field_name)
            self.assertTrue(field["status"].strip(), field_name)

        self.assertEqual(fields["xi_eff"]["formula"], "C_Rtheta / Z_theta")

    def test_no_empirical_promotion_without_coefficients(self) -> None:
        fields = self.summary["coefficient_fields"]
        all_coefficients_present = all(
            fields[field_name]["present"] for field_name in COEFFICIENT_FIELDS
        )

        if self.summary["promoted_to_empirical_prediction"]:
            self.assertTrue(
                all_coefficients_present,
                "empirical promotion requires all coefficient fields",
            )
            self.assertTrue(self.summary["source_action_locked_before_targets"])
            self.assertEqual(
                self.summary["anti_fitting"]["target_inputs_seen_in_current_source_derivation"],
                [],
            )
        else:
            self.assertFalse(all_coefficients_present)
            self.assertFalse(self.summary["target_comparison_permitted"])

        self.assertFalse(self.summary["claim_impact"]["GU_dark_energy_prediction_currently_established"])
        self.assertFalse(self.summary["claim_impact"]["GU_DESI_prediction_currently_established"])

    def test_first_missing_object_and_order_are_precise(self) -> None:
        missing = self.summary["first_exact_missing_object"]
        self.assertEqual(missing["id"], "SourceForcedIGDynamicsSelector")
        self.assertEqual(missing["blocks_before"], "scalar_theta_mode")
        self.assertIn("source_forced_S_IG_dyn_or_parent_action", missing["must_select"])

        ordered = self.summary["ordered_missing_objects"]
        self.assertEqual(ordered[0], "SourceForcedIGDynamicsSelector")
        self.assertLess(ordered.index("SourceForcedIGDynamicsSelector"), ordered.index("scalar_theta_mode") if "scalar_theta_mode" in ordered else ordered.index("FLRWScalarModeSurvivalCertificate"))
        self.assertLess(ordered.index("FLRWQuadraticReductionPacket"), ordered.index("Z_theta"))
        self.assertLess(ordered.index("Z_theta"), ordered.index("xi_eff"))

    def test_anti_fitting_protocol_is_explicit(self) -> None:
        anti = self.summary["anti_fitting"]
        self.assertEqual(anti["target_inputs_seen_in_current_source_derivation"], [])
        self.assertIn("xi_eff < -0.319", anti["target_windows_known_but_quarantined"])
        self.assertIn("DESI_Rubin_CPL_windows", anti["target_windows_known_but_quarantined"])

        rollbacks = set(anti["rollback_conditions"])
        missing = REQUIRED_ROLLBACKS - rollbacks
        self.assertFalse(missing, f"missing rollback conditions: {sorted(missing)}")

        forbidden_inputs = set(anti["forbidden_source_inputs"])
        self.assertIn("DESI_Rubin_likelihood", forbidden_inputs)
        self.assertIn("xi_eff_target", forbidden_inputs)
        self.assertIn("bare_Rtheta_rescue_term", forbidden_inputs)

    def test_target_fitting_language_is_not_unqualified(self) -> None:
        lower_text = self.text.lower()
        for claim in FORBIDDEN_UNQUALIFIED_TARGET_FIT_CLAIMS:
            self.assertNotIn(claim, lower_text, claim)

        promotion = set(self.summary["promotion_conditions"])
        self.assertIn("target_inputs_seen_empty", promotion)
        self.assertIn("anti_fitting_checks_passed", promotion)

        demotion = set(self.summary["demotion_conditions"])
        self.assertIn("target_leakage_upstream", demotion)
        self.assertIn("xi_eff_greater_equal_minus_0_319", demotion)

    def test_next_object_contains_required_outputs(self) -> None:
        next_object = self.summary["constructive_next_object"]
        self.assertEqual(next_object["id"], "SourceForcedThetaFLRWCoefficientPacket_V0")
        self.assertTrue(next_object["do_next"])
        required_outputs = set(next_object["required_outputs"])
        self.assertTrue(COEFFICIENT_FIELDS.issubset(required_outputs))
        self.assertIn("target_inputs_seen", required_outputs)
        self.assertIn("anti_fitting_log", required_outputs)


if __name__ == "__main__":
    unittest.main(verbosity=2)
