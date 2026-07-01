"""Audit the 0103 cycle 2 downstream firewall artifacts."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260626-0103"
ARTIFACTS = {
    "IG": ROOT / "explorations/hourly-20260626-0103-cycle2-ig-coefficient-firewall-gate.md",
    "RS": ROOT / "explorations/hourly-20260626-0103-cycle2-rs-nonframe-route-rejection-gate.md",
    "PTUJ": ROOT / "explorations/hourly-20260626-0103-cycle2-ptuj-cross-branch-assembly-firewall.md",
    "DGU": ROOT / "explorations/hourly-20260626-0103-cycle2-dgu-same-operator-source-row-firewall.md",
    "QFT": ROOT / "explorations/hourly-20260626-0103-cycle2-qft-carrier-selection-order-gate.md",
}


def extract_summary(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    blocks = re.findall(r"```json\s*(\{.*?\})\s*```", text, flags=re.DOTALL)
    if not blocks:
        raise AssertionError(f"missing JSON summary in {path}")
    return json.loads(blocks[-1])


class Cycle2DownstreamFirewallsAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.summaries = {route: extract_summary(path) for route, path in ARTIFACTS.items()}

    def test_artifacts_are_run_scoped_and_consume_cycle1(self) -> None:
        for route, summary in self.summaries.items():
            with self.subTest(route=route):
                self.assertEqual(summary["run_id"], RUN_ID)
                self.assertEqual(summary["cycle"], 2)
                self.assertTrue(summary["artifact_path"].startswith(f"explorations/{RUN_ID}-cycle2-"))
                self.assertTrue(summary["cycle1_consumed"])
                self.assertFalse(summary["target_import_used"])
                self.assertFalse(summary["claim_status_consistency_triggered"])
                self.assertFalse(summary["proof_restart_allowed"])

    def test_ig_coefficients_are_firewalled_before_locator(self) -> None:
        ig = self.summaries["IG"]
        self.assertFalse(ig["source_operator_locator_found"])
        self.assertFalse(ig["located_operator_binding_evaluable"])
        self.assertTrue(ig["coefficient_firewall_active"])
        self.assertFalse(ig["alpha_source_derived"])
        self.assertFalse(ig["beta_source_derived"])
        self.assertFalse(ig["finite_common_rows_promoted_to_selector"])

    def test_rs_nonframe_routes_are_rejected(self) -> None:
        rs = self.summaries["RS"]
        self.assertTrue(rs["approved_capture_toolchain_admitted"])
        self.assertTrue(rs["nonframe_route_firewall_active"])
        self.assertTrue(rs["challenge_page_rejected_as_evidence"])
        self.assertTrue(rs["metadata_route_rejected"])
        self.assertTrue(rs["thumbnail_route_rejected"])
        self.assertTrue(rs["transcript_route_rejected"])
        self.assertTrue(rs["unchecksummed_screenshot_rejected"])
        self.assertFalse(rs["external_immutable_frame_package_found"])
        self.assertEqual(rs["accepted_evidence_branch_count"], 0)
        self.assertFalse(rs["frame_manifest_allowed"])
        self.assertFalse(rs["typed_rs_intake_allowed"])

    def test_remaining_routes_block_downstream_work(self) -> None:
        ptuj = self.summaries["PTUJ"]
        self.assertFalse(ptuj["official_branch_complete"])
        self.assertFalse(ptuj["lawful_local_branch_complete"])
        self.assertTrue(ptuj["mixed_packet_rejected"])
        self.assertTrue(ptuj["cross_branch_firewall_active"])
        self.assertFalse(ptuj["branch_purity_invariant_satisfied"])
        self.assertEqual(ptuj["accepted_receipt_count"], 0)

        dgu = self.summaries["DGU"]
        self.assertFalse(dgu["source_row_payload_found"])
        self.assertTrue(dgu["same_operator_firewall_active"])
        self.assertFalse(dgu["same_operator_witness_evaluable"])
        self.assertFalse(dgu["typed_d_roll_allowed_as_source"])
        self.assertTrue(dgu["typed_d_roll_allowed_as_quarantined_screen"])
        self.assertFalse(dgu["symbol_certificate_allowed"])
        self.assertFalse(dgu["vz_replay_allowed"])

        qft = self.summaries["QFT"]
        self.assertTrue(qft["host_Y_available"])
        self.assertTrue(qft["carrier_selection_order_enforced"])
        self.assertEqual(qft["accepted_branch_label_source_row_count"], 0)
        self.assertFalse(qft["Y_b_branch_selected"])
        self.assertFalse(qft["local_groupoid_allowed"])
        self.assertFalse(qft["quotient_descent_allowed"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
