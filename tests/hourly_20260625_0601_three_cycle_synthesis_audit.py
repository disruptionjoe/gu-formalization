#!/usr/bin/env python3
"""Audit Hourly20260625_0601_ThreeCycleFifteenHoleSynthesis_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0601-three-cycle-fifteen-hole-synthesis.md"
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


class Hourly202606250601ThreeCycleSynthesisAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity_and_counts(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "Hourly20260625_0601_ThreeCycleFifteenHoleSynthesis_V1",
        )
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0601")
        self.assertEqual(self.summary["target_quality_holes"], 15)
        self.assertEqual(self.summary["actual_quality_holes"], 15)
        self.assertEqual(len(self.summary["holes"]), 15)

    def test_no_claim_promotion_or_restart(self) -> None:
        self.assertFalse(self.summary["major_gu_claim_promoted"])
        self.assertFalse(self.summary["global_no_go_promoted"])
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertEqual(self.summary["accepted_for_routing_count"], 0)
        self.assertEqual(self.summary["family_identity_checks_passed"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])

    def test_cycle_commits_and_audit_counts(self) -> None:
        commits = self.summary["cycle_commits"]
        self.assertEqual(commits["cycle_1"], "53e82c8")
        self.assertEqual(commits["cycle_2"], "3f50dab")
        self.assertEqual(commits["cycle_3"], "pending_at_synthesis_write")
        counts = self.summary["focused_audit_counts"]
        self.assertEqual(counts["cycle_1"], 28)
        self.assertEqual(counts["cycle_2"], 36)

    def test_next_frontier_objects(self) -> None:
        next_objects = set(self.summary["next_frontier_objects"])
        for required in [
            "OxfordPortalPowerPointFormulaFramePacket_V1",
            "KeatingPullThatUpJamieShiabProjectionFormulaAssetPacket_V1",
            "ManuscriptRepresentationTheoryBianchiRivalEliminatorForShiab_V1",
            "BosonicToDGU01SectorIdentityRule_V1",
            "ManualImageLevelRSFormulaDiagramAudit_V1",
            "QFTAlternatePrimarySourceQueryBundle_V1",
            "GlobalNegativeReceiptBundleAssembly_V1",
        ]:
            self.assertIn(required, next_objects)

    def test_category_review_blocks_invalid_promotions(self) -> None:
        review = self.summary["final_mathematical_category_review"]
        self.assertTrue(review["hosted_is_not_selected"])
        self.assertTrue(review["bosonic_locator_is_not_0_1_operator_receipt"])
        self.assertTrue(review["scoped_negative_is_not_global_no_go"])
        self.assertTrue(review["no_downstream_claim_promoted"])
        self.assertIn("A hosted object is not a selected object.", self.text)
        self.assertIn("A scoped negative is not a global no-go.", self.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
