"""Audit the 0103 cycle 1 source-admission artifacts."""

from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260626-0604"
ARTIFACTS = {
    "DGU": ROOT / "explorations/hourly-20260626-0604-cycle1-broader-dgu-source-surface-receipt.md",
    "TAU": ROOT / "explorations/hourly-20260626-0604-cycle1-tau-reference-slice-lock-receipt.md",
    "KIG": ROOT / "explorations/hourly-20260626-0604-cycle1-kig-exterior-codomain-finality-packet.md",
    "PRODUCT_AB": ROOT / "explorations/hourly-20260626-0604-cycle1-product-ab-family-member-inventory.md",
    "QFT": ROOT / "explorations/hourly-20260626-0604-cycle1-qft-source-branch-record-category-cocycle-packet.md",
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


class Cycle1SourceAdmissionAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.summaries = {name: extract_summary(path) for name, path in ARTIFACTS.items()}

    def test_all_artifacts_are_run_scoped_and_non_promotional(self) -> None:
        for name, summary in self.summaries.items():
            with self.subTest(name=name):
                self.assertEqual(summary["run_id"], RUN_ID)
                self.assertEqual(summary["cycle"], 1)
                self.assertTrue(summary["artifact_path"].startswith(f"explorations/{RUN_ID}-cycle1-"))
                self.assertFalse(summary["target_import_used"])
                self.assertFalse(summary["claim_status_consistency_triggered"])

    def test_dgu_broader_surface_does_not_unlock_operator_restarts(self) -> None:
        dgu = self.summaries["DGU"]
        self.assertFalse(dgu["admitted_primary_row"])
        self.assertFalse(dgu["broader_surface_receipt_admitted"])
        self.assertTrue(dgu["rs_image_delta_considered"])
        self.assertFalse(dgu["typed_D_roll_used_as_source_row"])
        self.assertFalse(dgu["same_operator_witness_allowed"])
        self.assertFalse(dgu["downstream_restarts_allowed"])
        self.assertEqual(dgu["next_frontier_object"], "DGUPrimaryRowAdmissionPredicate_V1")

    def test_tau_reference_is_not_a_slice_lock(self) -> None:
        tau = self.summaries["TAU"]
        self.assertTrue(tau["source_fixed_reference_present"])
        self.assertFalse(tau["slice_lock_admitted"])
        self.assertFalse(tau["branch2a_admitted"])
        self.assertFalse(tau["D_beta_Phi_source_derived"])
        self.assertFalse(tau["D_A_Phi_zero_proved"])
        self.assertTrue(tau["dynamic_A_branch2b_still_possible"])
        self.assertEqual(tau["next_frontier_object"], "TauSliceLockDecisionTable_2A_2B_V1")

    def test_kig_exterior_candidate_remains_multiple(self) -> None:
        kig = self.summaries["KIG"]
        self.assertFalse(kig["codomain_selector_closed"])
        self.assertFalse(kig["exterior_codomain_forced"])
        self.assertFalse(kig["kig_unique_before_targets"])
        self.assertTrue(kig["d_a_u_admissible"])
        self.assertFalse(kig["d_a_u_source_forced"])
        self.assertGreaterEqual(len(kig["surviving_rival_classes"]), 4)

    def test_product_ab_member_is_absent_before_binding(self) -> None:
        product = self.summaries["PRODUCT_AB"]
        self.assertFalse(product["operator_family_inventory_admitted"])
        self.assertFalse(product["operator_member_id_present"])
        self.assertFalse(product["productb_to_producta_direction_bound"])
        self.assertFalse(product["locator_receipt_admitted"])
        self.assertFalse(product["alpha_beta_identity_allowed"])
        self.assertFalse(product["kig_restart_allowed"])
        self.assertIn("V(omega_6)", product["common_rows"])

    def test_qft_branch_record_category_is_not_defined(self) -> None:
        qft = self.summaries["QFT"]
        self.assertFalse(qft["source_branch_record_category_defined"])
        self.assertFalse(qft["source_action_defined"])
        self.assertFalse(qft["source_orbit_or_stabilizer_or_descent_cocycle_defined"])
        self.assertFalse(qft["qft_hidden_branch_key_emitted"])
        self.assertFalse(qft["precarrier_independence_proof_present"])
        self.assertFalse(qft["carrier_work_allowed"])
        self.assertEqual(qft["next_frontier_object"], "QFTBranchRecordPrimitiveSchema_V1")


if __name__ == "__main__":
    unittest.main(verbosity=2)
