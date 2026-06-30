import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "explorations" / "hourly-20260625-0803-cycle3-next-frontier-dependency-dag.md"


def load_summary():
    text = ARTIFACT.read_text(encoding="utf-8")
    match = re.search(r"## 9\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```", text, re.S)
    if not match:
        raise AssertionError("machine-readable JSON summary block not found")
    return json.loads(match.group(1))


class NextFrontierDependencyDagAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.summary = load_summary()
        cls.candidates = cls.summary["candidates"]
        cls.by_id = {candidate["id"]: candidate for candidate in cls.candidates}

    def test_claimed_quality_candidate_count_is_real(self):
        quality = [candidate for candidate in self.candidates if candidate.get("quality") is True]
        self.assertGreaterEqual(self.summary["quality_candidates_claimed"], 18)
        self.assertEqual(self.summary["quality_candidates_claimed"], len(quality))
        self.assertGreaterEqual(len(quality), 18)

    def test_dependencies_reference_known_objects(self):
        known = set(self.summary["known_objects"])
        candidate_ids = set(self.by_id)
        self.assertTrue(candidate_ids.issubset(known))
        for candidate in self.candidates:
            for dependency in candidate.get("dependencies", []):
                self.assertIn(dependency, known, f"{candidate['id']} references unknown dependency {dependency}")

    def test_parallel_safe_lanes_have_disjoint_prerequisites_and_write_scopes(self):
        lanes = self.summary["immediate_parallel_safe_lanes"]
        self.assertEqual(5, len(lanes))
        all_prerequisites = []
        write_scopes = []
        for lane in lanes:
            self.assertIn(lane["id"], self.by_id)
            self.assertTrue(self.by_id[lane["id"]]["parallel_safe"])
            all_prerequisites.extend(lane.get("prerequisites", []))
            write_scopes.append(lane["write_scope"])
        self.assertEqual(len(all_prerequisites), len(set(all_prerequisites)))
        self.assertEqual(len(write_scopes), len(set(write_scopes)))

    def test_sequential_lanes_are_not_parallel(self):
        for lane_id in self.summary["sequential_lanes"]:
            self.assertIn(lane_id, self.by_id)
            candidate = self.by_id[lane_id]
            self.assertTrue(candidate["sequential"], lane_id)
            self.assertFalse(candidate["parallel_safe"], lane_id)

    def test_next_five_recommendation_is_parallel_safe(self):
        recommended = self.summary["next_five_goals_recommendation"]
        parallel_ids = {lane["id"] for lane in self.summary["immediate_parallel_safe_lanes"]}
        self.assertEqual(5, len(recommended))
        self.assertEqual(set(recommended), parallel_ids)

    def test_not_parallel_five_are_not_immediate_parallel_lanes(self):
        recommended = set(self.summary["next_five_goals_recommendation"])
        not_parallel = set(self.summary["next_five_not_parallel"])
        self.assertEqual(5, len(not_parallel))
        self.assertTrue(recommended.isdisjoint(not_parallel))
        self.assertIn("QFT_BELL_CHSH_FIREWALL_as_a_substitute_for_QFT_CONGRUENCE_GENERATORS", not_parallel)

    def test_wrapper_assessment_records_improvement_without_promotion(self):
        assessment = self.summary["wrapper_quality_assessment"]
        self.assertTrue(assessment["improved_quality"])
        self.assertEqual(
            "cycle1_blockers_became_cycle2_consequence_gates_and_cycle3_firewalls",
            assessment["improvement_kind"],
        )
        self.assertFalse(assessment["promotion_from_wrapper"])
        self.assertGreaterEqual(len(assessment["cycle1_blockers"]), 5)
        self.assertGreaterEqual(len(assessment["cycle2_consequence_gates"]), 5)
        self.assertGreaterEqual(len(assessment["cycle3_firewalls"]), 5)

    def test_no_receipts_or_restart_promoted(self):
        self.assertEqual(0, self.summary["accepted_receipt_count"])
        self.assertFalse(self.summary["proof_restart_allowed"])


if __name__ == "__main__":
    unittest.main()
