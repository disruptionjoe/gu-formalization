#!/usr/bin/env python3
"""Audit the 1302 three-cycle fifteen-hole synthesis."""

from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "explorations" / "hourly-20260625-1302-three-cycle-fifteen-hole-synthesis.md"

EXPECTED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Fifteen-hole Result Table",
    "## 3. Closed, Conditional, Blocked, Failed, No-go",
    "## 4. Next Frontier Objects",
    "## 5. Sequential Versus Parallel",
    "## 6. Wrapper Assessment",
    "## 7. Verification Summary",
    "## 8. Final Mathematical And Category Review",
    "## 9. What Materially Changed",
    "## 10. Machine-readable JSON summary",
]

EXPECTED_NEXT_FIVE = {
    "PTUJ_TOOLCHAIN_SOURCE_BYTE_MANIFEST",
    "IG_D7_MULTIPLICITY_TRANSCRIPT",
    "DGU_IDENTITY_FIELD_RECEIPT_BUNDLE",
    "RS_UCSD_FRAME_SEQUENCE_ACQUISITION",
    "QFT_LOCAL_GAUGE_ACTION_GROUPOID",
}


def load_summary() -> tuple[str, dict]:
    text = DOC.read_text(encoding="utf-8")
    match = re.search(
        r"## 10\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        re.DOTALL,
    )
    if not match:
        raise AssertionError("machine-readable JSON summary block not found")
    return text, json.loads(match.group(1))


class ThreeCycleSynthesis1302Audit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text, cls.summary = load_summary()

    def test_required_sections_present(self) -> None:
        for heading in EXPECTED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_identity_and_verdict(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "Hourly20260625_1302_ThreeCycleFifteenHoleSynthesis_V1",
        )
        self.assertEqual(self.summary["run_id"], "hourly-20260625-1302")
        self.assertEqual(self.summary["cycle"], 3)
        self.assertEqual(
            self.summary["verdict"],
            "FIFTEEN_QUALITY_HOLES_ZERO_ACCEPTED_RECEIPTS_NO_PROOF_RESTART",
        )
        self.assertEqual(self.summary["verdict_class"], "three_cycle_closeout")

    def test_fifteen_holes_and_cycle_distribution(self) -> None:
        holes = self.summary["holes"]
        self.assertEqual(len(holes), 15)
        self.assertEqual([hole["hole"] for hole in holes], list(range(1, 16)))
        by_cycle = {1: 0, 2: 0, 3: 0}
        for hole in holes:
            by_cycle[hole["cycle"]] += 1
        self.assertEqual(by_cycle, {1: 5, 2: 5, 3: 5})

    def test_no_receipts_restart_promotion_or_target_import(self) -> None:
        decision = self.summary["run_level_decision"]
        self.assertEqual(decision["accepted_receipt_count"], 0)
        self.assertEqual(decision["accepted_for_routing_count"], 0)
        self.assertEqual(decision["family_identity_checks_passed"], 0)
        self.assertFalse(decision["proof_restart_allowed"])
        self.assertFalse(decision["claim_promotion_allowed"])
        self.assertFalse(decision["major_GU_claim_promoted"])
        self.assertFalse(decision["global_no_go_promoted"])
        self.assertFalse(decision["target_import_used"])
        for hole in self.summary["holes"]:
            self.assertEqual(hole["accepted_receipt_count"], 0, hole["artifact"])
            self.assertFalse(hole["proof_restart_allowed"], hole["artifact"])

    def test_cycle3_matrix_counts_are_conservative(self) -> None:
        matrices = self.summary["cycle3_matrices"]
        self.assertEqual(matrices["routes_ready_count"], 0)
        self.assertEqual(matrices["normalized_candidate_rows"], 20)
        self.assertEqual(matrices["scoped_negative_count"], 5)
        self.assertEqual(matrices["promotions_allowed"], 0)
        self.assertEqual(matrices["quality_candidates_claimed"], 26)
        self.assertFalse(matrices["global_no_go_promoted"])
        self.assertFalse(matrices["target_import_used"])

    def test_next_five_and_sequential_lanes(self) -> None:
        self.assertEqual(set(self.summary["next_five_goals_recommendation"]), EXPECTED_NEXT_FIVE)
        sequential = set(self.summary["sequential_not_next_parallel"])
        for lane in [
            "PTUJ_FORMULA_PACKET",
            "IG_SELECTOR_THEOREM_RESTART",
            "DGU_VZ_REPLAY_GATE",
            "RS_GENERATION_INDEX_RESTART",
            "QFT_PRAW_PFIN_DESCENT",
            "GLOBAL_NEGATIVE_BUNDLE_POLICY",
        ]:
            self.assertIn(lane, sequential)
        self.assertTrue(EXPECTED_NEXT_FIVE.isdisjoint(sequential))

    def test_result_counts_match_holes(self) -> None:
        counts = self.summary["result_counts"]
        self.assertEqual(counts["hole_count"], 15)
        self.assertEqual(counts["closed_full_receipts"], 0)
        self.assertEqual(counts["accepted_receipts"], 0)
        self.assertEqual(counts["accepted_for_routing"], 0)
        self.assertEqual(counts["proof_restart_ready"], 0)
        self.assertEqual(counts["conditional_not_closed"], 1)
        self.assertEqual(counts["dependency_synthesis"], 1)
        self.assertEqual(counts["global_no_go_blocked"], 1)
        self.assertEqual(counts["no_go"], 0)
        self.assertGreaterEqual(counts["blocked_or_underdefined"], 10)

    def test_final_category_review_blocks_inflation(self) -> None:
        review = self.summary["final_category_review"]
        for key in [
            "ptuj_metadata_not_receipt",
            "ptuj_tool_check_not_formula_packet",
            "shiab_existence_not_K_IG_selector",
            "d7_missing_transcript_not_multiplicity_proof",
            "dgu_adjacent_anchors_not_actual_identity_fields",
            "dgu_protocol_zero_fields_not_vz_replay",
            "ucsd_transcript_not_typed_rs_operator",
            "ucsd_contract_not_frame_evidence",
            "qft_gauge_candidate_not_physical_quotient",
            "scoped_negative_not_global_no_go",
        ]:
            self.assertTrue(review[key], key)
        self.assertFalse(review["target_import_used"])

    def test_disallowed_positive_promotion_phrases_are_absent(self) -> None:
        forbidden_patterns = [
            r"accepted_receipt_count:\s*[1-9]",
            r'"accepted_receipt_count"\s*:\s*[1-9]',
            r"proof_restart_allowed:\s*true",
            r'"proof_restart_allowed"\s*:\s*true',
            r"global_no_go_promoted:\s*true",
            r'"global_no_go_promoted"\s*:\s*true',
            r"major_GU_claim_promoted:\s*true",
            r'"major_GU_claim_promoted"\s*:\s*true',
            r"target_import_used:\s*true",
            r'"target_import_used"\s*:\s*true',
            r"promotions_allowed:\s*[1-9]",
            r'"promotions_allowed"\s*:\s*[1-9]',
        ]
        for pattern in forbidden_patterns:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                f"forbidden promotion phrase matched: {pattern}",
            )


if __name__ == "__main__":
    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(ThreeCycleSynthesis1302Audit)
    )
    raise SystemExit(0 if result.wasSuccessful() else 1)
