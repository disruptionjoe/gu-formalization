import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "explorations" / "hourly-20260625-1503-cycle2-dgu-actual-01-source-window-packet.md"
AUDIT = ROOT / "tests" / "hourly_20260625_1503_cycle2_dgu_actual_01_source_window_packet_audit.py"


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


class DGUActual01SourceWindowPacketAudit(unittest.TestCase):
    def setUp(self):
        self.text = ARTIFACT.read_text(encoding="utf-8")
        self.frontmatter = extract_frontmatter(self.text)
        self.summary = extract_json_summary(self.text)

    def test_artifact_and_audit_paths(self):
        self.assertTrue(ARTIFACT.exists())
        self.assertTrue(AUDIT.exists())
        expected_artifact = "explorations/hourly-20260625-1503-cycle2-dgu-actual-01-source-window-packet.md"
        expected_audit = "tests/hourly_20260625_1503_cycle2_dgu_actual_01_source_window_packet_audit.py"
        self.assertEqual(self.frontmatter["owned_path"], expected_artifact)
        self.assertEqual(self.frontmatter["companion_audit"], expected_audit)
        self.assertEqual(self.summary["owned_path"], expected_artifact)
        self.assertEqual(self.summary["companion_audit"], expected_audit)

    def test_json_summary_required_fields(self):
        expected = {
            "source_window_declared": True,
            "source_window_inspected": True,
            "actual_01_packet_present": False,
            "sector_rule_present": False,
            "typed_domain_present": False,
            "typed_codomain_present": False,
            "coefficient_convention_present": False,
            "Q_projector_relation_present": False,
            "symbol_data_present": False,
            "family_identity_present": False,
            "actual_identity_witness_present": False,
            "scoped_negative_broadened": True,
            "vz_replay_allowed": False,
            "target_import_used": False,
        }
        for field, value in expected.items():
            self.assertIn(field, self.summary)
            self.assertIs(self.summary[field], value, field)

    def test_packet_identity_and_no_promotion_controls(self):
        self.assertEqual(self.summary["artifact_id"], "DGUActual01SectorIdentityPacket_V1")
        self.assertEqual(
            self.summary["first_exact_obstruction"],
            "missing_source_emitted_actual_DGU_01_sector_identity_packet_with_sector_rule",
        )
        self.assertEqual(self.summary["first_missing_field"], "sector_rule")
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["symbol_certificate_allowed"])
        self.assertFalse(self.summary["global_negative_claimed"])
        self.assertEqual(self.summary["accepted_positive_fields"], [])

    def test_source_window_is_tighter_and_inspected(self):
        methods = set(self.summary["source_window_inspection_methods"])
        self.assertIn("PyMuPDF_full_pdf_text_token_check", methods)
        self.assertIn("prior_rendered_manual_display_packet_for_pages_43_48_and_55_58", methods)
        self.assertIn("UCSD_transcript_window_read", methods)
        self.assertIn("D_GU", self.summary["local_pdf"]["literal_tokens_absent"])
        self.assertIn("Q_in", self.summary["local_pdf"]["literal_tokens_absent"])
        self.assertIn("lambda_d", self.summary["local_pdf"]["literal_tokens_absent"])


if __name__ == "__main__":
    unittest.main()
