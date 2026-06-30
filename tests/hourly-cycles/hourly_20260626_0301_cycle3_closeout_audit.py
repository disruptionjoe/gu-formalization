"""Audit the 0301 cycle 3 closeouts and three-cycle synthesis."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260626-0301"
ARTIFACTS = {
    "IG": ROOT / "explorations/hourly-20260626-0301-cycle3-ig-source-operator-transition-closeout.md",
    "RS": ROOT / "explorations/hourly-20260626-0301-cycle3-rs-frame-evidence-transition-closeout.md",
    "PTUJ": ROOT / "explorations/hourly-20260626-0301-cycle3-ptuj-branch-packet-transition-closeout.md",
    "DGU": ROOT / "explorations/hourly-20260626-0301-cycle3-dgu-primary-row-transition-closeout.md",
    "QFT": ROOT / "explorations/hourly-20260626-0301-cycle3-qft-branch-row-transition-closeout.md",
    "SYNTHESIS": ROOT / "explorations/hourly-20260626-0301-three-cycle-fifteen-hole-synthesis.md",
}


def extract_summary(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    blocks = re.findall(r"```json\s*(\{.*?\})\s*```", text, flags=re.DOTALL)
    if not blocks:
        raise AssertionError(f"missing JSON summary in {path}")
    return json.loads(blocks[-1])


class Cycle3CloseoutAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.summaries = {route: extract_summary(path) for route, path in ARTIFACTS.items()}

    def test_route_closeouts_are_run_scoped_and_consume_prior_cycles(self) -> None:
        for route in ("IG", "RS", "PTUJ", "DGU", "QFT"):
            summary = self.summaries[route]
            with self.subTest(route=route):
                self.assertEqual(summary["run_id"], RUN_ID)
                self.assertEqual(summary["cycle"], 3)
                self.assertTrue(summary["artifact_path"].startswith(f"explorations/{RUN_ID}-cycle3-"))
                self.assertTrue(summary["cycle1_consumed"])
                self.assertTrue(summary["cycle2_consumed"])
                self.assertFalse(summary["target_import_used"])
                self.assertFalse(summary["claim_status_consistency_triggered"])
                self.assertFalse(summary["proof_restart_allowed"])
                self.assertIn("next_frontier_object", summary)

    def test_rs_and_ig_closeouts_block_restart(self) -> None:
        rs = self.summaries["RS"]
        self.assertEqual(rs["accepted_evidence_branch_count"], 0)
        self.assertFalse(rs["first_frame_receipt_admitted"])
        self.assertFalse(rs["frame_manifest_allowed"])
        self.assertFalse(rs["typed_rs_intake_allowed"])
        self.assertEqual(rs["next_frontier_object"], "RSImmutableExternalFramePackage_V1")
        self.assertTrue(rs["next_rs_work_must_be_sequential"])

        ig = self.summaries["IG"]
        self.assertFalse(ig["source_operator_locator_found"])
        self.assertFalse(ig["source_natural_projector_identity_admitted"])
        self.assertFalse(ig["coefficient_derivation_allowed"])
        self.assertFalse(ig["selector_restart_allowed"])
        self.assertTrue(ig["ig_must_be_sequential_before_further_proof_work"])
        self.assertEqual(
            ig["next_frontier_object"],
            "ProductABSourceOperatorSourceLocatorReceipt_V1 -> SourceNaturalProductABRivalProjectorIdentity_V1",
        )

    def test_ptuj_dgu_qft_closeouts_block_downstream_work(self) -> None:
        ptuj = self.summaries["PTUJ"]
        self.assertEqual(ptuj["accepted_branch_count"], 0)
        self.assertFalse(ptuj["branch_purity_invariant_satisfied"])
        self.assertFalse(ptuj["formula_visibility_allowed"])
        self.assertFalse(ptuj["identity_comparison_allowed"])
        self.assertTrue(ptuj["ptuj_must_be_sequential_before_formula_work"])

        dgu = self.summaries["DGU"]
        self.assertFalse(dgu["primary_row_payload_found"])
        self.assertFalse(dgu["actual_operator_handle_found"])
        self.assertFalse(dgu["same_operator_witness_evaluable"])
        self.assertFalse(dgu["symbol_certificate_allowed"])
        self.assertFalse(dgu["vz_replay_allowed"])
        self.assertTrue(dgu["dgu_must_be_sequential_before_symbol_vz"])

        qft = self.summaries["QFT"]
        self.assertFalse(qft["branch_row_provenance_packet_admitted"])
        self.assertFalse(qft["carrier_assignment_allowed"])
        self.assertFalse(qft["Y_b_branch_selected"])
        self.assertFalse(qft["local_groupoid_allowed"])
        self.assertFalse(qft["quotient_descent_allowed"])
        self.assertTrue(qft["host_infrastructure_as_selector_rejected"])
        self.assertTrue(qft["qft_must_be_sequential_before_carrier_work"])

    def test_synthesis_records_fifteen_holes_and_no_receipts(self) -> None:
        syn = self.summaries["SYNTHESIS"]
        self.assertEqual(syn["run_id"], RUN_ID)
        self.assertEqual(syn["target_quality_holes"], 15)
        self.assertEqual(syn["quality_holes_completed"], 15)
        self.assertFalse(syn["target_import_used"])
        self.assertFalse(syn["claim_status_consistency_triggered"])
        self.assertFalse(syn["claim_promotion_allowed_any_route"])
        self.assertFalse(syn["proof_restart_allowed_any_route"])
        self.assertEqual(syn["new_route_local_receipts_admitted"], 0)
        self.assertEqual(syn["new_source_or_proof_receipts_admitted"], 0)
        self.assertEqual(syn["new_blocker_refinements"], 15)
        self.assertEqual(syn["rs_accepted_evidence_branch_count"], 0)
        self.assertEqual(len(syn["next_frontier_ranked"]), 5)
        self.assertTrue(syn["sequential_within_route_required"])
        self.assertTrue(syn["parallel_across_routes_allowed"])
        self.assertTrue(syn["three_cycle_wrapper_improved_quality"])
        self.assertTrue(syn["material_next_goal_refinement"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
