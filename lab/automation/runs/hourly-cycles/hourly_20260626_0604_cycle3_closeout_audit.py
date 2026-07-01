"""Audit the 0604 cycle 3 closeout and synthesis artifacts."""

from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260626-0604"
ARTIFACTS = {
    "STATE": ROOT / "explorations/hourly-20260626-0604-cycle3-source-admission-state-machine.md",
    "RS": ROOT / "explorations/hourly-20260626-0604-cycle3-rs-image-delta-intake-closeout.md",
    "READINESS": ROOT / "explorations/hourly-20260626-0604-cycle3-proof-restart-readiness-matrix.md",
    "FRONTIER": ROOT / "explorations/hourly-20260626-0604-cycle3-next-frontier-sequencing-matrix.md",
    "SYNTHESIS": ROOT / "explorations/hourly-20260626-0604-three-cycle-fifteen-hole-synthesis.md",
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

    def test_all_artifacts_are_run_scoped_and_non_promotional(self) -> None:
        for name, summary in self.summaries.items():
            with self.subTest(name=name):
                self.assertEqual(summary["run_id"], RUN_ID)
                self.assertFalse(summary["target_import_used"])
                self.assertFalse(summary["claim_status_consistency_triggered"])

    def test_state_machine_has_zero_admissions(self) -> None:
        state = self.summaries["STATE"]
        self.assertTrue(state["state_machine_defined"])
        self.assertEqual(state["source_admissions_count"], 0)
        self.assertFalse(state["proof_restart_allowed_any_route"])
        self.assertEqual(state["route_states"]["DGU"], "predicate_defined_no_row")

    def test_rs_image_delta_does_not_change_receipt_state(self) -> None:
        rs = self.summaries["RS"]
        self.assertTrue(rs["new_image_artifacts_accounted"])
        self.assertFalse(rs["image_delta_changes_0711_verdict"])
        self.assertFalse(rs["rs_receipt_admitted"])
        self.assertFalse(rs["dgu_row_admitted_from_images"])
        self.assertFalse(rs["proof_restart_allowed"])

    def test_readiness_matrix_locks_all_routes(self) -> None:
        readiness = self.summaries["READINESS"]
        self.assertFalse(readiness["proof_restart_allowed_any_route"])
        self.assertFalse(readiness["claim_promotion_allowed"])
        self.assertFalse(readiness["claim_demotion_required"])
        self.assertEqual(readiness["accepted_receipt_count"], 0)
        self.assertGreaterEqual(len(readiness["locked_routes"]), 6)

    def test_frontier_has_large_candidate_bank_and_no_downstream_parallelism(self) -> None:
        frontier = self.summaries["FRONTIER"]
        self.assertGreaterEqual(frontier["candidate_bank_count"], 18)
        self.assertTrue(frontier["parallel_source_intake_allowed"])
        self.assertFalse(frontier["downstream_proof_parallelism_allowed"])
        self.assertTrue(frontier["sequential_integration_required"])
        self.assertIn("PositivePrimarySourceDGU01SectorRuleRowCandidate_V1", frontier["ranked_next_frontier"])

    def test_synthesis_accounts_for_fifteen_holes(self) -> None:
        synthesis = self.summaries["SYNTHESIS"]
        self.assertEqual(synthesis["target_quality_holes"], 15)
        self.assertEqual(synthesis["quality_holes_completed"], 15)
        self.assertEqual(synthesis["source_admissions_count"], 0)
        self.assertEqual(synthesis["new_source_or_proof_receipts_admitted"], 0)
        self.assertFalse(synthesis["proof_restart_allowed_any_route"])
        self.assertFalse(synthesis["claim_promotion_allowed_any_route"])
        self.assertGreaterEqual(synthesis["candidate_bank_count"], 18)
        self.assertTrue(synthesis["three_cycle_wrapper_improved_quality"])
        self.assertTrue(synthesis["material_next_goal_refinement"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
