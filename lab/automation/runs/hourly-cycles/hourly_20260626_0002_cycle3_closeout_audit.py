"""Audit the 0002 cycle 3 route closeouts and synthesis."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260626-0002"
ARTIFACTS = {
    "IG": ROOT / "explorations/hourly-20260626-0002-cycle3-ig-proof-restart-closeout.md",
    "RS": ROOT / "explorations/hourly-20260626-0002-cycle3-rs-capture-route-closeout.md",
    "PTUJ": ROOT / "explorations/hourly-20260626-0002-cycle3-ptuj-formula-visibility-closeout.md",
    "DGU": ROOT / "explorations/hourly-20260626-0002-cycle3-dgu-symbol-transition-closeout.md",
    "QFT": ROOT / "explorations/hourly-20260626-0002-cycle3-qft-branch-transition-closeout.md",
    "SYNTHESIS": ROOT / "explorations/hourly-20260626-0002-three-cycle-fifteen-hole-synthesis.md",
}


def extract_summary(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    blocks = re.findall(r"```json\s*(\{.*?\})\s*```", text, flags=re.DOTALL)
    if not blocks:
        raise AssertionError(f"missing JSON summary in {path}")
    return json.loads(blocks[-1])


class Cycle3CloseoutAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.summaries = {route: extract_summary(path) for route, path in ARTIFACTS.items()}

    def test_cycle3_route_artifacts_are_run_scoped_and_no_restart(self) -> None:
        for route in ("IG", "RS", "PTUJ", "DGU", "QFT"):
            summary = self.summaries[route]
            with self.subTest(route=route):
                self.assertEqual(summary["run_id"], RUN_ID)
                self.assertEqual(summary["cycle"], 3)
                self.assertTrue(summary["artifact_path"].startswith(f"explorations/{RUN_ID}-cycle3-"))
                self.assertTrue(summary["cycle1_consumed"])
                self.assertTrue(summary["cycle2_consumed"])
                self.assertFalse(summary["target_import_used"])
                self.assertFalse(summary["claim_status_consistency_triggered"])
                self.assertFalse(summary["proof_restart_allowed"])
                self.assertFalse(summary["claim_promotion_allowed"])
                self.assertIn("next_frontier_object", summary)

    def test_route_next_frontiers(self) -> None:
        self.assertEqual(
            self.summaries["IG"]["next_frontier_object"],
            "ProductABSourceOperatorSourceLocatorReceipt_V1",
        )
        self.assertEqual(
            self.summaries["RS"]["next_frontier_object"],
            "RSBrowserCaptureToolchainAndFirstFrameReceipt_V1",
        )
        self.assertEqual(
            self.summaries["PTUJ"]["next_frontier_object"],
            "one_complete_branch_pure_PTUJ_source_packet_for_SingleCompletePTUJBranchReceipt_V1",
        )
        self.assertEqual(
            self.summaries["DGU"]["next_frontier_object"],
            "PrimarySourceDGU01SectorRuleRowInstance_V1",
        )
        self.assertEqual(
            self.summaries["QFT"]["next_frontier_object"],
            "QFTBranchLabelAdmissibilityPrimarySourceMiningPacket_V1",
        )

    def test_rs_toolchain_receipt_does_not_unlock_frame_or_proof(self) -> None:
        rs = self.summaries["RS"]
        self.assertTrue(rs["route_local_receipt_admitted"])
        self.assertTrue(rs["approved_capture_toolchain_admitted"])
        self.assertTrue(rs["capture_tool_identity_admitted"])
        self.assertTrue(rs["challenge_page_captured"])
        self.assertFalse(rs["source_timestamp_verification_passed"])
        self.assertFalse(rs["first_frame_receipt_admitted"])
        self.assertFalse(rs["frame_manifest_admitted"])
        self.assertFalse(rs["typed_rs_intake_allowed"])

    def test_synthesis_records_fifteen_holes_and_one_route_local_receipt(self) -> None:
        syn = self.summaries["SYNTHESIS"]
        self.assertEqual(syn["run_id"], RUN_ID)
        self.assertEqual(syn["target_quality_holes"], 15)
        self.assertEqual(syn["quality_holes_completed"], 15)
        self.assertFalse(syn["target_import_used"])
        self.assertFalse(syn["claim_status_consistency_triggered"])
        self.assertFalse(syn["claim_promotion_allowed_any_route"])
        self.assertFalse(syn["proof_restart_allowed_any_route"])
        self.assertEqual(syn["new_route_local_receipts_admitted"], 1)
        self.assertEqual(syn["new_source_or_proof_receipts_admitted"], 0)
        self.assertIn(
            "ApprovedBrowserCaptureToolchainForFBozSSLxFvIWindow_V1",
            syn["admitted_route_local_receipts"],
        )
        self.assertEqual(len(syn["next_frontier_ranked"]), 5)
        self.assertTrue(syn["sequential_within_route_required"])
        self.assertTrue(syn["three_cycle_wrapper_improved_quality"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
