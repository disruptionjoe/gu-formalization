"""Audit the 0502 cycle 1 source-lock artifacts."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260626-0502"
ARTIFACTS = {
    "DGU": ROOT / "explorations/hourly-20260626-0502-cycle1-negative-primary-dgu-source-receipt.md",
    "BRANCH2A": ROOT / "explorations/hourly-20260626-0502-cycle1-branch2a-source-constraint-test.md",
    "BRANCH3": ROOT / "explorations/hourly-20260626-0502-cycle1-branch3-kig-source-selection-test.md",
    "PRODUCT_AB": ROOT / "explorations/hourly-20260626-0502-cycle1-product-ab-locator-receipt-search.md",
    "QFT": ROOT / "explorations/hourly-20260626-0502-cycle1-hidden-branch-structure-audit.md",
}


def extract_summary(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    blocks = re.findall(r"```json\s*(\{.*?\})\s*```", text, flags=re.DOTALL)
    if not blocks:
        raise AssertionError(f"missing JSON summary in {path}")
    return json.loads(blocks[-1])


class Cycle1SourceLocksAudit(unittest.TestCase):
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
                self.assertFalse(summary.get("claim_status_consistency_triggered", False))

    def test_dgu_negative_receipt_blocks_downstream_restarts(self) -> None:
        dgu = self.summaries["DGU"]
        self.assertFalse(dgu["admitted_primary_row"])
        self.assertFalse(dgu["same_operator_witness_evaluable"])
        self.assertFalse(dgu["typed_D_roll_used_as_source_row"])
        self.assertFalse(dgu["proof_restart_allowed"])
        self.assertIn("RSGUPhysSymbolPacket_V0", dgu["downstream_routes_locked"])
        self.assertIn("VZActualEBlockAndSubprincipalCharacteristicCertificate_V0", dgu["downstream_routes_locked"])

    def test_branch_lock_options_remain_source_blocked(self) -> None:
        branch2a = self.summaries["BRANCH2A"]
        self.assertFalse(branch2a["branch2a_packet_present"])
        self.assertFalse(branch2a["source_phi_present"])
        self.assertFalse(branch2a["proper_K_beta_proved"])
        self.assertEqual(branch2a["next_frontier_object"], "TauFixedReferenceSliceCertificate_2A_V0")

        branch3 = self.summaries["BRANCH3"]
        self.assertFalse(branch3["branch3_packet_present"])
        self.assertFalse(branch3["kig_selector_present"])
        self.assertTrue(branch3["legitimate_branch3_template_exists"])
        self.assertEqual(branch3["candidate_kig"], "D_A U")
        self.assertEqual(branch3["next_frontier_object"], "SourceForcedCodomainSelectorForK_IG_V1")

    def test_product_ab_locator_blocks_identity_and_kig_restart(self) -> None:
        product = self.summaries["PRODUCT_AB"]
        self.assertFalse(product["locator_receipt_admitted"])
        self.assertFalse(product["binding_gate_allowed"])
        self.assertFalse(product["source_native_operator_locator_found"])
        self.assertFalse(product["coefficient_derivation_allowed"])
        self.assertFalse(product["rival_projector_identity_allowed"])
        self.assertFalse(product["kig_restart_allowed"])
        self.assertEqual(product["next_frontier_object"], "ProductABSourceOperatorSourceLocatorReceipt_V1")

    def test_qft_hidden_branch_rows_remain_absent(self) -> None:
        qft = self.summaries["QFT"]
        self.assertEqual(qft["accepted_source_branch_label_row_count"], 0)
        self.assertEqual(qft["accepted_admissibility_rule_source_row_count"], 0)
        self.assertFalse(qft["precarrier_independence_proof_present"])
        self.assertFalse(qft["carrier_work_allowed"])
        self.assertFalse(qft["local_groupoid_allowed"])
        self.assertFalse(qft["qft_state_work_allowed"])
        self.assertEqual(qft["next_frontier_object"], "QFTHiddenBranchOrbitCocycleReceipt_V0")


if __name__ == "__main__":
    unittest.main(verbosity=2)
