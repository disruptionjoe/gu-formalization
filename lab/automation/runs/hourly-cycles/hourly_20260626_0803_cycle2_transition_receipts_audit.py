"""Audit the 0803 cycle 2 transition-receipt artifacts."""

from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260626-0803"
ARTIFACTS = {
    "DGU": ROOT / "explorations/hourly-20260626-0803-cycle2-dgu-exact-locator-delta-query-log.md",
    "TAU": ROOT / "explorations/hourly-20260626-0803-cycle2-tau-connection-role-slice-exhaustion-packet.md",
    "KIG": ROOT / "explorations/hourly-20260626-0803-cycle2-kig-parent-slot-degree-source-receipt.md",
    "PRODUCT_AB": ROOT / "explorations/hourly-20260626-0803-cycle2-productab-narrow-source-window-receipt.md",
    "QFT": ROOT / "explorations/hourly-20260626-0803-cycle2-qft-descent-groupoid-action-witness.md",
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


class Cycle2TransitionReceiptsAudit(unittest.TestCase):
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

    def test_dgu_exact_locator_emits_only_scoped_negative_v3(self) -> None:
        dgu = self.summaries["DGU"]
        self.assertFalse(dgu["positive_delta_packet_admitted"])
        self.assertTrue(dgu["negative_v3_emitted"])
        self.assertFalse(dgu["sector_rule_id_present"])
        self.assertFalse(dgu["family_identity_evidence_present"])
        self.assertFalse(dgu["same_operator_witness_allowed"])
        self.assertFalse(dgu["proof_restart_allowed"])
        self.assertGreaterEqual(dgu["inspected_components_count"], 1)
        self.assertGreaterEqual(dgu["pointer_only_components_count"], 1)
        self.assertEqual(dgu["payload_query_summary"]["sector_rule_id_hits"], 0)
        self.assertEqual(dgu["payload_query_summary"]["family_identity_evidence_hits"], 0)

    def test_tau_keeps_corrected_2a_possible_but_not_admitted(self) -> None:
        tau = self.summaries["TAU"]
        self.assertTrue(tau["connection_role_decided"])
        self.assertEqual(tau["connection_role"], "still_ambiguous_in_action_variation")
        self.assertTrue(tau["source_fixed_tau_plus_reference_present"])
        self.assertFalse(tau["dynamic_A_forced_by_sources"])
        self.assertTrue(tau["corrected_2a_possible"])
        self.assertFalse(tau["corrected_2a_admitted"])
        self.assertFalse(tau["no_natural_slice_theorem_proved"])
        self.assertFalse(tau["branch3_forced"])
        self.assertFalse(tau["branch3_admitted"])
        self.assertFalse(tau["exact_gr_restart_allowed"])
        self.assertFalse(tau["theta_restart_allowed"])

    def test_kig_parent_slot_receipt_does_not_unlock_trace_exclusion(self) -> None:
        kig = self.summaries["KIG"]
        self.assertFalse(kig["parent_slot_degree_source_forced"])
        self.assertFalse(kig["selected_parent_momentum_degree_source_forced"])
        self.assertFalse(kig["positive_exterior_degree_rule_present"])
        self.assertFalse(kig["trace_contraction_exclusion_allowed"])
        self.assertFalse(kig["coderivative_trace_eliminated"])
        self.assertFalse(kig["d_a_u_source_forced"])
        self.assertFalse(kig["branch3_admitted"])
        self.assertTrue(kig["candidate_parent_slot_exists"])
        self.assertEqual(kig["first_missing_parent_slot_row"], "ParentSlotDegreeSelectorForK_IG")

    def test_product_ab_window_negative_keeps_downstream_locked(self) -> None:
        product = self.summaries["PRODUCT_AB"]
        self.assertTrue(product["window_receipt_completed"])
        self.assertFalse(product["recovered_member_present"])
        self.assertFalse(product["operator_member_id_present"])
        self.assertFalse(product["direction_proved"])
        self.assertFalse(product["domain_binding_present"])
        self.assertFalse(product["codomain_binding_present"])
        self.assertFalse(product["locator_receipt_allowed"])
        self.assertFalse(product["binding_gate_allowed"])
        self.assertTrue(product["acquisition_subtask_emitted"])
        self.assertTrue(product["negative_window_receipt_emitted"])
        self.assertFalse(product["kig_restart_allowed"])
        self.assertEqual(
            product["constructive_next_object"],
            "FrameLevelPullThatUpJamieTzSEvmqxu48FormulaCaptureAndManuscriptIdentityCheck_V1",
        )

    def test_qft_descent_witness_emits_scoped_negative(self) -> None:
        qft = self.summaries["QFT"]
        self.assertFalse(qft["descent_groupoid_witness_admitted"])
        self.assertFalse(qft["source_cover_present"])
        self.assertFalse(qft["transition_data_present"])
        self.assertFalse(qft["action_law_present"])
        self.assertFalse(qft["field_transport_receipts_present"])
        self.assertFalse(qft["hidden_branch_key_emitted"])
        self.assertFalse(qft["source_admissibility_predicate_emitted"])
        self.assertTrue(qft["negative_receipt_emitted"])
        self.assertFalse(qft["carrier_work_allowed"])
        self.assertTrue(qft["BrSch_available_as_verifier"])
        self.assertFalse(qft["BrSch_used_as_action"])
        self.assertEqual(
            qft["constructive_next_object"],
            "QFTSourceDescentCoverAndLocalRecordInventory_V1",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
