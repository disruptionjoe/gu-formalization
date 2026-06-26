"""Audit the 0803 cycle 1 frontier-gate artifacts."""

from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260626-0803"
ARTIFACTS = {
    "DGU": ROOT / "explorations/hourly-20260626-0803-cycle1-dgu-positive-delta-packet-intake.md",
    "TAU": ROOT / "explorations/hourly-20260626-0803-cycle1-tau-2b3-source-admission-fork-certificate.md",
    "KIG": ROOT / "explorations/hourly-20260626-0803-cycle1-kig-positive-exterior-degree-rule.md",
    "PRODUCT_AB": ROOT / "explorations/hourly-20260626-0803-cycle1-productab-recovered-member-acquisition.md",
    "QFT": ROOT / "explorations/hourly-20260626-0803-cycle1-qft-source-branch-action-input-data-packet.md",
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


class Cycle1FrontierGatesAudit(unittest.TestCase):
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

    def test_dgu_positive_delta_packet_remains_locked(self) -> None:
        dgu = self.summaries["DGU"]
        self.assertFalse(dgu["positive_delta_packet_admitted"])
        self.assertTrue(dgu["scoped_negative_v2_emitted"])
        self.assertFalse(dgu["global_no_go_claimed"])
        self.assertFalse(dgu["sector_rule_id_present"])
        self.assertFalse(dgu["family_identity_evidence_present"])
        self.assertFalse(dgu["same_operator_witness_allowed"])
        self.assertFalse(dgu["proof_restart_allowed"])
        self.assertIn("sector_rule_id_for_actual_D_GU_epsilon_0_1", dgu["first_failed_fields"])
        self.assertIn("family_identity_evidence_to_actual_D_GU_epsilon_0_1", dgu["first_failed_fields"])

    def test_tau_fork_does_not_admit_2b_or_3(self) -> None:
        tau = self.summaries["TAU"]
        self.assertEqual(tau["current_decision"], "TAU_BOTH_POSSIBLE_NOT_ADMITTED")
        self.assertFalse(tau["failed_2a_forces_dynamic_A_2b"])
        self.assertFalse(tau["failed_2a_forces_branch3"])
        self.assertTrue(tau["branch2b_possible"])
        self.assertFalse(tau["branch2b_admitted"])
        self.assertTrue(tau["branch3_possible"])
        self.assertFalse(tau["branch3_forced"])
        self.assertFalse(tau["branch3_admitted"])
        self.assertFalse(tau["exact_gr_restart_allowed"])
        self.assertFalse(tau["theta_restart_allowed"])
        self.assertFalse(tau["target_replacement_guard"]["decision_changed"])

    def test_kig_exterior_degree_is_not_source_forced(self) -> None:
        kig = self.summaries["KIG"]
        self.assertFalse(kig["positive_exterior_degree_rule_present"])
        self.assertFalse(kig["selected_codomain_source_forced"])
        self.assertFalse(kig["selected_parent_momentum_degree_source_forced"])
        self.assertTrue(kig["d_a_u_admissible"])
        self.assertFalse(kig["d_a_u_source_forced"])
        self.assertFalse(kig["branch3_admitted"])
        self.assertIn("CODERIVATIVE_TRACE", kig["surviving_classes"])
        self.assertEqual(kig["first_blocking_rival"], "CODERIVATIVE_TRACE")
        self.assertEqual(kig["narrower_next_object"], "KIGParentSlotDegreeSourceReceipt_V1")

    def test_product_ab_recovered_member_stays_absent(self) -> None:
        product = self.summaries["PRODUCT_AB"]
        self.assertFalse(product["recovered_member_present"])
        self.assertFalse(product["operator_member_id_present"])
        self.assertFalse(product["locator_receipt_allowed"])
        self.assertFalse(product["binding_gate_allowed"])
        self.assertFalse(product["alpha_beta_identity_allowed"])
        self.assertFalse(product["source_natural_product_ab_rival_projector_identity_allowed"])
        self.assertFalse(product["kig_restart_allowed"])
        self.assertFalse(product["negative_is_global_no_go"])
        self.assertEqual(product["next_frontier_object"], "ProductABNarrowSourceWindowRecoveredMemberReceipt_V1")
        self.assertFalse(product["negative_coverage_v2_allowed_now"])

    def test_qft_packet_is_verifier_only(self) -> None:
        qft = self.summaries["QFT"]
        self.assertTrue(qft["packet_schema_defined"])
        self.assertFalse(qft["admitted_packet_instance_present"])
        self.assertTrue(qft["schema_category_available_as_verifier"])
        self.assertFalse(qft["schema_category_used_as_source_action"])
        self.assertFalse(qft["source_action_defined"])
        self.assertFalse(qft["orbit_stabilizer_defined"])
        self.assertFalse(qft["cocycle_defined"])
        self.assertFalse(qft["hidden_branch_key_emitted"])
        self.assertFalse(qft["source_admissibility_predicate_emitted"])
        self.assertFalse(qft["carrier_work_allowed"])
        self.assertEqual(qft["next_frontier_object"], "QFTSourceDescentGroupoidActionWitness_V1")


if __name__ == "__main__":
    unittest.main(verbosity=2)
