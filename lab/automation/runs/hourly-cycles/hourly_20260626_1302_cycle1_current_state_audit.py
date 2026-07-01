"""Audit the 1302 cycle 1 current-state frontier artifacts."""

from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260626-1302"
ARTIFACTS = {
    "DGU": ROOT / "explorations/hourly-20260626-1302-cycle1-dgu-execution-receipt-current-state.md",
    "TAU": ROOT / "explorations/hourly-20260626-1302-cycle1-tau-inhabited-certificate-current-state.md",
    "KIG": ROOT / "explorations/hourly-20260626-1302-cycle1-kig-source-row-current-state.md",
    "PRODUCT_AB": ROOT / "explorations/hourly-20260626-1302-cycle1-productab-content-access-current-state.md",
    "QFT": ROOT / "explorations/hourly-20260626-1302-cycle1-qft-candidate-packet-current-state.md",
}


def extract_summary(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    marker = "```json"
    start = text.rfind(marker)
    if start == -1:
        raise AssertionError(f"missing JSON summary in {path}")
    start = text.find("\n", start) + 1
    end = text.find("```", start)
    if end == -1:
        raise AssertionError(f"unterminated JSON summary in {path}")
    return json.loads(text[start:end])


class Cycle1CurrentStateAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.summaries = {name: extract_summary(path) for name, path in ARTIFACTS.items()}

    def test_artifacts_are_run_scoped_and_non_promotional(self) -> None:
        for name, summary in self.summaries.items():
            with self.subTest(name=name):
                self.assertEqual(summary["run_id"], RUN_ID)
                self.assertEqual(summary["cycle"], 1)
                self.assertTrue(summary["artifact_path"].startswith(f"explorations/{RUN_ID}-cycle1-"))
                self.assertFalse(summary["target_import_used"])
                self.assertFalse(summary["claim_status_change"])

    def test_dgu_execution_receipt_is_absent_before_retries(self) -> None:
        dgu = self.summaries["DGU"]
        self.assertTrue(dgu["manifest_available"])
        self.assertFalse(dgu["execution_receipt_present"])
        self.assertFalse(dgu["acquisition_performed"])
        self.assertFalse(dgu["lawful_route_selected"])
        self.assertFalse(dgu["source_byte_path_present"])
        self.assertFalse(dgu["sha256_present"])
        self.assertFalse(dgu["producer_retry_allowed"])
        self.assertEqual(dgu["constructive_next_object"], "UCSDDGU01ExecutionReceiptAdmissionVerifier_V1")

    def test_tau_certificate_still_lacks_action_field_space(self) -> None:
        tau = self.summaries["TAU"]
        self.assertTrue(tau["certificate_spec_available"])
        self.assertFalse(tau["certificate_instance_present"])
        self.assertFalse(tau["action_field_space_declared"])
        self.assertFalse(tau["field_space_theorem_present"])
        self.assertFalse(tau["D_A_Phi_tau_zero_proved"])
        self.assertFalse(tau["exact_gr_restart_allowed"])
        self.assertEqual(tau["lower_next_object"], "TauFixedAlephActionFieldSpaceDeclaration_V1")

    def test_kig_source_row_is_absent_and_coderivative_trace_survives(self) -> None:
        kig = self.summaries["KIG"]
        self.assertFalse(kig["source_row_present"])
        self.assertTrue(kig["candidate_packet_schema_available"])
        self.assertFalse(kig["source_handle_present"])
        self.assertFalse(kig["degree_pig_2_pre_operator_found"])
        self.assertFalse(kig["source_selected_branch3_admitted"])
        self.assertEqual(kig["first_blocking_rival"], "CODERIVATIVE_TRACE")
        self.assertIn("CODERIVATIVE_TRACE", kig["surviving_parent_classes"])

    def test_productab_content_access_packet_is_absent(self) -> None:
        product = self.summaries["PRODUCT_AB"]
        self.assertFalse(product["content_access_packet_present"])
        self.assertTrue(product["packet_schema_available"])
        self.assertTrue(product["official_ptuj_locator_present"])
        self.assertEqual(product["video_id"], "TzSEvmqxu48")
        self.assertFalse(product["content_bearing_asset_present"])
        self.assertFalse(product["checksum_or_custody_present"])
        self.assertFalse(product["visible_formula_transcription_allowed"])

    def test_qft_same_context_candidate_is_absent(self) -> None:
        qft = self.summaries["QFT"]
        self.assertFalse(qft["candidate_packet_present"])
        self.assertTrue(qft["candidate_packet_schema_available"])
        self.assertFalse(qft["source_context_locator_found"])
        self.assertFalse(qft["cover_vocabulary_authorized"])
        self.assertFalse(qft["roles_type_over_same_context"])
        self.assertFalse(qft["carrier_work_allowed"])
        self.assertEqual(qft["lower_next_object"], "QFTSameContextSourceAnchorTriadReceipt_V1")


if __name__ == "__main__":
    unittest.main(verbosity=2)
