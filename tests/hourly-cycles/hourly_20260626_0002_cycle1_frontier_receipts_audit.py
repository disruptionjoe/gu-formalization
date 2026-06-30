"""Audit the 0002 cycle 1 frontier receipt/source-mining artifacts."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260626-0002"
ARTIFACTS = {
    "IG": ROOT / "explorations/hourly-20260626-0002-cycle1-ig-source-locator-mining-packet.md",
    "RS": ROOT / "explorations/hourly-20260626-0002-cycle1-rs-approved-capture-toolchain-receipt.md",
    "PTUJ": ROOT / "explorations/hourly-20260626-0002-cycle1-ptuj-branch-source-packet-mining.md",
    "DGU": ROOT / "explorations/hourly-20260626-0002-cycle1-dgu-primary-source-row-mining.md",
    "QFT": ROOT / "explorations/hourly-20260626-0002-cycle1-qft-primary-source-mining-packet.md",
}


def extract_summary(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    blocks = re.findall(r"```json\s*(\{.*?\})\s*```", text, flags=re.DOTALL)
    if not blocks:
        raise AssertionError(f"missing JSON summary in {path}")
    return json.loads(blocks[-1])


class Cycle1FrontierReceiptsAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.summaries = {route: extract_summary(path) for route, path in ARTIFACTS.items()}

    def test_artifacts_are_run_scoped_and_no_proof_restart(self) -> None:
        self.assertEqual(set(self.summaries), {"IG", "RS", "PTUJ", "DGU", "QFT"})
        for route, summary in self.summaries.items():
            with self.subTest(route=route):
                self.assertEqual(summary["run_id"], RUN_ID)
                self.assertEqual(summary["cycle"], 1)
                self.assertTrue(summary["artifact_path"].startswith(f"explorations/{RUN_ID}-cycle1-"))
                self.assertFalse(summary["target_import_used"])
                self.assertFalse(summary["claim_status_consistency_triggered"])
                self.assertFalse(summary["proof_restart_allowed"])

    def test_rs_closes_capture_tool_identity_only(self) -> None:
        rs = self.summaries["RS"]
        self.assertEqual(rs["verdict_class"], "conditional_toolchain_admitted_no_frame")
        self.assertTrue(rs["directory_policy_row_consumed"])
        self.assertTrue(rs["directory_policy_row_admitted"])
        self.assertTrue(rs["chrome_capture_tool_found"])
        self.assertTrue(rs["edge_capture_tool_found"])
        self.assertTrue(rs["capture_tool_identity_admitted"])
        self.assertTrue(rs["approved_capture_toolchain_admitted"])
        self.assertTrue(rs["capture_operation_rule_defined"])
        self.assertTrue(rs["source_timestamp_verification_rule_defined"])
        self.assertTrue(rs["output_root_binding_defined"])
        self.assertTrue(rs["hash_rule_defined"])
        self.assertEqual(
            rs["closed_field"],
            "ApprovedBrowserCaptureToolchainForFBozSSLxFvIWindow_V1.capture_tool_identity",
        )
        self.assertFalse(rs["first_frame_persisted"])
        self.assertEqual(rs["persisted_frame_count"], 0)
        self.assertFalse(rs["first_frame_sha256_admitted"])
        self.assertFalse(rs["typed_rs_intake_allowed"])
        self.assertEqual(
            rs["constructive_next_object"],
            "RSBrowserCaptureToolchainAndFirstFrameReceipt_V1",
        )

    def test_other_routes_remain_blocked_before_downstream_work(self) -> None:
        ig = self.summaries["IG"]
        self.assertFalse(ig["source_operator_locator_found"])
        self.assertFalse(ig["coefficient_derivation_allowed"])
        self.assertEqual(
            ig["constructive_next_object"],
            "ProductABSourceOperatorSourceLocatorReceipt_V1",
        )

        ptuj = self.summaries["PTUJ"]
        self.assertEqual(ptuj["accepted_branch_count"], 0)
        self.assertEqual(ptuj["accepted_receipt_count"], 0)
        self.assertFalse(ptuj["formula_visibility_allowed"])
        self.assertFalse(ptuj["official_branch_complete"])
        self.assertFalse(ptuj["lawful_local_branch_complete"])

        dgu = self.summaries["DGU"]
        self.assertFalse(dgu["primary_source_row_instance_found"])
        self.assertFalse(dgu["sector_rule_locator_admitted"])
        self.assertFalse(dgu["same_operator_witness_evaluable"])
        self.assertFalse(dgu["symbol_certificate_allowed"])
        self.assertTrue(dgu["typed_d_roll_allowed_as_quarantined_screen"])

        qft = self.summaries["QFT"]
        self.assertEqual(qft["accepted_branch_label_source_row_count"], 0)
        self.assertEqual(qft["accepted_admissibility_rule_source_row_count"], 0)
        self.assertFalse(qft["Y_b_branch_selected"])
        self.assertFalse(qft["local_groupoid_allowed"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
