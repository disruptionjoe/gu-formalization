#!/usr/bin/env python3
"""Audit BosonicOxfordReplacementToDGU01IdentityTest_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0703-cycle2-oxford-bosonic-dgu01-identity-test.md"
)

REQUIRED_ANCHORS = {
    "OxfordPortal_PPT_023510_Swervature": "02:35:10",
    "OxfordPortal_PPT_023612_Displasion": "02:36:12",
}

REQUIRED_IDENTITY_FIELDS = {
    "sector_rule",
    "operator_source_primary_action_or_EL",
    "actual_operator_formula_or_actual_EL_formula",
    "domain",
    "codomain",
    "chirality_or_epsilon_convention",
    "coefficient_packet",
    "principal_symbol_or_sufficient_first_order_data",
    "projectors_or_inclusions",
    "family_identity",
    "target_import_screen",
}


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 9\. JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing JSON Summary block")
    return json.loads(match.group(1))


class BosonicOxfordReplacementToDGU01IdentityTestAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = DOC.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "BosonicOxfordReplacementToDGU01IdentityTest_V1",
        )
        self.assertEqual(
            self.summary["artifact_id"],
            "BosonicOxfordReplacementToDGU01IdentityTest_V1",
        )
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0703")
        self.assertEqual(self.summary["cycle"], 2)
        self.assertEqual(self.summary["lane"], 1)

    def test_required_oxford_anchors_are_present(self) -> None:
        self.assertEqual(set(self.summary["oxford_anchor_ids"]), set(REQUIRED_ANCHORS))
        self.assertEqual(
            set(self.summary["oxford_anchor_timestamps"]),
            set(REQUIRED_ANCHORS.values()),
        )
        for anchor_id, timestamp in REQUIRED_ANCHORS.items():
            self.assertIn(anchor_id, self.text)
            self.assertIn(timestamp, self.text)

    def test_category_change_guard_blocks_without_identity_fields(self) -> None:
        self.assertFalse(self.summary["category_change_guard_passed"])
        category_change = self.summary["category_change"]
        self.assertEqual(category_change["from"], "bosonic_gauge_field_equation_on_Y")
        self.assertEqual(
            category_change["to"],
            "actual_D_GU_epsilon_0_1_operator_action_EL_principal_symbol_receipt",
        )
        self.assertTrue(category_change["guard_required"])
        self.assertFalse(category_change["guard_passed"])
        self.assertIn("bosonic gauge-field equation", self.text)
        self.assertIn("actual `D_GU^epsilon` 0/1", self.text)

    def test_no_receipts_routing_or_restart_accepted(self) -> None:
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertEqual(self.summary["accepted_for_routing_count"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])
        self.assertEqual(self.summary["accepted_receipts"], [])
        self.assertEqual(self.summary["accepted_for_routing"], [])

    def test_identity_fields_are_required_and_missing(self) -> None:
        self.assertEqual(set(self.summary["required_identity_fields"]), REQUIRED_IDENTITY_FIELDS)
        statuses = self.summary["identity_field_status"]
        self.assertEqual(set(statuses), REQUIRED_IDENTITY_FIELDS)
        for field, status in statuses.items():
            if field == "target_import_screen":
                self.assertIn("quarantine", status)
                self.assertIn("not_for_routing", status)
            else:
                self.assertIn("missing", status)

    def test_positive_locator_does_not_route(self) -> None:
        positive = self.summary["positive_locator"]
        self.assertTrue(positive["exists"])
        self.assertEqual(positive["classification"], "source_hosted_bosonic_visual_locator")
        anchors = positive["anchors"]
        self.assertEqual(len(anchors), 2)
        for row in anchors:
            self.assertIn(row["timestamp"], REQUIRED_ANCHORS.values())
            self.assertFalse(row["accepted_for_routing"])
            self.assertIn("bosonic", row["category"])

    def test_first_obstruction_and_next_frontier_are_exact(self) -> None:
        self.assertEqual(
            self.summary["first_obstruction"],
            "missing_source_clean_identity_from_Oxford_bosonic_equation_to_actual_D_GU_epsilon_0_1",
        )
        self.assertIn("sector rule", self.summary["first_missing_proof_object"])
        self.assertIn("principal symbol", self.summary["first_missing_proof_object"])
        self.assertEqual(
            self.summary["next_frontier_object"],
            "OxfordBosonicTwoAnchorDGU01IdentityPacket_V1",
        )
        self.assertIn(
            "NegativePrimarySourceReceiptInstance_V1:DGU_01:OXFORD_PORTAL_2013:anchors_023510_023612",
            self.summary["demotion_candidate_if_full_source_pass_negative"],
        )


if __name__ == "__main__":
    unittest.main()
