"""Audit the 2028 cycle 1 delta receipt artifacts."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260625-2028"
ARTIFACTS = {
    "PTUJ": ROOT / "explorations/hourly-20260625-2028-cycle1-ptuj-single-branch-delta-receipt.md",
    "IG": ROOT / "explorations/hourly-20260625-2028-cycle1-ig-product-b-d7-delta-transcript.md",
    "DGU": ROOT / "explorations/hourly-20260625-2028-cycle1-dgu-sector-same-operator-delta-receipt.md",
    "RS": ROOT / "explorations/hourly-20260625-2028-cycle1-rs-lawful-acquisition-route-delta.md",
    "QFT": ROOT / "explorations/hourly-20260625-2028-cycle1-qft-iota-rraw-delta-receipt.md",
}

EXPECTED_TARGETS = {
    "PTUJ": "PTUJ_SINGLE_COMPLETE_BRANCH_RECEIPT",
    "IG": "IG_PRODUCT_B_FULL_D7_SUMMAND_MULTIPLICITY_DIMENSION_RECEIPT",
    "DGU": "DGU_SOURCE_EMITTED_SECTOR_RULE_AND_SAME_OPERATOR_RECEIPT",
    "RS": "RS_LAWFUL_SOURCE_ACQUISITION_ROUTE_OR_BROWSER_CAPTURE_ROUTE",
    "QFT": "QFT_SOURCE_DEFINED_IOTA_B_AND_TYPED_R_RAW_B_O_RECEIPT",
}


def extract_summary(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    match = re.search(
        r"## 8\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError(f"missing JSON summary in {path}")
    return json.loads(match.group(1))


class Cycle1DeltaReceiptsAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.summaries = {route: extract_summary(path) for route, path in ARTIFACTS.items()}

    def test_all_routes_present_once(self) -> None:
        self.assertEqual(set(self.summaries), {"PTUJ", "IG", "DGU", "RS", "QFT"})
        self.assertEqual(len(self.summaries), 5)

    def test_identity_and_targets(self) -> None:
        for route, summary in self.summaries.items():
            with self.subTest(route=route):
                self.assertEqual(summary["run_id"], RUN_ID)
                self.assertEqual(summary["cycle"], 1)
                self.assertEqual(summary["route"], route)
                self.assertEqual(summary["decision_target"], EXPECTED_TARGETS[route])
                self.assertTrue(summary["artifact_path"].startswith("explorations/hourly-20260625-2028-cycle1-"))
                self.assertEqual(summary["owned_path"], summary["artifact_path"])

    def test_zero_receipts_and_no_restart(self) -> None:
        for route, summary in self.summaries.items():
            with self.subTest(route=route):
                self.assertEqual(summary["accepted_receipt_count"], 0)
                self.assertFalse(summary["proof_restart_allowed"])
                self.assertFalse(summary["claim_promotion_allowed"])
                self.assertFalse(summary["target_import_used"])
                self.assertFalse(summary["claim_status_consistency_triggered"])

    def test_verdicts_and_obstructions_are_decision_grade(self) -> None:
        self.assertEqual(self.summaries["QFT"]["verdict_class"], "underdefined")
        for route in {"PTUJ", "IG", "DGU", "RS"}:
            self.assertEqual(self.summaries[route]["verdict_class"], "blocked")
        for route, summary in self.summaries.items():
            with self.subTest(route=route):
                self.assertGreater(len(summary["first_obstruction"]), 20)
                self.assertGreater(len(summary["constructive_next_object"]), 20)
                self.assertGreaterEqual(len(summary["forbidden_bypasses"]), 5)

    def test_route_specific_firewalls(self) -> None:
        self.assertIn("cross_branch_assembly", self.summaries["PTUJ"]["forbidden_bypasses"])
        self.assertIn("target_generation_count_selector", self.summaries["IG"]["forbidden_bypasses"])
        self.assertIn("typed_spine_as_source_receipt", self.summaries["DGU"]["forbidden_bypasses"])
        self.assertIn("transcript_locator_as_frame_packet", self.summaries["RS"]["forbidden_bypasses"])
        self.assertIn("schema_only_upgrade", self.summaries["QFT"]["forbidden_bypasses"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
