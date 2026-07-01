#!/usr/bin/env python3
"""Audit GlobalNegativeBundlePreconditionMatrix_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0601-cycle3-global-negative-bundle-precondition-matrix.md"
)


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary")
    return json.loads(match.group(1))


class GlobalNegativeBundlePreconditionMatrixAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "GlobalNegativeBundlePreconditionMatrix_V1",
        )
        self.assertEqual(self.summary["run"], "hourly-20260625-0601")
        self.assertEqual(self.summary["cycle"], 3)
        identity = self.summary["artifact_identity"]
        self.assertEqual(
            identity["artifact_id"],
            "GlobalNegativeBundlePreconditionMatrix_V1",
        )
        self.assertEqual(
            identity["owned_path"],
            "explorations/hourly-20260625-0601-cycle3-global-negative-bundle-precondition-matrix.md",
        )
        self.assertEqual(
            identity["companion_audit"],
            "tests/hourly_20260625_0601_cycle3_global_negative_bundle_precondition_matrix_audit.py",
        )

    def test_global_negative_bundles_are_named_missing_preconditions(self) -> None:
        bundle = self.summary["missing_global_negative_bundle"]
        self.assertEqual(bundle["id"], "GlobalNegativeReceiptBundle_V1")
        self.assertTrue(bundle["missing"])
        self.assertTrue(bundle["required_before_global_no_go"])
        self.assertTrue(bundle["required_before_global_demotion"])
        self.assertEqual(bundle["accepted_receipt_count_required"], 0)
        self.assertIn("synthesis_rule", bundle["required_fields"])

        rs_bundle = self.summary["missing_rs_global_negative_bundle"]
        self.assertEqual(rs_bundle["id"], "GlobalRSNegativeReceiptBundle_V1")
        self.assertTrue(rs_bundle["missing"])
        self.assertTrue(rs_bundle["required_before_RS_global_no_go"])
        self.assertIn(
            "synthesis_rule_from_scoped_negatives_to_global_RS_no_go",
            rs_bundle["required_fields"],
        )

    def test_no_global_no_go_or_demotion_is_allowed(self) -> None:
        self.assertEqual(self.summary["decision"], "no_global_no_go")
        self.assertFalse(self.summary["global_no_go_allowed"])
        self.assertFalse(self.summary["global_demotion_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])
        obstruction = self.summary["first_obstruction"]
        self.assertEqual(obstruction["id"], "missing_complete_GlobalNegativeReceiptBundle_V1")
        self.assertTrue(obstruction["blocks_global_no_go"])
        self.assertIn("global no-go", self.text.lower())

    def test_scoped_negatives_are_preserved_for_all_families(self) -> None:
        self.assertTrue(self.summary["scoped_negatives_preserved"])
        rows = {row["family"]: row for row in self.summary["family_rows"]}
        self.assertEqual(set(rows), {"RS", "QFT", "IG", "DGU"})
        for family, row in rows.items():
            self.assertTrue(row["scoped_negative_preserved"], family)
            self.assertFalse(row["global_no_go_allowed"], family)
            self.assertEqual(row["accepted_receipt_count"], 0, family)
            self.assertFalse(row["proof_restart_allowed"], family)
        self.assertEqual(rows["RS"]["missing_bundle"], "GlobalRSNegativeReceiptBundle_V1")

    def test_accepted_receipt_count_zero_and_proof_restart_false(self) -> None:
        self.assertEqual(self.summary["accepted_receipts"], [])
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])
        impact = self.summary["impact_if_closed"]
        self.assertFalse(impact["proof_restart_allowed"])
        self.assertFalse(impact["current_global_no_go_allowed"])

    def test_falsification_and_next_computation_require_bundle_not_proof_restart(self) -> None:
        conditions = self.summary["falsification_and_demotion_conditions"]
        self.assertIn("GlobalNegativeReceiptBundle_V1", conditions["artifact_falsified_by"])
        self.assertIn("GlobalRSNegativeReceiptBundle_V1", conditions["rs_global_demotion_condition"])
        self.assertTrue(conditions["any_positive_receipt_blocks_global_negative"])

        next_step = self.summary["next_meaningful_computation"]
        self.assertEqual(next_step["source_computation"], "GlobalNegativeReceiptBundleAssembly_V1")
        self.assertEqual(next_step["rs_sub_bundle"], "GlobalRSNegativeReceiptBundle_V1")
        self.assertFalse(next_step["proof_restart_currently_allowed"])
        self.assertFalse(next_step["global_demotion_currently_allowed"])

    def test_forbidden_promotions_cover_requested_failure_modes(self) -> None:
        forbidden = set(self.summary["forbidden_promotions"])
        self.assertIn("global_GU_no_go_from_current_cycle2_scoped_negatives", forbidden)
        self.assertIn(
            "RS_d_RS_minus_1_globally_absent_from_GU_without_GlobalRSNegativeReceiptBundle_V1",
            forbidden,
        )
        self.assertIn("proof_restart_before_accepted_receipt_and_family_identity_check", forbidden)
        self.assertIn("global_demotion_before_synthesis_rule", forbidden)


if __name__ == "__main__":
    unittest.main()
