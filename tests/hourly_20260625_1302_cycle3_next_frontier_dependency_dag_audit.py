import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "explorations" / "hourly-20260625-1302-cycle3-next-frontier-dependency-dag.md"


def load_summary():
    text = ARTIFACT.read_text(encoding="utf-8")
    match = re.search(r"## 7\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```", text, re.S)
    if not match:
        raise AssertionError("machine-readable JSON summary block not found")
    return json.loads(match.group(1))


class NextFrontierDependencyDagAfter1302Audit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.summary = load_summary()
        cls.candidates = cls.summary["candidates"]
        cls.by_id = {candidate["id"]: candidate for candidate in cls.candidates}

    def test_candidate_count_consistency(self):
        quality_candidates = [candidate for candidate in self.candidates if candidate.get("quality") is True]
        self.assertGreaterEqual(self.summary["quality_candidates_claimed"], 18)
        self.assertEqual(self.summary["quality_candidates_claimed"], len(quality_candidates))

    def test_dependencies_reference_known_objects(self):
        known = set(self.summary["known_objects"])
        self.assertTrue(set(self.by_id).issubset(known))
        for candidate in self.candidates:
            for dependency in candidate.get("dependencies", []):
                self.assertIn(dependency, known, f"{candidate['id']} references unknown dependency {dependency}")

    def test_immediate_parallel_lanes_have_disjoint_write_scopes(self):
        lanes = self.summary["immediate_parallel_safe_lanes"]
        self.assertEqual(5, len(lanes))
        write_scopes = [lane["write_scope"] for lane in lanes]
        self.assertEqual(len(write_scopes), len(set(write_scopes)))
        for lane in lanes:
            candidate = self.by_id[lane["id"]]
            self.assertTrue(candidate["parallel_safe"], lane["id"])
            self.assertFalse(candidate["sequential"], lane["id"])
            self.assertEqual(candidate["write_scope"], lane["write_scope"])

    def test_immediate_parallel_lanes_have_disjoint_upstream_prerequisites(self):
        prerequisites = []
        for lane in self.summary["immediate_parallel_safe_lanes"]:
            prerequisites.extend(lane.get("prerequisites", []))
        self.assertEqual(len(prerequisites), len(set(prerequisites)))

    def test_sequential_lanes_are_not_marked_immediate_parallel(self):
        immediate_ids = {lane["id"] for lane in self.summary["immediate_parallel_safe_lanes"]}
        for lane_id in self.summary["sequential_lanes"]:
            self.assertIn(lane_id, self.by_id)
            self.assertNotIn(lane_id, immediate_ids)
            self.assertTrue(self.by_id[lane_id]["sequential"], lane_id)
            self.assertFalse(self.by_id[lane_id]["parallel_safe"], lane_id)

    def test_next_five_are_parallel_safe(self):
        next_five = self.summary["next_five_goals_recommendation"]
        immediate_ids = {lane["id"] for lane in self.summary["immediate_parallel_safe_lanes"]}
        self.assertEqual(5, len(next_five))
        self.assertEqual(set(next_five), immediate_ids)
        for lane_id in next_five:
            self.assertTrue(self.by_id[lane_id]["parallel_safe"], lane_id)
            self.assertFalse(self.by_id[lane_id]["sequential"], lane_id)

    def test_no_receipts_and_no_proof_restart(self):
        self.assertEqual(0, self.summary["accepted_receipt_count"])
        self.assertFalse(self.summary["proof_restart_allowed"])


if __name__ == "__main__":
    unittest.main()
