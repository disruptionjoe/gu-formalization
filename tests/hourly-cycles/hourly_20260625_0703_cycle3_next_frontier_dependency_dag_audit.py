#!/usr/bin/env python3
"""Audit NextFrontierDependencyDAGAfterHourly20260625_0703_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0703-cycle3-next-frontier-dependency-dag.md"
)

REQUIRED_JSON_KEYS = {
    "artifact",
    "run_id",
    "cycle",
    "lane",
    "artifact_id",
    "verdict",
    "next_objects",
    "dependency_edges",
    "parallel_safe_next_objects",
    "sequential_lanes",
    "proof_restart_allowed",
    "material_change_to_next_goals",
    "first_obstruction",
    "companion_audit",
}


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 9\. JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing next-frontier dependency DAG JSON summary")
    return json.loads(match.group(1))


class NextFrontierDependencyDAGAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_json_identity_and_required_keys(self) -> None:
        self.assertTrue(REQUIRED_JSON_KEYS.issubset(self.summary))
        self.assertEqual(
            self.summary["artifact"],
            "NextFrontierDependencyDAGAfterHourly20260625_0703_V1",
        )
        self.assertEqual(
            self.summary["artifact_id"],
            "NextFrontierDependencyDAGAfterHourly20260625_0703_V1",
        )
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0703")
        self.assertEqual(self.summary["cycle"], 3)
        self.assertEqual(self.summary["lane"], 4)
        self.assertEqual(
            self.summary["companion_audit"],
            "tests/hourly_20260625_0703_cycle3_next_frontier_dependency_dag_audit.py",
        )

    def test_at_least_six_next_objects_present(self) -> None:
        next_objects = self.summary["next_objects"]
        self.assertGreaterEqual(len(next_objects), 6)
        required = {
            "VisualFormulaReceiptCandidateLedgerForOxfordPortalFrames_V1",
            "OxfordBosonicTwoAnchorDGU01IdentityPacket_V1",
            "DecodableTzSEvmqxu48ArchiveOrSourceAssetWithFormulaFrameAudit_V1",
            "FrameAndFormulaCompletionBundleForQFTPFinBDeclaredSurfaces_V1",
            "RecoveredBianchiHighestWeightSelectorForShiab_V1",
            "TimestampedTranscriptAcquisitionForModernRSSurfaces_V1",
        }
        object_ids = {row["object_id"] for row in next_objects.values()}
        self.assertTrue(required.issubset(object_ids))
        for object_id in required:
            self.assertIn(object_id, self.text)

    def test_dependency_edges_include_receipt_identity_restart_chain(self) -> None:
        edges = {tuple(edge) for edge in self.summary["dependency_edges"]}
        self.assertIn(("accepted_receipt_row", "family_identity_check"), edges)
        self.assertIn(("family_identity_check", "proof_restart_readiness_classifier"), edges)
        self.assertIn(
            ("proof_restart_readiness_classifier", "downstream_proof_replay"),
            edges,
        )

    def test_proof_restart_forbidden_and_material_change_true(self) -> None:
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])
        self.assertTrue(self.summary["material_change_to_next_goals"])
        self.assertEqual(self.summary["accepted_family_receipts"], 0)
        self.assertEqual(self.summary["family_identity_checks_passed"], 0)

    def test_parallel_safe_and_sequential_lanes_are_separated(self) -> None:
        parallel_safe = set(self.summary["parallel_safe_next_objects"])
        self.assertGreaterEqual(len(parallel_safe), 6)
        sequential = self.summary["sequential_lanes"]
        self.assertTrue(all(not lane["parallel_safe_now"] for lane in sequential))
        generic = next(
            lane for lane in sequential if lane["id"] == "generic_receipt_to_restart_chain"
        )
        self.assertEqual(
            generic["steps"],
            [
                "source_or_formula_completion",
                "accepted_receipt_row",
                "family_identity_check",
                "proof_restart_readiness_classifier",
                "downstream_proof_replay",
            ],
        )

    def test_material_deltas_reflect_cycle_results(self) -> None:
        deltas = {row["id"]: row["delta"] for row in self.summary["source_deltas"]}
        self.assertEqual(
            deltas["oxford_frames"],
            "checksummed_transcribed_candidate_rows_exist",
        )
        self.assertEqual(
            deltas["keating_tzsevmqxu48"],
            "storyboard_negative_full_stream_decode_blocked",
        )
        self.assertEqual(
            deltas["qft_toe_jaimungal"],
            "captions_newly_fetchable_no_P_fin_b_payload",
        )
        self.assertEqual(
            deltas["ig_shiab"],
            "source_window_inventory_exists_selector_theorem_missing",
        )
        self.assertEqual(
            deltas["rs_alternate"],
            "scoped_negative_extended_global_no_go_blocked",
        )
        self.assertEqual(
            deltas["oxford_dgu"],
            "category_change_guard_active_for_bosonic_to_DGU01",
        )

    def test_required_sections_present(self) -> None:
        for heading in [
            "## 1. Verdict",
            "## 2. Specific Claim/Bridge Under Test",
            "## 3. Owned Path and Sources Read First",
            "## 4. Strongest Positive Construction Attempt",
            "## 5. First Exact Obstruction",
            "## 6. What Would Change If Closed",
            "## 7. Falsification/Demotion Condition",
            "## 8. Next Meaningful Computation",
            "## 9. JSON Summary",
        ]:
            self.assertIn(heading, self.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
