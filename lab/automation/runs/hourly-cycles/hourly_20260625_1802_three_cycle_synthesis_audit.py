#!/usr/bin/env python3
"""Audit the hourly 1802 three-cycle synthesis artifact."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "explorations" / "hourly-20260625-1802-three-cycle-fifteen-hole-synthesis.md"


def read_artifact() -> str:
    return ARTIFACT.read_text(encoding="utf-8")


def extract_summary(text: str) -> dict:
    match = re.search(
        r"## 8\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary")
    return json.loads(match.group(1))


class Hourly1802ThreeCycleSynthesisAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_artifact()
        cls.summary = extract_summary(cls.text)

    def test_frontmatter_and_identity(self) -> None:
        self.assertTrue(self.text.startswith("---\n"))
        self.assertIn(
            'artifact_id: "Hourly20260625_1802_ThreeCycleFifteenHoleSynthesis_V1"',
            self.text,
        )
        self.assertEqual(
            self.summary["artifact"],
            "Hourly20260625_1802_ThreeCycleFifteenHoleSynthesis_V1",
        )
        self.assertEqual(self.summary["run_id"], "hourly-20260625-1802")
        self.assertEqual(self.summary["verdict_class"], "three_cycle_closeout")
        self.assertEqual(
            self.summary["owned_path"],
            "explorations/hourly-20260625-1802-three-cycle-fifteen-hole-synthesis.md",
        )
        self.assertEqual(
            self.summary["companion_audit"],
            "tests/hourly_20260625_1802_three_cycle_synthesis_audit.py",
        )

    def test_run_level_decision_blocks_promotion(self) -> None:
        decision = self.summary["run_level_decision"]
        self.assertEqual(decision["accepted_receipt_count"], 0)
        self.assertEqual(decision["accepted_for_routing_count"], 0)
        self.assertEqual(decision["routes_ready_count"], 0)
        self.assertFalse(decision["proof_restart_allowed"])
        self.assertFalse(decision["claim_promotion_allowed"])
        self.assertFalse(decision["major_GU_claim_promoted"])
        self.assertFalse(decision["global_no_go_promoted"])
        self.assertFalse(decision["target_import_used"])
        self.assertFalse(decision["downstream_replay_allowed"])

    def test_cycle_commits_and_audit_counts_are_recorded(self) -> None:
        commits = self.summary["cycle_commits"]
        self.assertEqual(commits["cycle_1"], "e3bebc6")
        self.assertEqual(commits["cycle_2"], "2413325")
        self.assertEqual(commits["cycle_3"], "pending_parent_commit")
        self.assertEqual(self.summary["interleaved_non_run_commits"], ["d6fff4d", "0f71cd1"])
        self.assertEqual(self.summary["audit_counts"]["cycle_1"], 35)
        self.assertEqual(self.summary["audit_counts"]["cycle_2"], 36)
        self.assertEqual(self.summary["audit_counts"]["cycle_3"], 27)
        self.assertEqual(self.summary["audit_counts"]["pre_synthesis_total"], 98)

    def test_fifteen_holes_are_all_non_promoting(self) -> None:
        holes = self.summary["holes"]
        self.assertEqual(len(holes), 15)
        self.assertEqual(self.summary["result_counts"]["hole_count"], 15)
        self.assertEqual(self.summary["result_counts"]["accepted_receipts"], 0)
        self.assertEqual(self.summary["result_counts"]["accepted_for_routing"], 0)
        self.assertEqual(self.summary["result_counts"]["proof_restart_ready"], 0)
        self.assertEqual(self.summary["result_counts"]["underdefined"], 2)
        for hole in holes:
            self.assertEqual(hole["accepted_receipt_count"], 0, hole)
            self.assertFalse(hole["proof_restart_allowed"], hole)
            self.assertTrue(hole["first_obstruction"], hole)
            self.assertTrue(hole["next_object"], hole)

    def test_next_frontier_is_five_parallel_producer_lanes(self) -> None:
        recommended = self.summary["recommended_next_five"]
        self.assertEqual(len(recommended), 5)
        self.assertEqual(len(set(recommended)), 5)
        self.assertIn("PTUJ_SINGLE_COMPLETE_BRANCH_RECEIPT", recommended)
        self.assertIn("IG_PRODUCT_B_FULL_D7_SUMMAND_MULTIPLICITY_DIMENSION_RECEIPT", recommended)
        self.assertIn("DGU_SOURCE_EMITTED_SECTOR_RULE_AND_SAME_OPERATOR_RECEIPT", recommended)
        self.assertIn("RS_LAWFUL_CAPTURE_ROUTE_OR_FULL_VISUAL_DENIAL_PACKET", recommended)
        self.assertIn("QFT_SOURCE_DEFINED_IOTA_B_AND_TYPED_R_RAW_B_O_RECEIPT", recommended)
        self.assertGreaterEqual(len(self.summary["sequential_deferred"]), 5)

    def test_final_category_review_rejects_forbidden_promotions(self) -> None:
        review = self.summary["final_category_review"]
        for key in [
            "ptuj_cross_branch_conflation_rejected",
            "ptuj_metadata_not_receipt",
            "product_A_or_chirality_not_Product_B_transcript",
            "target_generation_count_not_selector_evidence",
            "typed_spine_not_actual_dgu_identity_packet",
            "dgu_symbol_compatibility_not_sector_rule",
            "transcript_locator_not_typed_rs_operator",
            "failed_local_capture_not_full_unavailability",
            "qft_schema_not_source_defined_groupoid",
            "downstream_qft_desiderata_not_source_selectors",
            "scoped_blockers_not_global_no_go",
        ]:
            self.assertTrue(review[key], key)
        self.assertFalse(review["target_import_used"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
