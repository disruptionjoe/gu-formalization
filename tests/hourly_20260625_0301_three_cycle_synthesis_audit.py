#!/usr/bin/env python3
"""Audit Hourly20260625_0301_ThreeCycleFifteenHoleSynthesis_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0301-three-cycle-fifteen-hole-synthesis.md"
)


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 9\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing three-cycle synthesis JSON")
    return json.loads(match.group(1))


class Hourly202606250301ThreeCycleSynthesisAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity_models_and_counts(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "Hourly20260625_0301_ThreeCycleFifteenHoleSynthesis_V1",
        )
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0301")
        self.assertEqual(
            self.summary["runbook"],
            "process/runbooks/three-cycle-fifteen-hole-run.md",
        )
        self.assertEqual(self.summary["orchestrator_model"], "gpt-5.5")
        self.assertEqual(self.summary["orchestrator_reasoning"], "high")
        self.assertEqual(self.summary["worker_reasoning"], "medium")
        self.assertEqual(self.summary["final_review_reasoning"], "high")
        self.assertEqual(self.summary["target_quality_holes"], 15)
        self.assertEqual(self.summary["actual_quality_holes"], 15)
        self.assertEqual(len(self.summary["holes"]), 15)

    def test_local_manuscript_acquired_but_no_claim_promotion(self) -> None:
        manuscript = self.summary["local_author_manuscript"]
        self.assertEqual(manuscript["status"], "acquired_pending_query")
        self.assertEqual(manuscript["page_count"], 69)
        self.assertEqual(
            manuscript["sha256"],
            "3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4",
        )
        self.assertFalse(self.summary["major_gu_claim_promoted"])
        self.assertFalse(self.summary["global_no_go_promoted"])
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertEqual(self.summary["accepted_for_routing_count"], 0)
        self.assertEqual(self.summary["family_identity_checks_passed"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])
        self.assertFalse(self.summary["principal_symbol_work_allowed"])

    def test_hole_table_covers_expected_artifact_families(self) -> None:
        holes = self.summary["holes"]
        artifacts = {hole["artifact"] for hole in holes}
        for required in [
            "AcquiredAuthorManuscriptObject_V1",
            "ManuscriptIGSelectorIdentityPacket_V1",
            "RenderedCriticalDisplayTranscriptionPacket_IG_V1",
            "RenderedCriticalDisplayTranscriptionPacket_RS_V1",
            "RenderedCriticalDisplayTranscriptionPacket_DGU01_V1",
            "FiniteLocalQFTExtractionMapSpec_V1",
            "UCSDVisualFrameCaptureFeasibilityGate_V1",
        ]:
            self.assertIn(required, artifacts)

        self.assertEqual(
            [hole["cycle"] for hole in holes].count(1),
            5,
        )
        self.assertEqual(
            [hole["cycle"] for hole in holes].count(2),
            5,
        )
        self.assertEqual(
            [hole["cycle"] for hole in holes].count(3),
            5,
        )

    def test_cycle_commits_and_audit_counts(self) -> None:
        commits = self.summary["cycle_commits"]
        self.assertEqual(commits["cycle_1"], "8eefa20")
        self.assertEqual(commits["cycle_2"], "d73467b")
        self.assertEqual(commits["cycle_3"], "pending_at_synthesis_write")
        counts = self.summary["focused_audit_counts"]
        self.assertEqual(counts["cycle_1"], 5)
        self.assertEqual(counts["cycle_2"], 5)
        self.assertEqual(counts["cycle_3"], 5)

    def test_next_frontier_and_sequencing_are_source_first(self) -> None:
        next_objects = set(self.summary["next_frontier_objects"])
        for required in [
            "ShiabRepresentationBianchiRivalEliminatorTable_IG_V1",
            "RSSourceMinusOneMapIdentityPacket_V1",
            "DGU01SourceEstablishedIdentityPacket_V1",
            "SingleObservationFiniteExtractionPilot_V1",
            "UCSDSourceSafeVisualArtifactPacket_V1",
            "SourceEmittedFiniteLocalExtractionOperatorWithFiniteCodomain_V1",
        ]:
            self.assertIn(required, next_objects)

        sequential = self.summary["sequential_before_proof_restart"]
        self.assertEqual(sequential[0], "accepted_source_receipt")
        self.assertIn("family_identity_check", sequential)
        self.assertIn("proof_restart_readiness_classifier", sequential)

    def test_final_category_review_blocks_invalid_promotions(self) -> None:
        review = self.summary["final_mathematical_category_review"]
        self.assertTrue(review["hosted_is_not_accepted_receipt"])
        self.assertTrue(review["source_native_action_EL_cluster_is_not_DGU01_target_identity"])
        self.assertTrue(review["scoped_negative_is_not_global_no_go"])
        self.assertTrue(review["reconstruction_spec_is_not_source_derivation"])
        self.assertTrue(review["transcript_anchor_is_not_visual_formula_receipt"])
        self.assertTrue(review["no_downstream_claim_promoted"])

        self.assertIn("A source-hosted or rendered-confirmed formula family", self.text)
        self.assertIn("A scoped negative is not a global no-go.", self.text)
        self.assertIn("A reconstruction-grade specification shell", self.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
