"""Audit the 2302 cycle 2 downstream frontier gates."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260625-2302"
ARTIFACTS = {
    "IG": ROOT / "explorations/hourly-20260625-2302-cycle2-ig-two-row-coefficient-gate.md",
    "RS": ROOT / "explorations/hourly-20260625-2302-cycle2-rs-first-frame-receipt-gate.md",
    "PTUJ": ROOT / "explorations/hourly-20260625-2302-cycle2-ptuj-branch-purity-audit-gate.md",
    "DGU": ROOT / "explorations/hourly-20260625-2302-cycle2-dgu-same-operator-precondition-gate.md",
    "QFT": ROOT / "explorations/hourly-20260625-2302-cycle2-qft-source-row-inventory-gate.md",
}


def extract_summary(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    blocks = re.findall(r"```json\s*(\{.*?\})\s*```", text, flags=re.DOTALL)
    if not blocks:
        raise AssertionError(f"missing JSON summary in {path}")
    return json.loads(blocks[-1])


class Cycle2DownstreamGatesAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.summaries = {route: extract_summary(path) for route, path in ARTIFACTS.items()}

    def test_all_cycle2_artifacts_are_run_scoped_and_no_restart(self) -> None:
        self.assertEqual(set(self.summaries), {"IG", "RS", "PTUJ", "DGU", "QFT"})
        for route, summary in self.summaries.items():
            with self.subTest(route=route):
                self.assertEqual(summary["run_id"], RUN_ID)
                self.assertEqual(summary["cycle"], 2)
                self.assertTrue(summary["artifact_path"].startswith(f"explorations/{RUN_ID}-cycle2-"))
                self.assertFalse(summary["target_import_used"])
                self.assertFalse(summary["claim_status_consistency_triggered"])
                self.assertFalse(summary["proof_restart_allowed"])

    def test_ig_forbids_coefficients_without_source_locator(self) -> None:
        ig = self.summaries["IG"]
        self.assertEqual(
            ig["verdict_class"],
            "blocked_source_locator_absent_host_not_coefficient_derivation",
        )
        self.assertTrue(ig["cycle1_producer_contract_consumed"])
        self.assertFalse(ig["source_operator_locator_found"])
        self.assertFalse(ig["coefficient_derivation_allowed"])
        self.assertFalse(ig["alpha_source_derived"])
        self.assertFalse(ig["beta_source_derived"])
        self.assertFalse(ig["finite_host_data_used_as_coefficients"])
        self.assertFalse(ig["rival_row_killed"])
        self.assertFalse(ig["desired_row_retained"])
        self.assertFalse(ig["selector_restart_allowed"])
        self.assertEqual(
            ig["first_missing_field"],
            "ProductABSourceOperatorSourceLocatorReceipt_V1.source_native_operator_locator",
        )

    def test_rs_first_frame_receipt_blocks_on_capture_toolchain(self) -> None:
        rs = self.summaries["RS"]
        self.assertEqual(
            rs["verdict_class"],
            "blocked_before_first_frame_receipt_missing_approved_capture_toolchain",
        )
        self.assertTrue(rs["cycle1_capture_contract_consumed"])
        self.assertFalse(rs["approved_capture_toolchain_found"])
        self.assertFalse(rs["first_frame_receipt_admitted"])
        self.assertFalse(rs["first_frame_persisted"])
        self.assertEqual(rs["persisted_frame_count"], 0)
        self.assertFalse(rs["first_frame_sha256_admitted"])
        self.assertFalse(rs["crop_or_ocr_allowed"])
        self.assertFalse(rs["typed_rs_intake_allowed"])
        self.assertFalse(rs["generation_restart_allowed"])
        self.assertEqual(
            rs["first_missing_field"],
            "ApprovedBrowserCaptureToolchainForFBozSSLxFvIWindow_V1.capture_tool_identity",
        )

    def test_ptuj_branch_purity_invariant_is_defined_but_unsatisfied(self) -> None:
        ptuj = self.summaries["PTUJ"]
        self.assertEqual(ptuj["verdict_class"], "blocked_branch_purity_gate")
        self.assertTrue(ptuj["cycle1_producer_contract_consumed"])
        self.assertTrue(ptuj["branch_purity_invariant_defined"])
        self.assertFalse(ptuj["branch_purity_invariant_satisfied"])
        self.assertEqual(ptuj["accepted_branch_count"], 0)
        self.assertEqual(ptuj["accepted_receipt_count"], 0)
        self.assertFalse(ptuj["official_branch_complete"])
        self.assertFalse(ptuj["lawful_local_branch_complete"])
        self.assertTrue(ptuj["mixed_branch_packet_rejected"])
        self.assertFalse(ptuj["cross_branch_assembly_allowed"])
        self.assertFalse(ptuj["formula_visibility_allowed"])

    def test_dgu_same_operator_is_not_evaluable_without_sector_locator(self) -> None:
        dgu = self.summaries["DGU"]
        self.assertEqual(dgu["verdict_class"], "blocked_precondition_gate")
        self.assertTrue(dgu["cycle1_sector_contract_consumed"])
        self.assertFalse(dgu["sector_rule_locator_admitted"])
        self.assertFalse(dgu["same_operator_witness_evaluable"])
        self.assertFalse(dgu["same_operator_witness_found"])
        self.assertFalse(dgu["symbol_certificate_allowed"])
        self.assertFalse(dgu["vz_replay_allowed"])
        self.assertFalse(dgu["typed_d_roll_allowed_as_source"])
        self.assertTrue(dgu["typed_d_roll_allowed_as_quarantined_screen"])

    def test_qft_inventory_finds_only_host_schema_and_target_candidates(self) -> None:
        qft = self.summaries["QFT"]
        self.assertEqual(
            qft["verdict_class"],
            "underdefined_negative_source_row_inventory_only_host_schema_target_candidates",
        )
        self.assertTrue(qft["cycle1_producer_contract_consumed"])
        self.assertTrue(qft["inventory_gate_defined"])
        self.assertEqual(qft["accepted_branch_label_source_row_count"], 0)
        self.assertEqual(qft["accepted_admissibility_rule_source_row_count"], 0)
        self.assertGreater(qft["host_infrastructure_candidate_count"], 0)
        self.assertGreater(qft["target_import_candidate_count"], 0)
        self.assertFalse(qft["generic_Y_promoted_to_branch_receipt"])
        self.assertFalse(qft["Y_b_branch_selected"])
        self.assertFalse(qft["source_defined_iota_b_admitted"])
        self.assertFalse(qft["typed_R_raw_b_O_admitted"])
        self.assertFalse(qft["local_groupoid_allowed"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
