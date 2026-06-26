"""Audit the 0502 cycle 3 closeouts and three-cycle synthesis."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260626-0502"
ARTIFACTS = {
    "DGU": ROOT / "explorations/hourly-20260626-0502-cycle3-dgu-source-acquisition-transition-closeout.md",
    "BRANCH": ROOT / "explorations/hourly-20260626-0502-cycle3-branch-ig-source-lock-transition-closeout.md",
    "PRODUCT_AB": ROOT / "explorations/hourly-20260626-0502-cycle3-product-ab-identity-transition-closeout.md",
    "QFT": ROOT / "explorations/hourly-20260626-0502-cycle3-qft-branch-provenance-transition-closeout.md",
    "MATRIX": ROOT / "explorations/hourly-20260626-0502-cycle3-cross-route-frontier-matrix.md",
    "SYNTHESIS": ROOT / "explorations/hourly-20260626-0502-three-cycle-fifteen-hole-synthesis.md",
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
        cls.summaries = {name: extract_summary(path) for name, path in ARTIFACTS.items()}

    def test_route_closeouts_are_run_scoped_and_non_promotional(self) -> None:
        for name in ("DGU", "BRANCH", "PRODUCT_AB", "QFT", "MATRIX"):
            summary = self.summaries[name]
            with self.subTest(name=name):
                self.assertEqual(summary["run_id"], RUN_ID)
                self.assertEqual(summary["cycle"], 3)
                self.assertTrue(summary["artifact_path"].startswith(f"explorations/{RUN_ID}-cycle3-"))
                self.assertFalse(summary["target_import_used"])
                self.assertFalse(summary.get("claim_status_consistency_triggered", False))

    def test_dgu_transition_locks_all_operator_restarts(self) -> None:
        dgu = self.summaries["DGU"]
        self.assertFalse(dgu["proof_restart_allowed"])
        self.assertFalse(dgu["primary_row_admitted"])
        self.assertFalse(dgu["same_operator_witness_allowed"])
        self.assertFalse(dgu["downstream_restarts_allowed"])
        self.assertIn("RSGUPhysSymbolPacket_V0", dgu["locked_downstream_routes"])
        self.assertIn("VZActualEBlockAndSubprincipalCharacteristicCertificate_V0", dgu["locked_downstream_routes"])
        self.assertIn("FamiliesIndexPushforwardGate_V0", dgu["locked_downstream_routes"])
        self.assertEqual(dgu["next_frontier_object"], "BroaderPrimarySourceSurfaceDGU01SectorRuleRowReceipt_V1")

    def test_branch_ig_transition_locks_exact_gr_and_theta(self) -> None:
        branch = self.summaries["BRANCH"]
        self.assertFalse(branch["branch_source_lock_closed"])
        self.assertFalse(branch["branch2a_admitted"])
        self.assertFalse(branch["branch3_admitted"])
        self.assertFalse(branch["exact_gr_restart_allowed"])
        self.assertFalse(branch["theta_restart_allowed"])
        self.assertFalse(branch["residual_restart_allowed"])
        self.assertEqual(branch["branch2a_gate"], "TauReferenceAndSliceLockReceipt_2A_V1")
        self.assertEqual(branch["branch3_gate"], "K_IGExteriorCodomainFinalityAxiomPacket_V0")

    def test_product_ab_transition_locks_identity_chain(self) -> None:
        product = self.summaries["PRODUCT_AB"]
        self.assertTrue(product["cycle1_consumed"])
        self.assertTrue(product["cycle2_consumed"])
        self.assertFalse(product["operator_family_inventory_admitted"])
        self.assertFalse(product["locator_receipt_admitted"])
        self.assertFalse(product["binding_gate_allowed"])
        self.assertFalse(product["two_row_matrix_allowed"])
        self.assertFalse(product["alpha_beta_identity_allowed"])
        self.assertFalse(product["kig_restart_allowed"])
        self.assertEqual(
            product["next_frontier_object"],
            "ManuscriptOxfordPTUJUCSD_ProductABShiabBianchiOperatorFamilyMemberInventory_V1",
        )

    def test_qft_transition_locks_downstream_qft_work(self) -> None:
        qft = self.summaries["QFT"]
        self.assertTrue(qft["cycle1_consumed"])
        self.assertTrue(qft["cycle2_consumed"])
        self.assertFalse(qft["qft_branch_provenance_packet_admitted"])
        self.assertFalse(qft["qft_branch_provenance_packet_restart_allowed"])
        self.assertFalse(qft["carrier_work_allowed"])
        self.assertFalse(qft["local_groupoid_allowed"])
        self.assertFalse(qft["local_algebra_allowed"])
        self.assertFalse(qft["qft_state_work_allowed"])
        self.assertEqual(qft["next_frontier_object"], "QFTSourceBranchRecordCategoryActionCocyclePacket_V0")

    def test_matrix_and_synthesis_agree_on_ranked_frontier(self) -> None:
        matrix = self.summaries["MATRIX"]
        synthesis = self.summaries["SYNTHESIS"]
        self.assertEqual(len(matrix["quality_holes_accounted_so_far"]), 10)
        self.assertEqual(matrix["quality_holes_accounted_count"], 10)
        self.assertFalse(matrix["proof_restart_allowed_any_route"])
        self.assertTrue(matrix["sequential_within_route_required"])
        self.assertTrue(matrix["parallel_across_routes_allowed"])

        self.assertEqual(synthesis["run_id"], RUN_ID)
        self.assertEqual(synthesis["target_quality_holes"], 15)
        self.assertEqual(synthesis["quality_holes_completed"], 15)
        self.assertEqual(synthesis["proof_closed_holes"], 0)
        self.assertEqual(synthesis["new_source_or_proof_receipts_admitted"], 0)
        self.assertFalse(synthesis["target_import_used"])
        self.assertFalse(synthesis["claim_status_consistency_triggered"])
        self.assertFalse(synthesis["claim_promotion_allowed_any_route"])
        self.assertFalse(synthesis["proof_restart_allowed_any_route"])
        self.assertEqual(synthesis["next_frontier_ranked"], matrix["next_frontier_ranked"])
        self.assertTrue(synthesis["three_cycle_wrapper_improved_quality"])
        self.assertTrue(synthesis["material_next_goal_refinement"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
