"""Audit the 0701 cycle 3 closeout and synthesis artifacts."""

from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260626-0701"
ARTIFACTS = {
    "DGU": ROOT / "explorations/hourly-20260626-0701-cycle3-dgu-scoped-negative-delta-receipt-classifier.md",
    "TAU": ROOT / "explorations/hourly-20260626-0701-cycle3-tau-dynamic-a-or-no-natural-slice-classifier.md",
    "KIG": ROOT / "explorations/hourly-20260626-0701-cycle3-kig-coderivative-trace-eliminator.md",
    "QFT": ROOT / "explorations/hourly-20260626-0701-cycle3-qft-source-branch-action-orbit-cocycle-candidate.md",
    "SYNTHESIS": ROOT / "explorations/hourly-20260626-0701-three-cycle-fifteen-hole-synthesis.md",
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


class Cycle3CloseoutAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.summaries = {name: extract_summary(path) for name, path in ARTIFACTS.items()}

    def test_route_artifacts_are_run_scoped_and_non_promotional(self) -> None:
        for name in ("DGU", "TAU", "KIG", "QFT"):
            summary = self.summaries[name]
            with self.subTest(name=name):
                self.assertEqual(summary["run_id"], RUN_ID)
                self.assertEqual(summary["cycle"], 3)
                self.assertTrue(summary["artifact_path"].startswith(f"explorations/{RUN_ID}-cycle3-"))
                self.assertFalse(summary["target_import_used"])
                self.assertFalse(summary["claim_status_consistency_triggered"])

    def test_dgu_negative_is_scoped_and_does_not_restart_proofs(self) -> None:
        dgu = self.summaries["DGU"]
        self.assertTrue(dgu["scoped_negative_delta_receipt_emitted"])
        self.assertFalse(dgu["global_no_go_claimed"])
        self.assertFalse(dgu["delta_packet_admitted"])
        self.assertFalse(dgu["sector_rule_id_present"])
        self.assertFalse(dgu["family_identity_evidence_present"])
        self.assertFalse(dgu["same_operator_witness_allowed"])
        self.assertFalse(dgu["proof_restart_allowed"])

    def test_tau_classifier_admits_no_branch_or_restart(self) -> None:
        tau = self.summaries["TAU"]
        self.assertTrue(tau["classifier_defined"])
        self.assertFalse(tau["branch2a_admitted"])
        self.assertFalse(tau["branch2b_admitted"])
        self.assertFalse(tau["branch3_forced"])
        self.assertFalse(tau["branch3_admitted"])
        self.assertFalse(tau["exact_gr_restart_allowed"])
        self.assertFalse(tau["theta_restart_allowed"])

    def test_kig_trace_eliminator_keeps_coderivative_alive(self) -> None:
        kig = self.summaries["KIG"]
        self.assertFalse(kig["coderivative_trace_eliminator_admitted"])
        self.assertFalse(kig["positive_exterior_degree_rule_present"])
        self.assertFalse(kig["coderivative_trace_eliminated"])
        self.assertEqual(kig["surviving_class_count"], len(kig["surviving_classes"]))
        self.assertIn("CODERIVATIVE_TRACE", kig["surviving_classes"])
        self.assertFalse(kig["d_a_u_source_forced"])
        self.assertFalse(kig["branch3_admitted"])

    def test_qft_action_cocycle_gate_uses_schema_only(self) -> None:
        qft = self.summaries["QFT"]
        self.assertTrue(qft["schema_category_available"])
        self.assertFalse(qft["source_action_defined"])
        self.assertFalse(qft["orbit_stabilizer_defined"])
        self.assertFalse(qft["cocycle_defined"])
        self.assertFalse(qft["hidden_branch_key_emitted"])
        self.assertFalse(qft["source_admissibility_predicate_emitted"])
        self.assertFalse(qft["carrier_work_allowed"])

    def test_synthesis_accounts_for_fifteen_holes_and_no_restarts(self) -> None:
        synthesis = self.summaries["SYNTHESIS"]
        self.assertEqual(synthesis["run_id"], RUN_ID)
        self.assertEqual(synthesis["target_quality_holes"], 15)
        self.assertEqual(synthesis["quality_holes_completed"], 15)
        self.assertEqual(synthesis["quality_holes_pending_integration"], 0)
        self.assertEqual(synthesis["schema_level_closes_count"], 1)
        self.assertEqual(synthesis["source_admissions_count"], 0)
        self.assertFalse(synthesis["proof_restart_allowed_any_route"])
        self.assertEqual(synthesis["new_source_or_proof_receipts_admitted"], 1)
        self.assertFalse(synthesis["claim_status_consistency_triggered"])
        self.assertFalse(synthesis["claim_promotion_allowed_any_route"])
        self.assertFalse(synthesis["target_import_used"])
        self.assertGreaterEqual(synthesis["candidate_bank_count"], 15)
        self.assertTrue(synthesis["three_cycle_wrapper_improved_quality"])
        self.assertTrue(synthesis["material_next_goal_refinement"])
        self.assertEqual(synthesis["cycle_commits"]["cycle1"], "beaed38")
        self.assertEqual(synthesis["cycle_commits"]["cycle2"], "c2339cf")


if __name__ == "__main__":
    unittest.main(verbosity=2)
