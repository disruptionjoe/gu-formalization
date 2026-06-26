"""Audit the 0904 cycle 1 frontier receipt artifacts."""

from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260626-0904"
ARTIFACTS = {
    "DGU": ROOT / "explorations/hourly-20260626-0904-cycle1-dgu-ucsd-visual-frame-rows.md",
    "TAU": ROOT / "explorations/hourly-20260626-0904-cycle1-tau-field-space-lock-or-eliminator.md",
    "KIG": ROOT / "explorations/hourly-20260626-0904-cycle1-kig-parent-variation-exterior-slot-receipt.md",
    "PRODUCT_AB": ROOT / "explorations/hourly-20260626-0904-cycle1-productab-branch-pure-ptuj-source-packet.md",
    "QFT": ROOT / "explorations/hourly-20260626-0904-cycle1-qft-cover-context-overlap-restriction-receipt.md",
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


class Cycle1FrontierReceiptsAudit(unittest.TestCase):
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
                self.assertFalse(summary["claim_status_change"])

    def test_dgu_visual_frame_receipt_keeps_restart_locked(self) -> None:
        dgu = self.summaries["DGU"]
        self.assertTrue(dgu["ucsd_visual_frame_lane_executed"])
        self.assertTrue(dgu["transcript_windows_present"])
        self.assertFalse(dgu["repo_local_visual_frame_assets_present"])
        self.assertFalse(dgu["frame_rows_admitted"])
        self.assertFalse(dgu["displayed_formula_transcribed"])
        self.assertFalse(dgu["sector_rule_id_present"])
        self.assertFalse(dgu["family_identity_evidence_present"])
        self.assertFalse(dgu["same_operator_witness_allowed"])
        self.assertFalse(dgu["proof_restart_allowed"])
        self.assertEqual(
            dgu["constructive_next_object"],
            "UCSDDGU01VisualFrameAssetManifestOrNegativeReceipt_V1",
        )

    def test_tau_lock_or_eliminator_remains_blocked(self) -> None:
        tau = self.summaries["TAU"]
        self.assertTrue(tau["field_space_lock_attempted"])
        self.assertTrue(tau["source_fixed_reference_present"])
        self.assertFalse(tau["action_field_space_lock_proved"])
        self.assertFalse(tau["fixed_reference_graph_eliminated"])
        self.assertFalse(tau["corrected_2a_admitted"])
        self.assertTrue(tau["corrected_2a_still_possible"])
        self.assertFalse(tau["dynamic_A_2b_forced"])
        self.assertFalse(tau["branch3_forced"])
        self.assertFalse(tau["exact_gr_restart_allowed"])
        self.assertFalse(tau["theta_restart_allowed"])

    def test_kig_parent_slot_receipt_does_not_eliminate_trace(self) -> None:
        kig = self.summaries["KIG"]
        self.assertTrue(kig["parent_variation_slot_receipt_attempted"])
        self.assertFalse(kig["source_independent_exterior_parent_slot_present"])
        self.assertFalse(kig["degree_P_IG_2_source_forced_before_codomain"])
        self.assertTrue(kig["conditional_exterior_candidate_present"])
        self.assertTrue(kig["rival_parent_classes_survive"])
        self.assertIn("CODERIVATIVE_TRACE", kig["surviving_parent_classes"])
        self.assertEqual(kig["first_blocking_rival"], "CODERIVATIVE_TRACE")
        self.assertFalse(kig["coderivative_trace_eliminated"])
        self.assertFalse(kig["trace_contraction_exclusion_allowed"])
        self.assertFalse(kig["branch3_admitted"])

    def test_product_ab_has_no_complete_ptuj_branch(self) -> None:
        product = self.summaries["PRODUCT_AB"]
        self.assertTrue(product["single_complete_ptuj_branch_attempted"])
        self.assertFalse(product["official_custodian_branch_complete"])
        self.assertFalse(product["lawful_local_branch_complete"])
        self.assertFalse(product["keating_sheet_branch_complete"])
        self.assertEqual(product["accepted_branch_count"], 0)
        self.assertFalse(product["formula_bearing_asset_present"])
        self.assertFalse(product["visible_formula_transcribed"])
        self.assertFalse(product["productab_member_emitted"])
        self.assertFalse(product["operator_member_id_present"])
        self.assertFalse(product["binding_gate_allowed"])

    def test_qft_cover_receipt_keeps_records_and_carrier_locked(self) -> None:
        qft = self.summaries["QFT"]
        self.assertTrue(qft["cover_context_receipt_attempted"])
        self.assertFalse(qft["source_labeled_contexts_present"])
        self.assertFalse(qft["cover_relation_present"])
        self.assertFalse(qft["pairwise_overlaps_present"])
        self.assertFalse(qft["triple_overlaps_present"])
        self.assertFalse(qft["restriction_maps_present"])
        self.assertFalse(qft["restriction_functoriality_present"])
        self.assertFalse(qft["local_branch_records_allowed"])
        self.assertFalse(qft["BrSch_checks_possible"])
        self.assertFalse(qft["carrier_work_allowed"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
