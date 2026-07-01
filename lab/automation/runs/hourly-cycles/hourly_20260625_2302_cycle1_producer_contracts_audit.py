"""Audit the 2302 cycle 1 producer-contract frontier gates."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260625-2302"
ARTIFACTS = {
    "IG": ROOT
    / "explorations/hourly-20260625-2302-cycle1-ig-source-operator-producer-contract.md",
    "RS": ROOT
    / "explorations/hourly-20260625-2302-cycle1-rs-capture-toolchain-producer-contract.md",
    "PTUJ": ROOT
    / "explorations/hourly-20260625-2302-cycle1-ptuj-single-branch-producer-contract.md",
    "DGU": ROOT
    / "explorations/hourly-20260625-2302-cycle1-dgu-sector-rule-producer-contract.md",
    "QFT": ROOT
    / "explorations/hourly-20260625-2302-cycle1-qft-branch-admissibility-producer-contract.md",
}


def extract_summary(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    blocks = re.findall(r"```json\s*(\{.*?\})\s*```", text, flags=re.DOTALL)
    if not blocks:
        raise AssertionError(f"missing JSON summary in {path}")
    return json.loads(blocks[-1])


class Cycle1ProducerContractsAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.summaries = {route: extract_summary(path) for route, path in ARTIFACTS.items()}

    def test_all_cycle1_artifacts_are_run_scoped_and_no_restart(self) -> None:
        self.assertEqual(set(self.summaries), {"IG", "RS", "PTUJ", "DGU", "QFT"})
        for route, summary in self.summaries.items():
            with self.subTest(route=route):
                self.assertEqual(summary["run_id"], RUN_ID)
                self.assertEqual(summary["cycle"], 1)
                self.assertTrue(summary["artifact_path"].startswith(f"explorations/{RUN_ID}-cycle1-"))
                self.assertFalse(summary["target_import_used"])
                self.assertFalse(summary["claim_status_consistency_triggered"])
                self.assertFalse(summary["proof_restart_allowed"])

    def test_ig_contract_is_host_only_without_source_locator(self) -> None:
        ig = self.summaries["IG"]
        self.assertEqual(ig["verdict_class"], "host")
        self.assertTrue(ig["product_a_receipt_consumed"])
        self.assertTrue(ig["product_b_receipt_consumed"])
        self.assertTrue(ig["abstract_two_row_matrix_defined"])
        self.assertTrue(ig["producer_contract_defined"])
        self.assertFalse(ig["producer_contract_filled"])
        self.assertFalse(ig["source_operator_locator_found"])
        self.assertFalse(ig["source_operator_definition_admitted"])
        self.assertFalse(ig["alpha_source_derived"])
        self.assertFalse(ig["beta_source_derived"])
        self.assertFalse(ig["rival_projector_identity_admitted"])
        self.assertFalse(ig["selector_restart_allowed"])
        self.assertEqual(
            ig["first_missing_field"],
            "ProductABSourceOperatorSourceLocatorReceipt_V1.source_native_operator_locator",
        )

    def test_rs_contract_blocks_before_first_frame(self) -> None:
        rs = self.summaries["RS"]
        self.assertEqual(rs["verdict_class"], "blocked_approved_producer_identity_absent")
        self.assertTrue(rs["directory_policy_row_consumed"])
        self.assertTrue(rs["directory_policy_row_admitted"])
        self.assertFalse(rs["approved_capture_toolchain_found"])
        self.assertFalse(rs["capture_tool_identity_admitted"])
        self.assertFalse(rs["immutable_output_contract_admitted"])
        self.assertFalse(rs["first_frame_persisted"])
        self.assertEqual(rs["persisted_frame_count"], 0)
        self.assertFalse(rs["frame_checksum_admitted"])
        self.assertFalse(rs["crop_or_ocr_allowed"])
        self.assertFalse(rs["typed_rs_intake_allowed"])
        self.assertFalse(rs["generation_restart_allowed"])
        self.assertEqual(
            rs["first_missing_field"],
            "ApprovedBrowserCaptureToolchainForFBozSSLxFvIWindow_V1.capture_tool_identity",
        )

    def test_ptuj_contract_rejects_cross_branch_assembly(self) -> None:
        ptuj = self.summaries["PTUJ"]
        self.assertEqual(ptuj["verdict_class"], "blocked_producer_contract")
        self.assertTrue(ptuj["official_branch_checked"])
        self.assertTrue(ptuj["lawful_local_branch_checked"])
        self.assertFalse(ptuj["official_custodian_asset_record_admitted"])
        self.assertFalse(ptuj["lawful_source_byte_object_admitted"])
        self.assertFalse(ptuj["lawful_toolchain_admitted"])
        self.assertFalse(ptuj["output_manifest_admitted"])
        self.assertEqual(ptuj["accepted_branch_count"], 0)
        self.assertEqual(ptuj["accepted_receipt_count"], 0)
        self.assertFalse(ptuj["cross_branch_assembly_allowed"])
        self.assertFalse(ptuj["formula_visibility_allowed"])
        self.assertEqual(
            ptuj["constructive_next_object"],
            "one_complete_branch_local_PTUJ_source_packet_for_SingleCompletePTUJBranchReceipt_V1",
        )

    def test_dgu_contract_quarantines_typed_work(self) -> None:
        dgu = self.summaries["DGU"]
        self.assertEqual(dgu["verdict_class"], "blocked_contract_defined")
        self.assertTrue(dgu["producer_contract_defined"])
        self.assertTrue(dgu["producer_contract_admitted_as_gate"])
        self.assertFalse(dgu["source_emitted_0_1_sector_rule_found"])
        self.assertFalse(dgu["sector_rule_locator_admitted"])
        self.assertFalse(dgu["same_operator_witness_evaluable"])
        self.assertFalse(dgu["typed_d_roll_allowed_as_source"])
        self.assertTrue(dgu["typed_d_roll_allowed_as_quarantined_screen"])
        self.assertFalse(dgu["symbol_certificate_allowed"])
        self.assertFalse(dgu["vz_replay_allowed"])

    def test_qft_contract_keeps_generic_carrier_from_selecting_branch(self) -> None:
        qft = self.summaries["QFT"]
        self.assertEqual(qft["verdict_class"], "underdefined_producer_contract_not_admitted")
        self.assertFalse(qft["branch_label_source_row_found"])
        self.assertFalse(qft["admissibility_rule_source_defined"])
        self.assertFalse(qft["observation_section_source_defined"])
        self.assertFalse(qft["Y_b_branch_selected"])
        self.assertTrue(qft["generic_Y_carrier_schema_available"])
        self.assertFalse(qft["generic_Y_promoted_to_branch_receipt"])
        self.assertFalse(qft["source_defined_iota_b_admitted"])
        self.assertFalse(qft["typed_R_raw_b_O_admitted"])
        self.assertFalse(qft["local_groupoid_allowed"])
        self.assertEqual(
            qft["constructive_next_object"],
            "QFTBranchLabelAdmissibilitySourceRowInventory_V1",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
