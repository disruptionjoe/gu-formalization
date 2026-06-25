#!/usr/bin/env python3
"""Audit KeatingTOEModernReceiptMiningPacket_V1.

The audit parses the embedded JSON summary and checks the modern receipt-mining
contract: source IDs are represented, locator-only sources are quarantined, all
four family blockers are considered, no claim is promoted, and the constructive
next object points to transcript acquisition under RepoLocalPrimaryGUSourceReceiptMap_V1.
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
    / "hourly-20260625-0203-cycle1-keating-toe-receipt-mining-packet.md"
)

EXPECTED_HEADINGS = [
    "## 1. Verdict",
    "## 2. What Was Derived Directly From Repo Sources",
    "## 3. Candidate Receipt Rows",
    "## 4. Strongest Positive Result",
    "## 5. First Exact Obstruction Or Missing Object",
    "## 6. Constructive Next Object",
    "## 7. GU Claim Impact And Forbidden Promotions",
    "## 8. Next Meaningful Source-Mining Or Proof Step",
    "## 9. Machine-Readable JSON Summary",
]

REQUIRED_SOURCE_IDS = {
    "GU-MEDIA-KEATING-QG-FBOZSSLXFVI",
    "GU-POD-2025-KEATING-DESI-GU",
    "GU-POD-2025-TOE-JAIMUNGAL-GU-40",
    "GU-POD-2021-KEATING-REVEALED-1",
    "GU-POD-2021-KEATING-REVEALED-2",
}

REQUIRED_FAMILIES = {"IG", "RS", "QFT", "DGU_VZ"}

REQUIRED_REQUIRED_OBJECTS = {
    "IG": "SourceForcedCodomainSelectorForK_IG",
    "RS": "source.action_or_operator for d_RS,-1",
    "QFT": "P_fin^b: F_phys^b(O) -> K_b",
    "DGU_VZ": "operator_source_primary_action_or_EL for D_GU^epsilon 0/1",
}

QUARANTINED_SOURCE_KINDS = {
    "outline_available",
    "metadata_checked",
    "official_video_metadata_timestamp_needed",
    "generated_transcript_excerpt_plus_metadata",
}


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing receipt mining packet: {DOC}") from exc


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 9\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class KeatingTOEModernReceiptMiningPacketAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)
        cls.rows = cls.summary["candidate_receipt_rows"]
        cls.family_rows = {
            row["family"]: row for row in cls.summary["family_blockers_considered"]
        }
        cls.source_classification = cls.summary["source_surface_classification"]

    def test_required_sections_present(self) -> None:
        for heading in EXPECTED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_identity_and_blocked_verdict(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "KeatingTOEModernReceiptMiningPacket_V1",
        )
        self.assertEqual(
            self.summary["verdict"],
            "BLOCKED_MODERN_SURFACES_ONLY_LOCATOR_CANDIDATES",
        )
        self.assertEqual(self.summary["verdict_class"], "blocked")
        self.assertIs(self.summary["not_a_claim_promotion"], True)
        self.assertEqual(self.summary["accepted_receipt_count"], 0)

    def test_modern_source_ids_are_represented(self) -> None:
        represented = set(self.summary["modern_source_ids_represented"])
        self.assertEqual(represented, REQUIRED_SOURCE_IDS)
        row_source_ids = {row["source_id"] for row in self.rows}
        self.assertTrue(REQUIRED_SOURCE_IDS <= row_source_ids)
        self.assertEqual(set(self.source_classification), REQUIRED_SOURCE_IDS)

    def test_outline_and_metadata_sources_are_quarantined_not_accepted(self) -> None:
        for source_id, status in self.source_classification.items():
            self.assertEqual(
                status["packet_status"],
                "quarantined_locator_candidate",
                source_id,
            )
            self.assertIs(status["accepted_for_routing"], False, source_id)

        for row in self.rows:
            if row["source_kind"] in QUARANTINED_SOURCE_KINDS:
                self.assertEqual(row["acceptance_status"], "quarantined", row)
                self.assertNotEqual(row["acceptance_status"], "accepted_for_routing", row)
                self.assertEqual(row["restart_gate"], "blocked", row)
                self.assertEqual(row["emitted_object_type"], "none_supplied", row)
                self.assertEqual(row["emitted_formula_or_rule"], "none", row)

    def test_all_four_family_blockers_are_considered(self) -> None:
        self.assertEqual(set(self.family_rows), REQUIRED_FAMILIES)
        families_in_rows = {row["family"] for row in self.rows}
        self.assertEqual(families_in_rows, REQUIRED_FAMILIES)

        for family, required_object in REQUIRED_REQUIRED_OBJECTS.items():
            family_row = self.family_rows[family]
            self.assertEqual(family_row["required_object"], required_object)
            self.assertIs(family_row["receipt_found"], False)
            self.assertEqual(family_row["restart_gate"], "blocked")
            self.assertIn("first_missing_object", family_row)

    def test_no_claim_promotion(self) -> None:
        promotions = self.summary["no_claim_promotions"]
        for key, value in promotions.items():
            self.assertIs(value, False, key)

        self.assertIn("No GU claim is promoted.", self.text)
        forbidden = set(self.summary["forbidden_promotions"])
        for forbidden_item in [
            "outline_as_receipt",
            "metadata_as_receipt",
            "generated_transcript_excerpt_as_accepted_receipt",
            "DESI_target_language_as_source_selector",
        ]:
            self.assertIn(forbidden_item, forbidden)

    def test_constructive_next_object_points_to_receipt_map_with_transcript_tasks(self) -> None:
        next_object = self.summary["constructive_next_object"]
        self.assertEqual(next_object["id"], "RepoLocalPrimaryGUSourceReceiptMap_V1")
        self.assertEqual(next_object["entry_type"], "PrimarySourceReceiptInstance_V1")
        self.assertIn("transcript", next_object["next_step"])

        tasks = next_object["transcript_acquisition_tasks"]
        task_source_ids = {task["source_id"] for task in tasks}
        self.assertEqual(task_source_ids, REQUIRED_SOURCE_IDS)
        for task in tasks:
            self.assertIn("acquire", task["task"])
            self.assertIn("transcript", task["task"])

    def test_first_obstruction_is_missing_emitted_formula_or_rule(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(
            obstruction["id"],
            "RepoLocalPrimaryGUSourceReceiptMap_V1.modern_keating_toe_rows",
        )
        self.assertEqual(obstruction["missing_field"], "emitted_formula_or_rule")
        self.assertIn("selector action operator projector or EL", obstruction["description"])


if __name__ == "__main__":
    unittest.main()
