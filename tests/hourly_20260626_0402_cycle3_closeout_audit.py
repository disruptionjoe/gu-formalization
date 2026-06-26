"""Audit the 0402 cycle 3 closeouts and three-cycle synthesis."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260626-0402"
ARTIFACTS = {
    "DGU": ROOT / "explorations/hourly-20260626-0402-cycle3-dgu-primary-row-unlock-closeout.md",
    "BRANCH_IG": ROOT / "explorations/hourly-20260626-0402-cycle3-branch-ig-source-lock-closeout.md",
    "IG": ROOT / "explorations/hourly-20260626-0402-cycle3-ig-locator-identity-transition-closeout.md",
    "QFT": ROOT / "explorations/hourly-20260626-0402-cycle3-qft-hidden-branch-transition-closeout.md",
    "MATRIX": ROOT / "explorations/hourly-20260626-0402-cycle3-cross-route-transition-matrix.md",
    "SYNTHESIS": ROOT / "explorations/hourly-20260626-0402-three-cycle-fifteen-hole-synthesis.md",
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
        for name in ("DGU", "BRANCH_IG", "IG", "QFT", "MATRIX"):
            summary = self.summaries[name]
            with self.subTest(name=name):
                self.assertEqual(summary["run_id"], RUN_ID)
                self.assertEqual(summary["cycle"], 3)
                self.assertTrue(summary["artifact_path"].startswith(f"explorations/{RUN_ID}-cycle3-"))
                self.assertFalse(summary["target_import_used"])
                self.assertFalse(summary["claim_status_consistency_triggered"])

    def test_dgu_blocks_rs_and_vz_restarts(self) -> None:
        dgu = self.summaries["DGU"]
        self.assertTrue(dgu["cycle1_consumed"])
        self.assertTrue(dgu["cycle2_consumed"])
        self.assertFalse(dgu["rs_symbol_restart_allowed"])
        self.assertFalse(dgu["vz_actual_certificate_restart_allowed"])
        self.assertFalse(dgu["primary_dgu_row_present"])
        self.assertFalse(dgu["same_operator_witness_present"])
        self.assertEqual(dgu["first_missing_field"], "PrimarySourceDGU01SectorRuleRowInstance_V1.source_row_payload")
        self.assertEqual(dgu["next_frontier_object"], "PrimarySourceDGU01SectorRuleRowInstance_V1")

    def test_branch_ig_blocks_exact_gr_and_theta_restarts(self) -> None:
        branch = self.summaries["BRANCH_IG"]
        self.assertFalse(branch["exact_gr_restart_allowed"])
        self.assertFalse(branch["theta_coefficient_restart_allowed"])
        self.assertFalse(branch["branch2a_source_lock_present"])
        self.assertFalse(branch["branch3_source_lock_present"])
        self.assertIn("DerivedAIndependentIGConstraintPacket_2A", branch["first_missing_object"])
        self.assertIn("SourceForcedSIGDynPacket_3", branch["first_missing_object"])
        self.assertEqual(branch["next_frontier_object"], "BranchFixedIGVariationSourceLock_V0")

    def test_ig_locator_identity_transition_is_locked(self) -> None:
        ig = self.summaries["IG"]
        self.assertTrue(ig["cycle1_consumed"])
        self.assertTrue(ig["cycle2_consumed"])
        self.assertFalse(ig["locator_receipt_admitted"])
        self.assertFalse(ig["binding_gate_allowed"])
        self.assertFalse(ig["two_row_matrix_allowed"])
        self.assertFalse(ig["rival_projector_identity_allowed"])
        self.assertFalse(ig["kig_restart_allowed"])
        self.assertEqual(ig["next_frontier_object"], "ProductABSourceOperatorSourceLocatorReceipt_V1")

    def test_qft_hidden_branch_transition_is_locked(self) -> None:
        qft = self.summaries["QFT"]
        self.assertTrue(qft["cycle2_consumed"])
        self.assertFalse(qft["hidden_branch_structure_audit_present"])
        self.assertFalse(qft["branch_row_provenance_packet_admitted"])
        self.assertFalse(qft["carrier_work_allowed"])
        self.assertFalse(qft["local_groupoid_allowed"])
        self.assertFalse(qft["qft_state_work_allowed"])
        self.assertEqual(qft["next_frontier_object"], "HiddenBranchStructureAudit_V0")

    def test_matrix_and_synthesis_record_fifteen_holes_no_restart(self) -> None:
        matrix = self.summaries["MATRIX"]
        self.assertEqual(matrix["route_count"], 6)
        self.assertEqual(len(matrix["quality_holes_accounted_so_far"]), 7)
        self.assertFalse(matrix["proof_restart_allowed_any_route"])
        self.assertEqual(len(matrix["next_frontier_ranked"]), 5)
        self.assertTrue(matrix["sequential_within_route_required"])
        self.assertTrue(matrix["parallel_across_routes_allowed"])

        syn = self.summaries["SYNTHESIS"]
        self.assertEqual(syn["run_id"], RUN_ID)
        self.assertEqual(syn["target_quality_holes"], 15)
        self.assertEqual(syn["quality_holes_completed"], 15)
        self.assertEqual(syn["blocked_or_underdefined_holes"], 15)
        self.assertEqual(syn["new_source_or_proof_receipts_admitted"], 0)
        self.assertFalse(syn["target_import_used"])
        self.assertFalse(syn["claim_status_consistency_triggered"])
        self.assertFalse(syn["claim_promotion_allowed_any_route"])
        self.assertFalse(syn["claim_demotion_required_any_route"])
        self.assertFalse(syn["proof_restart_allowed_any_route"])
        self.assertEqual(syn["next_frontier_ranked"], matrix["next_frontier_ranked"])
        self.assertTrue(syn["three_cycle_wrapper_improved_quality"])
        self.assertTrue(syn["material_next_goal_refinement"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
