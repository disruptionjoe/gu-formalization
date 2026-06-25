#!/usr/bin/env python3
"""Audit UCSDTranscriptReceiptMiningPacket_V1.

The audit parses the embedded JSON summary and checks that the packet uses the
UCSD local transcript as a mined source surface without promoting any family
claim. It verifies four-family coverage, timestamp/locator discipline, intake
status rules, blocked restart gates, and the next object target.
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
    / "hourly-20260625-0203-cycle1-ucsd-transcript-receipt-mining-packet.md"
)

EXPECTED_HEADINGS = [
    "## 1. Verdict",
    "## 2. What Was Derived Directly From Repo Sources",
    "## 3. Candidate Receipt Rows",
    "## 4. Strongest Positive Result",
    "## 5. First Exact Obstruction or Missing Object",
    "## 6. Constructive Next Object That Would Remove or Test the Obstruction",
    "## 7. GU Claim Impact and Forbidden Promotions",
    "## 8. Next Meaningful Source-Mining or Proof Step",
    "## 9. Machine-Readable JSON Summary",
]

REQUIRED_FAMILIES = {"IG", "RS", "QFT", "DGU_VZ"}

REQUIRED_OBJECTS = {
    "IG": "SourceForcedCodomainSelectorForK_IG",
    "RS": "source.action_or_operator for d_RS,-1",
    "QFT": "P_fin^b: F_phys^b(O) -> K_b",
    "DGU_VZ": "operator_source_primary_action_or_EL for D_GU^epsilon 0/1",
}

ALLOWED_IMPORT_STATUS = {
    "source_emitted",
    "candidate_import",
    "target_import",
    "ambiguous",
    "rejected",
}

ALLOWED_ACCEPTANCE_STATUS = {
    "accepted_for_routing",
    "quarantined",
    "rejected",
    "needs_second_reader",
    "missing",
}

ALLOWED_RESTART_GATE = {"closed", "blocked", "family_limited"}


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing UCSD receipt mining packet: {DOC}") from exc


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 9\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class UCSDTranscriptReceiptMiningPacketAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)
        cls.rows = {
            row["family"]: row
            for row in cls.summary["candidate_receipt_rows"]  # type: ignore[index]
        }

    def test_required_sections_present(self) -> None:
        for heading in EXPECTED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_artifact_identity_and_source_paths(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "UCSDTranscriptReceiptMiningPacket_V1",
        )
        self.assertEqual(self.summary["verdict_class"], "blocked")
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertEqual(self.summary["all_downstream_restart_gates"], "blocked")

        source = self.summary["source"]
        self.assertEqual(source["source_id"], "RepoLocalUCSDTranscript_2025_04")
        self.assertEqual(
            source["source_path"],
            "literature/weinstein-ucsd-2025-04-transcript.md",
        )
        self.assertEqual(
            source["analysis_path"],
            "explorations/weinstein-ucsd-2025-04-analysis-2026-06-22.md",
        )
        self.assertEqual(source["source_status"], "raw_transcript")

    def test_transcript_timestamp_locator_discipline_recorded(self) -> None:
        discipline = set(self.summary["source"]["locator_discipline"])
        self.assertIn("transcript_timestamp", discipline)
        self.assertIn("local_line_number", discipline)
        self.assertIn("short_exact_fragment_only", discipline)

        timestamped_rows = [
            row
            for row in self.rows.values()
            if row["locator"]["timestamp_range"] != "not_found"
        ]
        self.assertGreaterEqual(len(timestamped_rows), 3)
        for row in timestamped_rows:
            self.assertRegex(row["locator"]["timestamp_range"], r"\[00:\d{2}:\d{2}\]")
            self.assertRegex(row["locator"]["line_range"], r"\d+")

    def test_all_four_family_blockers_are_considered(self) -> None:
        self.assertEqual(set(self.summary["families_considered"]), REQUIRED_FAMILIES)
        self.assertEqual(set(self.rows), REQUIRED_FAMILIES)
        for family, required_object in REQUIRED_OBJECTS.items():
            self.assertEqual(self.rows[family]["required_object"], required_object)

    def test_rows_follow_intake_status_rules(self) -> None:
        for family, row in self.rows.items():
            self.assertIn(row["import_status"], ALLOWED_IMPORT_STATUS, family)
            self.assertIn(row["acceptance_status"], ALLOWED_ACCEPTANCE_STATUS, family)
            self.assertIn(row["restart_gate"], ALLOWED_RESTART_GATE, family)
            self.assertIs(row["promotion_allowed"], False, family)
            self.assertEqual(row["source_id"], "RepoLocalUCSDTranscript_2025_04")
            self.assertEqual(
                row["source_path"],
                "literature/weinstein-ucsd-2025-04-transcript.md",
                family,
            )
            self.assertEqual(row["source_status"], "raw_transcript", family)
            self.assertEqual(row["target_data_seen"], [], family)

            if row["acceptance_status"] == "quarantined":
                self.assertEqual(row["import_status"], "candidate_import", family)
                self.assertNotEqual(row["emitted_object_type"], "none_supplied", family)
                self.assertEqual(row["restart_gate"], "blocked", family)
            if row["acceptance_status"] == "missing":
                self.assertEqual(row["import_status"], "rejected", family)
                self.assertEqual(row["emitted_object_type"], "none_supplied", family)
                self.assertEqual(row["restart_gate"], "blocked", family)

    def test_no_rows_are_accepted_or_restartable(self) -> None:
        for family, row in self.rows.items():
            self.assertNotEqual(row["acceptance_status"], "accepted_for_routing", family)
            self.assertNotEqual(row["import_status"], "source_emitted", family)
            self.assertEqual(row["restart_gate"], "blocked", family)

    def test_no_claim_promotion(self) -> None:
        promotions = self.summary["no_claim_promotions"]
        for key, value in promotions.items():
            self.assertIs(value, False, key)
        self.assertIn("No GU claim is promoted.", self.text)
        self.assertIn("Forbidden promotions", self.text)

    def test_constructive_next_object_points_to_receipt_map(self) -> None:
        next_object = self.summary["constructive_next_object"]
        self.assertEqual(next_object["id"], "RepoLocalPrimaryGUSourceReceiptMap_V1")
        self.assertIn("quarantined or missing", next_object["entry_policy"])
        self.assertIn("UCSD", next_object["next_source_mining_step"])

        predecessor = self.summary["predecessor_ledger"]
        self.assertEqual(
            predecessor["first_missing_global_object"],
            "RepoLocalPrimaryGUSourceReceiptMap_V1",
        )

    def test_next_objects_remain_family_specific(self) -> None:
        next_by_family = self.summary["next_objects_by_family"]
        self.assertEqual(set(next_by_family), REQUIRED_FAMILIES)
        self.assertIn("K_IG", next_by_family["IG"])
        self.assertIn("d_RS,-1", next_by_family["RS"])
        self.assertIn("P_fin^b", next_by_family["QFT"])
        self.assertIn("D_GU^epsilon", next_by_family["DGU_VZ"])


if __name__ == "__main__":
    unittest.main()
