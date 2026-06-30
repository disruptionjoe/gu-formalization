import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "explorations" / "hourly-20260625-1503-cycle3-receipt-transition-matrix.md"


class ReceiptTransitionMatrixAfter1503Audit(unittest.TestCase):
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

    def test_frontmatter_and_summary_identity(self):
        self.assertTrue(ARTIFACT.exists())
        self.assertIn('run_id: "hourly-20260625-1503"', self.text)
        self.assertIn("cycle: 3", self.text)
        self.assertIn("lane: 2", self.text)
        self.assertIn('artifact_id: "ReceiptTransitionMatrixAfter1503_V1"', self.text)

        self.assertEqual(self.data["artifact_id"], "ReceiptTransitionMatrixAfter1503_V1")
        self.assertEqual(self.data["run_id"], "hourly-20260625-1503")
        self.assertEqual(self.data["cycle"], 3)
        self.assertEqual(self.data["lane"], 2)
        self.assertEqual(self.data["cycle_commits"]["cycle_1"], "b1a2cc5")
        self.assertEqual(self.data["cycle_commits"]["cycle_2"], "74090c4")

    def test_required_counts_are_zero_or_sufficient(self):
        self.assertGreaterEqual(self.data["normalized_candidate_rows"], 20)
        self.assertEqual(self.data["normalized_candidate_rows"], len(self.rows))
        self.assertEqual(self.data["accepted_receipt_count"], 0)
        self.assertEqual(self.data["accepted_for_routing_count"], 0)
        self.assertEqual(self.data["proof_restart_ready_count"], 0)

        self.assertEqual([row for row in self.rows if row["accepted_receipt"]], [])
        self.assertEqual([row for row in self.rows if row["accepted_for_routing"]], [])
        self.assertEqual([row for row in self.rows if row["proof_restart_ready"]], [])
        self.assertFalse(self.data["transition_decision"]["any_accepted_receipt"])
        self.assertFalse(self.data["transition_decision"]["any_accepted_for_routing"])
        self.assertFalse(self.data["transition_decision"]["any_proof_restart_ready"])

    def test_all_five_routes_present(self):
        required_routes = {"PTUJ", "IG", "DGU/VZ", "RS", "QFT"}
        self.assertEqual(set(self.data["required_routes"]), required_routes)
        self.assertEqual(set(self.data["route_counts"]), required_routes)
        self.assertEqual(set(row["route"] for row in self.rows), required_routes)

    def test_cycle_transition_identifiers_present(self):
        required_identifiers = {
            "C1_PTUJ_TOOLCHAIN_SOURCE_BYTE_MANIFEST",
            "C1_IG_D7_MULTIPLICITY_TRANSCRIPT",
            "C1_DGU_IDENTITY_FIELD_RECEIPT_BUNDLE",
            "C1_RS_UCSD_FRAME_SEQUENCE_ACQUISITION",
            "C1_QFT_LOCAL_GAUGE_ACTION_GROUPOID",
            "C2_PTUJ_OFFICIAL_SOURCE_ASSET_BRANCH",
            "C2_IG_D7_PROOF_OBJECT_ADMISSION",
            "C2_DGU_ACTUAL_01_SOURCE_WINDOW_PACKET",
            "C2_RS_UCSD_VISUAL_LOCATOR_UNAVAILABILITY_PACKET",
            "C2_QFT_SOURCE_OBSERVED_RAW_BRANCH_PACKET",
        }
        self.assertTrue(required_identifiers.issubset(set(self.data["cycle_transition_identifiers"])))
        self.assertTrue(required_identifiers.issubset({row["row_id"] for row in self.rows}))
        for identifier in required_identifiers:
            self.assertIn(identifier, self.text)

    def test_required_row_shape(self):
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


if __name__ == "__main__":
    unittest.main()
