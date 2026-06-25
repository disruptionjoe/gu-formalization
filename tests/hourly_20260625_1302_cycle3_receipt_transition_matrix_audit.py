import json
import re
import unittest
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "explorations" / "hourly-20260625-1302-cycle3-receipt-transition-matrix.md"


class ReceiptTransitionMatrixAfter1302Audit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        match = re.search(
            r"## 6\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
            cls.text,
            re.DOTALL,
        )
        if not match:
            raise AssertionError("Machine-readable JSON summary block not found")
        cls.data = json.loads(match.group(1))
        cls.rows = cls.data["candidate_rows"]

    def test_required_routes_appear_once_in_route_counts(self):
        required_routes = {"PTUJ", "IG", "DGU/VZ", "RS", "QFT"}
        self.assertEqual(set(self.data["required_routes"]), required_routes)
        self.assertEqual(set(self.data["route_counts"]), required_routes)
        self.assertEqual(set(row["route"] for row in self.rows), required_routes)

    def test_row_and_route_counts_are_consistent(self):
        route_counts = Counter(row["route"] for row in self.rows)

        self.assertEqual(self.data["normalized_candidate_rows"], len(self.rows))
        self.assertEqual(self.data["normalized_candidate_rows"], 20)
        self.assertEqual(dict(route_counts), self.data["route_counts"])

        for route, route_summary in self.data["route_transition_counts"].items():
            rows = [row for row in self.rows if row["route"] == route]
            self.assertEqual(route_summary["rows"], len(rows))
            self.assertEqual(route_summary["accepted_receipts"], 0)
            self.assertEqual(route_summary["accepted_for_routing"], 0)
            self.assertEqual(route_summary["proof_restart_ready"], 0)

    def test_state_counts_are_consistent(self):
        state_counts = Counter(row["current_state"] for row in self.rows)

        self.assertEqual(dict(state_counts), self.data["state_counts"])
        self.assertEqual(sum(self.data["state_counts"].values()), len(self.rows))
        self.assertEqual(
            self.data["blocked_rows"],
            state_counts["blocked_acquisition"]
            + state_counts["blocked_identity"]
            + state_counts["blocked_computation"]
            + state_counts["blocked_descent"],
        )
        self.assertEqual(self.data["conditional_rows"], state_counts["conditional"])
        self.assertEqual(self.data["underdefined_rows"], state_counts["underdefined"])
        self.assertEqual(self.data["contract_rows"], state_counts["contract_defined"])
        self.assertEqual(self.data["hosted_rows"], state_counts["hosted_candidate"])
        self.assertEqual(self.data["schema_rows"], state_counts["schema_taxonomy"])

    def test_zero_receipts_routing_and_restart_are_directly_supported(self):
        self.assertEqual([row for row in self.rows if row["accepted_receipt"]], [])
        self.assertEqual([row for row in self.rows if row["accepted_for_routing"]], [])
        self.assertEqual([row for row in self.rows if row["proof_restart_ready"]], [])

        self.assertEqual(self.data["accepted_receipt_count"], 0)
        self.assertEqual(self.data["accepted_for_routing_count"], 0)
        self.assertEqual(self.data["proof_restart_ready_count"], 0)
        self.assertFalse(self.data["transition_decision"]["any_accepted_receipt"])
        self.assertFalse(self.data["transition_decision"]["any_accepted_for_routing"])
        self.assertFalse(self.data["transition_decision"]["any_proof_restart_ready"])
        self.assertFalse(self.data["target_import_used"])

    def test_required_row_fields_and_unique_ids(self):
        required_fields = {
            "row_id",
            "route",
            "candidate",
            "source_object",
            "current_state",
            "accepted_receipt",
            "accepted_for_routing",
            "proof_restart_ready",
            "next_required_object",
        }
        seen = set()
        for row in self.rows:
            self.assertEqual(set(row), required_fields)
            self.assertNotIn(row["row_id"], seen)
            seen.add(row["row_id"])
            self.assertIsInstance(row["next_required_object"], str)
            self.assertTrue(row["next_required_object"])

    def test_no_transition_to_proof_promotion_phrases(self):
        forbidden_patterns = [
            r"\bpromoted?\s+to\s+proof\b",
            r"\btransition(?:ed|s|ing)?\s+to\s+proof\b",
            r"\bready\s+for\s+proof\b",
            r"\bproof-ready\b",
            r"\bproof\s+restart\s+is\s+allowed\b",
            r"\bproof\s+restart\s+allowed:\s*true\b",
            r"\baccepted_for_routing:\s*true\b",
            r"\bproof_restart_ready:\s*true\b",
        ]
        for pattern in forbidden_patterns:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                f"promotion phrase matched: {pattern}",
            )


if __name__ == "__main__":
    unittest.main()
