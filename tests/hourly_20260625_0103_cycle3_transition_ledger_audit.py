#!/usr/bin/env python3
"""Audit the completed cycle-3 transition ledger."""

from __future__ import annotations

import json
import unittest
from collections import Counter
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
LEDGER = REPO_ROOT / "explorations" / "hourly-20260625-0103-cycle3-transition-ledger.json"
LOCKED_FIELDS = {
    "row_id",
    "item_id",
    "session_id",
    "cycle_index",
    "worker_id",
    "owned_artifact_path",
    "owned_audit_path",
}


def load_ledger() -> dict:
    return json.loads(LEDGER.read_text(encoding="utf-8"))


class Cycle3TransitionLedgerAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.ledger = load_ledger()

    def test_completed_shape_and_gate(self) -> None:
        ledger = self.ledger
        self.assertEqual(ledger["ledger_version"], "CycleLocalTransitionLedger_3_1_5_4_V1")
        self.assertEqual(ledger["run_id"], "hourly-20260625-0103")
        self.assertEqual(ledger["cycle_index"], 3)
        self.assertIs(ledger["synthesis_allowed"], True)
        self.assertEqual(len(ledger["pre_rows"]), 5)
        self.assertEqual(len(ledger["post_rows"]), 5)
        self.assertEqual(len(ledger["classifier_results"]), 5)
        gate = ledger["acceptance_gate"]
        self.assertEqual(gate["status"], "passed")
        self.assertIs(gate["identity_links_valid"], True)
        self.assertIs(gate["locked_pre_rows_overwritten"], False)
        self.assertIs(gate["process_metrics_separated_from_gu_claims"], True)

    def test_identity_links_and_guard_declarations(self) -> None:
        pre_by_id = {row["row_id"]: row for row in self.ledger["pre_rows"]}
        post_by_id = {row["row_id"]: row for row in self.ledger["post_rows"]}
        self.assertEqual(set(pre_by_id), set(post_by_id))
        for row_id, pre in pre_by_id.items():
            post = post_by_id[row_id]
            for field in LOCKED_FIELDS:
                self.assertEqual(post[field], pre[field], f"{row_id}:{field}")
            self.assertFalse(post["guard_declarations"]["same_session_closure_attempted"])
            self.assertFalse(post["guard_declarations"]["target_import_detected"])
            self.assertFalse(post["guard_declarations"]["required_object_already_present"])

    def test_owned_paths_exist(self) -> None:
        for row in self.ledger["pre_rows"]:
            self.assertTrue((REPO_ROOT / row["owned_artifact_path"]).exists())
            self.assertTrue((REPO_ROOT / row["owned_audit_path"]).exists())

    def test_classifier_counts_are_upgrade_without_closure_only(self) -> None:
        counts = Counter(row["selected_transition_type"] for row in self.ledger["classifier_results"])
        self.assertEqual(counts["upgrade_without_closure"], 5)
        self.assertEqual(sum(counts.values()), 5)
        gate_counts = self.ledger["acceptance_gate"]["classification_counts"]
        self.assertEqual(gate_counts["upgrade_without_closure"], 5)
        self.assertEqual(gate_counts["closure"], 0)
        self.assertEqual(gate_counts["target_import_violation"], 0)
        self.assertEqual(gate_counts["false_negative"], 0)
        for result in self.ledger["classifier_results"]:
            self.assertTrue(result["precedence_applied"])
            self.assertEqual(result["guard_failures"], [])

    def test_no_claim_closure_or_target_import(self) -> None:
        text = LEDGER.read_text(encoding="utf-8")
        self.assertNotIn('"same_session_closure_attempted": true', text)
        self.assertNotIn('"target_import_detected": true', text)
        self.assertNotIn('"required_object_already_present": true', text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
