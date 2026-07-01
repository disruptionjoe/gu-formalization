import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "explorations" / "hourly-20260625-1702-cycle1-dgu-actual-01-source-surface-receipt.md"
AUDIT = ROOT / "tests" / "hourly_20260625_1702_cycle1_dgu_actual_01_source_surface_receipt_audit.py"


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


class DGUActual01SourceSurfaceReceiptAudit(unittest.TestCase):
    def setUp(self):
        self.text = ARTIFACT.read_text(encoding="utf-8")
        self.frontmatter = extract_frontmatter(self.text)
        self.summary = extract_json_summary(self.text)

    def test_identity_and_owned_paths(self):
        self.assertEqual(self.summary["run_id"], "hourly-20260625-1702")
        self.assertEqual(
            self.summary["artifact_id"],
            "OxfordManuscriptUCSDSourceSurfaceReceiptForSourceEmittedActualDGU01IdentityPacket_V1",
        )
        expected_artifact = "explorations/hourly-20260625-1702-cycle1-dgu-actual-01-source-surface-receipt.md"
        expected_audit = "tests/hourly_20260625_1702_cycle1_dgu_actual_01_source_surface_receipt_audit.py"
        self.assertEqual(self.frontmatter["owned_path"], expected_artifact)
        self.assertEqual(self.frontmatter["companion_audit"], expected_audit)
        self.assertEqual(self.summary["owned_path"], expected_artifact)
        self.assertEqual(self.summary["companion_audit"], expected_audit)
        self.assertTrue(AUDIT.exists())

    def test_gate_counts_and_no_restart(self):
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertEqual(self.summary["accepted_source_surface_row_count"], 0)
        self.assertFalse(self.summary["actual_identity_packet_present"])
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["vz_replay_allowed"])
        self.assertFalse(self.summary["symbol_certificate_allowed"])
        self.assertFalse(self.summary["target_import_used"])
        self.assertFalse(self.summary["claim_promotion_allowed"])
        self.assertFalse(self.summary["global_no_go_promoted"])

    def test_required_field_matrix_contract(self):
        fields = {row["field"]: row for row in self.summary["required_field_matrix"]}
        expected_fields = {
            "source_surface",
            "sector_rule",
            "domain",
            "codomain",
            "coefficients",
            "Q_projector_relation",
            "symbol_relation",
            "family_identity",
            "same_operator_witness",
            "target_import_screen",
        }
        self.assertEqual(set(fields), expected_fields)
        self.assertEqual(self.summary["required_field_counts"]["field_count"], 10)
        self.assertEqual(self.summary["required_field_counts"]["accepted"], 0)
        for row in fields.values():
            self.assertIs(row["accepted"], False)
        self.assertEqual(fields["sector_rule"]["status"], "absent")
        self.assertEqual(fields["Q_projector_relation"]["status"], "adjacent_only")
        self.assertEqual(fields["symbol_relation"]["status"], "adjacent_only")

    def test_source_surface_rows(self):
        rows = {row["id"]: row for row in self.summary["source_surface_rows"]}
        self.assertEqual(set(rows), {
            "local_2021_manuscript_pdf",
            "ucsd_2025_transcript",
            "oxford_media_index",
            "prior_oxford_frame_artifacts",
        })
        self.assertEqual(rows["local_2021_manuscript_pdf"]["status"], "inspected")
        self.assertEqual(rows["ucsd_2025_transcript"]["packet_decision"], "adjacent_only")
        self.assertEqual(rows["oxford_media_index"]["packet_decision"], "locator_only_not_packet")
        self.assertFalse(any(row["accepted"] for row in rows.values()))
        self.assertIn("D_GU", self.summary["local_pdf"]["literal_tokens_absent"])
        self.assertIn("Q_in", self.summary["local_pdf"]["literal_tokens_absent"])
        self.assertIn("lambda_d", self.summary["local_pdf"]["literal_tokens_absent"])

    def test_obstruction_next_object_and_promotion_firewall(self):
        self.assertEqual(
            self.summary["first_obstruction"],
            "missing_source_emitted_sector_rule_for_actual_D_GU_epsilon_0_1_identity_packet",
        )
        self.assertEqual(self.summary["first_missing_field"], "sector_rule")
        self.assertEqual(self.summary["next_object"], "SourceEmittedActualDGU01IdentityPacket_V1")
        self.assertIn("source_stable_Oxford_frames", self.summary["constructive_next_object"])
        firewall = self.summary["promotion_firewall"]
        self.assertTrue(firewall["block_typed_spine_to_actual_packet"])
        self.assertTrue(firewall["block_adjacent_DGU_VZ_spine_to_source_receipt"])
        self.assertTrue(firewall["block_oxford_bosonic_anchor_to_0_1_identity"])
        self.assertTrue(firewall["block_manuscript_action_EL_cluster_to_actual_DGU_identity"])
        self.assertTrue(firewall["block_ucsd_family_language_to_same_operator_packet"])
        self.assertTrue(firewall["block_vz_replay_without_actual_packet"])
        self.assertTrue(firewall["block_symbol_certificate_without_actual_packet"])
        self.assertTrue(firewall["block_scoped_negative_to_global_no_go"])


if __name__ == "__main__":
    unittest.main()
