"""Audit the 0502 cycle 2 dependent receipt artifacts."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260626-0502"
ARTIFACTS = {
    "DGU": ROOT / "explorations/hourly-20260626-0502-cycle2-dgu-source-scope-expansion-receipt.md",
    "TAU": ROOT / "explorations/hourly-20260626-0502-cycle2-tau-fixed-reference-slice-certificate.md",
    "KIG": ROOT / "explorations/hourly-20260626-0502-cycle2-kig-codomain-selector-gate.md",
    "PRODUCT_AB": ROOT / "explorations/hourly-20260626-0502-cycle2-product-ab-operator-family-inventory.md",
    "QFT": ROOT / "explorations/hourly-20260626-0502-cycle2-hidden-branch-orbit-cocycle-receipt.md",
}


def extract_summary(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    blocks = re.findall(r"```json\s*(\{.*?\})\s*```", text, flags=re.DOTALL)
    if not blocks:
        raise AssertionError(f"missing JSON summary in {path}")
    return json.loads(blocks[-1])


class Cycle2ReceiptsAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.summaries = {name: extract_summary(path) for name, path in ARTIFACTS.items()}

    def test_all_artifacts_are_run_scoped_and_non_promotional(self) -> None:
        for name, summary in self.summaries.items():
            with self.subTest(name=name):
                self.assertEqual(summary["run_id"], RUN_ID)
                self.assertEqual(summary["cycle"], 2)
                self.assertTrue(summary["artifact_path"].startswith(f"explorations/{RUN_ID}-cycle2-"))
                self.assertFalse(summary["target_import_used"])
                self.assertFalse(summary.get("claim_status_consistency_triggered", False))

    def test_dgu_expanded_scope_does_not_unlock_operator_chain(self) -> None:
        dgu = self.summaries["DGU"]
        self.assertFalse(dgu["admitted_primary_row"])
        self.assertFalse(dgu["expanded_scope_admits_receipt"])
        self.assertFalse(dgu["proof_restart_allowed"])
        self.assertFalse(dgu["same_operator_witness_evaluable"])
        self.assertEqual(dgu["next_frontier_object"], "BroaderPrimarySourceSurfaceDGU01SectorRuleRowReceipt_V1")
        self.assertIn("DGU01SameOperatorWitness_V1", dgu["routes_blocked"])

    def test_branch_2a_tau_slice_remains_reference_only(self) -> None:
        tau = self.summaries["TAU"]
        self.assertFalse(tau["tau_fixed_reference_slice_admitted"])
        self.assertTrue(tau["source_fixed_gamma_present"])
        self.assertFalse(tau["source_to_slice_lock_present"])
        self.assertFalse(tau["D_beta_Phi_source_derived"])
        self.assertFalse(tau["D_A_Phi_zero_proved"])
        self.assertEqual(tau["next_frontier_object"], "TauReferenceAndSliceLockReceipt_2A_V1")

    def test_branch_3_kig_codomain_selector_remains_multiple(self) -> None:
        kig = self.summaries["KIG"]
        self.assertFalse(kig["codomain_selector_closed"])
        self.assertFalse(kig["exterior_codomain_forced"])
        self.assertFalse(kig["kig_unique_before_targets"])
        self.assertTrue(kig["d_a_u_admissible"])
        self.assertFalse(kig["d_a_u_source_forced"])
        self.assertGreaterEqual(len(kig["surviving_rival_classes"]), 4)
        self.assertEqual(kig["next_frontier_object"], "K_IGExteriorCodomainFinalityAxiomPacket_V0")

    def test_product_ab_inventory_does_not_admit_locator_chain(self) -> None:
        product = self.summaries["PRODUCT_AB"]
        self.assertFalse(product["operator_family_inventory_admitted"])
        self.assertFalse(product["operator_member_id_present"])
        self.assertFalse(product["productb_to_producta_direction_bound"])
        self.assertFalse(product["locator_receipt_admitted"])
        self.assertFalse(product["binding_gate_allowed"])
        self.assertFalse(product["alpha_beta_identity_allowed"])
        self.assertFalse(product["kig_restart_allowed"])
        self.assertEqual(
            product["next_frontier_object"],
            "ManuscriptOxfordPTUJUCSD_ProductABShiabBianchiOperatorFamilyMemberInventory_V1",
        )

    def test_qft_orbit_cocycle_receipt_not_admitted(self) -> None:
        qft = self.summaries["QFT"]
        self.assertFalse(qft["orbit_cocycle_receipt_admitted"])
        self.assertFalse(qft["source_branch_record_category_defined"])
        self.assertFalse(qft["source_action_defined"])
        self.assertFalse(qft["source_orbit_or_stabilizer_or_descent_cocycle_defined"])
        self.assertFalse(qft["qft_hidden_branch_key_emitted"])
        self.assertFalse(qft["source_admissibility_predicate_emitted"])
        self.assertFalse(qft["precarrier_independence_proof_present"])
        self.assertEqual(qft["next_frontier_object"], "QFTSourceBranchRecordCategoryActionCocyclePacket_V0")


if __name__ == "__main__":
    unittest.main(verbosity=2)
