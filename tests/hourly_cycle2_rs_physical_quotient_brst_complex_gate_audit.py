#!/usr/bin/env python3
"""Audit the hourly Cycle 2 RS physical quotient/BRST complex gate.

This audit checks the next lower blocker for the RS effective-rank program:
Pi_RS^phys is not defined until a source-defined physical quotient or BRST
complex is supplied. The audit enforces that the artifact names every required
quotient/BRST field, leaves rank_4 and rank_8 unpromoted, marks target division
as rollback, and does not treat the raw 96_C projector rank as a physical rank.
"""

from __future__ import annotations

import json
from pathlib import Path
import re
import sys
import unittest

TESTS_DIR = Path(__file__).resolve().parent
if str(TESTS_DIR) not in sys.path:
    sys.path.insert(0, str(TESTS_DIR))

from rs_clifford_projector_model import compute_model


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-cycle2-rs-physical-quotient-brst-complex-gate-2026-06-24.md"
)


REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Physical Quotient/BRST Complex Signature",
    "## 3. What Raw Projector Code Does And Does Not Establish",
    "## 4. Strongest Positive Construction Attempt",
    "## 5. First Exact Missing Object",
    "## 6. Impact For Rank 4/Rank 8/Generation Count",
    "## 7. Rollback/Falsification Conditions",
    "## 8. Next Meaningful Computation",
    "## 9. Machine-Readable JSON Summary",
]

REQUIRED_SIGNATURE_FIELDS = {
    "source_operator",
    "domain",
    "gamma_trace_constraint",
    "gauge_map",
    "gauge_fixing_condition",
    "BRST_differential",
    "ghost_subtraction",
    "symbol_exactness",
    "ellipticity",
    "physical_cohomology",
    "Pi_RS_phys",
    "E_RS_eff",
    "H_linear_trace",
    "source_selected_F_ch2",
    "K3_Y14_bridge",
    "target_quarantine",
}

REQUIRED_SOURCE_DECISIONS = {
    "domain",
    "gauge_map",
    "gamma_trace_constraint",
    "ghost_subtraction",
    "ellipticity_or_symbol_exactness",
    "H_linear_trace",
    "source_selected_F_ch2",
    "K3_Y14_bridge",
}

REQUIRED_ROLLBACK_CONDITIONS = {
    "claims_rank_4_from_8_divided_by_Ahat_K3",
    "claims_rank_8_without_source_defined_physical_quotient_BRST_complex",
    "identifies_Pi_raw_with_Pi_RS_phys_without_gauge_BRST_differential",
    "treats_raw_rank_96C_as_effective_physical_rank",
    "halves_complex_rank_without_H_linear_trace_certificate",
    "uses_BRST_style_subtraction_without_source_derived_ghost_complex",
    "assumes_F_ch2_background_without_source_selection",
    "uses_K3_control_without_same_operator_Y14_bridge_or_APS_corrections",
    "claims_three_generations_before_source_derived_physical_RS_rank",
    "claims_four_generations_before_source_derived_physical_RS_rank",
    "selects_normalization_after_target_comparison",
}

