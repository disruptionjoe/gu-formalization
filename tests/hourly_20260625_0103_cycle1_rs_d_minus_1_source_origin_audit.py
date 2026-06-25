#!/usr/bin/env python3
"""Audit the hourly RS d_RS,-1 source-origin certificate.

The audit enforces that the certificate preserves the raw principal-symbol
context, records the candidate formula, stops at the missing source
action/operator field, and does not promote physical rank or generation claims.
"""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "explorations"
    / "hourly-20260625-0103-cycle1-rs-d-minus-1-source-origin-certificate.md"
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

REQUIRED_TOP_LEVEL_FIELDS = {
    "artifact",
    "version",
    "run",
    "cycle",
    "lane",
    "verdict",
    "verdict_class",
    "decision_status",
    "certificate_object",
    "required_map",
    "candidate",
    "raw_symbol_context",
    "source",
    "projection",
    "finality",
    "loss",
    "rank_generation_quarantine",
    "first_exact_obstruction",
    "constructive_next_object",
    "impact_on_GU_claim",
    "rollback_conditions",
}

REQUIRED_EFFECT_FIELDS = {"source", "projection", "finality", "loss"}

FORBIDDEN_PROMOTION_PATTERNS = [
    r"\bphysical rank is derived\b",
    r"\bH-index is derived\b",
    r"\brank\s*3\s+(is|has been)\s+(derived|promoted|proved|closed)\b",
    r"\brank\s*4\s+(is|has been)\s+(derived|promoted|proved|closed)\b",
    r"\brank\s*8\s+(is|has been)\s+(derived|promoted|proved|closed)\b",
    r"\bthree generations\s+(are|is|have been|has been)\s+derived\b",
    r"\bfour generations\s+(are|is|have been|has been)\s+derived\b",
    r"\bPi_raw\s*=\s*Pi_RS\^phys\b",
    r"\braw principal symbol proves d_RS,-1\b",
]


def extract_summary(text: str) -> dict[str, object]:
    for block in re.findall(r"```json\s*(.*?)\s*```", text, re.DOTALL):
        data = json.loads(block)
        if data.get("artifact") == "RS_D_MINUS_1_SOURCE_ORIGIN_CERTIFICATE_V1":
            return data
    raise AssertionError("RS d_RS,-1 source-origin certificate JSON summary not found")


