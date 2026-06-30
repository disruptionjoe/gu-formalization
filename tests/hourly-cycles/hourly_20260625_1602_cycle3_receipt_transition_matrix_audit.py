import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "explorations" / "hourly-20260625-1602-cycle3-receipt-transition-matrix.md"


class ReceiptTransitionMatrixAfter1602Audit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        match = re.search(
            r"## 7\. Machine-readable JSON summary\.\s*```json\s*(\{.*?\})\s*```",
            cls.text,
            re.DOTALL,
        )
        if not match:
            raise AssertionError("Machine-readable JSON summary block not found")
        cls.data = json.loads(match.group(1))
        cls.rows = cls.data["transition_rows"]

    def test_identity(self):
        self.assertTrue(ARTIFACT.exists())
        self.assertEqual(self.data["artifact_id"], "ReceiptTransitionMatrixAfter1602_V1")
        self.assertEqual(self.data["run_id"], "hourly-20260625-1602")
        self.assertEqual(self.data["cycle"], 3)
        self.assertEqual(self.data["lane"], 2)

    def test_required_counts(self):
        self.assertGreaterEqual(self.data["route_count"], 5)
        self.assertEqual(self.data["route_count"], len(set(row["route"] for row in self.rows)))
        self.assertEqual(self.data["normalized_transition_rows"], len(self.rows))
        self.assertEqual(self.data["accepted_receipt_count"], 0)
        self.assertEqual(self.data["accepted_for_routing_count"], 0)
        self.assertEqual(self.data["proof_restart_ready_count"], 0)
        self.assertGreaterEqual(self.data["schema_only_upgrade_count"], 1)
        self.assertFalse(self.data["target_import_used"])

    def test_all_routes_have_required_transition_shape(self):
        required_routes = {"PTUJ", "IG", "DGU/VZ", "RS", "QFT"}
        self.assertEqual(set(self.data["required_routes"]), required_routes)
        self.assertEqual(set(row["route"] for row in self.rows), required_routes)

        required_fields = {
            "route",
            "cycle1_state",
            "cycle2_state",
            "transition_result",
            "next_object",
        }
        for row in self.rows:
            for field in required_fields:
                self.assertIn(field, row)
                self.assertIsInstance(row[field], str)
                self.assertTrue(row[field])
            self.assertFalse(row["accepted_receipt"])
            self.assertFalse(row["accepted_for_routing"])
            self.assertFalse(row["proof_restart_ready"])

    def test_next_objects_cover_each_route(self):
        next_objects = self.data["next_objects"]
        self.assertEqual(len(next_objects), self.data["route_count"])
        self.assertEqual(set(item["route"] for item in next_objects), set(row["route"] for row in self.rows))
        for item in next_objects:
            self.assertTrue(item["object"])
            self.assertTrue(item["acceptance_condition"])


if __name__ == "__main__":
    unittest.main()
