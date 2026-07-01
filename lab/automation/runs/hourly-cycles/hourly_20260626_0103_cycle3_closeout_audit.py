"""Audit the 0103 cycle 3 closeout and synthesis artifacts."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260626-0103"
ARTIFACTS = {
    "IG": ROOT / "explorations/hourly-20260626-0103-cycle3-ig-proof-restart-readiness-closeout.md",
    "RS": ROOT / "explorations/hourly-20260626-0103-cycle3-rs-frame-evidence-transition-closeout.md",
    "PTUJ": ROOT / "explorations/hourly-20260626-0103-cycle3-ptuj-branch-receipt-transition-closeout.md",
    "DGU": ROOT / "explorations/hourly-20260626-0103-cycle3-dgu-symbol-vz-transition-closeout.md",
    "QFT": ROOT / "explorations/hourly-20260626-0103-cycle3-qft-carrier-groupoid-transition-closeout.md",
    "SYNTHESIS": ROOT / "explorations/hourly-20260626-0103-three-cycle-fifteen-hole-synthesis.md",
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

    def test_route_closeouts_are_run_scoped_and_no_restart(self) -> None:
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
                self.assertFalse(summary["claim_promotion_allowed"])
                self.assertFalse(summary["proof_restart_allowed"])
                self.assertIn("next_frontier_object", summary)

    def test_route_closeout_blocks_match_frontiers(self) -> None:
        self.assertFalse(self.summaries["IG"]["source_operator_locator_found"])
        self.assertTrue(self.summaries["IG"]["coefficient_firewall_active"])

        rs = self.summaries["RS"]
        self.assertTrue(rs["approved_capture_toolchain_admitted"])
        self.assertTrue(rs["nonframe_route_firewall_active"])
        self.assertEqual(rs["accepted_evidence_branch_count"], 0)
        self.assertFalse(rs["first_frame_receipt_admitted"])
        self.assertFalse(rs["typed_rs_intake_allowed"])

        ptuj = self.summaries["PTUJ"]
        self.assertEqual(ptuj["accepted_branch_count"], 0)
        self.assertTrue(ptuj["cross_branch_firewall_active"])
        self.assertFalse(ptuj["formula_visibility_allowed"])

        dgu = self.summaries["DGU"]
        self.assertFalse(dgu["source_row_payload_found"])
        self.assertFalse(dgu["same_operator_witness_evaluable"])
        self.assertFalse(dgu["symbol_certificate_allowed"])
        self.assertFalse(dgu["vz_replay_allowed"])

        qft = self.summaries["QFT"]
        self.assertEqual(qft["accepted_branch_label_source_row_count"], 0)
        self.assertEqual(qft["accepted_admissibility_rule_source_row_count"], 0)
        self.assertTrue(qft["host_Y_available"])
        self.assertFalse(qft["local_groupoid_allowed"])

    def test_synthesis_records_fifteen_holes_and_no_new_receipts(self) -> None:
        syn = self.summaries["SYNTHESIS"]
        self.assertEqual(syn["run_id"], RUN_ID)
        self.assertEqual(syn["target_quality_holes"], 15)
        self.assertEqual(syn["quality_holes_completed"], 15)
        self.assertFalse(syn["target_import_used"])
        self.assertFalse(syn["claim_status_consistency_triggered"])
        self.assertFalse(syn["claim_promotion_allowed_any_route"])
        self.assertFalse(syn["proof_restart_allowed_any_route"])
        self.assertEqual(syn["new_route_local_receipts_admitted"], 0)
        self.assertEqual(syn["new_source_or_proof_receipts_admitted"], 0)
        self.assertEqual(syn["new_blocker_refinements"], 15)
        self.assertEqual(syn["rs_accepted_evidence_branch_count"], 0)
        self.assertEqual(len(syn["next_frontier_ranked"]), 5)
        self.assertTrue(syn["sequential_within_route_required"])
        self.assertTrue(syn["three_cycle_wrapper_improved_quality"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