class HourlyRSdMinus1SourceOriginAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_required_headings_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_json_summary_has_required_top_level_fields(self) -> None:
        self.assertEqual(set(self.summary), REQUIRED_TOP_LEVEL_FIELDS)
        for field in REQUIRED_EFFECT_FIELDS:
            self.assertIn(field, self.summary)

    def test_decision_blocks_at_source_action_or_operator(self) -> None:
        self.assertEqual(self.summary["verdict"], "BLOCKED_SOURCE_ACTION_OR_OPERATOR_MISSING")
        self.assertEqual(self.summary["verdict_class"], "blocked")
        self.assertEqual(
            self.summary["decision_status"],
            "FAIL_SOURCE_ACTION_OR_OPERATOR_MISSING",
        )
        self.assertEqual(self.summary["certificate_object"], "d_RS,-1")
        self.assertEqual(self.summary["required_map"], "Ghost_RS,H^src -> Field_RS,H^src")

        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["field"], "source.action_or_operator")
        self.assertEqual(obstruction["status"], "MISSING")
        self.assertIn("No current repo source derives d_RS,-1", obstruction["description"])

    def test_candidate_formula_and_raw_symbol_context_are_present_but_unpromoted(self) -> None:
        candidate = self.summary["candidate"]
        self.assertEqual(
            candidate["formula"],
            "d_candidate(epsilon)=Pi_gamma_free(nabla^A epsilon)",
        )
        self.assertEqual(candidate["principal_symbol"], "P_plus(xi tensor epsilon)")
        self.assertEqual(candidate["status"], "CANDIDATE_SHAPE_ONLY_NOT_SOURCE_DERIVED")
        self.assertTrue(candidate["uses_raw_symbol_context"])
        self.assertTrue(candidate["uses_reconstruction_gauge_phrase"])

        raw = self.summary["raw_symbol_context"]
        self.assertTrue(raw["available"])
        self.assertEqual(raw["formula"], "epsilon -> xi tensor epsilon")
        self.assertEqual(raw["source_file"], "tests/rs_clifford_projector_model.py")
        self.assertEqual(raw["projected_candidate_symbol"], "g_xi(epsilon)=P_+(xi tensor epsilon)")
        self.assertEqual(raw["raw_projected_gauge_image_rank_C_context"], 32)
        self.assertFalse(raw["promoted_to_source_differential"])
        self.assertFalse(raw["promoted_to_physical_loss"])

    def test_source_projection_finality_loss_fields_have_required_statuses(self) -> None:
        source = self.summary["source"]
        self.assertEqual(source["status"], "FAIL")
        self.assertEqual(source["action_or_operator"]["status"], "MISSING")
        self.assertEqual(source["Noether_or_BRST_theorem"]["status"], "MISSING")
        self.assertEqual(source["actual_D_GU_source_closed_operator"]["status"], "MISSING")
        self.assertEqual(source["first_missing_field"], "source.action_or_operator")

        projection = self.summary["projection"]
        self.assertEqual(projection["status"], "BLOCKED_BY_SOURCE")
        self.assertFalse(projection["Pi_RS_phys_defined"])
        self.assertFalse(projection["image_identified_as_physical_gauge_direction"])
        self.assertFalse(projection["may_identify_Pi_raw_with_Pi_RS_phys"])

        finality = self.summary["finality"]
        self.assertEqual(finality["status"], "BLOCKED_BY_SOURCE")
        self.assertFalse(finality["BRST_complex_available"])
        self.assertFalse(finality["gauge_fixed_elliptic_block_available"])
        self.assertFalse(finality["symbol_exact_or_elliptic_for_all_nonzero_xi"])
        self.assertFalse(finality["H_linear_Fredholm_or_trace_object_available"])

        loss = self.summary["loss"]
        self.assertEqual(loss["status"], "BLOCKED_BY_SOURCE")
        self.assertFalse(loss["loss_ledger_complete"])
        self.assertEqual(
            set(loss["required_losses"]),
            {
                "gamma_trace_loss",
                "gauge_image_loss",
                "ghost_antighost_subtraction",
                "complex_to_H_conversion",
                "source_selected_background_F_ch2",
                "APS_eta_h_spectral_flow_if_used",
            },
        )

    def test_first_obstruction_rejects_raw_symbol_and_reconstruction_phrase_as_sufficient(self) -> None:
        not_enough = set(self.summary["first_exact_obstruction"]["not_enough"])
        self.assertIn("raw principal symbol epsilon -> xi tensor epsilon", not_enough)
        self.assertIn(
            "reconstruction-grade psi_a^RS ~ psi_a^RS + nabla_a epsilon",
            not_enough,
        )
        self.assertIn("raw projected gauge image rank context", not_enough)
        self.assertIn("rank or generation comparison arithmetic", not_enough)

    def test_rank_and_generation_claims_are_quarantined(self) -> None:
        quarantine = self.summary["rank_generation_quarantine"]
        self.assertEqual(quarantine["status"], "ACTIVE")
        for key in [
            "promote_physical_rank",
            "promote_H_index",
            "promote_rank_3",
            "promote_rank_4",
            "promote_rank_8",
            "promote_three_generations",
            "promote_four_generations",
        ]:
            self.assertFalse(quarantine[key])
        for forbidden in [
            "raw_projector_rank_as_physical_rank",
            "raw_projected_gauge_image_as_physical_loss",
            "rank_3",
            "rank_4",
            "rank_8",
            "three_generations",
            "four_generations",
            "target_normalization",
        ]:
            self.assertIn(forbidden, quarantine["forbidden_promotions"])

    def test_constructive_next_object_requires_source_first_then_downstream_fields(self) -> None:
        next_object = self.summary["constructive_next_object"]
        self.assertEqual(next_object["id"], "RS_D_MINUS_1_SOURCE_ORIGIN_CERTIFICATE_V1_FILLED")
        self.assertEqual(next_object["first_required_field"], "source.action_or_operator")
        for field in [
            "source.Noether_or_BRST_theorem",
            "ghost_module",
            "field_module",
            "differential.right_H_linearity_proof",
            "differential.connection_compatibility_proof",
            "projection.image_identification",
            "finality.BRST_or_gauge_fixed_elliptic_block",
            "loss.complete_ledger",
        ]:
            self.assertIn(field, next_object["then_required_fields"])

    def test_impact_keeps_gu_open_but_source_origin_blocked(self) -> None:
        impact = self.summary["impact_on_GU_claim"]
        self.assertFalse(impact["GU_RS_branch_falsified"])
        self.assertEqual(impact["current_status"], "SOURCE_ORIGIN_BLOCKED")
        self.assertIn("source-derived H-linear d_RS,-1", impact["required_if_branch_correct"])
        self.assertEqual(impact["rank_generation_claim_status"], "QUARANTINED_NOT_DERIVED")

    def test_rollback_conditions_cover_source_projection_finality_loss_and_targets(self) -> None:
        rollback = set(self.summary["rollback_conditions"])
        for condition in [
            "promotes_raw_symbol_to_source_derived_d_RS_minus_1",
            "promotes_AF4_gauge_phrase_to_source_derived_d_RS_minus_1",
            "identifies_Pi_raw_with_Pi_RS_phys_without_source_certificate",
            "uses_raw_projected_gauge_image_as_physical_loss_without_finality",
            "claims_physical_rank_or_H_index_before_source_finality",
            "claims_rank_3_or_rank_4_or_rank_8_before_source_finality",
            "claims_three_or_four_generations_before_source_finality",
            "uses_target_rank_or_generation_as_construction_input",
        ]:
            self.assertIn(condition, rollback)

    def test_no_forbidden_promotion_language(self) -> None:
        for pattern in FORBIDDEN_PROMOTION_PATTERNS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                msg=f"forbidden promotion pattern present: {pattern}",
            )


def main() -> int:
    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(
            HourlyRSdMinus1SourceOriginAuditTests
        )
    )
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
