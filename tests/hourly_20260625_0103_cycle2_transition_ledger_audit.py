#!/usr/bin/env python3
"""Audit the completed cycle-2 transition ledger."""

from __future__ import annotations

import json
import unittest
from collections import Counter
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
LEDGER = REPO_ROOT / "explorations" / "hourly-20260625-0103-cycle2-transition-ledger.json"

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


class Cycle2TransitionLedgerAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.ledger = load_ledger()

    def test_completed_shape_and_acceptance_gate(self) -> None:
        ledger = self.ledger
        self.assertEqual(ledger["ledger_version"], "CycleLocalTransitionLedger_3_1_5_4_V1")
        self.assertEqual(ledger["run_id"], "hourly-20260625-0103")
        self.assertEqual(ledger["cycle_index"], 2)
        self.assertIs(ledger["synthesis_allowed"], True)
        self.assertEqual(len(ledger["pre_rows"]), 5)
        self.assertEqual(len(ledger["post_rows"]), 5)
        self.assertEqual(len(ledger["classifier_results"]), 5)
        gate = ledger["acceptance_gate"]
        self.assertEqual(gate["status"], "passed")
        self.assertEqual(gate["pre_rows_count"], 5)
        self.assertEqual(gate["post_rows_count"], 5)
        self.assertEqual(gate["classifier_results_count"], 5)
        self.assertIs(gate["identity_links_valid"], True)
        self.assertIs(gate["process_metrics_separated_from_gu_claims"], True)
        self.assertIs(gate["synthesis_allowed"], True)

    def test_pre_post_identity_links_match(self) -> None:
        pre_by_id = {row["row_id"]: row for row in self.ledger["pre_rows"]}
        post_by_id = {row["row_id"]: row for row in self.ledger["post_rows"]}
        self.assertEqual(set(pre_by_id), set(post_by_id))
        for row_id, pre in pre_by_id.items():
            post = post_by_id[row_id]
            for field in LOCKED_FIELDS:
                self.assertEqual(post[field], pre[field], f"{row_id}:{field}")
            self.assertEqual(post["row_phase"], "post")
            self.assertIn(post["new_state"]["verdict"], {"blocked", "underdefined", "conditional"})
            self.assertFalse(post["guard_declarations"]["same_session_closure_attempted"])
            self.assertFalse(post["guard_declarations"]["target_import_detected"])
            self.assertFalse(post["guard_declarations"]["required_object_already_present"])

    def test_owned_paths_exist_and_are_disjoint(self) -> None:
        paths = []
        for row in self.ledger["pre_rows"]:
            paths.append(row["owned_artifact_path"])
            paths.append(row["owned_audit_path"])
        self.assertEqual(len(paths), len(set(paths)))
        for path in paths:
            self.assertTrue((REPO_ROOT / path).exists(), path)

    def test_classifier_results_are_all_same_status_refinements(self) -> None:
        result_ids = {row["row_id"] for row in self.ledger["classifier_results"]}
        self.assertEqual(result_ids, {row["row_id"] for row in self.ledger["pre_rows"]})
        counts = Counter(row["selected_transition_type"] for row in self.ledger["classifier_results"])
        self.assertEqual(counts["same_status_refinement"], 5)
        self.assertEqual(sum(counts.values()), 5)
        for result in self.ledger["classifier_results"]:
            self.assertTrue(result["precedence_applied"])
            self.assertEqual(result["guard_failures"], [])

    def test_no_closure_or_target_import_claims(self) -> None:
        text = LEDGER.read_text(encoding="utf-8")
        self.assertNotIn('"target_import_detected": true', text)
        self.assertNotIn('"same_session_closure_attempted": true', text)
        self.assertEqual(self.ledger["acceptance_gate"]["classification_counts"]["closure"], 0)
        self.assertEqual(
            self.ledger["acceptance_gate"]["classification_counts"]["target_import_violation"],
            0,
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
