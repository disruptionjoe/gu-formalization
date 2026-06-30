#!/usr/bin/env python3
"""Audit the Cycle 1 effect-typed witness RS quotient artifact.

The audit checks that the artifact turns the prior d_RS,-1 blocker into a
machine-readable source/projection/finality/loss transport contract without
promoting raw ranks or target generation values.
"""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-cycle1-effect-typed-witness-rs-quotient-2026-06-25.md"
)


REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. What Was Derived Directly From Repo Sources",
    "## 3. The Strongest Positive Result",
    "## 4. The First Exact Obstruction Or Missing Proof Object",
    "## 5. The Constructive Next Object That Would Remove Or Test The Obstruction",
    "## 6. What This Means For The Relevant GU Claim",
    "## 7. Next Meaningful Proof Or Computation Step",
    "## 8. Machine-Readable JSON Summary",
]

REQUIRED_EFFECT_LAYERS = {
    "source",
    "projection",
    "finality",
    "loss",
}

REQUIRED_SOURCE_FACTS = {
    "raw_gamma_trace_projector_available",
    "raw_rank_C_Pi_raw_E_plus_Pi_raw",
    "raw_projected_gauge_image_rank_C",
    "physical_quotient_brst_defined",
    "d_RS_minus_1_defined",
    "H_linear_trace_defined",
    "source_selected_F_ch2_defined",
    "same_operator_K3_Y14_or_APS_bridge_defined",
}

REQUIRED_ROLLBACK_CONDITIONS = {
    "claims_rank_3_or_generations_without_source_derived_physical_RS_index",
    "claims_rank_4_from_8_divided_by_Ahat_K3",
    "claims_rank_8_without_effect_typed_transport_instance",
    "identifies_Pi_raw_with_Pi_RS_phys_without_d_RS_minus_1_witness",
    "promotes_raw_rank_96C_to_effective_APS_rank",
    "uses_raw_projected_gauge_image_32C_as_loss_without_source_finality",
    "omits_loss_ledger_while_claiming_physical_RS_rank",
    "converts_complex_rank_to_H_rank_without_H_linear_trace_certificate",
    "assumes_F_ch2_background_without_source_selection",
    "uses_K3_control_without_same_operator_Y14_bridge_or_APS_corrections",
    "selects_normalization_after_target_comparison",
}

REQUIRED_NEXT_STATUSES = {
    "MISSING_SOURCE_WITNESS",
    "RAW_ONLY_NOT_PHYSICAL_QUOTIENT",
    "MISSING_PROJECTION_FINALITY",
    "MISSING_LOSS_LEDGER",
    "NON_ELLIPTIC_OR_UNPROVED_SYMBOL_COMPLEX",
    "COMPLEX_ONLY_H_STRUCTURE_MISSING",
    "BACKGROUND_UNDERDEFINED",
    "K3_CONTROL_ONLY",
    "TRANSPORT_READY_FOR_SYMBOL_INDEX",
}

FORBIDDEN_POSITIVE_PATTERNS = [
    r"\bthree generations\s+(is|are|were|have been|has been)\s+derived\b",
    r"\bfour generations\s+(is|are|were|have been|has been)\s+derived\b",
    r"\brank\s*3\s+(is|has been)\s+(promoted|justified|proved|derived|closed)\b",
    r"\brank\s*4\s+(is|has been)\s+(promoted|justified|proved|derived|closed)\b",
    r"\brank\s*8\s+(is|has been)\s+(promoted|justified|proved|derived|closed)\b",
    r"\braw\s*96_C\s+(is|has been)\s+(the\s+)?(physical|effective)\s+rank\b",
    r"\bPi_raw\s*=\s*Pi_RS\^phys\b",
]


def artifact_text() -> str:
    return ARTIFACT.read_text(encoding="utf-8")


def extract_summary(text: str) -> dict[str, object]:
    for block in re.findall(r"```json\s*(.*?)\s*```", text, re.DOTALL):
        data = json.loads(block)
        if data.get("artifact") == "HOURLY_CYCLE1_EFFECT_TYPED_WITNESS_RS_QUOTIENT":
            return data
    raise AssertionError("effect-typed witness RS quotient JSON summary not found")


