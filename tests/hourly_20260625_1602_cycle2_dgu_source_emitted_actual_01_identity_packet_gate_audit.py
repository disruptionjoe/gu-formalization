import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "explorations" / "hourly-20260625-1602-cycle2-dgu-source-emitted-actual-01-identity-packet-gate.md"


def extract_json_summary(text: str) -> dict:
    match = re.search(r"## 9\. Machine-readable JSON summary\.\s*```json\s*(\{.*?\})\s*```", text, re.S)
    if not match:
        raise AssertionError("Machine-readable JSON summary block not found")
    return json.loads(match.group(1))


class SourceEmittedActualDGU01IdentityPacketGateAudit(unittest.TestCase):
    def setUp(self):
        self.text = ARTIFACT.read_text(encoding="utf-8")
        self.summary = extract_json_summary(self.text)

    def test_required_boolean_gate_controls(self):
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertFalse(self.summary["actual_identity_packet_present"])
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["vz_replay_allowed"])
        self.assertFalse(self.summary["global_no_go_promoted"])
        self.assertFalse(self.summary["target_import_used"])

    def test_missing_required_fields_are_explicit(self):
        required = set(self.summary["required_fields"])
        missing = set(self.summary["missing_fields"])
        expected_missing = {
            "exact_source_locator_for_actual_D_GU_epsilon_0_1_object",
            "source_emitted_sector_rule",
            "family_identity_to_DGU_VZ_actual_family",
            "operator_action_EL_origin_for_same_object",
            "typed_domain",
            "typed_codomain",
            "epsilon_and_0_1_convention",
            "coefficient_conventions_a_b_lambda_d_or_equivalent",
            "Q_projector_relation_Q_in_Q_out_I_Q_in_P_Q_out_or_equivalent",
            "principal_symbol_or_same_operator_first_order_symbol_data",
        }

        self.assertTrue(expected_missing.issubset(required))
        self.assertEqual(missing, expected_missing)
        self.assertIn("target_import_screen", required)

    def test_next_object_and_first_obstruction_are_explicit(self):
        self.assertEqual(
            self.summary["first_obstruction"],
            "missing_source_emitted_sector_rule_for_actual_D_GU_epsilon_0_1_identity_packet",
        )
        self.assertEqual(
            self.summary["next_object"],
            "OxfordManuscriptUCSDSourceSurfaceReceiptForSourceEmittedActualDGU01IdentityPacket_V1",
        )

    def test_candidate_matrix_covers_required_surfaces(self):
        candidates = {row["candidate"]: row for row in self.summary["candidate_rows"]}
        self.assertEqual(candidates["typed_spine_D_roll"]["decision"], "proposal_target_not_actual_packet")
        self.assertEqual(candidates["UCSD_windows"]["decision"], "adjacent_only")
        self.assertEqual(candidates["Oxford_windows"]["decision"], "adjacent_only")
        self.assertEqual(candidates["manuscript_sections_8_12"]["decision"], "adjacent_only")
        self.assertEqual(candidates["scoped_negatives_1503_and_1602_cycle1"]["decision"], "scoped_negative_only")

    def test_promotion_firewall_is_active(self):
        firewall = self.summary["promotion_firewall"]
        self.assertTrue(firewall["block_typed_spine_to_actual_packet"])
        self.assertTrue(firewall["block_ucsd_family_language_to_same_operator_packet"])
        self.assertTrue(firewall["block_oxford_bosonic_anchor_to_0_1_identity"])
        self.assertTrue(firewall["block_manuscript_action_EL_cluster_to_actual_DGU_identity"])
        self.assertTrue(firewall["block_scoped_negative_to_global_no_go"])
        self.assertTrue(firewall["block_vz_replay_without_actual_packet"])


if __name__ == "__main__":
    unittest.main()
