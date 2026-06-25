#!/usr/bin/env python3
"""Audit JRETranscriptReceiptExecution_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "explorations"
    / "hourly-20260625-0502-cycle1-jre-transcript-receipt-execution.md"
)

REQUIRED_SOURCE_IDS = {
    "GU-MEDIA-2020-JRE-1453",
    "GU-POD-2021-JRE-1628",
}

REQUIRED_FAMILIES = {
    "IG": "SourceForcedCodomainSelectorForK_IG",
    "RS": "source.action_or_operator for d_RS,-1",
    "QFT": "P_fin^b: F_phys^b(O) -> K_b",
    "DGU_VZ": "operator_source_primary_action_or_EL for D_GU^epsilon 0/1",
}


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 9\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing JRETranscriptReceiptExecution_V1 JSON summary")
    return json.loads(match.group(1))


class JRETranscriptReceiptExecutionAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "JRETranscriptReceiptExecution_V1",
        )
        self.assertEqual(self.summary["run"], "hourly-20260625-0502")
        self.assertEqual(self.summary["cycle"], 1)
        self.assertEqual(self.summary["lane"], 2)
        self.assertEqual(
            self.summary["verdict"],
            "TRANSCRIPT_SURFACES_REACHABLE_LOCATORS_FOUND_ACCEPTED_RECEIPTS_ZERO_PROOF_RESTART_BLOCKED",
        )
        identity = self.summary["artifact_identity"]
        self.assertEqual(
            identity["owned_path"],
            "explorations/hourly-20260625-0502-cycle1-jre-transcript-receipt-execution.md",
        )
        self.assertEqual(
            identity["companion_audit"],
            "tests/hourly_20260625_0502_cycle1_jre_transcript_receipt_execution_audit.py",
        )

    def test_both_source_ids_represented(self) -> None:
        self.assertEqual(set(self.summary["source_ids_represented"]), REQUIRED_SOURCE_IDS)
        surface_ids = {surface["source_id"] for surface in self.summary["source_surfaces"]}
        row_ids = {row["source_id"] for row in self.summary["receipt_attempt_rows"]}
        self.assertEqual(surface_ids, REQUIRED_SOURCE_IDS)
        self.assertEqual(row_ids, REQUIRED_SOURCE_IDS)
        for surface in self.summary["source_surfaces"]:
            self.assertEqual(surface["surface_status"], "reachable_transcript_surface")
            self.assertIn("portal_line_locator", surface["strongest_positive_locator"])

    def test_required_family_coverage(self) -> None:
        self.assertEqual(self.summary["required_family_coverage"], REQUIRED_FAMILIES)
        expected_pairs = {
            (source_id, family)
            for source_id in REQUIRED_SOURCE_IDS
            for family in REQUIRED_FAMILIES
        }
        actual_pairs = {
            (row["source_id"], row["family"])
            for row in self.summary["receipt_attempt_rows"]
        }
        self.assertEqual(actual_pairs, expected_pairs)
        for row in self.summary["receipt_attempt_rows"]:
            self.assertEqual(row["required_object"], REQUIRED_FAMILIES[row["family"]])

    def test_no_receipt_acceptance_or_restart(self) -> None:
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])
        self.assertFalse(self.summary["negative_receipt_allowed"])
        for row in self.summary["receipt_attempt_rows"]:
            self.assertFalse(row["accepted"])
            self.assertEqual(row["emitted_object_type"], "none")
            self.assertNotEqual(row["intake_status"], "accepted_for_routing")

    def test_first_exact_obstruction(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(
            obstruction["id"],
            "PortalWikiJRETranscriptReceiptExecution_V1.no_family_required_object_emitted",
        )
        self.assertIn("family-required selector", obstruction["description"])
        self.assertIn("source action/operator", obstruction["description"])
        self.assertIn("finite projector", obstruction["description"])
        self.assertIn("D_GU action/operator/EL", obstruction["description"])

    def test_scope_controls_and_next_object(self) -> None:
        controls = self.summary["scope_controls"]
        self.assertTrue(controls["owned_paths_only"])
        self.assertTrue(controls["transcript_fetching_possible"])
        self.assertTrue(controls["portal_wiki_surfaces_reachable"])
        self.assertFalse(controls["full_local_transcript_body_persisted"])
        self.assertFalse(controls["long_transcript_excerpt_pasted"])

        next_object = self.summary["constructive_next_object"]
        self.assertEqual(
            next_object["id"],
            "PortalWikiJRETranscriptQueryLogAndCandidateRows_V1",
        )
        self.assertEqual(
            next_object["must_precede"],
            "any_accepted_receipt_or_negative_receipt_from_JRE_transcripts",
        )


if __name__ == "__main__":
    unittest.main()
