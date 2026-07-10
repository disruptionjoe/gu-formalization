import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "explorations"
    / "generation-sector" / "three-generation-route-alternatives-after-rs-failure-2026-06-26.md"
)
NEXT_STEPS = ROOT / "NEXT-STEPS.md"
Y14_GATE = ROOT / "explorations" / "generation-sector" / "y14-k3-end-data-topography-gate-2026-06-26.md"


class ThreeGenerationRouteAlternativesAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.next_steps = NEXT_STEPS.read_text(encoding="utf-8")
        cls.y14_gate = Y14_GATE.read_text(encoding="utf-8")

    def test_three_route_objects_are_present(self):
        for token in [
            "WholeOperatorIndexRoute_V0",
            "PhysicalTopologyGenerationClass_V0",
            "RSDecompositionValidityAudit_V0",
        ]:
            with self.subTest(token=token):
                self.assertIn(token, self.text)
                self.assertIn(token, self.next_steps)
                self.assertIn(token, self.y14_gate)

    def test_guardrails_block_target_smuggling(self):
        required = [
            "Do not use `ind_H(D_RS)=8` as input.",
            "Do not use `16 + 8 = 24` as input.",
            "No loose numerology from `24`, binary tetrahedral order, `chi(K3)`, or `Ahat(K3)`.",
            "No hidden rational factor such as an unexplained `3/2`.",
            "Do not treat kinematic polarization counting as an analytic Fredholm index.",
        ]
        for phrase in required:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.text)

    def test_execution_order_uses_decomposition_as_firewall(self):
        self.assertIn("RSDecompositionValidityAudit_V0 as a firewall", self.y14_gate)
        self.assertIn("Treat `RSDecompositionValidityAudit_V0` as a firewall", self.next_steps)
        self.assertIn("recommended_execution_order", self.text)

    def test_machine_readable_summary_blocks_promotion(self):
        match = re.search(
            r"```json\n(\{\n  \"artifact\": \"THREE_GENERATION_ROUTE_ALTERNATIVES_AFTER_RS_FAILURE\".*?\n\})\n```",
            self.text,
            re.DOTALL,
        )
        self.assertIsNotNone(match, "machine-readable summary block not found")
        payload = json.loads(match.group(1))
        self.assertFalse(payload["promotion_allowed_now"])
        self.assertEqual(
            payload["recommended_execution_order"][0],
            "RSDecompositionValidityAudit_V0",
        )
        self.assertIn("hidden_3_over_2_factor", payload["blocked_inputs"])


if __name__ == "__main__":
    unittest.main()
