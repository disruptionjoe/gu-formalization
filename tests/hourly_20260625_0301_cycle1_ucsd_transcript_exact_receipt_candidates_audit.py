#!/usr/bin/env python3
"""Audit UCSDTranscriptExactReceiptCandidates_V1.

The audit checks that the transcript-only lane instantiated all four UCSD
timestamp windows as candidate rows while making no visual-capture claim, no
accepted receipt claim, no proof restart, and no family proof promotion.
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
    / "hourly-20260625-0301-cycle1-ucsd-transcript-exact-receipt-candidates.md"
)

EXPECTED_WINDOWS = {
    "[00:02:05]-[00:04:08]",
    "[00:18:03]-[00:24:00]",
    "[00:34:27]-[00:36:13]",
    "[00:48:49]-[00:50:09]",
}

EXPECTED_ROW_GROUPS = {
    "UCSD_TXT_EXACT_001_DGU_dark_energy_formula",
    "UCSD_TXT_EXACT_002_DGU_theta_double_quotient",
    "UCSD_TXT_EXACT_003_IG_RS_shiab_complex",
    "UCSD_TXT_EXACT_004_QFT_DGU_unified_field_content",
}


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing UCSD transcript candidate artifact: {DOC}") from exc


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 9\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class UCSDTranscriptExactReceiptCandidatesAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)
        cls.rows = cls.summary["candidate_row_groups"]

    def test_artifact_identity(self) -> None:
        self.assertEqual(self.summary["artifact"], "UCSDTranscriptExactReceiptCandidates_V1")
        self.assertEqual(self.summary["version"], "2026-06-25")
        self.assertEqual(self.summary["run"], "hourly-20260625-0301")
        self.assertEqual(self.summary["cycle"], 1)
        self.assertEqual(self.summary["lane"], 5)
        self.assertEqual(self.summary["verdict_class"], "conditional")

    def test_all_four_timestamp_windows_checked(self) -> None:
        self.assertEqual(set(self.summary["timestamp_windows_checked"]), EXPECTED_WINDOWS)
        row_windows = {row["timestamp_locator"] for row in self.rows}
        self.assertEqual(row_windows, EXPECTED_WINDOWS)

    def test_all_four_candidate_row_groups_present(self) -> None:
        row_ids = {row["row_group_id"] for row in self.rows}
        self.assertEqual(row_ids, EXPECTED_ROW_GROUPS)
        self.assertEqual(len(self.rows), 4)

    def test_transcript_only_no_visual_capture_claim(self) -> None:
        scope = self.summary["scope"]
        self.assertIs(scope["transcript_scope_only"], True)
        self.assertIs(scope["browsing_performed"], False)
        self.assertIs(scope["visual_material_captured"], False)
        self.assertIs(scope["image_capture_performed"], False)
        self.assertIs(scope["visual_capture_claim"], False)
        self.assertIn("This lane performed no browsing and no image capture.", self.text)

    def test_accepted_receipt_count_explicit_zero(self) -> None:
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertEqual(self.summary["accepted_receipts"], [])
        self.assertIn("Accepted receipt count from these transcript-only rows: **0**.", self.text)
        for row in self.rows:
            self.assertIs(row["accepted_for_routing"], False, row["row_group_id"])
            self.assertEqual(row["acceptance_status"], "quarantined_transcript_hint")

    def test_no_proof_restart_or_family_promotion(self) -> None:
        self.assertIs(self.summary["proof_restart_allowed"], False)
        self.assertIs(self.summary["family_proof_promotion_allowed"], False)
        self.assertIs(self.summary["claim_promotion_allowed"], False)
        for row in self.rows:
            self.assertEqual(row["restart_gate"], "blocked", row["row_group_id"])
        promotions = self.summary["no_claim_promotions"]
        for key, value in promotions.items():
            self.assertIs(value, False, key)

    def test_rows_have_required_receipt_fields_and_no_target_data(self) -> None:
        for row in self.rows:
            for key in [
                "source_id",
                "timestamp_locator",
                "families",
                "required_object",
                "exact_local_transcript_basis",
                "emitted_object_type",
                "formula_rule_status",
                "target_import_flags",
                "acceptance_status",
                "restart_gate",
            ]:
                self.assertIn(key, row, row["row_group_id"])
            self.assertEqual(row["source_id"], "RepoLocalUCSDTranscript_2025_04")
            self.assertEqual(row["formula_rule_status"], "not_source_emitted_required_family_object")
            self.assertEqual(row["target_import_flags"]["target_data_seen"], [])
            self.assertIs(row["target_import_flags"]["target_import_detected"], False)
            self.assertIs(row["slide_or_frame_capture_remains_required"], True)


if __name__ == "__main__":
    unittest.main()
