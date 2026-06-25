import json
import re
import unittest
from collections import Counter
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = REPO_ROOT / "explorations" / "hourly-20260625-0711-cycle3-receipt-transition-matrix.md"


def load_summary():
    text = ARTIFACT.read_text(encoding="utf-8")
    match = re.search(r"```json\s*(\{.*?\})\s*```", text, re.DOTALL)
    if not match:
        raise AssertionError("machine-readable JSON summary block not found")
    return json.loads(match.group(1))


class ReceiptTransitionMatrixAudit(unittest.TestCase):
    def setUp(self):
        self.summary = load_summary()
        self.rows = self.summary["candidate_rows"]

    def test_row_and_status_counts_match_rows(self):
        self.assertEqual(self.summary["row_count"], len(self.rows))
        status_counts = Counter(row["status"] for row in self.rows)
        normalized_counts = {
            status: status_counts.get(status, 0)
            for status in self.summary["status_counts"]
        }
        self.assertEqual(normalized_counts, self.summary["status_counts"])

    def test_zero_accepted_and_zero_proof_ready(self):
        self.assertEqual(self.summary["status_counts"]["accepted_for_routing"], 0)
        self.assertEqual(self.summary["status_counts"]["proof_restart_ready"], 0)
        self.assertEqual(self.summary["transition_counts"]["accepted_for_routing"], 0)
        self.assertEqual(self.summary["transition_counts"]["proof_restart_ready"], 0)
        self.assertFalse(
            self.summary["transition_decision"][
                "any_candidate_transitioned_to_accepted_for_routing"
            ]
        )
        self.assertFalse(any(row["accepted_for_routing"] for row in self.rows))
        self.assertFalse(any(row["proof_restart_ready"] for row in self.rows))
        self.assertEqual(self.summary["accepted_for_routing"], [])
        self.assertEqual(self.summary["proof_restart_ready"], [])

    def test_required_status_vocabulary_present_and_consistent(self):
        required_statuses = {
            "verified_frame_candidate",
            "caption_metadata_only",
            "hosted_candidate",
            "blocked_identity",
            "scoped_fail",
            "underdefined_spec",
            "accepted_for_routing",
            "proof_restart_ready",
        }
        self.assertEqual(set(self.summary["status_counts"]), required_statuses)
        observed = {row["status"] for row in self.rows}
        self.assertTrue(observed.issubset(required_statuses))
        self.assertGreater(self.summary["status_counts"]["verified_frame_candidate"], 0)
        self.assertGreater(self.summary["status_counts"]["caption_metadata_only"], 0)
        self.assertGreater(self.summary["status_counts"]["hosted_candidate"], 0)
        self.assertGreater(self.summary["status_counts"]["blocked_identity"], 0)
        self.assertGreater(self.summary["status_counts"]["scoped_fail"], 0)
        self.assertGreater(self.summary["status_counts"]["underdefined_spec"], 0)

    def test_required_route_coverage_and_counts(self):
        required_routes = {
            "Oxford_anchors",
            "PTUJ_Keating",
            "IG_bridge",
            "DGU",
            "RS",
            "QFT",
        }
        route_counts = Counter(row["route"] for row in self.rows)
        self.assertEqual(set(route_counts), required_routes)
        self.assertEqual(dict(route_counts), self.summary["route_counts"])
        self.assertEqual(set(self.summary["route_status"]), required_routes)

        for route, route_summary in self.summary["route_status"].items():
            route_rows = [row for row in self.rows if row["route"] == route]
            self.assertEqual(route_summary["row_count"], len(route_rows))
            self.assertEqual(
                route_summary["status_counts"],
                dict(Counter(row["status"] for row in route_rows)),
            )
            self.assertEqual(route_summary["accepted_for_routing"], 0)
            self.assertEqual(route_summary["proof_restart_ready"], 0)
            self.assertIn("first_obstruction", route_summary)

    def test_route_specific_statuses(self):
        by_route = {
            route: Counter(row["status"] for row in self.rows if row["route"] == route)
            for route in self.summary["route_counts"]
        }
        self.assertEqual(
            by_route["Oxford_anchors"],
            Counter({"verified_frame_candidate": 3, "blocked_identity": 2}),
        )
        self.assertEqual(
            by_route["PTUJ_Keating"],
            Counter({"caption_metadata_only": 3, "hosted_candidate": 1}),
        )
        self.assertEqual(
            by_route["IG_bridge"],
            Counter(
                {
                    "hosted_candidate": 8,
                    "verified_frame_candidate": 1,
                    "caption_metadata_only": 1,
                }
            ),
        )
        self.assertEqual(by_route["DGU"], Counter({"blocked_identity": 6}))
        self.assertEqual(by_route["RS"], Counter({"scoped_fail": 13}))
        self.assertEqual(by_route["QFT"], Counter({"underdefined_spec": 1}))


if __name__ == "__main__":
    unittest.main()
