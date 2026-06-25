#!/usr/bin/env python3
"""Audit the hourly 20260625 0103 three-cycle synthesis."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = REPO_ROOT / "explorations" / "hourly-20260625-0103-three-cycle-fifteen-hole-synthesis.md"


def read_doc() -> str:
    return DOC.read_text(encoding="utf-8")


def extract_summary(text: str) -> dict:
    match = re.search(
        r"## 10\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary")
    return json.loads(match.group(1))


class ThreeCycleSynthesisAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_no_major_promotion_or_global_nogo(self) -> None:
        self.assertFalse(self.summary["major_gu_claim_promoted"])
        self.assertFalse(self.summary["global_no_go_promoted"])
        self.assertTrue(self.summary["source_receipt_frontier"])
        self.assertRegex(self.text, r"no major GU claim\s+promotion")

    def test_fifteen_holes_and_audit_counts(self) -> None:
        self.assertEqual(self.summary["hole_counts"], {"cycle_1": 5, "cycle_2": 5, "cycle_3": 5, "total": 15})
        self.assertEqual(self.summary["focused_audit_counts"]["cycle_1"], 49)
        self.assertEqual(self.summary["focused_audit_counts"]["cycle_2"], 55)
        self.assertEqual(self.summary["focused_audit_counts"]["cycle_3"], 62)
        self.assertEqual(self.summary["focused_audit_counts"]["total"], 166)

    def test_blocked_objects_and_next_frontier_are_source_receipts(self) -> None:
        blocked = set(self.summary["blocked_primary_objects"])
        for required in [
            "SourceForcedCodomainSelectorForK_IG",
            "source_action_or_noether_locator_for_d_RS_minus_1",
            "source_projector_P_fin_b",
            "operator_source_primary_action_or_EL",
            "PrimarySourceReceiptInstance_V1",
        ]:
            self.assertIn(required, blocked)
        next_objects = set(self.summary["next_frontier_objects"])
        for required in [
            "PFinBSourceReceiptRow_V1",
            "DGU01OperatorSourceReceipt_V1",
            "RS_SOURCE_ACTION_NOETHER_RECEIPT_V1",
            "K_IGSourceReceiptRow_V1",
            "RepoLocalPrimaryGUSourceReceiptMap_V1",
        ]:
            self.assertIn(required, next_objects)

    def test_target_facing_work_remains_blocked(self) -> None:
        blocked = set(self.summary["blocked_before_target_facing_work"])
        for required in [
            "theta_FLRW_coefficients",
            "RS_rank_index_generation",
            "QFT_finite_seed_covariance_rho_AB_CHSH",
            "actual_DGU_VZ_closure",
        ]:
            self.assertIn(required, blocked)
        self.assertNotIn('"major_gu_claim_promoted": true', self.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
