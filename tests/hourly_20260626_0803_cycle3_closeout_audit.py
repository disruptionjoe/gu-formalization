"""Audit the 0803 cycle 3 artifacts and three-cycle synthesis."""

from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260626-0803"
ARTIFACTS = {
    "DGU": ROOT / "explorations/hourly-20260626-0803-cycle3-dgu-binding-producer.md",
    "TAU": ROOT / "explorations/hourly-20260626-0803-cycle3-tau-corrected-2a-reference-graph-gate.md",
    "KIG": ROOT / "explorations/hourly-20260626-0803-cycle3-kig-parent-degree-selector.md",
    "PRODUCT_AB": ROOT / "explorations/hourly-20260626-0803-cycle3-productab-ptuj-frame-manuscript-check.md",
    "QFT": ROOT / "explorations/hourly-20260626-0803-cycle3-qft-descent-cover-local-record-inventory.md",
    "SYNTHESIS": ROOT / "explorations/hourly-20260626-0803-three-cycle-fifteen-hole-synthesis.md",
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

    def test_dgu_binding_producer_keeps_restart_locked(self) -> None:
        dgu = self.summaries["DGU"]
        self.assertTrue(dgu["binding_producer_executed"])
        self.assertFalse(dgu["positive_delta_packet_admitted"])
        self.assertTrue(dgu["negative_v4_emitted"])
        self.assertFalse(dgu["sector_rule_id_present"])
        self.assertFalse(dgu["family_identity_evidence_present"])
        self.assertFalse(dgu["binding_accepted"])
        self.assertFalse(dgu["same_operator_witness_allowed"])
        self.assertFalse(dgu["proof_restart_allowed"])
        self.assertEqual(
            dgu["exact_next_source_component"],
            "UCSDVisualFrameRows_DGU01_003246_003613_004916_005009_V1",
        )

    def test_tau_corrected_2a_is_blocked_not_eliminated(self) -> None:
        tau = self.summaries["TAU"]
        self.assertTrue(tau["corrected_2a_gate_executed"])
        self.assertFalse(tau["corrected_2a_admitted"])
        self.assertFalse(tau["corrected_2a_eliminated"])
        self.assertFalse(tau["action_field_space_lock_proved"])
        self.assertTrue(tau["D_A_Phi_zero_proved"])
        self.assertTrue(tau["K_beta_proper_proved"])
        self.assertTrue(tau["nonzero_theta_allowed"])
        self.assertFalse(tau["branch3_forced"])
        self.assertFalse(tau["exact_gr_restart_allowed"])
        self.assertFalse(tau["theta_restart_allowed"])
        self.assertEqual(tau["constructive_next_object"], "TauAlephGraphFieldSpaceLockOrEliminator_V1")

    def test_kig_parent_degree_selector_is_not_admitted(self) -> None:
        kig = self.summaries["KIG"]
        self.assertTrue(kig["parent_degree_selector_executed"])
        self.assertFalse(kig["parent_degree_selector_admitted"])
        self.assertFalse(kig["degree_P_IG_2_source_forced"])
        self.assertFalse(kig["independent_of_selected_codomain"])
        self.assertFalse(kig["trace_contraction_exclusion_allowed"])
        self.assertFalse(kig["coderivative_trace_eliminated"])
        self.assertFalse(kig["branch3_admitted"])
        self.assertEqual(kig["constructive_next_object"], "TauPlusParentVariationExteriorSlotReceiptForK_IG_V1")

    def test_product_ab_frame_check_blocks_on_missing_asset(self) -> None:
        product = self.summaries["PRODUCT_AB"]
        self.assertTrue(product["frame_check_executed"])
        self.assertFalse(product["formula_bearing_asset_present"])
        self.assertFalse(product["stable_locator_present"])
        self.assertFalse(product["visible_formula_transcribed"])
        self.assertFalse(product["manuscript_identity_checked"])
        self.assertFalse(product["productab_member_emitted"])
        self.assertFalse(product["operator_member_id_present"])
        self.assertTrue(product["acquisition_receipt_emitted"])
        self.assertFalse(product["locator_receipt_allowed"])
        self.assertFalse(product["binding_gate_allowed"])
        self.assertEqual(
            product["constructive_next_acquisition_object"],
            "one_complete_branch_pure_PTUJ_source_packet_for_SingleCompletePTUJBranchReceipt_V1",
        )

    def test_qft_cover_inventory_is_negative(self) -> None:
        qft = self.summaries["QFT"]
        self.assertTrue(qft["descent_cover_inventory_executed"])
        self.assertFalse(qft["source_cover_present"])
        self.assertFalse(qft["overlaps_present"])
        self.assertFalse(qft["restriction_maps_present"])
        self.assertFalse(qft["local_records_present"])
        self.assertFalse(qft["BrSch_checks_possible"])
        self.assertTrue(qft["transition_generator_placeholder_present"])
        self.assertTrue(qft["negative_cover_inventory_emitted"])
        self.assertFalse(qft["carrier_work_allowed"])
        self.assertEqual(
            qft["constructive_next_object"],
            "QFTSourceCoverContextAndOverlapRestrictionReceipt_V1",
        )

    def test_synthesis_integrates_all_fifteen_without_restart(self) -> None:
        synthesis = self.summaries["SYNTHESIS"]
        self.assertEqual(synthesis["run_id"], RUN_ID)
        self.assertEqual(synthesis["target_quality_holes"], 15)
        self.assertEqual(synthesis["quality_holes_completed"], 15)
        self.assertEqual(synthesis["source_admissions_count"], 0)
        self.assertEqual(synthesis["positive_delta_packets"], 0)
        self.assertFalse(synthesis["proof_restart_allowed_any_route"])
        self.assertFalse(synthesis["target_import_used"])
        self.assertFalse(synthesis["claim_status_consistency_triggered"])
        self.assertEqual(synthesis["claim_promotions"], 0)
        self.assertTrue(synthesis["three_cycle_wrapper_improved_quality"])
        self.assertEqual(len(synthesis["cycle3_next_frontier"]), 5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
