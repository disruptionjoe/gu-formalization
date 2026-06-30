import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "explorations" / "hourly-20260625-1602-cycle1-dgu-expanded-identity-field-source-scope-bundle.md"
AUDIT = ROOT / "tests" / "hourly_20260625_1602_cycle1_dgu_expanded_identity_field_source_scope_bundle_audit.py"


def extract_json_summary(text: str) -> dict:
    match = re.search(r"## 8\. Machine-readable JSON summary\.\s*```json\s*(\{.*?\})\s*```", text, re.S)
    if not match:
        raise AssertionError("Machine-readable JSON summary block not found")
    return json.loads(match.group(1))


def extract_frontmatter(text: str) -> dict:
    match = re.match(r"---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not match:
        raise AssertionError("frontmatter block not found")
    data = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


class DGUExpandedIdentityFieldSourceScopeBundleAudit(unittest.TestCase):
    def setUp(self):
        self.text = ARTIFACT.read_text(encoding="utf-8")
        self.frontmatter = extract_frontmatter(self.text)
        self.summary = extract_json_summary(self.text)

    def test_artifact_identity_and_paths(self):
        expected_artifact = "DGUExpandedIdentityFieldSourceScopeBundle_1602_C1_L3_V1"
        expected_path = "explorations/hourly-20260625-1602-cycle1-dgu-expanded-identity-field-source-scope-bundle.md"
        expected_audit = "tests/hourly_20260625_1602_cycle1_dgu_expanded_identity_field_source_scope_bundle_audit.py"

        self.assertTrue(ARTIFACT.exists())
        self.assertTrue(AUDIT.exists())
        self.assertEqual(self.frontmatter["artifact_id"], expected_artifact)
        self.assertEqual(self.summary["artifact_id"], expected_artifact)
        self.assertEqual(self.frontmatter["owned_path"], expected_path)
        self.assertEqual(self.summary["owned_path"], expected_path)
        self.assertEqual(self.frontmatter["companion_audit"], expected_audit)
        self.assertEqual(self.summary["companion_audit"], expected_audit)

    def test_required_decision_controls(self):
        self.assertEqual(self.summary["run_id"], "hourly-20260625-1602")
        self.assertEqual(self.summary["verdict_class"], "blocked")
        self.assertFalse(self.summary["actual_identity_packet_present"])
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertEqual(self.summary["accepted_identity_packet_count"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["target_import_used"])
        self.assertTrue(self.summary["scoped_negative_only"])
        self.assertFalse(self.summary["global_no_go_promoted"])
        self.assertFalse(self.summary["global_negative_claimed"])

    def test_promotion_firewall_booleans(self):
        firewall = self.summary["promotion_firewall"]
        self.assertTrue(firewall["block_bosonic_locator_to_actual_identity"])
        self.assertTrue(firewall["block_typed_spine_to_source_receipt"])
        self.assertTrue(firewall["block_scoped_negative_to_global_no_go"])
        self.assertTrue(firewall["block_vz_replay_without_actual_packet"])

        booleans = self.summary["promotion_firewall_booleans"]
        self.assertFalse(booleans["global_no_go_promoted"])
        self.assertFalse(booleans["claim_promotion_allowed"])
        self.assertFalse(booleans["proof_restart_allowed"])
        self.assertFalse(booleans["target_import_used"])
        self.assertFalse(booleans["actual_identity_packet_present"])
        self.assertTrue(booleans["scoped_negative_only"])

    def test_source_scope_and_next_object_are_explicit(self):
        self.assertGreaterEqual(self.summary["source_window_count"], 9)
        self.assertEqual(len(self.summary["source_windows_checked"]), self.summary["source_window_count"])
        self.assertIn("Oxford_023510_bosonic_frame_route", self.summary["source_windows_checked"])
        self.assertIn("typed_operator_action_spine_proposal_window", self.summary["source_windows_checked"])
        self.assertEqual(
            self.summary["first_obstruction"],
            "missing_source_emitted_actual_DGU_01_identity_packet_with_sector_rule_and_family_identity",
        )
        self.assertEqual(self.summary["first_missing_field"], "source_emitted_sector_rule")
        self.assertEqual(self.summary["next_object"], "SourceEmittedActualDGU01IdentityPacket_V1")
        self.assertIn("sector_rule", self.summary["minimum_next_object_fields"])
        self.assertIn("family_identity_to_DGU_VZ_actual_family", self.summary["minimum_next_object_fields"])

    def test_dgu_vz_consequences_remain_blocked(self):
        consequence = self.summary["dgu_vz_consequence"]
        self.assertFalse(consequence["symbol_certificate_allowed"])
        self.assertFalse(consequence["vz_replay_allowed"])
        self.assertFalse(consequence["vz_evasion_promotion_allowed"])
        self.assertFalse(consequence["physical_recovery_promotion_allowed"])
        self.assertTrue(consequence["constructive_route_live"])
        self.assertEqual(consequence["route_status"], "blocked_on_source_identity_packet")
        self.assertEqual(self.summary["accepted_positive_fields"], [])


if __name__ == "__main__":
    unittest.main()
