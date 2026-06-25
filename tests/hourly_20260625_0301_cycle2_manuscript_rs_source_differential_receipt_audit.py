#!/usr/bin/env python3
"""Audit the Cycle 2 manuscript RS source differential receipt artifact."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "explorations"
    / "hourly-20260625-0301-cycle2-manuscript-rs-source-differential-receipt.md"
)

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. What Was Derived Directly From Repo Sources",
    "## 3. The Strongest Positive Result",
    "## 4. First Exact Obstruction Or Missing Proof Object",
    "## 5. The Constructive Next Object",
    "## 6. What This Means For The Relevant GU Claim",
    "## 7. Next Meaningful Proof Or Computation Step",
    "## Receipt Rows",
    "## Machine-Readable JSON Summary",
]

REQUIRED_RECEIPT_FIELDS = {
    "receipt_id",
    "source_locator",
    "source_kind",
    "rs_field",
    "rs_parameter_or_ghost",
    "emitted_map",
    "source_operator_context",
    "quotient_semantics",
    "target_import_guard",
    "acceptance_status",
    "accepted",
    "first_blocker",
}

ALLOWED_SOURCE_KINDS = {
    "action",
    "operator",
    "Euler_Lagrange_variation",
    "Noether_identity",
    "BRST_rule",
    "deformation_complex_map",
}

REQUIRED_PAGES = {43, 44, 45, 46, 47, 48, 62, 63, 64, 65}

FORBIDDEN_ACCEPTED_STATUSES = {
    "accepted",
    "accepted_for_routing",
    "accepted_source_differential",
}


def extract_summary(text: str) -> dict[str, object]:
    for block in re.findall(r"```json\s*(.*?)\s*```", text, re.DOTALL):
        data = json.loads(block)
        if data.get("artifact") == "ManuscriptRSSourceDifferentialReceipt_V1":
            return data
    raise AssertionError("ManuscriptRSSourceDifferentialReceipt_V1 JSON not found")


class ManuscriptRSSourceDifferentialReceiptAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_required_headings_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_required_receipt_schema_fields_are_declared(self) -> None:
        schema = self.summary["receipt_schema"]
        self.assertEqual(schema["id"], "ManuscriptRSSourceDifferentialReceipt_V1")
        self.assertEqual(set(schema["required_fields"]), {
            "source_locator",
            "source_kind",
            "rs_field",
            "rs_parameter_or_ghost",
            "emitted_map",
            "source_operator_context",
            "quotient_semantics",
            "target_import_guard",
            "acceptance_status",
        })
        self.assertEqual(set(schema["allowed_source_kinds"]), ALLOWED_SOURCE_KINDS)

    def test_pages_searched_are_exact_requested_neighborhoods(self) -> None:
        source = self.summary["source"]
        self.assertEqual(source["path"], "Geometric_UnityDraftApril1st2021.pdf")
        self.assertEqual(set(source["pages_searched"]), REQUIRED_PAGES)

    def test_all_receipt_rows_have_required_fields_and_allowed_kinds(self) -> None:
        rows = self.summary["receipt_rows"]
        self.assertGreaterEqual(len(rows), 5)
        for row in rows:
            self.assertEqual(set(row), REQUIRED_RECEIPT_FIELDS)
            self.assertIn(row["source_kind"], ALLOWED_SOURCE_KINDS)
            self.assertIn("Geometric_UnityDraftApril1st2021.pdf", row["source_locator"])
            self.assertIsInstance(row["target_import_guard"], dict)
            self.assertIn("rank_or_generation_target_used", row["target_import_guard"])
            self.assertFalse(row["target_import_guard"]["rank_or_generation_target_used"])

    def test_zero_accepted_receipts_and_no_accepted_status(self) -> None:
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertFalse(self.summary["accepted_source_differential_for_d_RS_minus_1"])
        for row in self.summary["receipt_rows"]:
            self.assertFalse(row["accepted"], f"unexpected accepted row: {row}")
            normalized = row["acceptance_status"].lower()
            self.assertFalse(
                normalized in FORBIDDEN_ACCEPTED_STATUSES
                or normalized.startswith("accepted"),
                f"unexpected accepted status: {row}",
            )

    def test_required_positive_and_negative_locators_are_present(self) -> None:
        locators = " ".join(row["source_locator"] for row in self.summary["receipt_rows"])
        for expected in ["p.46", "p.47", "p.48", "p.62", "pp.64-65"]:
            self.assertIn(expected, locators)

        blockers = " ".join(row["first_blocker"] for row in self.summary["receipt_rows"])
        self.assertIn("RS parameter-or-ghost", blockers)
        self.assertIn("domain/codomain", blockers)
        self.assertIn("source RS minus-one map", blockers)

    def test_generation_count_promotion_is_blocked(self) -> None:
        self.assertFalse(self.summary["generation_count_promotion_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])
        forbidden = self.summary["GU_claim_impact"]["forbidden_promotions"]
        self.assertIn("RS_generation_count_proof_restart", forbidden)
        self.assertIn("page_62_or_65_generation_branching_supplies_source_map", forbidden)

    def test_proof_restart_blocked_without_accepted_source_differential_and_identity_gate(self) -> None:
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["accepted_source_differential_for_d_RS_minus_1"])
        next_step = self.summary["next_meaningful_step"]
        self.assertIn("accepted source differential plus identity gate", next_step)

        next_object = self.summary["constructive_next_object"]
        self.assertEqual(next_object["id"], "RSSourceMinusOneMapIdentityPacket_V1")
        self.assertIn(
            "identity gate such as delta_omega,2 o delta_RS,-1 = 0",
            next_object["must_supply"],
        )

    def test_first_obstruction_is_missing_source_emitted_rs_minus_one_map(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["field"], "source_emitted_RS_minus_one_map")
        self.assertEqual(obstruction["status"], "MISSING")
        self.assertIn("No checked manuscript page emits", obstruction["description"])
        for term in ["Noether identity", "BRST rule", "deformation-complex map"]:
            self.assertIn(term, obstruction["description"])


if __name__ == "__main__":
    unittest.main()
