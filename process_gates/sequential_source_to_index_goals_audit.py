import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GOAL1 = ROOT / "explorations" / "generation-sector" / "sequential-goal-1-dgu-source-row-same-operator-2026-06-26.md"
GOAL2 = ROOT / "explorations" / "generation-sector" / "sequential-goal-2-y14-k3-families-pushforward-2026-06-26.md"
GOAL3 = ROOT / "explorations" / "generation-sector" / "sequential-goal-3-sx-characteristic-readout-2026-06-26.md"
NEXT_STEPS = ROOT / "NEXT-STEPS.md"


def extract_summary(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    blocks = re.findall(r"```json\s*(\{.*?\})\s*```", text, flags=re.DOTALL)
    if not blocks:
        raise AssertionError(f"missing JSON summary in {path}")
    return json.loads(blocks[-1])


class SequentialSourceToIndexGoalsAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.goal1_text = GOAL1.read_text(encoding="utf-8")
        cls.goal2_text = GOAL2.read_text(encoding="utf-8")
        cls.goal3_text = GOAL3.read_text(encoding="utf-8")
        cls.next_steps = NEXT_STEPS.read_text(encoding="utf-8")
        cls.goal1 = extract_summary(GOAL1)
        cls.goal2 = extract_summary(GOAL2)
        cls.goal3 = extract_summary(GOAL3)

    def test_goal_order_and_dependency_chain(self):
        self.assertEqual(self.goal1["goal_order"], 1)
        self.assertEqual(self.goal2["goal_order"], 2)
        self.assertEqual(self.goal3["goal_order"], 3)
        self.assertTrue(self.goal2["depends_on_goal1"])
        self.assertTrue(self.goal3["depends_on_goal1"])
        self.assertTrue(self.goal3["depends_on_goal2"])

    def test_goal1_blocks_same_operator_without_target_import(self):
        self.assertEqual(
            self.goal1["verdict_class"],
            "SCOPED_NEGATIVE_SOURCE_ROW_SAME_OPERATOR_BLOCKED",
        )
        self.assertFalse(self.goal1["target_import_used"])
        self.assertFalse(self.goal1["admitted_primary_row"])
        self.assertTrue(self.goal1["candidate_source_payloads_found"])
        self.assertFalse(self.goal1["actual_operator_handle_present"])
        self.assertFalse(self.goal1["same_operator_witness_evaluable"])
        self.assertFalse(self.goal1["typed_d_roll_allowed_as_source_row"])
        self.assertIn("DGU01SameOperatorWitness_V1", self.goal1["downstream_locked"])
        self.assertIn("PrimarySourceDGU01SectorRuleRowInstance_V1", self.goal1_text)

    def test_goal2_keeps_pushforward_not_defined(self):
        self.assertEqual(
            self.goal2["verdict_class"],
            "PUSHFORWARD_NOT_DEFINED_BLOCKED_ON_SOURCE_OPERATOR_AND_END_MODEL",
        )
        self.assertFalse(self.goal2["target_import_used"])
        self.assertFalse(self.goal2["goal1_admitted_primary_row"])
        self.assertEqual(self.goal2["physical_operator_symbol"], "GUARDED_NON_ELLIPTIC_NULL_CONE")
        self.assertEqual(self.goal2["phi_role"], "LOWER_ORDER_BUT_DOMAIN_OPEN")
        self.assertEqual(self.goal2["fredholm_framework"], "NOT_DEFINED")
        self.assertEqual(self.goal2["pushforward"], "NOT_DEFINED")
        self.assertEqual(self.goal2["k3_use"], "K3_CONTROL_ONLY")
        self.assertFalse(self.goal2["families_pushforward_closed"])
        self.assertFalse(self.goal2["generation_readout_allowed"])

    def test_goal3_keeps_characteristic_readout_open(self):
        self.assertEqual(
            self.goal3["verdict_class"],
            "CHARACTERISTIC_PACKET_NOT_COMPUTED_CONNECTION_AND_NORMALIZATION_OPEN",
        )
        self.assertFalse(self.goal3["source_connection_defined"])
        self.assertFalse(self.goal3["curvature_2_form_defined"])
        self.assertFalse(self.goal3["ch2_computed"])
        self.assertFalse(self.goal3["eta_computed"])
        self.assertFalse(self.goal3["h_line_normalization_accepted"])
        self.assertFalse(self.goal3["generation_readout_allowed"])
        self.assertEqual(self.goal3["readout_decision"], "NOT_COMPUTED")
        self.assertEqual(self.goal3["generation_count_status"], "OPEN")
        self.assertIn("RSRankTerrainGate_V0", self.goal3["blocked_by"])

    def test_no_generation_promotion_language(self):
        combined = "\n".join([self.goal1_text, self.goal2_text, self.goal3_text])
        forbidden = [
            "generation count is resolved",
            "generation count is closed",
            "CONDITIONALLY_RESOLVED",
            "ind_H(D_GU)=24 is proved",
            "24 / 8 = 3 is derived",
        ]
        for phrase in forbidden:
            with self.subTest(phrase=phrase):
                self.assertNotIn(phrase, combined)
        self.assertIn("No generation-count promotion is allowed", self.next_steps)

    def test_next_steps_links_all_three_artifacts(self):
        for path in [
            "explorations/generation-sector/sequential-goal-1-dgu-source-row-same-operator-2026-06-26.md",
            "explorations/generation-sector/sequential-goal-2-y14-k3-families-pushforward-2026-06-26.md",
            "explorations/generation-sector/sequential-goal-3-sx-characteristic-readout-2026-06-26.md",
        ]:
            with self.subTest(path=path):
                self.assertIn(path, self.next_steps)


if __name__ == "__main__":
    unittest.main()
