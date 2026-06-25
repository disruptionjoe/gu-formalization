#!/usr/bin/env python3
"""Audit the hourly 1602 three-cycle synthesis artifact."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "explorations" / "hourly-20260625-1602-three-cycle-fifteen-hole-synthesis.md"


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


class Hourly1602ThreeCycleSynthesisAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_artifact()
        cls.summary = extract_summary(cls.text)

    def test_frontmatter_and_identity(self) -> None:
        self.assertTrue(self.text.startswith("---\n"))
        self.assertIn('artifact_id: "Hourly20260625_1602_ThreeCycleFifteenHoleSynthesis_V1"', self.text)
        self.assertEqual(self.summary["artifact"], "Hourly20260625_1602_ThreeCycleFifteenHoleSynthesis_V1")
        self.assertEqual(self.summary["run_id"], "hourly-20260625-1602")
        self.assertEqual(self.summary["verdict_class"], "three_cycle_closeout")

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

    def test_cycle_commits_and_audit_counts_are_recorded(self) -> None:
        commits = self.summary["cycle_commits"]
        self.assertEqual(commits["cycle_1"], "acaa062")
        self.assertEqual(commits["cycle_2"], "a2c4bfa")
        self.assertEqual(commits["cycle_3"], "pending_parent_commit")
        self.assertEqual(self.summary["audit_counts"]["cycle_1"], 35)
        self.assertEqual(self.summary["audit_counts"]["cycle_2"], 36)
        self.assertEqual(self.summary["audit_counts"]["cycle_3"], 28)

    def test_fifteen_holes_are_all_non_promoting(self) -> None:
        holes = self.summary["holes"]
        self.assertEqual(len(holes), 15)
        self.assertEqual(self.summary["result_counts"]["hole_count"], 15)
        for hole in holes:
            self.assertEqual(hole["accepted_receipt_count"], 0, hole)
            self.assertFalse(hole["proof_restart_allowed"], hole)
            self.assertIn("next_object", hole)
            self.assertTrue(hole["next_object"])

    def test_next_frontier_is_five_parallel_producer_lanes(self) -> None:
        recommended = self.summary["recommended_next_five"]
        self.assertEqual(len(recommended), 5)
        self.assertEqual(len(set(recommended)), 5)
        self.assertIn("PTUJ_ACCEPTED_SOURCE_OBJECT_BRANCH_RECEIPT", recommended)
        self.assertIn("RAW_OR_FORMAL_D7_BRANCHING_TRANSCRIPT_FOR_SHIAB_HOM_SPACE", recommended)
        self.assertIn("SOURCE_DEFINED_RAW_BRANCH_LOCAL_GAUGE_GROUPOID_PACKET_FOR_R_RAW_B_O", recommended)
        self.assertGreaterEqual(len(self.summary["sequential_deferred"]), 5)

    def test_final_category_review_rejects_forbidden_promotions(self) -> None:
        review = self.summary["final_category_review"]
        for key in [
            "ptuj_metadata_not_receipt",
            "chirality_not_selector_theorem",
            "typed_spine_not_actual_dgu_identity_packet",
            "repo_local_absence_not_visual_unavailability_packet",
            "qft_schema_not_source_defined_groupoid",
            "scoped_blockers_not_global_no_go",
        ]:
            self.assertTrue(review[key], key)
        self.assertFalse(review["target_import_used"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
