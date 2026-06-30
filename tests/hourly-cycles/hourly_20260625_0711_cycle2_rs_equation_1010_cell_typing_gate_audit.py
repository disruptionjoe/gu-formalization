#!/usr/bin/env python3
"""Audit HighResolutionEquation1010CellMap_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0711-cycle2-rs-equation-1010-cell-typing-gate.md"
)
EXPECTED_REQUIRED_OBJECT = "source.action_or_operator for d_RS,-1"


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing HighResolutionEquation1010CellMap_V1 JSON")
    return json.loads(match.group(1))


class HighResolutionEquation1010CellMapAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_identity_required_object_and_equation(self) -> None:
        self.assertEqual(self.summary["artifact"], "HighResolutionEquation1010CellMap_V1")
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0711")
        self.assertEqual(self.summary["cycle"], 2)
        self.assertEqual(self.summary["lane"], 4)
        self.assertEqual(self.summary["equation_target"], "10.10")
        self.assertEqual(self.summary["family"], "RS")
        self.assertEqual(self.summary["required_object"], EXPECTED_REQUIRED_OBJECT)

    def test_page_coverage_and_no_rendered_images_written(self) -> None:
        coverage = self.summary["page_coverage"]
        self.assertEqual(coverage["pdf_page_count"], 69)
        self.assertEqual(coverage["equation_pdf_page"], 49)
        self.assertEqual(coverage["equation_page_index_zero_based"], 48)
        self.assertEqual(coverage["immediate_context_pages"], [48, 49, 50])
        self.assertIn("10.10", coverage["checked_locators"])
        self.assertIn("11.4", coverage["checked_locators"])
        self.assertIn("page_index_48", coverage["source_surface"])
        self.assertEqual(coverage["image_files_written"], [])

    def test_cell_typing_fields_are_complete(self) -> None:
        fields = set(self.summary["cell_typing_fields"])
        for field in [
            "cell_id",
            "visible_label",
            "cell_kind",
            "source_space",
            "target_space",
            "degree_or_slot",
            "rule_kind",
            "field_component_identity",
            "family_identity_status",
            "accepted",
        ]:
            self.assertIn(field, fields)

        for cell in self.summary["cell_map"]:
            self.assertTrue(fields.issubset(cell.keys()))
            self.assertFalse(cell["accepted"])
            self.assertEqual(cell["family_identity_status"], "not_runnable")

    def test_expected_cell_inventory_and_zero_accepted_count(self) -> None:
        cell_ids = {cell["cell_id"] for cell in self.summary["cell_map"]}
        for cell_id in ["E1010-N1", "E1010-N2", "E1010-N3", "E1010-N4", "E1010-N5", "E1010-A7"]:
            self.assertIn(cell_id, cell_ids)

        self.assertEqual(self.summary["accepted_cells"], [])
        self.assertEqual(self.summary["accepted_cell_count"], 0)
        self.assertEqual(self.summary["accepted_receipts"], [])
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertEqual(
            self.summary["cell_typing_status"],
            "mixed_underdefined_not_RS_minus_one_rule",
        )

    def test_scoped_negative_and_no_proof_restart(self) -> None:
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])

        scoped = self.summary["scoped_negative_status"]
        self.assertTrue(scoped["scoped_negative"])
        self.assertEqual(
            scoped["negative_scope"],
            "acquired_2021_author_manuscript_equation_10.10_rendered_cell_map",
        )
        self.assertFalse(scoped["global_RS_no_go"])
        self.assertFalse(scoped["global_branch_demotion_allowed"])
        self.assertFalse(scoped["generation_count_proof_restart_allowed"])

    def test_obstruction_required_object_and_next_object_decision(self) -> None:
        obstruction = self.summary["first_obstruction"]
        self.assertEqual(
            obstruction["id"],
            "no_equation_1010_cell_types_as_ImageTypedRSMinusOneRuleCell_V1",
        )
        self.assertIn(EXPECTED_REQUIRED_OBJECT, obstruction["description"])

        required = self.summary["required_next_receipt_object"]
        self.assertEqual(required["id"], "ImageTypedRSMinusOneRuleCell_V1")
        self.assertTrue(required["missing"])
        for field in [
            "source_surface",
            "cell_locator",
            "family",
            "required_object",
            "source_space",
            "target_space",
            "degree_or_slot",
            "rule_kind",
            "field_component_identity",
            "family_identity_status",
        ]:
            self.assertIn(field, required["required_fields"])

        decision = self.summary["next_exact_missing_object_decision"]
        self.assertEqual(
            decision["local_equation_1010_receipt_object"],
            "ImageTypedRSMinusOneRuleCell_V1",
        )
        self.assertEqual(
            decision["next_meaningful_source_work_after_cell_map"],
            "AlternatePrimarySourceRSMinusOneRuleSearchBundle_V1",
        )
        self.assertEqual(
            decision["global_negative_bundle_required_for_no_go"],
            "GlobalRSNegativeReceiptBundle_V1",
        )
        self.assertIn("alternate_primary_source_bundle", decision["decision"])

    def test_forbidden_promotions(self) -> None:
        forbidden = set(self.summary["forbidden_promotions"])
        for claim in [
            "equation_10.10_accepted_as_RS_differential",
            "RS_d_RS_minus_1_source_derived",
            "RS_generation_count_proof_restart_allowed",
            "rank_H_S_RS_plus_source_derived",
            "ind_H_D_RS_source_derived",
            "equation_10.10_cell_fail_is_global_RS_no_go",
        ]:
            self.assertIn(claim, forbidden)


if __name__ == "__main__":
    unittest.main()
