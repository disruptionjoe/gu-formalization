"""Audit the 0904 cycle 3 artifacts and synthesis."""

from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260626-0904"
ARTIFACTS = {
    "DGU": ROOT / "explorations/hourly-20260626-0904-cycle3-dgu-ucsd-frame-acquisition-preconditions.md",
    "TAU": ROOT / "explorations/hourly-20260626-0904-cycle3-tau-field-space-trichotomy.md",
    "KIG": ROOT / "explorations/hourly-20260626-0904-cycle3-kig-rival-parent-firewall.md",
    "PRODUCT_AB": ROOT / "explorations/hourly-20260626-0904-cycle3-productab-formula-visibility-prereq.md",
    "QFT": ROOT / "explorations/hourly-20260626-0904-cycle3-qft-cover-to-local-record-readiness.md",
    "SYNTHESIS": ROOT / "explorations/hourly-20260626-0904-three-cycle-fifteen-hole-synthesis.md",
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

    def test_cycle3_artifacts_are_run_scoped_and_non_promotional(self) -> None:
        for name in ["DGU", "TAU", "KIG", "PRODUCT_AB", "QFT"]:
            summary = self.summaries[name]
            with self.subTest(name=name):
                self.assertEqual(summary["run_id"], RUN_ID)
                self.assertEqual(summary["cycle"], 3)
                self.assertTrue(summary["artifact_path"].startswith(f"explorations/{RUN_ID}-cycle3-"))
                self.assertFalse(summary["target_import_used"])
                self.assertFalse(summary["claim_status_consistency_triggered"])
                self.assertFalse(summary["claim_status_change"])

    def test_dgu_precondition_matrix_locks_restart(self) -> None:
        dgu = self.summaries["DGU"]
        self.assertTrue(dgu["precondition_matrix_executed"])
        self.assertFalse(dgu["official_ucsd_still_branch_ready"])
        self.assertFalse(dgu["lawful_local_ucsd_video_branch_ready"])
        self.assertFalse(dgu["alternate_source_equivalent_branch_ready"])
        self.assertFalse(dgu["visual_row_retry_allowed"])
        self.assertFalse(dgu["sector_rule_retry_allowed"])
        self.assertFalse(dgu["same_operator_witness_allowed"])
        self.assertFalse(dgu["proof_restart_allowed"])
        self.assertTrue(dgu["sequential_next"])

    def test_tau_trichotomy_keeps_restarts_blocked(self) -> None:
        tau = self.summaries["TAU"]
        self.assertTrue(tau["trichotomy_table_executed"])
        self.assertFalse(tau["full_IG_free_beta_selected"])
        self.assertFalse(tau["fixed_aleph_graph_selected"])
        self.assertFalse(tau["dynamic_A_graph_selected"])
        self.assertTrue(tau["all_three_states_remain_logically_possible"])
        self.assertFalse(tau["corrected_2a_admitted"])
        self.assertFalse(tau["dynamic_A_2b_admitted"])
        self.assertFalse(tau["branch3_forced"])
        self.assertFalse(tau["exact_gr_restart_allowed"])
        self.assertFalse(tau["theta_restart_allowed"])

    def test_kig_firewall_blocks_trace_retry(self) -> None:
        kig = self.summaries["KIG"]
        self.assertTrue(kig["rival_parent_firewall_executed"])
        self.assertFalse(kig["positive_source_row_present_now"])
        self.assertTrue(kig["firewall_acceptance_fields_defined"])
        self.assertFalse(kig["coderivative_trace_eliminated"])
        self.assertFalse(kig["trace_eliminator_retry_allowed"])
        self.assertFalse(kig["branch3_admitted"])

    def test_product_ab_visibility_prereqs_are_absent(self) -> None:
        product = self.summaries["PRODUCT_AB"]
        self.assertTrue(product["formula_visibility_prereq_gate_executed"])
        self.assertFalse(product["content_access_or_source_bytes_present"])
        self.assertFalse(product["checksum_or_custody_present"])
        self.assertFalse(product["decode_output_manifest_present"])
        self.assertFalse(product["formula_visibility_scope_present"])
        self.assertFalse(product["formula_visibility_audit_allowed"])
        self.assertFalse(product["visible_formula_transcription_allowed"])
        self.assertFalse(product["productab_member_emitted"])
        self.assertFalse(product["binding_gate_allowed"])

    def test_qft_readiness_matrix_blocks_downstream(self) -> None:
        qft = self.summaries["QFT"]
        self.assertTrue(qft["readiness_matrix_executed"])
        self.assertFalse(qft["cover_declaration_ready"])
        self.assertFalse(qft["local_branch_record_receipt_ready"])
        self.assertFalse(qft["BrSch_checks_ready"])
        self.assertFalse(qft["transition_generator_ready"])
        self.assertFalse(qft["carrier_work_allowed"])

    def test_synthesis_integrates_fifteen_holes(self) -> None:
        synthesis = self.summaries["SYNTHESIS"]
        self.assertEqual(synthesis["run_id"], RUN_ID)
        self.assertEqual(synthesis["target_quality_holes"], 15)
        self.assertEqual(synthesis["quality_holes_completed"], 15)
        self.assertEqual(synthesis["source_admissions_count"], 0)
        self.assertEqual(synthesis["claim_promotions"], 0)
        self.assertFalse(synthesis["claim_status_consistency_triggered"])
        self.assertFalse(synthesis["proof_restart_allowed_any_route"])
        self.assertFalse(synthesis["target_import_used"])
        self.assertEqual(len(synthesis["cycle3_next_frontier"]), 5)
        self.assertEqual(len(synthesis["sequential_next_lanes"]), 5)
        self.assertTrue(synthesis["three_cycle_wrapper_improved_quality"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
