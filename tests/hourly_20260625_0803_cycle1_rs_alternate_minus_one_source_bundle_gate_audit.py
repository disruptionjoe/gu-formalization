#!/usr/bin/env python3
"""Audit the 0803 cycle-1 RS alternate source bundle gate."""

from __future__ import annotations

import json
import re
from pathlib import Path
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0803-cycle1-rs-alternate-minus-one-source-bundle-gate.md"
)


def extract_json_summary(text: str) -> dict[str, object]:
    matches = list(re.finditer(r"```json\s*(\{.*?\})\s*```", text, re.DOTALL))
    if not matches:
        raise AssertionError("No JSON summary block found")
    return json.loads(matches[-1].group(1))


class RSAlternateMinusOneSourceBundleGateAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_json_summary(cls.text)

    def test_equation_1010_scoped_failure_is_separate_from_ucsd_candidate(self) -> None:
        eq = self.summary["equation_1010_scoped_failure"]
        ucsd = self.summary["ucsd_hosted_candidate"]

        self.assertEqual(eq["status"], "scoped_fail")
        self.assertEqual(eq["missing_object"], "ImageTypedRSMinusOneRuleCell_V1")
        self.assertFalse(eq["global_rs_no_go"])
        self.assertTrue(eq["kept_separate_from_ucsd_candidate"])

        self.assertEqual(ucsd["status"], "hosted_underdefined_candidate")
        self.assertEqual(ucsd["source_id"], "UCSD-April-2025-transcript")
        self.assertFalse(ucsd["accepted_as_rs_minus_one_rule"])
        self.assertNotEqual(eq["source_surface"], ucsd["source_surface"])

    def test_no_rs_receipt_or_proof_restart_without_typed_rule(self) -> None:
        self.assertEqual(self.summary["accepted_rs_receipt_count"], 0)
        self.assertEqual(self.summary["accepted_rs_proof_restart_count"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])

        forbidden = set(self.summary["forbidden_promotions"])
        self.assertIn("ucsd_hosted_candidate_as_accepted_receipt", forbidden)
        self.assertIn("RS_generation_count_proof_restart_allowed", forbidden)

    def test_first_exact_missing_object_is_named_and_has_required_fields(self) -> None:
        missing = self.summary["first_exact_missing_object"]
        self.assertEqual(missing["id"], "UCSDTypedRSMinusOneOperator_V1")
        self.assertIn("rs_projection_or_quotient", missing["missing_fields"])
        self.assertIn("degree_or_slot_minus_one", missing["missing_fields"])
        self.assertIn("typed_middle_map_or_symbol", missing["missing_fields"])

    def test_positive_candidate_maps_remain_underdefined(self) -> None:
        ucsd = self.summary["ucsd_hosted_candidate"]
        map_statuses = {item["id"]: item["status"] for item in ucsd["candidate_maps_hosted"]}
        self.assertEqual(map_statuses["middle_map_M"], "named_as_problem_not_formula")
        self.assertEqual(map_statuses["ship_in_bottle_symbol_B"], "described_not_typed_as_RS_minus_one")
        self.assertEqual(map_statuses["rolled_operator_B_d_A"], "derived_attempt_not_source_typed")

        construction = self.summary["strongest_positive_construction_attempt"]
        self.assertEqual(construction["status"], "hosted_but_underdefined")
        self.assertIn("no_RS_projection_or_quotient", construction["why_not_accepted"])


if __name__ == "__main__":
    unittest.main()
