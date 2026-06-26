"""Audit the 0402 cycle 2 source-object frontier artifacts."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260626-0402"
ARTIFACTS = {
    "RSGUPhysSymbolPacketGate": ROOT
    / "explorations/hourly-20260626-0402-cycle2-rs-gu-phys-symbol-packet-gate.md",
    "VZActualEBlockSubprincipalCertificateGate": ROOT
    / "explorations/hourly-20260626-0402-cycle2-vz-actual-eblock-subprincipal-certificate-gate.md",
    "BranchFixedIGVariationPacketGate": ROOT
    / "explorations/hourly-20260626-0402-cycle2-branch-fixed-ig-variation-packet-gate.md",
    "IGSourceOperatorLocatorReceiptGate": ROOT
    / "explorations/hourly-20260626-0402-cycle2-ig-source-operator-locator-receipt-gate.md",
    "QFTBranchRowProvenanceSourceAudit": ROOT
    / "explorations/hourly-20260626-0402-cycle2-qft-branch-row-provenance-source-audit.md",
}


def extract_summary(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    blocks = re.findall(r"```json\s*(\{.*?\})\s*```", text, flags=re.DOTALL)
    if not blocks:
        raise AssertionError(f"missing JSON summary in {path}")
    return json.loads(blocks[-1])


class Cycle2SourceObjectGatesAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.summaries = {lane: extract_summary(path) for lane, path in ARTIFACTS.items()}

    def test_all_lanes_are_run_scoped_and_non_promotional(self) -> None:
        self.assertEqual(set(self.summaries), set(ARTIFACTS))
        for lane, summary in self.summaries.items():
            with self.subTest(lane=lane):
                self.assertEqual(summary["run_id"], RUN_ID)
                self.assertEqual(summary["cycle"], 2)
                self.assertEqual(summary["lane"], lane)
                self.assertTrue(summary["artifact_path"].startswith(f"explorations/{RUN_ID}-cycle2-"))
                self.assertFalse(summary["target_import_used"])
                self.assertFalse(summary["claim_status_consistency_triggered"])

    def test_rs_symbol_packet_waits_on_primary_dgu_row(self) -> None:
        rs = self.summaries["RSGUPhysSymbolPacketGate"]
        self.assertTrue(rs["cycle1_consumed"])
        self.assertFalse(rs["packet_instantiable_now"])
        self.assertFalse(rs["generation_readout_allowed"])
        self.assertTrue(rs["depends_on_primary_dgu_row"])
        self.assertEqual(rs["first_missing_field"], "RSGUPhysSymbolPacket_V0.accepted_source_operator_handle")
        self.assertEqual(rs["next_frontier_object"], "PrimarySourceDGU01SectorRuleRowInstance_V1")

    def test_vz_actual_certificate_waits_on_primary_dgu_row(self) -> None:
        vz = self.summaries["VZActualEBlockSubprincipalCertificateGate"]
        self.assertTrue(vz["cycle1_consumed"])
        self.assertFalse(vz["actual_eblock_instantiable_now"])
        self.assertFalse(vz["subprincipal_characteristic_instantiable_now"])
        self.assertFalse(vz["typed_principal_replay_allowed"])
        self.assertEqual(
            vz["first_missing_field"],
            "PrimarySourceDGU01SectorRuleRowInstance_V1.source_row_payload",
        )
        self.assertEqual(vz["next_frontier_object"], "PrimarySourceDGU01SectorRuleRowInstance_V1")

    def test_branch_fixed_ig_variation_packet_is_not_instantiated(self) -> None:
        ig = self.summaries["BranchFixedIGVariationPacketGate"]
        self.assertTrue(ig["cycle1_consumed"])
        self.assertFalse(ig["branch2a_packet_present"])
        self.assertFalse(ig["branch3_packet_present"])
        self.assertFalse(ig["branch_selected_from_target_success"])
        self.assertFalse(ig["packet_instantiable_now"])
        self.assertIn("Branch 2A lacks source-derived Phi", ig["first_missing_object"])
        self.assertIn("Branch 3 lacks K_IG_selector", ig["first_missing_object"])
        self.assertEqual(ig["next_frontier_object"], "BranchFixedIGVariationSourceLock_V0")

    def test_ig_locator_receipt_stays_before_binding_and_chirality(self) -> None:
        locator = self.summaries["IGSourceOperatorLocatorReceiptGate"]
        self.assertTrue(locator["cycle1_consumed"])
        self.assertFalse(locator["locator_receipt_admitted"])
        self.assertFalse(locator["source_native_operator_locator_found"])
        self.assertFalse(locator["binding_gate_evaluable"])
        self.assertFalse(locator["downstream_chirality_used"])
        self.assertIn("ProductABSourceOperatorSourceLocatorReceipt_V1.source_native_operator_locator", locator["first_missing_field"])
        self.assertEqual(locator["next_frontier_object"], "ProductABSourceOperatorSourceLocatorReceipt_V1")

    def test_qft_provenance_packet_keeps_carrier_work_locked(self) -> None:
        qft = self.summaries["QFTBranchRowProvenanceSourceAudit"]
        self.assertFalse(qft["branch_row_provenance_packet_admitted"])
        self.assertEqual(qft["accepted_source_branch_label_row_count"], 0)
        self.assertEqual(qft["accepted_admissibility_rule_source_row_count"], 0)
        self.assertFalse(qft["precarrier_independence_proof_present"])
        self.assertFalse(qft["carrier_work_allowed"])
        self.assertEqual(
            qft["exact_missing_rows"],
            [
                "QFTBranchRowProvenancePacket_V1.source_branch_label_row",
                "QFTBranchRowProvenancePacket_V1.admissibility_rule_source_row",
                "QFTBranchRowProvenancePacket_V1.precarrier_independence_proof",
            ],
        )
        self.assertEqual(qft["next_frontier_object"], "HiddenBranchStructureAudit_V0")


if __name__ == "__main__":
    unittest.main(verbosity=2)
