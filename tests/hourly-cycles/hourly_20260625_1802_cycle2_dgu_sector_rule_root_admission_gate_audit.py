import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "explorations" / "hourly-20260625-1802-cycle2-dgu-sector-rule-root-admission-gate.md"
AUDIT = ROOT / "tests" / "hourly_20260625_1802_cycle2_dgu_sector_rule_root_admission_gate_audit.py"


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


class DGUSectorRuleRootAdmissionGateAudit(unittest.TestCase):
    def setUp(self):
        self.text = ARTIFACT.read_text(encoding="utf-8")
        self.frontmatter = extract_frontmatter(self.text)
        self.summary = extract_json_summary(self.text)

    def test_identity_and_paths(self):
        expected_artifact = "explorations/hourly-20260625-1802-cycle2-dgu-sector-rule-root-admission-gate.md"
        expected_audit = "tests/hourly_20260625_1802_cycle2_dgu_sector_rule_root_admission_gate_audit.py"
        self.assertEqual(self.summary["run_id"], "hourly-20260625-1802")
        self.assertEqual(self.summary["artifact_path"], expected_artifact)
        self.assertEqual(self.summary["owned_path"], expected_artifact)
        self.assertEqual(self.summary["companion_audit"], expected_audit)
        self.assertEqual(self.frontmatter["owned_path"], expected_artifact)
        self.assertEqual(self.frontmatter["companion_audit"], expected_audit)
        self.assertTrue(AUDIT.exists())

    def test_root_gate_blocks_all_bypasses(self):
        self.assertIs(self.summary["sector_rule_root_required"], True)
        self.assertIs(self.summary["adjacent_surface_bypass_allowed"], False)
        self.assertIs(self.summary["typed_spine_substitution_allowed"], False)
        self.assertIs(self.summary["packet_admitted"], False)
        self.assertEqual(self.summary["accepted_receipt_count"], 0)

    def test_no_symbol_certificate_vz_replay_or_proof_restart(self):
        self.assertIs(self.summary["symbol_certificate_allowed"], False)
        self.assertIs(self.summary["vz_replay_allowed"], False)
        self.assertIs(self.summary["proof_restart_allowed"], False)
        consequence = self.summary["dgu_vz_consequence"]
        self.assertIs(consequence["symbol_certificate_allowed"], False)
        self.assertIs(consequence["vz_replay_allowed"], False)
        self.assertIs(consequence["proof_restart_allowed"], False)

    def test_next_object_names_sector_rule_and_same_operator_receipt(self):
        next_object = self.summary["next_object"]
        self.assertIn("SectorRule", next_object)
        self.assertIn("SameOperator", next_object)
        self.assertIn("Receipt", next_object)
        self.assertEqual(
            next_object,
            "SourceEmittedDGU01SectorRuleAndSameOperatorReceipt_V1",
        )
        self.assertIn("sector rule", self.summary["next_object_description"])
        self.assertIn("same-operator receipt", self.summary["next_object_description"])

    def test_gate_rows_do_not_admit_source_or_bypass_routes(self):
        rows = {row["row"]: row for row in self.summary["admission_gate_rows"]}
        required_false_rows = [
            "source_emitted_sector_rule",
            "same_operator_witness",
            "actual_same_operator_packet",
            "adjacent_source_surface_bypass",
            "typed_spine_substitution",
            "Q_projector_row_bypass",
            "symbol_certificate_bypass",
            "VZ_replay_bypass",
        ]
        for row_name in required_false_rows:
            with self.subTest(row=row_name):
                self.assertIn(row_name, rows)
                self.assertIs(rows[row_name]["admitted"], False)

    def test_bypass_decisions_all_false(self):
        decisions = self.summary["bypass_decisions"]
        for route in [
            "adjacent_source_surfaces",
            "typed_spines",
            "symbol_relations",
            "candidate_Q_projector_rows",
            "VZ_replay",
        ]:
            with self.subTest(route=route):
                self.assertIn(route, decisions)
                self.assertIs(decisions[route]["allowed"], False)

    def test_required_receipt_fields_include_root_receipt(self):
        fields = self.summary["required_receipt_fields"]
        self.assertIn("source_emitted_sector_rule_selecting_actual_D_GU_epsilon_0_1_object", fields)
        self.assertIn("same_operator_witness_to_DGU_VZ_actual_family", fields)
        self.assertIn("typed_spine_exclusion", fields)


if __name__ == "__main__":
    unittest.main()
