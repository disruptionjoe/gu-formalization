"""Audit the 0701 cycle 2 transition-gate artifacts."""

from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260626-0701"
ARTIFACTS = {
    "DGU": ROOT / "explorations/hourly-20260626-0701-cycle2-dgu-sector-rule-family-identity-delta-packet.md",
    "TAU": ROOT / "explorations/hourly-20260626-0701-cycle2-tau-source-to-slice-restriction-theorem.md",
    "KIG": ROOT / "explorations/hourly-20260626-0701-cycle2-kig-nonexterior-rival-eliminator-bundle.md",
    "PRODUCT_AB": ROOT / "explorations/hourly-20260626-0701-cycle2-product-ab-source-operator-locator-receipt-lock.md",
    "QFT": ROOT / "explorations/hourly-20260626-0701-cycle2-qft-morphism-typing-equality-law.md",
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


class Cycle2TransitionGatesAudit(unittest.TestCase):
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
                self.assertFalse(summary["claim_status_consistency_triggered"])

    def test_dgu_delta_packet_does_not_unlock_same_operator(self) -> None:
        dgu = self.summaries["DGU"]
        self.assertFalse(dgu["delta_packet_admitted"])
        self.assertFalse(dgu["sector_rule_id_present"])
        self.assertFalse(dgu["family_identity_evidence_present"])
        self.assertFalse(dgu["row_candidate_admitted"])
        self.assertFalse(dgu["same_operator_witness_allowed"])
        self.assertTrue(dgu["same_operator_work_forbidden"])
        self.assertFalse(dgu["proof_restart_allowed"])

    def test_tau_source_to_slice_theorem_remains_unproved(self) -> None:
        tau = self.summaries["TAU"]
        self.assertFalse(tau["source_to_slice_theorem_proved"])
        self.assertFalse(tau["allowed_field_space_is_tau_graph"])
        self.assertFalse(tau["D_A_Phi_tau_zero_proved"])
        self.assertFalse(tau["branch2a_admitted"])
        self.assertFalse(tau["branch2b_admitted"])
        self.assertFalse(tau["branch3_forced"])
        self.assertFalse(tau["exact_gr_restart_allowed"])
        self.assertFalse(tau["theta_restart_allowed"])

    def test_kig_eliminator_bundle_eliminates_no_rivals(self) -> None:
        kig = self.summaries["KIG"]
        self.assertFalse(kig["eliminator_bundle_admitted"])
        self.assertEqual(kig["eliminated_rivals_count"], 0)
        self.assertEqual(kig["surviving_class_count"], len(kig["surviving_classes"]))
        self.assertIn("CODERIVATIVE_TRACE", kig["surviving_classes"])
        self.assertEqual(kig["first_missing_eliminator"], "CoderivativeTraceEliminatorForK_IG")
        self.assertFalse(kig["d_a_u_source_forced"])
        self.assertFalse(kig["branch3_admitted"])

    def test_product_ab_locator_receipt_stays_locked(self) -> None:
        product = self.summaries["PRODUCT_AB"]
        self.assertFalse(product["source_operator_locator_receipt_emitted"])
        self.assertFalse(product["recovered_candidate_admitted"])
        self.assertFalse(product["operator_member_id_present"])
        self.assertFalse(product["binding_gate_allowed"])
        self.assertFalse(product["alpha_beta_identity_allowed"])
        self.assertFalse(product["kig_restart_allowed"])
        self.assertFalse(product["negative_is_global_no_go"])
        self.assertEqual(product["receipt_locked_object"], "ProductABSourceOperatorSourceLocatorReceipt_V1")

    def test_qft_closes_only_as_strict_schema_category(self) -> None:
        qft = self.summaries["QFT"]
        self.assertTrue(qft["morphism_typing_equality_law_defined"])
        self.assertTrue(qft["category_laws_close_at_schema_level"])
        self.assertFalse(qft["source_admitted_category"])
        self.assertFalse(qft["source_action_defined"])
        self.assertFalse(qft["cocycle_defined"])
        self.assertFalse(qft["carrier_work_allowed"])
        self.assertEqual(qft["next_frontier_object"], "QFTSourceBranchActionOrbitCocycleCandidate_V1")


if __name__ == "__main__":
    unittest.main(verbosity=2)
