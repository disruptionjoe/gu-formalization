#!/usr/bin/env python3
"""Audit ManualImageLevelRSFormulaDiagramAudit_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0711-cycle1-rs-manual-image-formula-diagram-audit.md"
)

EXPECTED_REQUIRED_OBJECT = "source.action_or_operator for d_RS,-1"


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing ManualImageLevelRSFormulaDiagramAudit_V1 JSON")
    return json.loads(match.group(1))


class ManualImageLevelRSFormulaDiagramAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_identity_and_required_object(self) -> None:
        self.assertEqual(
            self.summary["artifact"], "ManualImageLevelRSFormulaDiagramAudit_V1"
        )
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0711")
        self.assertEqual(self.summary["cycle"], 1)
        self.assertEqual(self.summary["lane"], 5)
        self.assertEqual(self.summary["family"], "RS")
        self.assertEqual(self.summary["required_object"], EXPECTED_REQUIRED_OBJECT)
        self.assertEqual(
            self.summary["verdict"],
            "IMAGE_AUDIT_PRESERVES_SCOPED_RS_FAIL_ZERO_ACCEPTED_RECEIPTS",
        )

    def test_page_and_locator_coverage(self) -> None:
        scope = self.summary["audit_scope"]
        self.assertEqual(scope["scope_kind"], "acquired_2021_author_manuscript_formula_diagram_windows")
        self.assertEqual(scope["pdf_page_count"], 69)
        self.assertEqual(scope["text_extraction_tool"], "PyMuPDF")
        self.assertIn(49, scope["close_image_inspection_pages"])
        self.assertIn(49, scope["manually_image_inspected_pages"])
        self.assertIn(49, scope["rendered_pages"])
        self.assertIn(65, scope["rendered_pages"])
        self.assertFalse(scope["scope_is_global_RS_source_space"])

        locators = set(scope["checked_locators"])
        for locator in ["9.16", "9.22", "10.1", "10.10", "11.4", "12.9", "12.22", "summary_page_65"]:
            self.assertIn(locator, locators)

    def test_image_text_audit_state(self) -> None:
        state = self.summary["image_text_audit_state"]
        self.assertTrue(state["text_window_checked"])
        self.assertTrue(state["rendered_image_window_checked"])
        self.assertTrue(state["manual_close_read_of_10_10"])
        self.assertFalse(state["hidden_image_level_rs_minus_one_cell_found"])
        self.assertFalse(state["prior_rs_fail_remains_text_only"])
        self.assertTrue(state["prior_rs_fail_now_text_plus_image_scoped"])

    def test_strongest_positive_attempt_not_accepted(self) -> None:
        strongest = self.summary["strongest_positive_image_attempt"]
        self.assertEqual(strongest["locator"], "10.10")
        self.assertEqual(strongest["manuscript_page"], 49)
        self.assertEqual(strongest["content_type"], "mixed_spinor_ad_deformation_diagram")
        self.assertEqual(strongest["decision"], "not_accepted")
        reasons = set(strongest["reasons"])
        self.assertIn("no pure RS source space is identified", reasons)
        self.assertIn("no degree_or_slot_minus_1 is identified", reasons)
        self.assertIn("family identity to source.action_or_operator for d_RS,-1 is not runnable", reasons)

    def test_zero_receipts_no_restart_no_family_identity(self) -> None:
        self.assertEqual(self.summary["accepted_receipts"], [])
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])
        family_identity = self.summary["family_identity_check"]
        self.assertTrue(family_identity["required_before_receipt_promotion"])
        self.assertEqual(family_identity["status"], "not_runnable")
        self.assertIn("zero accepted RS", family_identity["reason"])

    def test_scoped_negative_not_global_no_go(self) -> None:
        scoped = self.summary["scoped_negative_status"]
        self.assertTrue(scoped["scoped_negative"])
        self.assertEqual(
            scoped["negative_scope"],
            "acquired_2021_author_manuscript_formula_diagram_windows_text_plus_rendered_image_audit",
        )
        self.assertFalse(scoped["global_RS_no_go"])
        self.assertFalse(scoped["global_branch_demotion_allowed"])
        self.assertFalse(scoped["generation_count_proof_restart_allowed"])

    def test_first_obstruction_and_next_objects(self) -> None:
        obstruction = self.summary["first_obstruction"]
        self.assertEqual(
            obstruction["id"],
            "image_10_10_is_mixed_spinor_ad_not_typed_RS_minus_one_rule",
        )
        self.assertEqual(
            obstruction["first_decisive_failed_image_object"],
            "equation_10_10_page_49_rendered_diagram",
        )
        self.assertIn(EXPECTED_REQUIRED_OBJECT, obstruction["description"])

        required = self.summary["required_next_image_object"]
        self.assertEqual(required["id"], "ImageTypedRSMinusOneRuleCell_V1")
        self.assertTrue(required["missing"])
        required_fields = set(required["fields"])
        for field in [
            "source_surface",
            "cell_locator",
            "source_space",
            "target_space",
            "degree_or_slot",
            "rule_kind",
            "field_component_identity",
            "family_identity_status",
        ]:
            self.assertIn(field, required_fields)

        next_step = self.summary["next_meaningful_image_step"]
        self.assertEqual(next_step["id"], "HighResolutionEquation1010CellMap_V1")
        self.assertIn("cell-by-cell decision", next_step["description"])
        self.assertEqual(
            self.summary["next_meaningful_source_step_if_still_failing"],
            "AlternatePrimarySourceRSMinusOneRuleSearchBundle_V1",
        )

    def test_forbidden_promotions(self) -> None:
        forbidden = set(self.summary["forbidden_promotions"])
        for claim in [
            "equation_10_10_accepted_as_RS_differential",
            "RS_d_RS_minus_1_source_derived",
            "RS_generation_count_proof_restart_allowed",
            "rank_H_S_RS_plus_source_derived",
            "ind_H_D_RS_source_derived",
            "acquired_manuscript_image_fail_is_global_RS_no_go",
        ]:
            self.assertIn(claim, forbidden)


if __name__ == "__main__":
    unittest.main()
