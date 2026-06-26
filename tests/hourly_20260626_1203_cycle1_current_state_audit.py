"""Audit the 1203 cycle 1 current-state frontier artifacts."""

from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260626-1203"
ARTIFACTS = {
    "DGU": ROOT / "explorations/hourly-20260626-1203-cycle1-dgu-custody-packet-current-state.md",
    "TAU": ROOT / "explorations/hourly-20260626-1203-cycle1-tau-fixed-aleph-packet-attempt.md",
    "KIG": ROOT / "explorations/hourly-20260626-1203-cycle1-kig-pre-codomain-row-current-state.md",
    "PRODUCT_AB": ROOT / "explorations/hourly-20260626-1203-cycle1-productab-formula-source-object-current-state.md",
    "QFT": ROOT / "explorations/hourly-20260626-1203-cycle1-qft-same-context-edge-current-state.md",
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


class Cycle1CurrentStateAudit(unittest.TestCase):
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
                self.assertFalse(summary["claim_status_change"])

    def test_dgu_custody_packet_is_absent_and_retries_locked(self) -> None:
        dgu = self.summaries["DGU"]
        self.assertFalse(dgu["custody_packet_instance_present"])
        self.assertFalse(dgu["source_byte_path_present"])
        self.assertFalse(dgu["sha256_present"])
        self.assertFalse(dgu["lawful_basis_present"])
        self.assertFalse(dgu["custody_record_present"])
        self.assertFalse(dgu["extraction_policy_present"])
        self.assertFalse(dgu["producer_positive_rerun_allowed"])
        self.assertFalse(dgu["frame_retry_allowed"])
        self.assertFalse(dgu["same_operator_retry_allowed"])
        self.assertEqual(dgu["constructive_next_object"], "LawfulLocalUCSDDGU01CustodyPacketAdmissionVerifier_V1")

    def test_tau_fixed_aleph_packet_is_only_a_scaffold(self) -> None:
        tau = self.summaries["TAU"]
        self.assertTrue(tau["packet_candidate_scaffolded"])
        self.assertFalse(tau["packet_complete"])
        self.assertFalse(tau["source_selected_branch_mode_present"])
        self.assertTrue(tau["graph_equation_available_as_candidate"])
        self.assertFalse(tau["field_space_theorem_present"])
        self.assertFalse(tau["tangent_certificate_present"])
        self.assertFalse(tau["D_A_Phi_tau_zero_proved"])
        self.assertFalse(tau["full_EL_tuple_present"])
        self.assertFalse(tau["exact_gr_restart_allowed"])
        self.assertFalse(tau["theta_restart_allowed"])

    def test_kig_pre_codomain_source_row_absent(self) -> None:
        kig = self.summaries["KIG"]
        self.assertFalse(kig["source_row_present"])
        self.assertFalse(kig["parent_slot_pre_codomain_found"])
        self.assertFalse(kig["degree_pig_2_pre_operator_found"])
        self.assertFalse(kig["rival_parent_classes_closed"])
        self.assertFalse(kig["source_selected_branch3_admitted"])
        self.assertFalse(kig["trace_eliminator_retry_allowed"])
        self.assertEqual(kig["first_blocking_rival"], "CODERIVATIVE_TRACE")
        self.assertIn("CODERIVATIVE_TRACE", kig["surviving_parent_classes"])

    def test_productab_formula_source_object_absent(self) -> None:
        product = self.summaries["PRODUCT_AB"]
        self.assertTrue(product["official_ptuj_locator_present"])
        self.assertEqual(product["video_id"], "TzSEvmqxu48")
        self.assertFalse(product["formula_bearing_source_object_present"])
        self.assertFalse(product["source_bytes_or_official_asset_present"])
        self.assertFalse(product["checksum_or_custody_present"])
        self.assertFalse(product["formula_visibility_scope_present"])
        self.assertFalse(product["visible_formula_transcription_allowed"])
        self.assertFalse(product["productab_member_emitted"])
        self.assertFalse(product["productab_kig_restart_allowed"])

    def test_qft_same_context_edge_absent(self) -> None:
        qft = self.summaries["QFT"]
        self.assertFalse(qft["same_context_edge_present"])
        self.assertFalse(qft["source_context_locator_found"])
        self.assertFalse(qft["cover_vocabulary_authorized"])
        self.assertFalse(qft["admissibility_authority_found"])
        self.assertFalse(qft["dependency_DAG_positive_instance_present"])
        self.assertFalse(qft["qft_cover_declaration_retry_allowed"])
        self.assertFalse(qft["local_records_unlocked"])
        self.assertFalse(qft["brsch_checks_unlocked"])
        self.assertFalse(qft["carrier_work_allowed"])


if __name__ == "__main__":
    unittest.main(verbosity=2)

