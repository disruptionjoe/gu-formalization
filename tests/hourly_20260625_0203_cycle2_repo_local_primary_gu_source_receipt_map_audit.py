#!/usr/bin/env python3
"""Audit RepoLocalPrimaryGUSourceReceiptMap_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "explorations"
    / "hourly-20260625-0203-cycle2-repo-local-primary-gu-source-receipt-map.md"
)

REQUIRED_SURFACES = {
    "OxfordPortal",
    "UCSDTranscript2025",
    "JRETranscripts",
    "KeatingTOEModern",
    "AuthorManuscript2021DraftRelease",
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
        raise AssertionError("missing RepoLocalPrimaryGUSourceReceiptMap_V1 JSON")
    return json.loads(match.group(1))


class RepoLocalPrimaryGUSourceReceiptMapAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)
        cls.rows = cls.summary["map_rows"]

    def test_artifact_identity_and_map_id(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "RepoLocalPrimaryGUSourceReceiptMap_V1",
        )
        self.assertEqual(
            self.summary["artifact_identity"]["map_id"],
            "RepoLocalPrimaryGUSourceReceiptMap_V1",
        )
        self.assertEqual(
            self.summary["artifact_identity"]["owned_path"],
            "explorations/hourly-20260625-0203-cycle2-repo-local-primary-gu-source-receipt-map.md",
        )
        self.assertEqual(
            self.summary["verdict"],
            "BLOCKED_MAP_EXISTS_ZERO_ACCEPTED_RECEIPTS",
        )
        self.assertTrue(self.summary["process_map_exists"])
        self.assertTrue(
            self.summary["predecessor_missing_object_closed_at_process_level_only"]
        )

    def test_all_cycle1_source_surfaces_are_represented(self) -> None:
        self.assertEqual(
            set(self.summary["cycle1_source_surfaces_represented"]),
            REQUIRED_SURFACES,
        )
        row_surfaces = {row["source_surface_group"] for row in self.rows}
        self.assertEqual(row_surfaces, REQUIRED_SURFACES)

    def test_all_four_families_are_represented_for_each_surface(self) -> None:
        self.assertEqual(set(self.summary["families_represented"]), set(REQUIRED_FAMILIES))
        self.assertEqual(self.summary["required_objects"], REQUIRED_FAMILIES)

        for surface in REQUIRED_SURFACES:
            rows = [row for row in self.rows if row["source_surface_group"] == surface]
            self.assertEqual({row["family"] for row in rows}, set(REQUIRED_FAMILIES))
            for row in rows:
                self.assertEqual(row["required_object"], REQUIRED_FAMILIES[row["family"]])

    def test_accepted_receipt_count_is_zero_everywhere(self) -> None:
        self.assertEqual(self.summary["accepted_receipts"], [])
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        for row in self.rows:
            self.assertEqual(row["accepted_receipt_count"], 0)
            self.assertNotEqual(row["row_status"], "accepted_receipt")

    def test_process_map_existence_does_not_permit_proof_restart(self) -> None:
        self.assertFalse(self.summary["process_map_existence_permits_proof_restart"])
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])
        for row in self.rows:
            self.assertFalse(row["proof_restart_allowed"])
        self.assertIn("Process existence does not permit proof restart.", self.text)

    def test_no_claim_promotion(self) -> None:
        promotions = self.summary["no_claim_promotions"]
        for key, value in promotions.items():
            self.assertFalse(value, key)
        self.assertIn(
            "process map existence permits proof restart",
            self.summary["forbidden_promotions"],
        )
        self.assertIn("No GU claim is promoted by this map.", self.text)

    def test_next_obstruction_is_accepted_receipt_then_identity_check(self) -> None:
        obstruction = self.summary["first_exact_obstruction_after_map_instantiation"]
        self.assertEqual(
            obstruction["id"],
            "accepted PrimarySourceReceiptInstance_V1/family identity check",
        )
        self.assertTrue(obstruction["missing"])
        self.assertEqual(
            self.summary["next_obstruction"],
            "accepted PrimarySourceReceiptInstance_V1/family identity check",
        )
        self.assertIn(
            "family mathematical identity check",
            self.summary["next_meaningful_step"],
        )


if __name__ == "__main__":
    unittest.main()
