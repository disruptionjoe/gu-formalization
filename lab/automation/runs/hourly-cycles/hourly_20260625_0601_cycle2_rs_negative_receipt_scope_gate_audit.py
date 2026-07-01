#!/usr/bin/env python3
"""Audit RSNegativeReceiptScopeGate_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0601-cycle2-rs-negative-receipt-scope-gate.md"
)


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing RSNegativeReceiptScopeGate_V1 JSON summary")
    return json.loads(match.group(1))


class RSNegativeReceiptScopeGateAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity(self) -> None:
        self.assertEqual(self.summary["artifact"], "RSNegativeReceiptScopeGate_V1")
        self.assertEqual(self.summary["run"], "hourly-20260625-0601")
        self.assertEqual(self.summary["cycle"], 2)
        self.assertEqual(self.summary["lane"], 3)
        identity = self.summary["artifact_identity"]
        self.assertEqual(identity["artifact_id"], "RSNegativeReceiptScopeGate_V1")
        self.assertEqual(
            identity["owned_path"],
            "explorations/hourly-20260625-0601-cycle2-rs-negative-receipt-scope-gate.md",
        )
        self.assertEqual(
            identity["companion_audit"],
            "tests/hourly_20260625_0601_cycle2_rs_negative_receipt_scope_gate_audit.py",
        )
        self.assertIn("RS:d_RS_minus_1", identity["row_id"])

    def test_fail_for_rs_differential_receipt_is_scoped(self) -> None:
        cycle1 = self.summary["cycle1_fail_result"]
        self.assertEqual(cycle1["row_status"], "fail_for_RS_differential_receipt")
        self.assertEqual(cycle1["accepted_receipt_count"], 0)
        self.assertFalse(cycle1["proof_restart_allowed"])
        scope = self.summary["scope_decision"]
        self.assertTrue(scope["fail_for_RS_differential_receipt"])
        self.assertTrue(scope["scoped_negative"])
        self.assertEqual(
            scope["negative_scope"],
            "author_manuscript_formula_diagram_windows_only",
        )
        self.assertFalse(self.summary["source_scope"]["scope_is_global_RS_source_space"])

    def test_not_global_no_go_or_generation_count_demotion(self) -> None:
        scope = self.summary["scope_decision"]
        self.assertFalse(scope["global_RS_no_go"])
        self.assertFalse(scope["global_absence_claim_allowed"])
        self.assertFalse(scope["global_branch_demotion_allowed"])
        self.assertFalse(scope["generation_count_proof_demotion"])
        self.assertFalse(scope["generation_count_proof_restart_allowed"])
        self.assertFalse(scope["proof_restart_allowed"])
        self.assertIn("not a global RS no-go", self.text)

    def test_receipt_count_and_proof_restart_false(self) -> None:
        self.assertEqual(self.summary["accepted_receipts"], [])
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertFalse(self.summary["scope_decision"]["proof_restart_allowed"])
        self.assertFalse(self.summary["scope_decision"]["claim_promotion_allowed"])

    def test_missing_global_negative_bundle_named(self) -> None:
        bundle = self.summary["missing_global_negative_bundle"]
        self.assertEqual(bundle["id"], "GlobalRSNegativeReceiptBundle_V1")
        self.assertTrue(bundle["missing"])
        self.assertTrue(bundle["required_for_global_no_go"])
        required = set(bundle["required_fields"])
        self.assertIn("all_primary_GU_source_surfaces", required)
        self.assertIn("all_known_source_versions_and_corrected_variants", required)
        self.assertIn("synthesis_rule_from_scoped_negatives_to_global_no_go", required)

    def test_first_obstruction_and_scope_facts(self) -> None:
        obstruction = self.summary["first_obstruction"]
        self.assertEqual(
            obstruction["id"],
            "missing_stable_RS_only_source_rule_for_d_RS_minus_1_in_checked_manuscript_windows",
        )
        self.assertEqual(obstruction["first_decisive_failed_row"], "10.10")
        self.assertIn("source, target, degree/slot", obstruction["description"])
        locators = set(self.summary["source_scope"]["checked_locators"])
        for locator in ["9.16", "10.10", "11.4", "12.22", "summary_page_65"]:
            self.assertIn(locator, locators)

    def test_named_rollback_conditions_present_and_false(self) -> None:
        rollback = self.summary["rollback_conditions"]
        expected = {
            "manual_image_transcription_10_10_supplies_rule",
            "corrected_extraction_missing_formula_cell",
            "alternate_author_source_supplies_rule",
            "family_identity_check_passes_after_new_receipt",
        }
        self.assertEqual(set(rollback), expected)
        for name, value in rollback.items():
            self.assertFalse(value, name)

    def test_forbidden_promotions_cover_scope_errors(self) -> None:
        forbidden = set(self.summary["forbidden_promotions"])
        self.assertIn("RS_d_RS_minus_1_globally_absent_from_GU", forbidden)
        self.assertIn("all_RS_source_routes_are_closed", forbidden)
        self.assertIn("RS_generation_count_proof_globally_demoted", forbidden)
        self.assertIn("RS_generation_count_proof_restart_allowed", forbidden)
        self.assertIn("equation_10_10_accepted_as_RS_differential", forbidden)


if __name__ == "__main__":
    unittest.main()
