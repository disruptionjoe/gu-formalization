#!/usr/bin/env python3
"""Audit the 0803 cycle-2 UCSD typed RS operator classifier."""

from __future__ import annotations

import json
import re
from pathlib import Path
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0803-cycle2-rs-ucsd-typed-operator-source-origin-classifier.md"
)


def extract_json_summary(text: str) -> dict[str, object]:
    matches = list(re.finditer(r"```json\s*(\{.*?\})\s*```", text, re.DOTALL))
    if not matches:
        raise AssertionError("No JSON summary block found")
    return json.loads(matches[-1].group(1))


class RSUCSDTypedOperatorSourceOriginClassifierAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_json_summary(cls.text)

    def test_ucsd_is_hosted_candidate_not_accepted_operator_rule(self) -> None:
        ucsd = self.summary["ucsd_hosted_candidate"]

        self.assertEqual(ucsd["status"], "hosted_conditional_underdefined")
        self.assertTrue(ucsd["hosted_source_origin_surface"])
        self.assertTrue(ucsd["hosted_operator_idea"])
        self.assertFalse(ucsd["accepted_as_rs_minus_one_rule"])
        self.assertFalse(ucsd["family_identity_runnable"])
        self.assertFalse(self.summary["typed_source_origin_operator_rule_exists"])

    def test_equation_1010_remains_scoped_fail_and_separate(self) -> None:
        eq = self.summary["equation_1010_status"]

        self.assertEqual(eq["status"], "scoped_fail")
        self.assertEqual(eq["missing_object"], "ImageTypedRSMinusOneRuleCell_V1")
        self.assertEqual(eq["accepted_cell_count"], 0)
        self.assertEqual(eq["accepted_receipt_count"], 0)
        self.assertFalse(eq["global_rs_no_go"])
        self.assertEqual(
            eq["relation_to_ucsd_candidate"],
            "independent_prior_scoped_failure_not_repaired_by_ucsd_hosting",
        )

    def test_zero_accepted_rs_receipt_and_zero_proof_restart(self) -> None:
        self.assertEqual(self.summary["accepted_rs_receipt_count"], 0)
        self.assertEqual(self.summary["accepted_rs_proof_restart_count"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])

    def test_exact_missing_object_and_missing_fields(self) -> None:
        missing = self.summary["first_exact_missing_object"]

        self.assertEqual(missing["id"], "UCSDTypedRSMinusOneOperator_V1")
        self.assertFalse(missing["exists"])
        self.assertTrue(missing["conditional_specification_exists"])

        missing_fields = set(missing["missing_fields"])
        self.assertIn("pure_RS_domain", missing_fields)
        self.assertIn("pure_RS_codomain", missing_fields)
        self.assertIn("degree_or_slot_d_RS_minus_1", missing_fields)
        self.assertIn("P_RS_or_RS_quotient", missing_fields)
        self.assertIn("family_identity_status", missing_fields)

    def test_classifier_preserves_purity_and_family_identity_blocks(self) -> None:
        rows = {
            row["field"]: row
            for row in self.summary["typed_operator_source_origin_classifier"]
        }

        self.assertEqual(rows["RS_only_purity"]["decision"], "fail_for_purity")
        self.assertEqual(rows["family_identity"]["decision"], "blocked")
        self.assertEqual(
            rows["degree_or_slot"]["decision"],
            "missing_for_d_RS_minus_1",
        )
        self.assertEqual(
            rows["relation_to_equation_10_10"]["decision"],
            "separate_scoped_fail_preserved",
        )

    def test_no_generation_count_or_receipt_promotion(self) -> None:
        self.assertFalse(self.summary["generation_count_promotion_allowed"])

        impact = self.summary["impact_if_closed"]
        self.assertTrue(impact["candidate_receipt_would_exist"])
        self.assertEqual(
            impact["immediate_status_if_closed"],
            "candidate_receipt_pending_family_identity",
        )
        self.assertFalse(impact["equation_1010_repaired"])
        self.assertFalse(impact["proof_restart_automatically_allowed"])
        self.assertFalse(impact["generation_count_proved_by_this_gate"])

        forbidden = set(self.summary["forbidden_promotions"])
        self.assertIn("ucsd_hosted_candidate_as_accepted_receipt", forbidden)
        self.assertIn("RS_generation_count_proof_restart_allowed", forbidden)
        self.assertIn("generation_count_promotion_allowed", forbidden)


if __name__ == "__main__":
    unittest.main()
