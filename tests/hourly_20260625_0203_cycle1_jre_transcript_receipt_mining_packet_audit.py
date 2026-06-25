#!/usr/bin/env python3
"""Audit JRETranscriptReceiptMiningPacket_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "explorations"
    / "hourly-20260625-0203-cycle1-jre-transcript-receipt-mining-packet.md"
)

REQUIRED_FAMILIES = {
    "IG": "SourceForcedCodomainSelectorForK_IG",
    "RS": "source.action_or_operator for d_RS,-1",
    "QFT": "P_fin^b: F_phys^b(O) -> K_b",
    "DGU_VZ": "operator_source_primary_action_or_EL for D_GU^epsilon 0/1",
}

REQUIRED_SOURCE_IDS = {
    "GU-MEDIA-2020-JRE-1453",
    "GU-POD-2021-JRE-1628",
}


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 9\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing JRETranscriptReceiptMiningPacket_V1 JSON summary")
    return json.loads(match.group(1))


class JRETranscriptReceiptMiningPacketAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "JRETranscriptReceiptMiningPacket_V1",
        )
        self.assertEqual(self.summary["run"], "hourly-20260625-0203")
        self.assertEqual(self.summary["cycle"], 1)
        self.assertEqual(self.summary["lane"], 3)
        self.assertEqual(
            self.summary["verdict"],
            "BLOCKED_TRANSCRIPT_EXTRACTION_REQUIRED_NO_ACCEPTED_RECEIPTS",
        )
        self.assertEqual(
            self.summary["artifact_identity"]["owned_path"],
            "explorations/hourly-20260625-0203-cycle1-jre-transcript-receipt-mining-packet.md",
        )

    def test_both_jre_source_ids_are_represented(self) -> None:
        surface_ids = {row["source_id"] for row in self.summary["source_surfaces"]}
        row_ids = {row["source_id"] for row in self.summary["candidate_receipt_rows"]}
        self.assertEqual(surface_ids, REQUIRED_SOURCE_IDS)
        self.assertEqual(row_ids, REQUIRED_SOURCE_IDS)
        for surface in self.summary["source_surfaces"]:
            self.assertEqual(surface["indexed_status"], "transcript-available")
            self.assertFalse(surface["repo_local_transcript_text_found"])

    def test_no_accepted_receipt_from_outline_or_index_only_material(self) -> None:
        self.assertEqual(self.summary["accepted_receipts"], [])
        self.assertTrue(
            self.summary["no_accepted_receipt_from_outline_or_index_only_material"]
        )
        for row in self.summary["candidate_receipt_rows"]:
            self.assertNotEqual(row["acceptance_status"], "accepted_for_routing")
            self.assertNotEqual(row["import_status"], "source_emitted")
            self.assertEqual(row["source_kind"], "indexed_transcript_surface_no_local_text")
            self.assertEqual(row["emitted_object_type"], "none_supplied")
            self.assertEqual(row["restart_gate"], "blocked")

    def test_all_four_family_blockers_are_considered(self) -> None:
        family_rows = {
            row["family"]: row["required_object"]
            for row in self.summary["families_considered"]
        }
        self.assertEqual(family_rows, REQUIRED_FAMILIES)

        candidate_pairs = {
            (row["source_id"], row["family"])
            for row in self.summary["candidate_receipt_rows"]
        }
        expected_pairs = {
            (source_id, family)
            for source_id in REQUIRED_SOURCE_IDS
            for family in REQUIRED_FAMILIES
        }
        self.assertEqual(candidate_pairs, expected_pairs)

    def test_no_claim_promotion(self) -> None:
        promotions = self.summary["no_claim_promotions"]
        for key, value in promotions.items():
            self.assertFalse(value, msg=f"{key} should not be promoted")
        self.assertIn("IG selects K_IG", self.summary["forbidden_promotions"])
        self.assertIn(
            "blocked_until_timestamped_transcript_extraction_and_intake_acceptance",
            self.summary["proof_restart_policy"],
        )

    def test_next_task_extracts_transcript_before_proof_restart(self) -> None:
        task = self.summary["next_mining_task"]
        self.assertEqual(task["task"], "extract_transcript_text_before_proof_restart")
        self.assertTrue(task["before_proof_restart"])
        self.assertEqual(task["first_source"], "GU-MEDIA-2020-JRE-1453")
        self.assertEqual(task["second_source"], "GU-POD-2021-JRE-1628")

        next_object = self.summary["constructive_next_object"]
        self.assertEqual(next_object["id"], "JRETranscriptExtractionBatch_V1")
        self.assertEqual(next_object["must_precede"], "any_family_proof_restart")
        self.assertIn("short_exact_fragment", next_object["minimum_fields"])
        self.assertIn("emitted_formula_or_rule", next_object["minimum_fields"])


if __name__ == "__main__":
    unittest.main()
