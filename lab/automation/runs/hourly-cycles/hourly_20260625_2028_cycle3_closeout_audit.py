"""Audit the 2028 cycle 3 closeout and synthesis artifacts."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260625-2028"
CYCLE3 = {
    "readiness": ROOT / "explorations/hourly-20260625-2028-cycle3-proof-restart-readiness-classifier.md",
    "transition": ROOT / "explorations/hourly-20260625-2028-cycle3-receipt-transition-matrix.md",
    "global_negative": ROOT / "explorations/hourly-20260625-2028-cycle3-global-negative-precondition-matrix.md",
    "promotion": ROOT / "explorations/hourly-20260625-2028-cycle3-claim-promotion-firewall.md",
    "next_frontier": ROOT / "explorations/hourly-20260625-2028-cycle3-next-frontier-dependency-dag.md",
}
SYNTHESIS = ROOT / "explorations/hourly-20260625-2028-three-cycle-fifteen-hole-synthesis.md"


def extract_summary(path: Path, section: str = "Machine-readable JSON summary") -> dict:
    text = path.read_text(encoding="utf-8")
    match = re.search(
        rf"## [0-9]+\. {re.escape(section)}\s*```json\s*(\{{.*?\}})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError(f"missing JSON summary in {path}")
    return json.loads(match.group(1))


class Cycle3CloseoutAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cycle3 = {name: extract_summary(path) for name, path in CYCLE3.items()}
        cls.synthesis = extract_summary(SYNTHESIS)

    def test_cycle3_core_guards(self) -> None:
        for name, summary in self.cycle3.items():
            with self.subTest(name=name):
                self.assertEqual(summary["run_id"], RUN_ID)
                self.assertEqual(summary["cycle"], 3)
                self.assertEqual(summary["accepted_receipt_count"], 0)
                self.assertFalse(summary["proof_restart_allowed"])
                self.assertFalse(summary["claim_promotion_allowed"])
                self.assertFalse(summary["target_import_used"])
                self.assertFalse(summary["claim_status_consistency_triggered"])

    def test_cycle3_specific_decisions(self) -> None:
        self.assertEqual(self.cycle3["readiness"]["routes_ready_count"], 0)
        self.assertEqual(self.cycle3["transition"]["accepted_transition_count"], 0)
        self.assertFalse(self.cycle3["global_negative"]["global_no_go_promoted"])
        self.assertFalse(self.cycle3["promotion"]["status_change_proposed"])
        self.assertEqual(len(self.cycle3["next_frontier"]["recommended_next_five"]), 5)

    def test_synthesis_run_level_decision(self) -> None:
        decision = self.synthesis["run_level_decision"]
        self.assertEqual(decision["accepted_receipt_count"], 0)
        self.assertEqual(decision["accepted_for_routing_count"], 0)
        self.assertEqual(decision["routes_ready_count"], 0)
        self.assertFalse(decision["proof_restart_allowed"])
        self.assertFalse(decision["claim_promotion_allowed"])
        self.assertFalse(decision["global_no_go_promoted"])
        self.assertFalse(decision["target_import_used"])
        self.assertFalse(decision["downstream_replay_allowed"])

    def test_synthesis_counts_and_commits(self) -> None:
        self.assertEqual(self.synthesis["result_counts"]["hole_count"], 15)
        self.assertEqual(self.synthesis["result_counts"]["accepted_receipts"], 0)
        self.assertEqual(self.synthesis["result_counts"]["underdefined"], 2)
        self.assertEqual(self.synthesis["cycle_commits"]["cycle_1"], "a8296ed")
        self.assertEqual(self.synthesis["cycle_commits"]["cycle_2"], "f4dd6db")
        self.assertEqual(self.synthesis["cycle_commits"]["cycle_3"], "pending_parent_commit")
        self.assertEqual(len(self.synthesis["recommended_next_five"]), 5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
