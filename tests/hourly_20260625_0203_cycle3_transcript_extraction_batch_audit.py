#!/usr/bin/env python3
"""Audit TranscriptExtractionBatch_V1.

The audit parses the embedded JSON summary and checks that the cycle 3 lane 1
gate is a protocol, not a transcript acquisition result: all six required
source groups are included, accepted receipts are zero, proof restart is
blocked, negative receipts require complete transcript scope plus query logs,
and no claim promotion is allowed.
"""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0203-cycle3-transcript-extraction-batch.md"
)

REQUIRED_GROUPS = {
    "JRE_1453",
    "JRE_1628",
    "TOE_JAIMUNGAL_GU_40",
    "KEATING_QG",
    "KEATING_DESI",
    "KEATING_REVEALED_1_2",
}

REQUIRED_ROW_FIELDS = {
    "source_id",
    "transcript_origin",
    "locator",
    "exact_fragment",
    "family_query_hits",
    "emitted_object_type",
    "emitted_formula_or_rule",
    "intake_status",
}


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing transcript extraction artifact: {DOC}") from exc


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 9\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class TranscriptExtractionBatchAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity(self) -> None:
        self.assertEqual(self.summary["artifact"], "TranscriptExtractionBatch_V1")
        self.assertEqual(self.summary["version"], "2026-06-25")
        self.assertEqual(self.summary["run"], "hourly-20260625-0203")
        self.assertEqual(self.summary["cycle"], 3)
        self.assertEqual(self.summary["lane"], 1)
        identity = self.summary["artifact_identity"]
        self.assertEqual(
            identity["owned_path"],
            "explorations/hourly-20260625-0203-cycle3-transcript-extraction-batch.md",
        )
        self.assertEqual(
            identity["companion_audit"],
            "tests/hourly_20260625_0203_cycle3_transcript_extraction_batch_audit.py",
        )

    def test_includes_six_required_transcript_source_groups(self) -> None:
        groups = self.summary["required_source_groups"]
        group_ids = {group["group_id"] for group in groups}
        self.assertEqual(group_ids, REQUIRED_GROUPS)
        group_text = json.dumps(groups, sort_keys=True)
        for expected in [
            "GU-MEDIA-2020-JRE-1453",
            "GU-POD-2021-JRE-1628",
            "GU-POD-2025-TOE-JAIMUNGAL-GU-40",
            "GU-MEDIA-KEATING-QG-FBOZSSLXFVI",
            "GU-POD-2025-KEATING-DESI-GU",
            "GU-POD-2021-KEATING-REVEALED-1",
            "GU-POD-2021-KEATING-REVEALED-2",
        ]:
            self.assertIn(expected, group_text)
        for group in groups:
            self.assertFalse(group["transcript_body_acquired"], group["group_id"])
            self.assertEqual(group["intake_status_now"], "missing")
            self.assertFalse(group["proof_restart_allowed"], group["group_id"])
            self.assertGreater(len(group["query_set"]), 0, group["group_id"])

    def test_scope_controls_are_protocol_only(self) -> None:
        controls = self.summary["scope_controls"]
        self.assertFalse(controls["transcript_bodies_acquired_in_this_lane"])
        self.assertFalse(controls["browsing_or_acquisition_performed"])
        self.assertFalse(controls["copyrighted_transcript_bodies_ingested"])
        self.assertTrue(controls["protocol_ready_to_execute_after_acquisition"])

    def test_accepted_receipts_zero_and_restart_blocked(self) -> None:
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertTrue(self.summary["claim_promotion_forbidden"])
        self.assertIn("accepted receipts zero", self.text)
        self.assertIn("proof restart blocked", self.text)

    def test_row_schema_includes_required_fields(self) -> None:
        row_schema = set(self.summary["row_schema"])
        self.assertTrue(REQUIRED_ROW_FIELDS <= row_schema)
        self.assertIn("promotion_allowed", row_schema)
        self.assertIn("restart_gate", row_schema)

    def test_negative_receipt_requires_complete_transcript_and_query_log(self) -> None:
        requirements = self.summary["negative_receipt_requirements"]
        self.assertTrue(requirements["complete_acquired_transcript_scope"])
        self.assertTrue(requirements["declared_source_scope"])
        self.assertTrue(requirements["family_specific_query_log_preserved"])
        self.assertTrue(requirements["notation_variants_and_synonyms_logged"])
        self.assertTrue(
            requirements["inspected_hit_list_and_false_positive_decisions_logged"]
        )
        self.assertTrue(requirements["exact_required_object_absence_stated"])
        self.assertFalse(requirements["target_import_used_for_selection"])
        self.assertFalse(requirements["promotion_allowed"])
        self.assertEqual(requirements["restart_gate"], "blocked")
        self.assertIn("complete_acquired_transcript_scope", self.text)
        self.assertIn("family_specific_query_log_preserved", self.text)

    def test_no_claim_promotion(self) -> None:
        promotions = self.summary["no_claim_promotions"]
        for key, value in promotions.items():
            self.assertFalse(value, key)
        self.assertIn("No GU claim is promoted.", self.text)
        self.assertIn("source_contains_required_object_before_transcript_acquisition", " ".join(self.summary["forbidden_promotions"]))
        self.assertIn("negative_receipt_without_complete_transcript_and_query_log", " ".join(self.summary["forbidden_promotions"]))

    def test_first_obstruction_is_transcript_body_acquisition(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(
            obstruction["id"],
            "TranscriptExtractionBatch_V1.source_groups.transcript_body_acquired",
        )
        self.assertTrue(obstruction["missing_for_all_required_source_groups"])
        self.assertIn("complete acquired transcript body", obstruction["description"])
        self.assertIn("query log", obstruction["description"])


if __name__ == "__main__":
    unittest.main()
