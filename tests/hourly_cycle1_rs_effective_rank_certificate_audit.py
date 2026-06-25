#!/usr/bin/env python3
"""Audit the hourly Cycle 1 RS effective-rank certificate artifact.

This audit enforces the proof-contract distinction requested for the RS
effective rank gate: raw gamma-trace data is not physical quotient data,
physical quotient data is not an H-linear effective coefficient rank, and
target-fed generation arithmetic is not a source-derived rank certificate.
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
    / "hourly-cycle1-rs-effective-rank-certificate-2026-06-24.md"
)


REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. What Existing Code/Sources Actually Establish",
    "## 3. Strongest Positive Construction Attempt",
    "## 4. First Exact Obstruction Or Missing Proof Object",
    "## 5. What Would Change If The Obstruction Closed",
    "## 6. Rollback/Falsification Conditions",
    "## 7. Next Meaningful Computation",
    "## 8. Machine-Readable JSON Summary",
]

REQUIRED_LAYER_KEYS = {
    "raw_gamma_trace_projector",
    "physical_BRST_quotient",
    "effective_coefficient_bundle",
    "H_linear_trace",
    "source_selected_background",
    "same_operator_Y14_to_K3_bridge",
    "target_fed_route",
}

REQUIRED_MISSING_OBJECTS = {
    "M_RS,H^src_common_domain",
    "physical_or_BRST_quotient",
    "Pi_RS^phys",
    "E_RS^eff",
    "H_linear_trace_certificate",
    "source_selected_F_and_ch2_background",
    "same_operator_Y14_to_K3_or_APS_bridge",
    "target_quarantine_certificate",
}

REQUIRED_ROLLBACK_CONDITIONS = {
    "claims_rank_4_from_8_divided_by_Ahat_K3",
    "claims_rank_8_without_source_derived_physical_rank",
    "promotes_raw_rank_96C_to_effective_APS_rank",
    "omits_physical_quotient_or_BRST_while_claiming_physical_RS_rank",
    "converts_complex_rank_to_H_rank_without_H_linear_trace_certificate",
    "assumes_F_ch2_background_without_source_selection",
    "uses_K3_control_without_same_operator_Y14_bridge_or_APS_corrections",
    "claims_three_generations_before_source_derived_physical_RS_rank",
    "claims_four_generations_before_source_derived_physical_RS_rank",
    "selects_normalization_after_target_comparison",
}

FORBIDDEN_POSITIVE_PATTERNS = [
    r"\bthree generations\s+(is|are|were|have been|has been)\s+derived\b",
    r"\bfour generations\s+(is|are|were|have been|has been)\s+derived\b",
    r"\bthree-generation (branch|claim|candidate)\s+(is|has been)\s+(closed|proved|promoted|derived)\b",
    r"\bfour-generation (branch|claim|candidate)\s+(is|has been)\s+(closed|proved|promoted|derived)\b",
    r"\brank\s*4\s+(is|has been)\s+(justified|proved|derived|closed)\b",
    r"\brank\s*8\s+(is|has been)\s+(justified|proved|derived|closed)\b",
]


def artifact_text() -> str:
    return ARTIFACT.read_text(encoding="utf-8")


def extract_summary(text: str) -> dict[str, object]:
    for block in re.findall(r"```json\s*(.*?)\s*```", text, re.DOTALL):
        data = json.loads(block)
        if data.get("artifact") == "RS_EFFECTIVE_RANK_CERTIFICATE":
            return data
    raise AssertionError("RS_EFFECTIVE_RANK_CERTIFICATE JSON summary not found")


class HourlyCycle1RSEffectiveRankCertificateAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = artifact_text()
        cls.summary = extract_summary(cls.text)

    def test_required_deliverable_headings_are_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_no_three_or_four_generation_promotion_before_source_rank(self) -> None:
        for pattern in FORBIDDEN_POSITIVE_PATTERNS:
            self.assertIsNone(re.search(pattern, self.text, re.IGNORECASE))
        self.assertFalse(self.summary["source_derived_physical_rank_available"])
        self.assertFalse(self.summary["promotion_allowed_now"])
        self.assertFalse(self.summary["three_generations_derived"])
        self.assertFalse(self.summary["four_generations_derived"])
        self.assertEqual(self.summary["generation_count_claim_status"], "NOT_DERIVED")

    def test_rank_4_and_rank_8_statuses_are_required_and_not_justified(self) -> None:
        rank_status = self.summary["rank_status"]
        self.assertIn("rank_4", rank_status)
        self.assertIn("rank_8", rank_status)
        self.assertEqual(rank_status["rank_4"]["status"], "NOT_JUSTIFIED")
        self.assertEqual(rank_status["rank_8"]["status"], "NOT_JUSTIFIED")
        self.assertEqual(rank_status["physical_effective_rank"], "UNDERDEFINED")
        self.assertEqual(rank_status["neither"]["status"], "NOT_DECIDED")
        self.assertEqual(
            self.summary["current_decision"],
            "UNDERDEFINED_NOT_RANK_4_NOT_RANK_8",
        )

    def test_raw_physical_and_target_fed_layers_are_separated(self) -> None:
        layers = self.summary["certificate_layers"]
        self.assertEqual(set(layers), REQUIRED_LAYER_KEYS)
        self.assertEqual(
            layers["raw_gamma_trace_projector"]["status"],
            "ESTABLISHED_RAW_COMPLEX_ONLY",
        )
        self.assertEqual(layers["raw_gamma_trace_projector"]["field"], "C")
        self.assertFalse(layers["raw_gamma_trace_projector"]["may_promote_to_physical_rank"])
        self.assertEqual(layers["physical_BRST_quotient"]["status"], "MISSING")
        self.assertEqual(layers["effective_coefficient_bundle"]["status"], "MISSING")
        self.assertEqual(layers["H_linear_trace"]["status"], "MISSING")
        self.assertFalse(layers["H_linear_trace"]["complex_to_H_conversion_allowed"])
        self.assertEqual(layers["source_selected_background"]["status"], "UNDERDEFINED")
        self.assertEqual(layers["same_operator_Y14_to_K3_bridge"]["status"], "UNDERDEFINED")
        self.assertEqual(layers["target_fed_route"]["status"], "FORBIDDEN")

    def test_raw_rank_96_is_context_only_not_candidate_promotion(self) -> None:
        rank_status = self.summary["rank_status"]
        self.assertEqual(rank_status["raw_rank_C_Pi_raw_E_plus_Pi_raw"], 96)
        self.assertEqual(rank_status["raw_rank_status"], "RAW_ONLY_NOT_EFFECTIVE_RANK")
        self.assertNotEqual(rank_status["raw_rank_C_Pi_raw_E_plus_Pi_raw"], 4)
        self.assertNotEqual(rank_status["raw_rank_C_Pi_raw_E_plus_Pi_raw"], 8)
        self.assertEqual(
            self.summary["candidate_implications"]["raw_rank_96C"],
            "DOES_NOT_PROMOTE_EITHER_CANDIDATE",
        )

    def test_target_division_is_forbidden_machine_readably(self) -> None:
        target_division = self.summary["target_division_status"]
        self.assertTrue(target_division["forbidden"])
        self.assertEqual(
            target_division["forbidden_formula"],
            "rank_H(E_RS^eff)=ind_H(D_RS)/Ahat(K3)=8/2",
        )
        self.assertEqual(target_division["rollback_label"], "INVALID_TARGET_DIVISION")

    def test_missing_objects_cover_the_full_physical_certificate(self) -> None:
        self.assertEqual(set(self.summary["missing_proof_objects"]), REQUIRED_MISSING_OBJECTS)
        obstruction = self.summary["first_exact_obstruction"]
        self.assertIn("source-selected right-H physical module", obstruction)
        self.assertIn("Pi_RS^phys", obstruction)
        self.assertIn("E_RS^eff", obstruction)
        self.assertIn("H-linear trace", obstruction)

    def test_candidate_implications_are_conditional_only(self) -> None:
        implications = self.summary["candidate_implications"]
        self.assertEqual(
            implications["rank_4_if_source_derived"],
            "CANDIDATE_A_THREE_GENERATION_COMPARISON_SURVIVES_CONDITIONALLY",
        )
        self.assertEqual(
            implications["rank_8_if_source_derived"],
            "CANDIDATE_B_FOUR_GENERATION_COMPARISON_SURVIVES_CONDITIONALLY",
        )
        self.assertEqual(
            implications["other_rank_if_source_derived"],
            "CANDIDATES_A_AND_B_FAIL_OR_REQUIRE_REFORMULATION",
        )

    def test_rollback_conditions_include_raw_physical_target_distinctions(self) -> None:
        self.assertEqual(set(self.summary["rollback_conditions"]), REQUIRED_ROLLBACK_CONDITIONS)
        rollback_text = "\n".join(self.summary["rollback_conditions"])
        self.assertIn("raw_rank_96C", rollback_text)
        self.assertIn("physical_quotient_or_BRST", rollback_text)
        self.assertIn("H_linear_trace", rollback_text)
        self.assertIn("three_generations", rollback_text)
        self.assertIn("four_generations", rollback_text)


def main() -> int:
    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(
            HourlyCycle1RSEffectiveRankCertificateAuditTests
        )
    )
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
