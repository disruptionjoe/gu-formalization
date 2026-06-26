"""Audit the 0904 cycle 2 source declaration artifacts."""

from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260626-0904"
ARTIFACTS = {
    "DGU": ROOT / "explorations/hourly-20260626-0904-cycle2-dgu-visual-frame-asset-manifest.md",
    "TAU": ROOT / "explorations/hourly-20260626-0904-cycle2-tau-action-field-space-statement.md",
    "KIG": ROOT / "explorations/hourly-20260626-0904-cycle2-kig-parent-slot-source-row.md",
    "PRODUCT_AB": ROOT / "explorations/hourly-20260626-0904-cycle2-productab-ptuj-acquisition-manifest.md",
    "QFT": ROOT / "explorations/hourly-20260626-0904-cycle2-qft-source-context-cover-declaration.md",
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


class Cycle2SourceDeclarationsAudit(unittest.TestCase):
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
                self.assertFalse(summary["claim_status_change"])

    def test_dgu_manifest_is_negative_and_keeps_witness_locked(self) -> None:
        dgu = self.summaries["DGU"]
        self.assertTrue(dgu["visual_asset_manifest_attempted"])
        self.assertFalse(dgu["source_video_object_present"])
        self.assertFalse(dgu["official_still_rows_present"])
        self.assertFalse(dgu["extracted_frame_manifest_present"])
        self.assertFalse(dgu["frame_checksums_present"])
        self.assertFalse(dgu["visual_transcription_rows_present"])
        self.assertFalse(dgu["manifest_admitted"])
        self.assertTrue(dgu["negative_manifest_receipt_emitted"])
        self.assertFalse(dgu["sector_rule_retry_allowed"])
        self.assertFalse(dgu["same_operator_witness_allowed"])
        self.assertFalse(dgu["proof_restart_allowed"])

    def test_tau_trichotomy_is_unselected(self) -> None:
        tau = self.summaries["TAU"]
        self.assertTrue(tau["action_field_space_statement_attempted"])
        self.assertFalse(tau["full_IG_free_beta_source_selected"])
        self.assertFalse(tau["fixed_aleph_graph_source_selected"])
        self.assertFalse(tau["dynamic_A_graph_source_selected"])
        self.assertFalse(tau["field_space_statement_admitted"])
        self.assertFalse(tau["corrected_2a_admitted"])
        self.assertFalse(tau["corrected_2a_eliminated"])
        self.assertFalse(tau["dynamic_A_2b_admitted"])
        self.assertFalse(tau["branch3_forced"])
        self.assertTrue(tau["sequential_only_next"])

    def test_kig_parent_slot_source_row_absent(self) -> None:
        kig = self.summaries["KIG"]
        self.assertTrue(kig["parent_slot_source_row_gate_attempted"])
        self.assertFalse(kig["branch3_parent_slot_source_row_present"])
        self.assertTrue(kig["negative_parent_slot_receipt_emitted"])
        self.assertFalse(kig["degree_P_IG_2_source_forced_before_codomain"])
        self.assertFalse(kig["non_2_form_parent_slots_source_excluded"])
        self.assertFalse(kig["coderivative_trace_eliminated"])
        self.assertFalse(kig["trace_eliminator_retry_allowed"])
        self.assertFalse(kig["branch3_admitted"])

    def test_product_ab_acquisition_manifest_absent(self) -> None:
        product = self.summaries["PRODUCT_AB"]
        self.assertTrue(product["ptuj_acquisition_manifest_attempted"])
        self.assertFalse(product["official_branch_manifest_present"])
        self.assertFalse(product["lawful_local_branch_manifest_present"])
        self.assertFalse(product["keating_sheet_manifest_present"])
        self.assertFalse(product["decoded_output_manifest_present"])
        self.assertFalse(product["frame_checksums_present"])
        self.assertFalse(product["formula_visibility_scope_present"])
        self.assertFalse(product["acquisition_manifest_admitted"])
        self.assertFalse(product["formula_visibility_audit_allowed"])
        self.assertFalse(product["productab_member_emitted"])

    def test_qft_cover_declaration_is_negative(self) -> None:
        qft = self.summaries["QFT"]
        self.assertTrue(qft["source_context_cover_declaration_attempted"])
        self.assertFalse(qft["source_context_locator_present"])
        self.assertFalse(qft["cover_index_set_present"])
        self.assertFalse(qft["source_labeled_contexts_present"])
        self.assertFalse(qft["cover_relation_present"])
        self.assertFalse(qft["restriction_domains_typable"])
        self.assertTrue(qft["negative_cover_declaration_receipt_emitted"])
        self.assertFalse(qft["local_branch_record_receipt_allowed"])
        self.assertFalse(qft["transition_generator_allowed"])
        self.assertFalse(qft["carrier_work_allowed"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
