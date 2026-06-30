#!/usr/bin/env python3
"""Audit Hourly20260625_0502_ThreeCycleFifteenHoleSynthesis_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0502-three-cycle-fifteen-hole-synthesis.md"
)

EXPECTED_NEXT_OBJECTS = {
    "AuthorManuscriptIGSelectorIdentityPacket_V1",
    "ActualDGU01OperatorReceiptCandidateFromAuthorManuscript_V1",
    "AuthorManuscriptRSRuleExtractionCandidate_V1",
    "AuthorManuscriptQFTFiniteProjectorLocatorRow_V1",
    "OxfordPortalPowerPointFormulaFramePacket_V1",
    "KeatingRevealed_ShiabProjectionSheet_V1",
}


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing synthesis JSON summary")
    return json.loads(match.group(1))


class ThreeCycleSynthesisAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = DOC.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity_and_counts(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "Hourly20260625_0502_ThreeCycleFifteenHoleSynthesis_V1",
        )
        self.assertEqual(self.summary["run"], "hourly-20260625-0502")
        self.assertEqual(self.summary["target_quality_holes"], 15)
        self.assertEqual(self.summary["actual_quality_holes"], 15)
        self.assertEqual(len(self.summary["holes"]), 15)

    def test_no_claim_promotion_or_restart(self) -> None:
        self.assertFalse(self.summary["major_gu_claim_promoted"])
        self.assertFalse(self.summary["global_no_go_promoted"])
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertEqual(self.summary["family_identity_checks_passed"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])

    def test_manuscript_acquisition_recorded(self) -> None:
        manuscript = self.summary["acquired_author_manuscript_object"]
        self.assertTrue(self.summary["manuscript_acquired"])
        self.assertEqual(
            manuscript["object_id"],
            "AcquiredAuthorManuscriptObject_V1:GU-MEDIA-2021-DRAFT-RELEASE",
        )
        self.assertEqual(
            manuscript["sha256"],
            "3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4",
        )
        self.assertEqual(manuscript["page_count_observed"], 69)
        self.assertIn("AcquiredAuthorManuscriptObject_V1", self.text)

    def test_cycle_commits_and_audit_counts(self) -> None:
        commits = self.summary["cycle_commits"]
        self.assertEqual(commits["cycle_1"], "0cde3c9")
        self.assertEqual(commits["cycle_2"], "c619d39")
        self.assertEqual(commits["cycle_3"], "pending_at_synthesis_write")
        counts = self.summary["focused_audit_counts"]
        self.assertEqual(counts["cycle_1"], 36)
        self.assertEqual(counts["cycle_2"], 41)
        self.assertEqual(counts["cycle_3"], 41)

    def test_scoped_negative_not_global_no_go(self) -> None:
        negatives = self.summary["valid_negative_receipts"]
        self.assertEqual(len(negatives), 1)
        qft = negatives[0]
        self.assertEqual(qft["family"], "QFT")
        self.assertEqual(qft["scope"], "acquired_2021_author_manuscript_pdf_text_only")
        self.assertFalse(qft["global_no_go"])
        self.assertIn("GlobalNegativeReceiptBundle_V1", self.text)

    def test_next_frontier_objects(self) -> None:
        self.assertEqual(set(self.summary["next_frontier_objects"]), EXPECTED_NEXT_OBJECTS)
        self.assertIn(
            "accepted_source_receipt",
            self.summary["sequential_before_proof_restart"],
        )
        self.assertIn(
            "family_mathematical_identity_check",
            self.summary["sequential_before_proof_restart"],
        )

    def test_hole_table_covers_three_cycles(self) -> None:
        holes = self.summary["holes"]
        self.assertEqual([sum(1 for hole in holes if hole["cycle"] == cycle) for cycle in [1, 2, 3]], [5, 5, 5])
        verdicts = {hole["verdict_class"] for hole in holes}
        self.assertIn("conditional", verdicts)
        self.assertIn("quarantined", verdicts)
        self.assertIn("underdefined", verdicts)
        self.assertIn("scoped_negative_valid_global_no_go_blocked", verdicts)


if __name__ == "__main__":
    unittest.main()
