"""Audit the 1302 cycle 3 specs and synthesis."""

from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260626-1302"
ARTIFACTS = {
    "DGU": ROOT / "explorations/hourly-20260626-1302-cycle3-dgu-route-decision-receipt-spec.md",
    "TAU": ROOT / "explorations/hourly-20260626-1302-cycle3-tau-action-field-space-declaration-spec.md",
    "KIG": ROOT / "explorations/hourly-20260626-1302-cycle3-kig-source-window-order-log-spec.md",
    "PRODUCT_AB": ROOT / "explorations/hourly-20260626-1302-cycle3-productab-content-route-custody-basis-spec.md",
    "QFT": ROOT / "explorations/hourly-20260626-1302-cycle3-qft-source-anchor-triad-receipt-spec.md",
    "SYNTHESIS": ROOT / "explorations/hourly-20260626-1302-three-cycle-fifteen-hole-synthesis.md",
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
                self.assertFalse(summary["claim_status_change"])

    def test_dgu_route_decision_receipt_is_spec_only(self) -> None:
        dgu = self.summaries["DGU"]
        self.assertTrue(dgu["route_decision_receipt_spec_defined"])
        self.assertFalse(dgu["route_decision_receipt_present"])
        self.assertFalse(dgu["selected_route_present"])
        self.assertFalse(dgu["byte_acquisition_execution_allowed"])
        self.assertEqual(dgu["constructive_next_object"], "UCSDDGU01LawfulAcquisitionRouteDecisionReceipt_V1")

    def test_tau_action_field_space_declaration_is_spec_only(self) -> None:
        tau = self.summaries["TAU"]
        self.assertTrue(tau["action_field_space_declaration_spec_defined"])
        self.assertFalse(tau["action_field_space_declaration_present"])
        self.assertFalse(tau["fixed_aleph_graph_selected_as_action_domain"])
        self.assertFalse(tau["field_space_theorem_allowed"])
        self.assertEqual(tau["constructive_next_object"], "TauFixedAlephActionFieldSpaceDeclaration_V1")

    def test_kig_order_log_is_spec_only(self) -> None:
        kig = self.summaries["KIG"]
        self.assertTrue(kig["source_window_order_log_spec_defined"])
        self.assertFalse(kig["source_window_order_log_present"])
        self.assertFalse(kig["pre_codomain_order_proved"])
        self.assertFalse(kig["source_row_admission_allowed"])
        self.assertEqual(kig["first_blocking_rival"], "CODERIVATIVE_TRACE")

    def test_productab_content_route_receipt_is_spec_only(self) -> None:
        product = self.summaries["PRODUCT_AB"]
        self.assertTrue(product["content_route_custody_receipt_spec_defined"])
        self.assertFalse(product["content_route_custody_receipt_present"])
        self.assertFalse(product["official_content_route_present"])
        self.assertFalse(product["visibility_scope_allowed"])
        self.assertEqual(product["constructive_next_object"], "OfficialTzSEvmqxu48ContentRouteAndCustodyBasisReceipt_V1")

    def test_qft_anchor_triad_receipt_is_spec_only(self) -> None:
        qft = self.summaries["QFT"]
        self.assertTrue(qft["source_anchor_triad_receipt_spec_defined"])
        self.assertFalse(qft["source_anchor_triad_receipt_present"])
        self.assertFalse(qft["roles_type_over_same_context"])
        self.assertFalse(qft["same_context_candidate_allowed"])
        self.assertEqual(qft["constructive_next_object"], "QFTSameContextSourceAnchorTriadReceipt_V1")

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
        self.assertEqual(synthesis["cycle_commits"]["cycle1"], "be824ea")
        self.assertEqual(synthesis["cycle_commits"]["cycle2"], "0b8342b")
        self.assertEqual(synthesis["cycle_commits"]["cycle3"], "pending_main_thread")
        self.assertGreaterEqual(synthesis["candidate_bank_size"], 18)
        self.assertEqual(len(synthesis["cycle3_next_frontier"]), 5)
        self.assertEqual(len(synthesis["sequential_next_lanes"]), 5)
        self.assertTrue(synthesis["three_cycle_wrapper_improved_quality"])
        self.assertTrue(synthesis["material_next_goal_refinement"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
