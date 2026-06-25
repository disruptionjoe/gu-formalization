import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "explorations" / "hourly-20260625-0703-cycle1-rs-equation-1010-image-level-recheck.md"


def load_json_summary():
    text = ARTIFACT.read_text(encoding="utf-8")
    match = re.search(r"```json\s*(\{.*?\})\s*```", text, re.DOTALL)
    if not match:
        raise AssertionError("JSON Summary fenced block not found")
    return text, json.loads(match.group(1))


class ManualImageLevelRSFormulaDiagramAudit(unittest.TestCase):
    def setUp(self):
        self.text, self.summary = load_json_summary()

    def test_required_target_and_identity_fields_are_recorded(self):
        self.assertEqual(self.summary["artifact"], "ManualImageLevelRSFormulaDiagramAudit_V1")
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0703")
        self.assertEqual(self.summary["cycle"], 1)
        self.assertEqual(self.summary["lane"], 4)
        self.assertEqual(self.summary["artifact_id"], "ManualImageLevelRSFormulaDiagramAudit_V1")
        self.assertEqual(self.summary["equation_target"], "10.10")

    def test_scoped_negative_not_global_no_go(self):
        self.assertEqual(self.summary["verdict"], "fail")
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertTrue(self.summary["scoped_negative_preserved"])
        self.assertFalse(self.summary["global_no_go_promoted"])
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertIn("not a global", self.text.lower())

    def test_no_proof_restart_and_no_accepted_receipt_language(self):
        forbidden_acceptance_phrases = [
            "equation 10.10 is an accepted rs differential receipt",
            "proof_restart_allowed: true",
            "\"proof_restart_allowed\": true",
            "\"accepted_receipt_count\": 1",
            "\"global_no_go_promoted\": true",
        ]
        lowered = self.text.lower()
        for phrase in forbidden_acceptance_phrases:
            self.assertNotIn(phrase, lowered)

    def test_inspected_assets_include_image_level_and_context_assets(self):
        assets = self.summary["inspected_assets"]
        self.assertIn(
            "Geometric_UnityDraftApril1st2021.pdf#page_index_48_printed_page_49_equation_10.10",
            assets,
        )
        self.assertIn("tmp_pdf_text_pages/page-049.txt", assets)
        self.assertTrue(any(asset.startswith("scratch_render:") for asset in assets))

    def test_first_obstruction_and_next_frontier_are_specific(self):
        obstruction = self.summary["first_obstruction"]
        self.assertIn("d_RS,-1", obstruction)
        self.assertIn("stable RS-only source rule", obstruction)
        self.assertEqual(
            self.summary["next_frontier_object"],
            "AlternatePrimarySourceSearchForSourceEmittedRSMinusOneRule_V1",
        )
        self.assertEqual(
            self.summary["companion_audit"],
            "tests/hourly_20260625_0703_cycle1_rs_equation_1010_image_level_recheck_audit.py",
        )


if __name__ == "__main__":
    unittest.main()
