import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "explorations" / "hourly-20260625-1802-cycle1-dgu-source-emitted-actual-01-same-operator-packet.md"
AUDIT = ROOT / "tests" / "hourly_20260625_1802_cycle1_dgu_source_emitted_actual_01_same_operator_packet_audit.py"


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


class DGUSourceEmittedActual01SameOperatorPacketAudit(unittest.TestCase):
    def setUp(self):
        self.text = ARTIFACT.read_text(encoding="utf-8")
        self.frontmatter = extract_frontmatter(self.text)
        self.summary = extract_json_summary(self.text)

    def test_identity_and_owned_paths(self):
        expected_artifact = "explorations/hourly-20260625-1802-cycle1-dgu-source-emitted-actual-01-same-operator-packet.md"
        expected_audit = "tests/hourly_20260625_1802_cycle1_dgu_source_emitted_actual_01_same_operator_packet_audit.py"
        self.assertEqual(self.summary["run_id"], "hourly-20260625-1802")
        self.assertEqual(self.summary["artifact_id"], "SourceEmittedActualDGU01SameOperatorPacket_V1")
        self.assertEqual(self.summary["artifact_path"], expected_artifact)
        self.assertEqual(self.summary["owned_path"], expected_artifact)
        self.assertEqual(self.summary["companion_audit"], expected_audit)
        self.assertEqual(self.frontmatter["owned_path"], expected_artifact)
        self.assertEqual(self.frontmatter["companion_audit"], expected_audit)
        self.assertTrue(AUDIT.exists())

    def test_packet_not_admitted_and_no_receipts(self):
        self.assertIs(self.summary["packet_admitted"], False)
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertEqual(self.summary["accepted_packet_field_count"], 0)

    def test_required_source_emission_fields_are_false(self):
        self.assertIs(self.summary["sector_rule_source_emitted"], False)
        self.assertIs(self.summary["same_operator_witness_source_emitted"], False)
        rows = {row["field"]: row for row in self.summary["same_operator_field_rows"]}
        self.assertIs(rows["source_emitted_sector_rule"]["source_emitted"], False)
        self.assertIs(rows["source_emitted_sector_rule"]["accepted"], False)
        self.assertIs(rows["same_operator_witness"]["source_emitted"], False)
        self.assertIs(rows["same_operator_witness"]["accepted"], False)

    def test_typed_spine_substitution_is_false(self):
        self.assertIs(self.summary["typed_spine_substitution"], False)
        self.assertIs(self.summary["typed_spine_substitution_accepted"], False)
        self.assertTrue(self.summary["promotion_firewall"]["block_typed_spine_to_actual_packet"])

    def test_no_vz_replay_or_symbol_certification_unless_packet_admitted(self):
        if not self.summary["packet_admitted"]:
            self.assertIs(self.summary["vz_replay_allowed"], False)
            self.assertIs(self.summary["symbol_certification_allowed"], False)
        self.assertTrue(self.summary["promotion_firewall"]["block_vz_replay_without_actual_packet"])
        self.assertTrue(self.summary["promotion_firewall"]["block_symbol_certificate_without_actual_packet"])

    def test_blocked_artifact_has_nonempty_required_missing_fields(self):
        self.assertEqual(self.summary["verdict_class"], "blocked")
        missing = self.summary["required_missing_fields"]
        self.assertIsInstance(missing, list)
        self.assertGreater(len(missing), 0)
        self.assertIn("source_emitted_sector_rule", missing)
        self.assertIn("same_operator_witness", missing)

    def test_first_obstruction_and_next_receipt(self):
        self.assertEqual(
            self.summary["first_obstruction"],
            "missing_source_emitted_sector_rule_for_actual_D_GU_epsilon_0_1_same_operator_packet",
        )
        self.assertEqual(self.summary["first_missing_field"], "source_emitted_sector_rule")
        self.assertEqual(
            self.summary["minimal_source_emitted_receipt_needed_next"],
            "SourceEmittedDGU01SectorRuleAndSameOperatorWitnessReceipt_V1",
        )


if __name__ == "__main__":
    unittest.main()
