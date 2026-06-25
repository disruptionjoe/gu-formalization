import json
import re
import unittest
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "explorations" / "hourly-20260625-0803-cycle3-receipt-transition-matrix.md"


class ReceiptTransitionMatrixAfter0803Audit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        text = ARTIFACT.read_text(encoding="utf-8")
        match = re.search(
            r"## 7\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
            text,
            re.DOTALL,
        )
        if not match:
            raise AssertionError("Machine-readable JSON summary block not found")
        cls.data = json.loads(match.group(1))
        cls.rows = cls.data["candidate_rows"]

    def test_row_counts_match_candidate_rows(self):
        self.assertEqual(self.data["row_count"], len(self.rows))
        self.assertEqual(self.data["row_count"], 25)

    def test_required_routes_and_route_counts(self):
        required_routes = set(self.data["required_routes"])
        route_counts = Counter(row["route"] for row in self.rows)

        self.assertEqual(required_routes, {"PTUJ_Keating", "IG_selector", "DGU_Oxford", "RS", "QFT"})
        self.assertEqual(set(route_counts), required_routes)
        self.assertEqual(dict(route_counts), self.data["route_counts"])

        for route, expected_count in self.data["route_counts"].items():
            self.assertEqual(self.data["route_status"][route]["row_count"], expected_count)

    def test_status_counts_and_vocabulary_consistency(self):
        vocabulary = set(self.data["status_vocabulary"])
        status_counts = Counter(row["candidate_status"] for row in self.rows)

        self.assertTrue(set(status_counts).issubset(vocabulary))
        self.assertEqual(status_counts["contract_defined"], 2)
        self.assertEqual(status_counts["hosted_candidate"], 9)
        self.assertEqual(status_counts["blocked_identity"], 6)
        self.assertEqual(status_counts["blocked_acquisition"], 4)
        self.assertEqual(status_counts["source_schema_shell"], 3)
        self.assertEqual(status_counts["scoped_fail_preserved"], 1)

        expected_summary_counts = {
            key: value
            for key, value in self.data["status_counts"].items()
            if key not in {"accepted_for_routing", "proof_restart_ready"}
        }
        self.assertEqual(dict(status_counts), expected_summary_counts)
        self.assertEqual(self.data["status_counts"]["accepted_for_routing"], 0)
        self.assertEqual(self.data["status_counts"]["proof_restart_ready"], 0)

    def test_route_status_counts_recompute(self):
        for route, route_summary in self.data["route_status"].items():
            rows = [row for row in self.rows if row["route"] == route]
            status_counts = Counter(row["candidate_status"] for row in rows)
            self.assertEqual(dict(status_counts), route_summary["status_counts"])

    def test_zero_accepted_routing_and_proof_restart(self):
        accepted_receipts = [row for row in self.rows if row["accepted_receipt"]]
        accepted_for_routing = [row for row in self.rows if row["accepted_for_routing"]]
        proof_restart_ready = [row for row in self.rows if row["proof_restart_ready"]]

        self.assertEqual(accepted_receipts, [])
        self.assertEqual(accepted_for_routing, [])
        self.assertEqual(proof_restart_ready, [])
        self.assertEqual(self.data["transition_counts"]["accepted_receipt_count"], 0)
        self.assertEqual(self.data["transition_counts"]["accepted_for_routing_count"], 0)
        self.assertEqual(self.data["transition_counts"]["proof_restart_ready_count"], 0)
        self.assertFalse(self.data["transition_decision"]["any_candidate_transitioned_to_accepted_for_routing"])
        self.assertFalse(self.data["transition_decision"]["any_candidate_transitioned_to_proof_restart_ready"])

    def test_required_fields_present_on_every_row(self):
        required_fields = {
            "row_id",
            "route",
            "source_object",
            "candidate_status",
            "accepted_receipt",
            "accepted_for_routing",
            "family_identity",
            "proof_restart_ready",
            "first_obstruction",
            "next_object",
        }
        seen = set()
        for row in self.rows:
            self.assertEqual(set(row), required_fields)
            self.assertNotIn(row["row_id"], seen)
            seen.add(row["row_id"])
            self.assertIsInstance(row["first_obstruction"], str)
            self.assertTrue(row["first_obstruction"])
            self.assertIsInstance(row["next_object"], str)
            self.assertTrue(row["next_object"])


if __name__ == "__main__":
    unittest.main()
