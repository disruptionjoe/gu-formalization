"""Audit the 2302 cycle 3 route closeouts and synthesis."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260625-2302"
ARTIFACTS = {
    "IG": ROOT
    / "explorations/hourly-20260625-2302-cycle3-ig-proof-restart-readiness-classifier.md",
    "RS": ROOT / "explorations/hourly-20260625-2302-cycle3-rs-manifest-transition-gate.md",
    "PTUJ": ROOT
    / "explorations/hourly-20260625-2302-cycle3-ptuj-formula-visibility-transition-gate.md",
    "DGU": ROOT / "explorations/hourly-20260625-2302-cycle3-dgu-symbol-transition-gate.md",
    "QFT": ROOT
    / "explorations/hourly-20260625-2302-cycle3-qft-branch-to-groupoid-transition-gate.md",
    "SYNTHESIS": ROOT / "explorations/hourly-20260625-2302-three-cycle-fifteen-hole-synthesis.md",
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
                self.assertFalse(summary["target_import_used"])
                self.assertFalse(summary["claim_status_consistency_triggered"])
                self.assertFalse(summary["proof_restart_allowed"])
                self.assertFalse(summary["claim_promotion_allowed"])
                self.assertTrue(summary["cycle1_consumed"])
                self.assertTrue(summary["cycle2_consumed"])
                self.assertIn("next_frontier_object", summary)
                self.assertIn("sequential_next_edges", summary)

    def test_route_specific_next_frontiers_are_ordered(self) -> None:
        self.assertEqual(
            self.summaries["IG"]["next_frontier_object"],
            "ProductABSourceOperatorSourceLocatorReceipt_V1",
        )
        self.assertEqual(
            self.summaries["RS"]["next_frontier_object"],
            "ApprovedBrowserCaptureToolchainForFBozSSLxFvIWindow_V1",
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

    def test_ig_rs_ptuj_dgu_qft_downstream_locks_hold(self) -> None:
        ig = self.summaries["IG"]
        self.assertTrue(ig["finite_host_available"])
        self.assertFalse(ig["source_operator_locator_found"])
        self.assertFalse(ig["coefficient_derivation_allowed"])
        self.assertFalse(ig["selector_restart_allowed"])

        rs = self.summaries["RS"]
        self.assertTrue(rs["directory_policy_row_admitted"])
        self.assertFalse(rs["approved_capture_toolchain_found"])
        self.assertFalse(rs["first_frame_receipt_admitted"])
        self.assertFalse(rs["frame_manifest_admitted"])
        self.assertFalse(rs["typed_rs_intake_allowed"])
        self.assertFalse(rs["generation_restart_allowed"])

        ptuj = self.summaries["PTUJ"]
        self.assertTrue(ptuj["branch_purity_invariant_defined"])
        self.assertFalse(ptuj["branch_purity_invariant_satisfied"])
        self.assertEqual(ptuj["accepted_branch_count"], 0)
        self.assertEqual(ptuj["accepted_receipt_count"], 0)
        self.assertFalse(ptuj["formula_visibility_allowed"])

        dgu = self.summaries["DGU"]
        self.assertFalse(dgu["sector_rule_locator_admitted"])
        self.assertFalse(dgu["same_operator_witness_evaluable"])
        self.assertFalse(dgu["symbol_certificate_allowed"])
        self.assertFalse(dgu["vz_replay_allowed"])
        self.assertFalse(dgu["typed_d_roll_allowed_as_source"])
        self.assertTrue(dgu["typed_d_roll_allowed_as_quarantined_screen"])

        qft = self.summaries["QFT"]
        self.assertEqual(qft["accepted_branch_label_source_row_count"], 0)
        self.assertEqual(qft["accepted_admissibility_rule_source_row_count"], 0)
        self.assertFalse(qft["Y_b_branch_selected"])
        self.assertFalse(qft["source_defined_iota_b_admitted"])
        self.assertFalse(qft["typed_R_raw_b_O_admitted"])
        self.assertFalse(qft["local_groupoid_allowed"])
        self.assertFalse(qft["quotient_descent_allowed"])

    def test_synthesis_records_fifteen_holes_and_no_claim_change(self) -> None:
        syn = self.summaries["SYNTHESIS"]
        self.assertEqual(syn["run_id"], RUN_ID)
        self.assertEqual(syn["target_quality_holes"], 15)
        self.assertEqual(syn["quality_holes_completed"], 15)
        self.assertEqual(syn["new_receipts_admitted"], 0)
        self.assertFalse(syn["proof_restart_allowed_any_route"])
        self.assertFalse(syn["target_import_used"])
        self.assertFalse(syn["claim_status_consistency_triggered"])
        self.assertFalse(syn["claim_promotion_allowed_any_route"])
        self.assertTrue(syn["sequential_within_route_required"])
        self.assertTrue(syn["three_cycle_wrapper_improved_quality"])
        self.assertEqual(len(syn["next_frontier_ranked"]), 5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
