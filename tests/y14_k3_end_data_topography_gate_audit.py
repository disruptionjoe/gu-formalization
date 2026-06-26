import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "explorations" / "y14-k3-end-data-topography-gate-2026-06-26.md"


class Y14K3EndDataTopographyGateAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = ARTIFACT.read_text(encoding="utf-8")

    def test_verdict_and_terrain_are_present(self):
        required = [
            "K3_CONTROL_ONLY",
            "PHYSICAL_GENERATION_COUNT_BLOCKED_ON_RS_PAYLOAD_AND_END_DATA",
            "noncompact-aps-end",
            "transport-loss",
            "compact K3 arithmetic used as physical noncompact Y14 index",
        ]
        for token in required:
            with self.subTest(token=token):
                self.assertIn(token, self.text)

    def test_next_object_is_payload_before_bridge(self):
        self.assertIn("NEXT_OBJECT: PhysicalRSKTheoryClassGate_V0", self.text)
        self.assertIn("Do not run the bridge map first.", self.text)
        self.assertIn("First identify the physical RS K-theory / symbol payload", self.text)

    def test_machine_readable_summary_is_parseable_and_blocks_promotion(self):
        match = re.search(
            r"```json\n(\{\n  \"artifact\": \"Y14_K3_END_DATA_TOPOGRAPHY_GATE\".*?\n\})\n```",
            self.text,
            re.DOTALL,
        )
        self.assertIsNotNone(match, "machine-readable summary block not found")
        payload = json.loads(match.group(1))
        self.assertFalse(payload["promotion_allowed_now"])
        self.assertEqual(payload["next_object"], "PhysicalRSKTheoryClassGate_V0")
        self.assertEqual(payload["current_decisions"]["GEN_COUNT"], "OPEN")
        self.assertEqual(payload["current_decisions"]["K3_CONTROL"], "CONTROL_ONLY")
        self.assertIn("generation_target_used_as_input", payload["kill_conditions"])


if __name__ == "__main__":
    unittest.main()