class HourlyCycle1EffectTypedWitnessRSQuotientAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = artifact_text()
        cls.summary = extract_summary(cls.text)

    def test_required_deliverable_headings_are_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_transport_contract_is_specified_but_not_instantiated(self) -> None:
        self.assertEqual(self.summary["interface"], "EffectTypedWitnessTransport")
        self.assertTrue(self.summary["transport_contract_specified"])
        self.assertFalse(self.summary["transport_instance_available"])
        self.assertEqual(
            self.summary["current_decision"],
            "MISSING_SOURCE_WITNESS_FOR_D_RS_MINUS_1",
        )
        self.assertFalse(self.summary["pi_rs_phys_defined"])
        self.assertFalse(self.summary["source_derived_physical_rank_available"])
        self.assertFalse(self.summary["promotion_allowed_now"])

    def test_source_facts_are_provenance_limited(self) -> None:
        facts = self.summary["source_derived_facts"]
        self.assertEqual(set(facts), REQUIRED_SOURCE_FACTS)
        self.assertTrue(facts["raw_gamma_trace_projector_available"])
        self.assertEqual(facts["raw_rank_C_Pi_raw_E_plus_Pi_raw"], 96)
        self.assertEqual(facts["raw_projected_gauge_image_rank_C"], 32)
        self.assertFalse(facts["physical_quotient_brst_defined"])
        self.assertFalse(facts["d_RS_minus_1_defined"])
        self.assertFalse(facts["H_linear_trace_defined"])
        self.assertFalse(facts["source_selected_F_ch2_defined"])
        self.assertFalse(facts["same_operator_K3_Y14_or_APS_bridge_defined"])

    def test_effect_layers_cover_source_projection_finality_loss(self) -> None:
        layers = self.summary["effect_layers"]
        self.assertEqual(set(layers), REQUIRED_EFFECT_LAYERS)
        self.assertEqual(layers["source"]["status"], "MISSING_SOURCE_WITNESS")
        self.assertEqual(layers["source"]["required_object"], "d_RS,-1")
        self.assertTrue(layers["source"]["target_inputs_absent_required"])
        self.assertEqual(
            layers["projection"]["status"],
            "RAW_PROJECTOR_AVAILABLE_PHYSICAL_PROJECTION_MISSING",
        )
        self.assertFalse(layers["projection"]["may_identify_raw_with_physical"])
        self.assertEqual(
            layers["finality"]["status"],
            "MISSING_FINAL_QUOTIENT_BRST_OR_GAUGE_FIXED_OBJECT",
        )
        self.assertTrue(layers["finality"]["requires_symbol_exactness_or_ellipticity"])
        self.assertTrue(layers["finality"]["requires_H_linear_trace"])
        self.assertEqual(layers["loss"]["status"], "MISSING_LOSS_LEDGER")
        self.assertIn("gauge_image_loss", layers["loss"]["tracked_terms_required"])
        self.assertIn("APS_eta_h_spectral_flow_terms_if_boundary_used", layers["loss"]["tracked_terms_required"])

    def test_first_obstruction_is_d_rs_minus_1_transport_witness(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["id"], "d_RS,-1")
        self.assertIn("EffectTypedWitnessTransport source witness", obstruction["description"])
        self.assertIn("Pi_RS^phys cannot be defined", obstruction["why_first"])
        self.assertEqual(set(obstruction["missing_effects"]), REQUIRED_EFFECT_LAYERS)

    def test_rank_and_generation_anti_overclaim_conditions(self) -> None:
        self.assertFalse(self.summary["three_generations_derived"])
        self.assertFalse(self.summary["four_generations_derived"])
        self.assertEqual(self.summary["generation_count_claim_status"], "NOT_DERIVED")
        rank_status = self.summary["rank_status"]
        self.assertEqual(rank_status["rank_3"]["status"], "NOT_CLAIMED")
        self.assertEqual(rank_status["rank_4"]["status"], "NOT_PROMOTED")
        self.assertEqual(rank_status["rank_8"]["status"], "NOT_PROMOTED")
        self.assertEqual(rank_status["physical_effective_rank"], "UNDERDEFINED")
        self.assertEqual(rank_status["raw_rank_C_Pi_raw_E_plus_Pi_raw"], 96)
        self.assertEqual(rank_status["raw_rank_status"], "RAW_ONLY_NOT_PHYSICAL_EFFECTIVE_RANK")
        for pattern in FORBIDDEN_POSITIVE_PATTERNS:
            self.assertIsNone(re.search(pattern, self.text, re.IGNORECASE))

    def test_candidate_implications_are_conditional_only(self) -> None:
        implications = self.summary["candidate_implications"]
        self.assertEqual(
            implications["rank_H_index_8_if_source_derived_after_all_gates"],
            "CANDIDATE_A_THREE_GENERATION_COMPARISON_SURVIVES_CONDITIONALLY",
        )
        self.assertEqual(
            implications["rank_H_index_16_if_source_derived_after_all_gates"],
            "CANDIDATE_B_FOUR_GENERATION_COMPARISON_SURVIVES_CONDITIONALLY",
        )
        self.assertEqual(
            implications["other_H_index_if_source_derived_after_all_gates"],
            "CANDIDATES_A_AND_B_FAIL_OR_REQUIRE_REFORMULATION",
        )
        self.assertEqual(
            implications["raw_rank_96C"],
            "DOES_NOT_PROMOTE_EITHER_CANDIDATE",
        )

    def test_target_quarantine_blocks_rank_3_4_8_inputs(self) -> None:
        quarantine = self.summary["target_quarantine"]
        self.assertEqual(quarantine["status"], "ACTIVE")
        for forbidden in [
            "ind_H(D_RS)=8",
            "rank_H(E_RS^eff)=4",
            "total_ind_H(D_GU)=24",
            "three_generations",
            "four_generations",
            "normalization_chosen_after_target_comparison",
        ]:
            self.assertIn(forbidden, quarantine["forbidden_inputs"])
        self.assertFalse(quarantine["rank_3_claim_allowed_now"])
        self.assertFalse(quarantine["rank_4_claim_allowed_now"])
        self.assertFalse(quarantine["rank_8_claim_allowed_now"])

    def test_rollback_conditions_cover_rank_provenance_and_loss_overclaims(self) -> None:
        self.assertEqual(set(self.summary["rollback_conditions"]), REQUIRED_ROLLBACK_CONDITIONS)
        rollback_text = "\n".join(self.summary["rollback_conditions"])
        for required in [
            "rank_3",
            "rank_4",
            "rank_8",
            "Pi_raw",
            "d_RS_minus_1",
            "raw_rank_96C",
            "gauge_image_32C",
            "loss_ledger",
            "H_linear_trace",
            "F_ch2",
            "K3_control",
        ]:
            self.assertIn(required, rollback_text)

    def test_next_object_and_statuses_are_machine_readable(self) -> None:
        self.assertEqual(
            self.summary["constructive_next_object"],
            "EFFECT_TYPED_WITNESS_TRANSPORT_RS_QUOTIENT_BUILDER",
        )
        self.assertEqual(set(self.summary["next_decision_statuses"]), REQUIRED_NEXT_STATUSES)


def main() -> int:
    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(
            HourlyCycle1EffectTypedWitnessRSQuotientAuditTests
        )
    )
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
