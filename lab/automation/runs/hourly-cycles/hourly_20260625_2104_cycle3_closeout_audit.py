"""Audit the 2104 cycle 3 closeout gates and transition matrix."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260625-2104"
ARTIFACTS = {
    "IG": ROOT / "explorations/hourly-20260625-2104-cycle3-ig-rival-projector-identity-gate.md",
    "DGU": ROOT / "explorations/hourly-20260625-2104-cycle3-dgu-source-to-symbol-firewall.md",
    "RS": ROOT / "explorations/hourly-20260625-2104-cycle3-rs-owned-manifest-readiness-gate.md",
    "QFT": ROOT / "explorations/hourly-20260625-2104-cycle3-qft-branch-admissibility-map-gate.md",
    "MATRIX": ROOT / "explorations/hourly-20260625-2104-cycle3-proof-restart-transition-matrix.md",
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

    def test_all_cycle3_artifacts_present(self) -> None:
        self.assertEqual(set(self.summaries), {"IG", "DGU", "RS", "QFT", "MATRIX"})
        for route, summary in self.summaries.items():
            with self.subTest(route=route):
                self.assertEqual(summary["run_id"], RUN_ID)
                self.assertEqual(summary["cycle"], 3)
                self.assertTrue(summary["artifact_path"].startswith(f"explorations/{RUN_ID}-cycle3-"))
                self.assertFalse(summary["target_import_used"])

    def test_ig_rival_projector_identity_still_blocks_restart(self) -> None:
        ig = self.summaries["IG"]
        self.assertEqual(ig["verdict_class"], "blocked")
        self.assertEqual(ig["accepted_receipt_count"], 2)
        self.assertTrue(ig["product_a_admitted"])
        self.assertTrue(ig["product_b_admitted"])
        self.assertEqual(ig["common_row_count"], 2)
        self.assertFalse(ig["rival_projector_identity_admitted"])
        self.assertFalse(ig["selector_restart_allowed"])
        self.assertFalse(ig["proof_restart_allowed"])
        self.assertIn("two_row_projector_matrix", ig["first_obstruction"])

    def test_dgu_firewall_is_admitted_but_source_receipt_absent(self) -> None:
        dgu = self.summaries["DGU"]
        self.assertEqual(dgu["verdict_class"], "blocked")
        self.assertTrue(dgu["source_stable_packet_consumed"])
        self.assertFalse(dgu["source_emitted_receipt_admitted"])
        self.assertFalse(dgu["typed_d_roll_allowed_as_source"])
        self.assertTrue(dgu["typed_d_roll_allowed_as_quarantined_screen"])
        self.assertFalse(dgu["symbol_certificate_allowed"])
        self.assertFalse(dgu["vz_replay_allowed"])
        self.assertFalse(dgu["proof_restart_allowed"])
        self.assertTrue(dgu["firewall_admitted"])
        self.assertEqual(dgu["first_missing_object"], "SourceEmittedDGU01SectorRuleAndSameOperatorReceipt_V1")

    def test_rs_manifest_directory_gate_blocks_typed_intake(self) -> None:
        rs = self.summaries["RS"]
        self.assertEqual(rs["verdict_class"], "blocked_owned_manifest_directory_not_admitted")
        self.assertTrue(rs["route_receipt_consumed"])
        self.assertFalse(rs["frame_manifest_admitted"])
        self.assertFalse(rs["owned_manifest_directory_admitted"])
        self.assertEqual(rs["persisted_frame_count"], 0)
        self.assertFalse(rs["typed_rs_intake_allowed"])
        self.assertFalse(rs["generation_restart_allowed"])
        self.assertFalse(rs["index_restart_allowed"])
        self.assertFalse(rs["proof_restart_allowed"])
        self.assertIn("owned_artifact_directory_path", rs["missing_preconditions"])

    def test_qft_branch_admissibility_remains_underdefined(self) -> None:
        qft = self.summaries["QFT"]
        self.assertEqual(qft["verdict_class"], "underdefined")
        self.assertFalse(qft["branch_admissibility_admitted"])
        self.assertFalse(qft["source_defined_iota_b_admitted"])
        self.assertFalse(qft["carrier_admitted"])
        self.assertFalse(qft["typed_R_raw_allowed"])
        self.assertFalse(qft["local_groupoid_allowed"])
        self.assertFalse(qft["proof_restart_allowed"])
        self.assertEqual(qft["first_obstruction"], "source_native_branch_label_and_admissibility_rows_absent")
        self.assertEqual(qft["constructive_next_object"], "SourceNativeBranchLabelAdmissibilityAndObservationSectionLedger_V1")

    def test_transition_matrix_all_routes_block_proof_restart(self) -> None:
        matrix = self.summaries["MATRIX"]
        self.assertEqual(matrix["verdict_class"], "no_proof_restart_allowed")
        self.assertFalse(matrix["proof_restart_allowed_any_route"])
        self.assertEqual(matrix["blocked_routes"], ["PTUJ", "IG", "DGU", "RS", "QFT"])
        self.assertEqual(matrix["sequential_next_routes"], ["PTUJ", "IG", "DGU", "RS", "QFT"])
        self.assertEqual(
            matrix["accepted_receipts_by_route"]["IG"],
            [
                "ProductBFullD7SummandMultiplicityDimensionTableReceipt_V1",
                "ProductAFullKernelCokernelHighestWeightPacket_V1",
            ],
        )
        self.assertEqual(
            matrix["accepted_receipts_by_route"]["RS"],
            ["RSLawfulSourceAcquisitionRouteOrBrowserCaptureRouteForFBozSSLxFvIWindow_V1"],
        )
        self.assertEqual(matrix["accepted_receipts_by_route"]["PTUJ"], [])
        self.assertEqual(matrix["accepted_receipts_by_route"]["DGU"], [])
        self.assertEqual(matrix["accepted_receipts_by_route"]["QFT"], [])

    def test_next_quality_holes_are_ranked_and_sequential(self) -> None:
        matrix = self.summaries["MATRIX"]
        holes = matrix["next_quality_holes"]
        self.assertEqual([hole["rank"] for hole in holes], [1, 2, 3, 4, 5])
        self.assertEqual([hole["route"] for hole in holes], ["IG", "RS", "PTUJ", "DGU", "QFT"])
        first_missing = matrix["first_missing_objects_by_route"]
        self.assertEqual(first_missing["IG"], "SourceNaturalProductABRivalProjectorIdentity_V1")
        self.assertEqual(first_missing["RS"], "OwnedPersistentFrameCropOCRArtifactPathSetForFBozSSLxFvIWindow_V1")
        self.assertEqual(
            first_missing["PTUJ"],
            "one_complete_branch_local_PTUJ_source_packet_for_SingleCompletePTUJBranchReceipt_V1",
        )
        self.assertEqual(first_missing["DGU"], "SourceEmittedDGU01SectorRuleAndSameOperatorReceipt_V1")
        self.assertEqual(first_missing["QFT"], "BranchAdmissibilityAndObservationMapReceipt_V1")


if __name__ == "__main__":
    unittest.main(verbosity=2)
