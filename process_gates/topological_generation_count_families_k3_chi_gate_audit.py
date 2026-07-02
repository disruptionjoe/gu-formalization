import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "lab"
    / "active-research"
    / "topological-generation-count-families-k3-chi-gate-2026-06-26.md"
)
ACTIVE_README = ROOT / "lab" / "active-research" / "README.md"
NEXT_STEPS = ROOT / "NEXT-STEPS.md"
ROUTE_ALT = (
    ROOT
    / "explorations"
    / "generation-sector"
    / "three-generation-route-alternatives-after-rs-failure-2026-06-26.md"
)


class TopologicalGenerationCountFamiliesK3ChiGateAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.active_readme = ACTIVE_README.read_text(encoding="utf-8")
        cls.next_steps = NEXT_STEPS.read_text(encoding="utf-8")
        cls.route_alt = ROUTE_ALT.read_text(encoding="utf-8")

    def test_verdict_keeps_generation_count_open(self):
        self.assertIn("OPEN_GATED; FAMILIES_PUSHFORWARD_NOT_CLOSED", self.text)
        self.assertIn("does not close", self.text)
        self.assertIn("generation count | remains OPEN", self.text)
        self.assertNotIn("Verdict: CONDITIONALLY_CLOSED", self.text)

    def test_blocks_families_k3_chi_shortcuts(self):
        required = [
            "ind_H(D_GU) = ch(S_X)[X4] = chi(K3) = 24",
            "fixed-signature metric fiber is not a free contractible vector space",
            "pi_!(1) over the noncompact contractible fiber is not a theorem as written",
            "Shiab is not yet an index-preserving deformation certificate",
            "phi_zero_order_implies_standard_ellipticity",
            "Twisted de Rham index is not automatically chi(K3)",
            "K3 selection is downstream of open generation assumptions",
        ]
        for phrase in required:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.text)

    def test_names_next_gate_and_computation(self):
        self.assertIn("FamiliesIndexPushforwardGate_V0", self.text)
        self.assertIn("S_XCharacteristicClassPacket_V0", self.text)
        self.assertIn("ch2(S_X)[K3] or ch2(S(6,4))[K3]", self.text)

    def test_machine_readable_summary_blocks_promotion(self):
        match = re.search(
            r"```json\n(\{\n  \"artifact\": \"TOPOLOGICAL_GENERATION_COUNT_FAMILIES_K3_CHI_GATE\".*?\n\})\n```",
            self.text,
            re.DOTALL,
        )
        self.assertIsNotNone(match, "machine-readable summary block not found")
        payload = json.loads(match.group(1))
        self.assertFalse(payload["promotion_allowed_now"])
        self.assertEqual(payload["generation_count_status"], "OPEN")
        self.assertEqual(payload["required_next_object"], "FamiliesIndexPushforwardGate_V0")
        self.assertIn("ind_H(D_GU)=chi(K3)=24", payload["blocked_shortcuts"])

    def test_crosslinks_are_present(self):
        path = "lab/active-research/topological-generation-count-families-k3-chi-gate-2026-06-26.md"
        self.assertIn(path, self.active_readme)
        self.assertIn(path, self.next_steps)
        self.assertIn("FamiliesIndexPushforwardGate_V0", self.route_alt)


if __name__ == "__main__":
    unittest.main()
