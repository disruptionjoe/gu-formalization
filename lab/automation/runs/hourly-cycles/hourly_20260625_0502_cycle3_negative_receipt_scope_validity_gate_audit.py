#!/usr/bin/env python3
"""Audit NegativeReceiptScopeValidityGate_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0502-cycle3-negative-receipt-scope-validity-gate.md"
)


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 9\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary")
    return json.loads(match.group(1))


class NegativeReceiptScopeValidityGateAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)
        cls.receipts = {row["id"]: row for row in cls.summary["receipt_validity"]}

    def test_artifact_identity(self) -> None:
        self.assertEqual(self.summary["artifact"], "NegativeReceiptScopeValidityGate_V1")
        self.assertEqual(self.summary["run"], "hourly-20260625-0502")
        self.assertEqual(self.summary["cycle"], 3)
        self.assertEqual(self.summary["lane"], 3)
        identity = self.summary["artifact_identity"]
        self.assertEqual(
            identity["owned_path"],
            "explorations/hourly-20260625-0502-cycle3-negative-receipt-scope-validity-gate.md",
        )
        self.assertEqual(
            identity["companion_audit"],
            "tests/hourly_20260625_0502_cycle3_negative_receipt_scope_validity_gate_audit.py",
        )

    def test_no_global_no_go_or_demotion(self) -> None:
        self.assertFalse(self.summary["global_no_go_allowed"])
        self.assertFalse(self.summary["global_demotion_allowed"])
        missing = self.summary["first_exact_missing_condition_for_global_no_go"]
        self.assertEqual(missing["id"], "GlobalNegativeReceiptBundle_V1")
        self.assertTrue(missing["missing"])
        self.assertIn("all primary GU source surfaces", missing["description"])

    def test_qft_manuscript_scoped_absence_only(self) -> None:
        qft = self.receipts["QFT_P_fin_b_author_manuscript_2021"]
        self.assertEqual(qft["family"], "QFT")
        self.assertEqual(qft["negative_scope"], "manuscript_scoped_only")
        self.assertTrue(qft["complete_acquired_scope"])
        self.assertTrue(qft["query_log_preserved"])
        self.assertTrue(qft["variant_logging_preserved"])
        self.assertTrue(qft["inspected_hit_list_preserved"])
        self.assertTrue(qft["exact_required_object_absent"])
        self.assertTrue(qft["valid_negative_receipt"])
        self.assertFalse(qft["global_absence_claim_allowed"])
        self.assertIn("equivalent finite source extraction", qft["rollback_condition"])

    def test_rs_is_not_valid_negative_receipt(self) -> None:
        rs = self.receipts["RS_d_RS_minus_1_author_manuscript_2021"]
        self.assertEqual(rs["family"], "RS")
        self.assertEqual(rs["status"], "quarantined_underdefined")
        self.assertFalse(rs["query_log_preserved"])
        self.assertFalse(rs["variant_logging_preserved"])
        self.assertFalse(rs["exact_required_object_absent"])
        self.assertFalse(rs["valid_negative_receipt"])
        self.assertFalse(rs["global_absence_claim_allowed"])
        self.assertIn("d_RS,-1", rs["rollback_condition"])

    def test_transcript_scopes_are_incomplete(self) -> None:
        jre = self.receipts["JRE_1453_1628_transcripts"]
        toe = self.receipts["TOE_Jaimungal_GU40_transcript"]
        for row in [jre, toe]:
            self.assertFalse(row["complete_acquired_scope"])
            self.assertTrue(row["incomplete_transcript_scope"])
            self.assertFalse(row["query_log_preserved"])
            self.assertFalse(row["valid_negative_receipt"])
            self.assertFalse(row["global_absence_claim_allowed"])
            self.assertFalse(row["proof_restart_allowed"])
        self.assertFalse(toe["full_transcript_acquired"])

    def test_proof_restart_false_everywhere(self) -> None:
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["negative_policy_requirements_applied"]["proof_restart_allowed"])
        for row in self.summary["receipt_validity"]:
            self.assertFalse(row["proof_restart_allowed"], row["id"])
            self.assertFalse(row["claim_promotion_allowed"], row["id"])

    def test_rollback_conditions_are_present(self) -> None:
        for row in self.summary["receipt_validity"]:
            self.assertIn("rollback_condition", row, row["id"])
            self.assertGreater(len(row["rollback_condition"]), 40, row["id"])

    def test_claim_impact_and_forbidden_promotions(self) -> None:
        impact = self.summary["claim_impact"]
        self.assertTrue(impact["QFT_author_manuscript_source_receipt_for_P_fin_b_blocked"])
        self.assertFalse(impact["QFT_global_branch_demoted"])
        self.assertFalse(impact["RS_manuscript_negative_receipt_valid"])
        self.assertFalse(impact["RS_global_branch_demoted"])
        self.assertFalse(impact["transcript_absence_claims_valid"])
        self.assertFalse(impact["proof_restart_allowed"])
        forbidden = set(self.summary["forbidden_promotions"])
        self.assertIn("QFT_P_fin_b_globally_absent_from_GU", forbidden)
        self.assertIn("RS_d_RS_minus_1_globally_absent_from_GU", forbidden)
        self.assertIn("negative_receipt_permits_proof_restart", forbidden)


if __name__ == "__main__":
    unittest.main()
