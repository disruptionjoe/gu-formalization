#!/usr/bin/env python3
"""Audit Hourly20260625_0703_ThreeCycleFifteenHoleSynthesis_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0703-three-cycle-fifteen-hole-synthesis.md"
)


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing 0703 synthesis JSON summary")
    return json.loads(match.group(1))


class Hourly202606250703ThreeCycleSynthesisAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity_and_hole_count(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "Hourly20260625_0703_ThreeCycleFifteenHoleSynthesis_V1",
        )
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0703")
        self.assertEqual(self.summary["target_quality_holes"], 15)
        self.assertEqual(self.summary["actual_quality_holes"], 15)
        self.assertEqual(len(self.summary["holes"]), 15)

    def test_no_receipts_restart_or_promotions(self) -> None:
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertEqual(self.summary["accepted_for_routing_count"], 0)
        self.assertEqual(self.summary["family_identity_checks_passed"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])
        self.assertFalse(self.summary["major_gu_claim_promoted"])
        self.assertFalse(self.summary["global_no_go_promoted"])
        self.assertFalse(self.summary["canon_status_changed"])
        self.assertFalse(self.summary["active_research_status_changed"])

    def test_transition_matrix_count_preserved(self) -> None:
        self.assertEqual(self.summary["transition_rows_counted"], 68)
        self.assertIn("68 candidate/source/visual/acquisition rows", self.text)

    def test_cycle_commits_and_audit_counts(self) -> None:
        commits = self.summary["cycle_commits"]
        self.assertEqual(commits["cycle_1"], "7d21616")
        self.assertEqual(commits["cycle_2"], "e1ada8b")
        self.assertEqual(commits["cycle_3"], "pending_at_synthesis_write")
        counts = self.summary["focused_audit_counts"]
        self.assertEqual(counts["cycle_1"], 25)
        self.assertEqual(counts["cycle_2"], 30)
        self.assertEqual(counts["cycle_3"], 27)
        self.assertEqual(counts["synthesis"], 8)
        self.assertEqual(counts["total"], 90)

    def test_key_positive_deltas_are_recorded_without_acceptance(self) -> None:
        for phrase in [
            "Oxford/Portal frames",
            "Keating storyboard negative",
            "newly fetchable TOE/Jaimungal captions",
            "IG source-window inventory",
            "extended RS/QFT scoped negatives",
        ]:
            self.assertIn(phrase, self.text)

    def test_next_frontier_objects_are_source_and_identity_gates(self) -> None:
        next_objects = set(self.summary["next_frontier_objects"])
        expected = {
            "RecoveredBianchiHighestWeightSelectorForShiab_V1",
            "VisualFormulaReceiptCandidateLedgerForOxfordPortalFrames_V1",
            "OxfordBosonicTwoAnchorDGU01IdentityPacket_V1",
            "DecodableTzSEvmqxu48ArchiveOrSourceAssetWithFormulaFrameAudit_V1",
            "FrameAndFormulaCompletionBundleForQFTPFinBDeclaredSurfaces_V1",
            "TimestampedTranscriptAcquisitionForModernRSSurfaces_V1",
            "SixFamilyGlobalNegativeReceiptBundleAssemblyAfterHourly20260625_0703_V1",
        }
        self.assertEqual(next_objects, expected)

    def test_final_category_review_blocks_invalid_promotions(self) -> None:
        review = self.summary["final_mathematical_category_review"]
        for key in [
            "hosted_is_not_selected",
            "bosonic_visual_equation_is_not_DGU01_receipt",
            "scoped_negative_is_not_global_no_go",
            "captions_storyboards_transcripts_are_not_receipts",
            "source_window_inventory_is_not_selector_theorem",
            "no_downstream_claim_promoted",
        ]:
            self.assertTrue(review[key], key)

    def test_required_sections_present(self) -> None:
        for heading in [
            "## 1. Verdict",
            "## 2. Fifteen-Hole Result Table",
            "## 3. Closed, Conditional, Blocked, Failed, Or No-Go",
            "## 4. Next Frontier Objects",
            "## 5. Final Mathematical And Category Review",
            "## 6. Wrapper Assessment",
            "## 7. Verification Summary",
            "## 8. Machine-Readable JSON Summary",
        ]:
            self.assertIn(heading, self.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