FORBIDDEN_POSITIVE_PATTERNS = [
    r"\bthree generations\s+(is|are|were|have been|has been)\s+derived\b",
    r"\bfour generations\s+(is|are|were|have been|has been)\s+derived\b",
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
        if data.get("artifact") == "HOURLY_CYCLE2_RS_PHYSICAL_QUOTIENT_BRST_COMPLEX_GATE":
            return data
    raise AssertionError("hourly Cycle 2 RS quotient/BRST JSON summary not found")


class HourlyCycle2RSPhysicalQuotientBRSTComplexGateAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = artifact_text()
        cls.summary = extract_summary(cls.text)
        cls.raw_model = compute_model()

    def test_required_deliverable_headings_are_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_required_quotient_brst_signature_fields_are_machine_readable(self) -> None:
        signature = self.summary["quotient_brst_signature"]
        self.assertEqual(set(signature), REQUIRED_SIGNATURE_FIELDS)
        self.assertEqual(signature["domain"]["status"], "MISSING_SOURCE_SELECTED_RIGHT_H_DOMAIN")
        self.assertTrue(signature["domain"]["required_for_Pi_RS_phys"])
        self.assertEqual(
            signature["gamma_trace_constraint"]["status"],
            "RAW_COMPLEX_AVAILABLE_NOT_PHYSICAL",
        )
        self.assertTrue(signature["gamma_trace_constraint"]["raw_maps_available"])
        self.assertFalse(signature["gamma_trace_constraint"]["physical_constraint_source_defined"])
        self.assertEqual(
            signature["gauge_map"]["status"],
            "RAW_PRINCIPAL_SAMPLE_AVAILABLE_SOURCE_GAUGE_MISSING",
        )
        self.assertTrue(signature["gauge_map"]["raw_principal_map_available"])
        self.assertFalse(signature["gauge_map"]["source_global_gauge_map"])
        self.assertEqual(signature["gauge_map"]["projected_raw_gauge_image_rank_C"], 32)
        self.assertEqual(signature["BRST_differential"]["status"], "MISSING")
        self.assertEqual(signature["BRST_differential"]["required_object"], "d_RS,-1")
        self.assertEqual(signature["ghost_subtraction"]["status"], "MISSING_SOURCE_DERIVED")
        self.assertTrue(signature["ghost_subtraction"]["comparison_arithmetic_only"])
        self.assertEqual(signature["symbol_exactness"]["status"], "MISSING")
        self.assertEqual(signature["ellipticity"]["status"], "MISSING")
        self.assertEqual(signature["physical_cohomology"]["status"], "MISSING")

    def test_source_definition_decisions_cover_assignment_fields(self) -> None:
        decisions = self.summary["source_definition_decisions"]
        self.assertEqual(set(decisions), REQUIRED_SOURCE_DECISIONS)
        self.assertEqual(decisions["domain"], "missing")
        self.assertEqual(decisions["gauge_map"], "raw_principal_sample_only")
        self.assertEqual(decisions["gamma_trace_constraint"], "raw_complex_available_only")
        self.assertEqual(decisions["ghost_subtraction"], "missing_source_derived")
        self.assertEqual(decisions["ellipticity_or_symbol_exactness"], "missing")
        self.assertEqual(decisions["H_linear_trace"], "missing")
        self.assertEqual(decisions["source_selected_F_ch2"], "underdefined")
        self.assertEqual(decisions["K3_Y14_bridge"], "underdefined")

    def test_pi_rs_phys_and_effective_data_remain_missing(self) -> None:
        signature = self.summary["quotient_brst_signature"]
        self.assertFalse(self.summary["pi_rs_phys_defined"])
        self.assertEqual(signature["Pi_RS_phys"]["status"], "MISSING")
        self.assertFalse(signature["Pi_RS_phys"]["may_identify_with_Pi_raw"])
        self.assertEqual(signature["E_RS_eff"]["status"], "MISSING")
        self.assertFalse(signature["E_RS_eff"]["same_domain_as_Pi_RS_phys"])
        self.assertEqual(signature["H_linear_trace"]["status"], "MISSING")
        self.assertFalse(signature["H_linear_trace"]["complex_to_H_conversion_allowed"])
        self.assertEqual(signature["source_selected_F_ch2"]["status"], "UNDERDEFINED")
        self.assertEqual(signature["source_selected_F_ch2"]["rank_C_F_context"], 16)
        self.assertEqual(signature["K3_Y14_bridge"]["status"], "UNDERDEFINED")
        self.assertTrue(signature["K3_Y14_bridge"]["same_operator_required"])

    def test_rank_4_and_rank_8_remain_unpromoted(self) -> None:
        rank_status = self.summary["rank_status"]
        self.assertEqual(rank_status["rank_4"]["status"], "NOT_PROMOTED")
        self.assertEqual(rank_status["rank_8"]["status"], "NOT_PROMOTED")
        self.assertEqual(rank_status["physical_effective_rank"], "UNDERDEFINED")
        self.assertFalse(self.summary["source_derived_physical_rank_available"])
        self.assertFalse(self.summary["promotion_allowed_now"])
        self.assertFalse(self.summary["three_generations_derived"])
        self.assertFalse(self.summary["four_generations_derived"])
        self.assertEqual(self.summary["generation_count_claim_status"], "NOT_DERIVED")
        for pattern in FORBIDDEN_POSITIVE_PATTERNS:
            self.assertIsNone(re.search(pattern, self.text, re.IGNORECASE))

    def test_target_division_requires_rollback(self) -> None:
        target_division = self.summary["target_division_status"]
        self.assertTrue(target_division["forbidden"])
        self.assertEqual(
            target_division["forbidden_formula"],
            "rank_H(E_RS^eff)=ind_H(D_RS)/Ahat(K3)=8/2",
        )
        self.assertEqual(target_division["rollback_label"], "INVALID_TARGET_DIVISION")
        quarantine = self.summary["quotient_brst_signature"]["target_quarantine"]
        self.assertEqual(quarantine["status"], "ACTIVE")
        self.assertTrue(quarantine["target_division_forbidden"])
        self.assertEqual(quarantine["rollback_label"], "INVALID_TARGET_DIVISION")

    def test_raw_rank_96_is_recomputed_and_forbidden_as_physical_rank(self) -> None:
        raw_ranks = self.raw_model["raw_rank_summary"]
        raw_symbol = self.raw_model["sample_raw_projected_symbol"]
        self.assertEqual(raw_ranks["gamma_trace_kernel_rank_C"], 96)
        self.assertEqual(raw_symbol["projected_gauge_rank_C"], 32)

        raw_summary = self.summary["raw_projector_result"]
        self.assertEqual(raw_summary["rank"], 96)
        self.assertEqual(raw_summary["field"], "C")
        self.assertEqual(raw_summary["status"], "RAW_ONLY_NOT_PHYSICAL_EFFECTIVE_RANK")
        self.assertFalse(raw_summary["promoted_to_Pi_RS_phys"])
        self.assertFalse(raw_summary["promoted_to_effective_rank"])
        self.assertFalse(raw_summary["promoted_to_generation_claim"])
        self.assertEqual(
            self.summary["rank_status"]["raw_rank_C_Pi_raw_E_plus_Pi_raw"],
            96,
        )
        self.assertEqual(
            self.summary["candidate_implications"]["raw_rank_96C"],
            "DOES_NOT_PROMOTE_EITHER_CANDIDATE",
        )

    def test_first_missing_object_is_source_defined_gauge_brst_differential(self) -> None:
        missing = self.summary["first_exact_missing_object"]
        self.assertEqual(missing["id"], "d_RS,-1")
        self.assertIn("source-defined H-linear gauge/BRST differential", missing["description"])
        self.assertIn("Pi_RS^phys", missing["why_first"])
        self.assertEqual(
            self.summary["current_decision"],
            "MISSING_SOURCE_DEFINED_GAUGE_BRST_DIFFERENTIAL",
        )

    def test_candidate_implications_are_conditional_only(self) -> None:
        implications = self.summary["candidate_implications"]
        self.assertEqual(
            implications["rank_4_if_source_derived_after_all_gates"],
            "CANDIDATE_A_THREE_GENERATION_COMPARISON_SURVIVES_CONDITIONALLY",
        )
        self.assertEqual(
            implications["rank_8_if_source_derived_after_all_gates"],
            "CANDIDATE_B_FOUR_GENERATION_COMPARISON_SURVIVES_CONDITIONALLY",
        )
        self.assertEqual(
            implications["other_rank_if_source_derived_after_all_gates"],
            "CANDIDATES_A_AND_B_FAIL_OR_REQUIRE_REFORMULATION",
        )

    def test_rollback_conditions_cover_raw_target_quotient_trace_background_bridge(self) -> None:
        self.assertEqual(set(self.summary["rollback_conditions"]), REQUIRED_ROLLBACK_CONDITIONS)
        rollback_text = "\n".join(self.summary["rollback_conditions"])
        for required in [
            "rank_4",
            "rank_8",
            "Pi_raw",
            "raw_rank_96C",
            "H_linear_trace",
            "BRST_style_subtraction",
            "F_ch2",
            "K3_control",
            "three_generations",
            "four_generations",
        ]:
            self.assertIn(required, rollback_text)

    def test_next_meaningful_computation_is_certificate_builder(self) -> None:
        self.assertEqual(
            self.summary["next_meaningful_computation"],
            "RS_PHYSICAL_QUOTIENT_BRST_COMPLEX_BUILDER",
        )


def main() -> int:
    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(
            HourlyCycle2RSPhysicalQuotientBRSTComplexGateAuditTests
        )
    )
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
