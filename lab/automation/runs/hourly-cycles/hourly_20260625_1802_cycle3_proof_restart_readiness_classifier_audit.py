import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_PATH = (
    ROOT
    / "explorations"
    / "hourly-20260625-1802-cycle3-proof-restart-readiness-classifier.md"
)


def load_summary():
    text = ARTIFACT_PATH.read_text(encoding="utf-8")
    matches = re.findall(r"```json\s*(\{.*?\})\s*```", text, flags=re.DOTALL)
    if not matches:
        raise AssertionError("No JSON block found in classifier artifact")
    return json.loads(matches[-1])


class ProofRestartReadinessClassifierAudit(unittest.TestCase):
    def setUp(self):
        self.summary = load_summary()

    def test_global_contract(self):
        self.assertEqual(self.summary["run_id"], "hourly-20260625-1802")
        self.assertEqual(
            self.summary["artifact_path"],
            "explorations/hourly-20260625-1802-cycle3-proof-restart-readiness-classifier.md",
        )

        global_decision = self.summary["global_decision"]
        self.assertEqual(global_decision["accepted_receipt_count_total"], 0)
        self.assertEqual(global_decision["accepted_for_routing_count_total"], 0)
        self.assertFalse(global_decision["proof_restart_allowed"])
        self.assertFalse(global_decision["claim_promotion"])
        self.assertFalse(global_decision["global_no_go_promoted"])
        self.assertFalse(global_decision["target_import"])

    def test_route_rows_are_complete_and_all_blocked(self):
        route_rows = self.summary["route_rows"]
        self.assertEqual(len(route_rows), 7)
        self.assertEqual(
            [row["route"] for row in route_rows],
            ["PTUJ", "IG", "DGU/VZ", "RS", "QFT", "major GU claim", "global no-go"],
        )

        for row in route_rows:
            with self.subTest(route=row["route"]):
                self.assertEqual(row["accepted_receipt_count"], 0)
                self.assertEqual(row["accepted_for_routing_count"], 0)
                self.assertFalse(row["route_ready"])
                self.assertFalse(row["proof_restart_allowed"])
                self.assertFalse(row["claim_promotion"])
                self.assertFalse(row["target_import"])
                self.assertIn("exact_blocker", row)
                self.assertIsInstance(row["exact_blocker"], str)
                self.assertTrue(row["exact_blocker"].strip())
                self.assertIn("next_object", row)
                self.assertIsInstance(row["next_object"], str)
                self.assertTrue(row["next_object"].strip())


if __name__ == "__main__":
    unittest.main()
