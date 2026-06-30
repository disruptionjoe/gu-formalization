import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "explorations" / "hourly-20260625-1702-cycle2-dgu-sector-rule-same-operator-matrix.md"
AUDIT = ROOT / "tests" / "hourly_20260625_1702_cycle2_dgu_sector_rule_same_operator_matrix_audit.py"


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


class DGUSectorRuleSameOperatorMatrixAudit(unittest.TestCase):
    def setUp(self):
        self.text = ARTIFACT.read_text(encoding="utf-8")
        self.frontmatter = extract_frontmatter(self.text)
        self.summary = extract_json_summary(self.text)

    def test_identity_and_owned_paths(self):
        self.assertEqual(self.summary["run_id"], "hourly-20260625-1702")
        self.assertEqual(self.summary["cycle"], 2)
        self.assertEqual(self.summary["lane"], 3)
        self.assertEqual(
            self.summary["artifact_id"],
            "DGUSectorRuleSameOperatorAdmissionMatrix_V1",
        )
        expected_artifact = "explorations/hourly-20260625-1702-cycle2-dgu-sector-rule-same-operator-matrix.md"
        expected_audit = "tests/hourly_20260625_1702_cycle2_dgu_sector_rule_same_operator_matrix_audit.py"
        self.assertEqual(self.frontmatter["owned_path"], expected_artifact)
        self.assertEqual(self.frontmatter["companion_audit"], expected_audit)
        self.assertEqual(self.summary["owned_path"], expected_artifact)
        self.assertEqual(self.summary["companion_audit"], expected_audit)
        self.assertTrue(AUDIT.exists())

    def test_required_same_operator_rows(self):
        rows = {row["row"]: row for row in self.summary["same_operator_field_rows"]}
        expected_rows = {
            "source-emitted sector rule",
            "actual D_GU^epsilon identity statement",
            "domain/codomain",
            "coefficients",
            "Q/projector relation",
            "symbol relation",
            "family identity",
            "source surface",
            "same-operator witness",
            "no typed-spine substitution",
        }
        self.assertEqual(set(rows), expected_rows)
        self.assertEqual(self.summary["same_operator_row_counts"]["row_count"], 10)

    def test_missing_sector_rule_and_packet_rejection(self):
        rows = {row["row"]: row for row in self.summary["same_operator_field_rows"]}
        self.assertEqual(rows["source-emitted sector rule"]["status"], "missing")
        self.assertIs(rows["source-emitted sector rule"]["accepted"], False)
        self.assertIs(self.summary["accepted_sector_rule"], False)
        self.assertIs(self.summary["accepted_packet"], False)
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertIs(self.summary["actual_identity_packet_present"], False)

    def test_no_replay_import_or_certificate(self):
        self.assertIs(self.summary["proof_restart_allowed"], False)
        self.assertIs(self.summary["target_import_used"], False)
        self.assertIs(self.summary["vz_replay_allowed"], False)
        self.assertIs(self.summary["symbol_certificate_allowed"], False)
        firewall = self.summary["promotion_firewall"]
        self.assertTrue(firewall["block_vz_replay_without_actual_packet"])
        self.assertTrue(firewall["block_symbol_certificate_without_actual_packet"])
        self.assertTrue(firewall["block_scoped_negative_to_global_no_go"])

    def test_first_obstruction_and_next_object(self):
        self.assertEqual(
            self.summary["first_obstruction"],
            "missing_source_emitted_sector_rule_for_actual_D_GU_epsilon_0_1_same_operator_packet",
        )
        self.assertEqual(self.summary["first_missing_field"], "source-emitted sector rule")
        self.assertEqual(self.summary["next_object"], "SourceEmittedActualDGU01SameOperatorPacket_V1")
        self.assertIn("source_stable_Oxford", self.summary["constructive_next_object"])

    def test_typed_spine_not_accepted_as_actual_packet(self):
        rows = {row["row"]: row for row in self.summary["same_operator_field_rows"]}
        typed_spine_guard = rows["no typed-spine substitution"]
        self.assertEqual(typed_spine_guard["status"], "present")
        self.assertIs(typed_spine_guard["accepted"], True)
        self.assertIs(self.summary["typed_spine_substitution_accepted"], False)
        self.assertTrue(self.summary["promotion_firewall"]["block_typed_spine_to_actual_packet"])
        self.assertEqual(self.summary["same_operator_row_counts"]["packet_accepted_rows"], 0)
        self.assertEqual(self.summary["same_operator_row_counts"]["guard_accepted_rows"], 1)

    def test_adjacent_rows_are_non_admitting(self):
        rows = {row["row"]: row for row in self.summary["same_operator_field_rows"]}
        for name in ["domain/codomain", "Q/projector relation", "symbol relation"]:
            self.assertEqual(rows[name]["status"], "adjacent")
            self.assertIs(rows[name]["accepted"], False)
        self.assertEqual(self.summary["same_operator_row_counts"]["adjacent_rows"], 3)


if __name__ == "__main__":
    unittest.main()
