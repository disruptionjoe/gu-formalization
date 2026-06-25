#!/usr/bin/env python3
"""Audit TOEJaimungalModernTranscriptReceiptExecution_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0502-cycle1-toe-jaimungal-modern-transcript-receipt-execution.md"
)

EXPECTED_HEADINGS = [
    "## 1. Verdict",
    "## 2. What Was Derived Directly From Repo/Source Surfaces",
    "## 3. Strongest Positive Locator Or Construction Attempt",
    "## 4. First Exact Obstruction Or Missing Proof/Source Object",
    "## 5. Constructive Next Object That Would Remove Or Test The Obstruction",
    "## 6. What This Means For The Relevant GU Claim",
    "## 7. Next Meaningful Source/Proof Computation Step",
    "## 9. Machine-Readable JSON Summary",
]

REQUIRED_FAMILIES = {"IG", "RS", "QFT", "DGU_VZ"}

REQUIRED_OBJECTS = {
    "IG": "SourceForcedCodomainSelectorForK_IG",
    "RS": "source.action_or_operator for d_RS,-1",
    "QFT": "P_fin^b: F_phys^b(O) -> K_b",
    "DGU_VZ": "operator_source_primary_action_or_EL for D_GU^epsilon 0/1",
}

EXPECTED_SOURCE_ID = "GU-POD-2025-TOE-JAIMUNGAL-GU-40"


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing TOE/Jaimungal artifact: {DOC}") from exc


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 9\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class TOEJaimungalModernTranscriptReceiptExecutionAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_required_sections_present(self) -> None:
        for heading in EXPECTED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_artifact_identity(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "TOEJaimungalModernTranscriptReceiptExecution_V1",
        )
        self.assertEqual(self.summary["run"], "hourly-20260625-0502")
        self.assertEqual(self.summary["cycle"], 1)
        self.assertEqual(self.summary["lane"], 3)
        self.assertEqual(
            self.summary["verdict"],
            "BLOCKED_LOCATORS_ONLY_NO_ACCEPTED_RECEIPTS",
        )
        identity = self.summary["artifact_identity"]
        self.assertEqual(
            identity["owned_path"],
            "explorations/hourly-20260625-0502-cycle1-toe-jaimungal-modern-transcript-receipt-execution.md",
        )
        self.assertEqual(
            identity["companion_audit"],
            "tests/hourly_20260625_0502_cycle1_toe_jaimungal_modern_transcript_receipt_execution_audit.py",
        )

    def test_source_identity_and_fetch_status(self) -> None:
        source = self.summary["source"]
        self.assertEqual(source["source_id"], EXPECTED_SOURCE_ID)
        self.assertEqual(source["video_id"], "ILlhFKuu3NQ")
        self.assertIn("youtube.com/watch?v=ILlhFKuu3NQ", source["official_video_url"])
        self.assertEqual(source["lane_status_after_execution"], "locator-confirmed; transcript-not-acquired")

        fetching = self.summary["transcript_fetching"]
        self.assertIs(fetching["attempted"], True)
        self.assertEqual(fetching["result"], "IpBlocked")
        self.assertIs(fetching["full_transcript_acquired"], False)
        self.assertIs(fetching["copyrighted_transcript_body_ingested"], False)

    def test_target_import_guard_status(self) -> None:
        guard = self.summary["target_import_guard"]
        self.assertEqual(
            guard["status"],
            "passed_for_locator_only_quarantine_not_sufficient_for_receipt_acceptance",
        )
        self.assertIs(guard["target_import_used_for_selection"], False)
        self.assertEqual(guard["target_data_seen_in_candidate_rows"], [])
        self.assertIs(guard["guard_applied_before_acceptance"], True)
        self.assertIs(guard["accepted_for_routing_allowed"], False)

    def test_required_family_coverage(self) -> None:
        coverage = self.summary["required_family_coverage"]
        self.assertEqual(set(coverage), REQUIRED_FAMILIES)
        for family, row in coverage.items():
            self.assertEqual(row["required_object"], REQUIRED_OBJECTS[family])
            self.assertIs(row["covered"], True)
            self.assertIs(row["receipt_found"], False)
            self.assertEqual(row["restart_gate"], "blocked")
            self.assertIn("first_missing_object", row)

    def test_candidate_rows_are_quarantined_and_cover_families(self) -> None:
        rows = self.summary["candidate_locator_rows"]
        self.assertEqual({row["family"] for row in rows}, REQUIRED_FAMILIES)
        for row in rows:
            family = row["family"]
            self.assertEqual(row["source_id"], EXPECTED_SOURCE_ID)
            self.assertEqual(row["required_object"], REQUIRED_OBJECTS[family])
            self.assertTrue(row["locators"])
            self.assertEqual(row["emitted_object_type"], "none_supplied")
            self.assertEqual(row["emitted_formula_or_rule"], "none")
            self.assertEqual(row["target_data_seen"], [])
            self.assertIs(row["target_import_used_for_selection"], False)
            self.assertEqual(row["acceptance_status"], "quarantined_locator_candidate")
            self.assertEqual(row["restart_gate"], "blocked")

    def test_receipt_and_promotion_gates_are_closed(self) -> None:
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertIs(self.summary["proof_restart_allowed"], False)
        self.assertIs(self.summary["claim_promotion_allowed"], False)

        promotions = self.summary["no_claim_promotions"]
        for key, value in promotions.items():
            self.assertIs(value, False, key)
        self.assertIn("No GU claim is promoted.", self.text)

    def test_first_exact_obstruction(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(
            obstruction["id"],
            "TOEJaimungalModernTranscriptReceiptExecution_V1.full_transcript_body_acquired",
        )
        self.assertEqual(
            obstruction["missing_source_object"],
            "official_primary_archived_or_checked_full_transcript_body_split_by_outline_timestamps_with_family_query_log",
        )
        self.assertIn("no complete acquired transcript/query log", obstruction["description"])

    def test_constructive_next_object(self) -> None:
        next_object = self.summary["constructive_next_object"]
        self.assertEqual(next_object["id"], "TOEJaimungalGU40TranscriptExtractionRowBatch_V1")
        self.assertEqual(
            next_object["entry_type"],
            "PrimarySourceReceiptInstance_V1_candidate_or_checked_negative_row",
        )
        self.assertIn("Acquire a full official", next_object["next_step"])
        self.assertIn("target-import guard", next_object["next_step"])


if __name__ == "__main__":
    unittest.main()
