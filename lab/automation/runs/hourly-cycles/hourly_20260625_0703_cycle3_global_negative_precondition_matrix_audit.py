#!/usr/bin/env python3
"""Audit GlobalNegativePreconditionMatrixAfterHourly20260625_0703_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0703-cycle3-global-negative-precondition-matrix.md"
)


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 9\. JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing JSON summary")
    return json.loads(match.group(1))


class GlobalNegativePreconditionMatrixAfter0703Audit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_identity_and_json_parse(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "GlobalNegativePreconditionMatrixAfterHourly20260625_0703_V1",
        )
        self.assertEqual(
            self.summary["artifact_id"],
            "GlobalNegativePreconditionMatrixAfterHourly20260625_0703_V1",
        )
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0703")
        self.assertEqual(self.summary["cycle"], 3)
        self.assertEqual(self.summary["lane"], 3)
        self.assertEqual(
            self.summary["companion_audit"],
            "tests/hourly_20260625_0703_cycle3_global_negative_precondition_matrix_audit.py",
        )

    def test_all_six_families_present(self) -> None:
        rows = {row["family"]: row for row in self.summary["families"]}
        self.assertEqual(
            set(rows),
            {"RS", "QFT", "DGU/VZ", "IG", "Oxford", "Keating"},
        )
        for family, row in rows.items():
            self.assertIn("required_object", row, family)
            self.assertIn("missing_bundle_fields", row, family)
            self.assertGreaterEqual(len(row["missing_bundle_fields"]), 6, family)

    def test_no_global_no_go_or_global_demotion(self) -> None:
        self.assertFalse(self.summary["global_no_go_promoted"])
        self.assertEqual(self.summary["global_demote_allowed_count"], 0)
        for row in self.summary["families"]:
            self.assertFalse(row["global_no_go_promoted"], row["family"])
            self.assertFalse(row["global_demote_allowed"], row["family"])
            self.assertFalse(row["proof_restart_allowed"], row["family"])
            self.assertEqual(row["accepted_receipt_count"], 0, row["family"])

    def test_scoped_negatives_and_capture_failures_not_global_absence(self) -> None:
        distinctions = {row["family"]: row["distinction"] for row in self.summary["families"]}
        self.assertIn("scoped_negative_not_global_absence", distinctions["RS"])
        self.assertIn("partial_acquisition_not_global_absence", distinctions["QFT"])
        self.assertIn("identity_failure_for_route_not_global_absence", distinctions["DGU/VZ"])
        self.assertIn("blocked_capture_not_global_absence", distinctions["IG"])
        self.assertIn("positive_locator_not_accepted_receipt_or_global_absence", distinctions["Oxford"])
        self.assertIn("unavailable_or_blocked_source_not_global_absence", distinctions["Keating"])
        self.assertIn("scoped negative", self.text.lower())
        self.assertIn("unavailable source", self.text.lower())
        self.assertIn("blocked capture", self.text.lower())
        self.assertIn("global absence", self.text.lower())

    def test_missing_global_bundle_blocks_promotions(self) -> None:
        bundle = self.summary["missing_global_bundle"]
        self.assertEqual(
            bundle["id"],
            "SixFamilyGlobalNegativeReceiptBundleAfterHourly20260625_0703_V1",
        )
        self.assertTrue(bundle["missing"])
        self.assertTrue(bundle["required_before_global_no_go"])
        self.assertTrue(bundle["required_before_global_demotion"])
        self.assertIn("synthesis_rule", bundle["required_fields"])
        self.assertIn("target_import_screen_by_row", bundle["required_fields"])
        self.assertIn("family_identity_check_by_row", bundle["required_fields"])
        self.assertIn("blocked_capture", bundle["blocked_by_statuses"])

    def test_counts_and_next_frontier(self) -> None:
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertIn(
            "missing_complete_six_family_GlobalNegativeReceiptBundle",
            self.summary["first_obstruction"],
        )
        self.assertEqual(
            self.summary["next_frontier_object"],
            "SixFamilyGlobalNegativeReceiptBundleAssemblyAfterHourly20260625_0703_V1",
        )


if __name__ == "__main__":
    unittest.main()
