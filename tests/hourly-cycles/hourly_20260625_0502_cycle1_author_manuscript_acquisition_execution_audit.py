#!/usr/bin/env python3
"""Audit AuthorManuscriptAcquisitionExecution_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0502-cycle1-author-manuscript-acquisition-execution.md"
)

REQUIRED_FAMILIES = {"IG", "RS", "QFT", "DGU_VZ"}
REQUIRED_PROVENANCE = {
    "acquisition_origin",
    "acquisition_date",
    "local_or_archive_path",
    "checksum_or_archive_id",
    "custodian_or_archive_basis",
    "access_notes",
}


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 9\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing AuthorManuscriptAcquisitionExecution_V1 JSON")
    return json.loads(match.group(1))


class AuthorManuscriptAcquisitionExecutionAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "AuthorManuscriptAcquisitionExecution_V1",
        )
        self.assertEqual(
            self.summary["artifact_identity"]["owned_path"],
            "explorations/hourly-20260625-0502-cycle1-author-manuscript-acquisition-execution.md",
        )
        self.assertEqual(
            self.summary["artifact_identity"]["companion_audit"],
            "tests/hourly_20260625_0502_cycle1_author_manuscript_acquisition_execution_audit.py",
        )
        self.assertEqual(
            self.summary["artifact_identity"]["object_id"],
            "AuthorManuscriptAcquisitionExecution_V1:GU-MEDIA-2021-DRAFT-RELEASE",
        )

    def test_source_id_and_upgrade(self) -> None:
        self.assertEqual(self.summary["source_id"], "GU-MEDIA-2021-DRAFT-RELEASE")
        upgrade = self.summary["source_surface_upgrade"]
        self.assertEqual(upgrade["new_state"], "acquired_remote_public_pdf")
        self.assertTrue(upgrade["upgraded_to_acquired_author_manuscript_object"])
        self.assertFalse(upgrade["local_repo_source_file_written"])
        self.assertFalse(upgrade["copyrighted_text_pasted"])

    def test_acquired_object_has_required_provenance(self) -> None:
        manuscript = self.summary["acquired_author_manuscript_object"]
        self.assertEqual(manuscript["artifact"], "AcquiredAuthorManuscriptObject_V1")
        self.assertEqual(manuscript["source_id"], "GU-MEDIA-2021-DRAFT-RELEASE")
        self.assertEqual(manuscript["acquisition_state"], "acquired_remote_public_pdf")
        self.assertIn("geometricunity.nyc3.digitaloceanspaces.com", manuscript["local_or_archive_path"])
        self.assertTrue(manuscript["checksum_or_archive_id"].startswith("sha256:"))
        self.assertEqual(len(manuscript["sha256"]), 64)
        self.assertEqual(manuscript["content_type"], "application/pdf")
        self.assertEqual(manuscript["content_length_bytes"], 2087649)
        self.assertEqual(manuscript["page_count_observed"], 69)
        self.assertTrue(manuscript["provenance_record_present"])
        self.assertTrue(manuscript["locator_basis_present"])

        self.assertEqual(set(self.summary["required_provenance_fields"]), REQUIRED_PROVENANCE)
        satisfied = self.summary["required_provenance_fields_satisfied"]
        self.assertEqual(set(satisfied), REQUIRED_PROVENANCE)
        for field, value in satisfied.items():
            self.assertTrue(value, field)

    def test_family_coverage_after_acquisition(self) -> None:
        coverage = self.summary["family_coverage_after_acquisition"]
        self.assertEqual(set(coverage), REQUIRED_FAMILIES)
        for family, entry in coverage.items():
            with self.subTest(family=family):
                self.assertIn("required_object", entry)
                self.assertIn("coverage_status", entry)
                self.assertGreaterEqual(len(entry["candidate_locators"]), 1)
                self.assertFalse(entry["accepted_receipt"])
                self.assertIn("first_missing_field", entry)

        self.assertEqual(
            coverage["QFT"]["coverage_status"],
            "not_evaluable_missing_exact_required_object_locator",
        )
        self.assertIn("P_fin", coverage["QFT"]["first_missing_field"])

    def test_candidate_rows_and_receipt_gate(self) -> None:
        rows = self.summary["candidate_receipt_rows"]
        self.assertEqual({row["family"] for row in rows}, REQUIRED_FAMILIES)
        for row in rows:
            self.assertEqual(row["source_id"], "GU-MEDIA-2021-DRAFT-RELEASE")
            self.assertIn("Primary", row["acceptance_status"] + " Primary")
            self.assertFalse(row["proof_restart_allowed"])

        self.assertEqual(self.summary["accepted_receipts"], [])
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])

    def test_first_exact_obstruction(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(
            obstruction["id"],
            "accepted_PrimarySourceReceiptInstance_V1_followed_by_family_identity_check",
        )
        self.assertTrue(obstruction["missing"])
        self.assertIn("remote manuscript acquisition is satisfied", obstruction["description"])
        self.assertIn("family identity", self.summary["next_meaningful_step"])

    def test_no_claim_promotion(self) -> None:
        promotions = self.summary["no_claim_promotions"]
        for key, value in promotions.items():
            self.assertFalse(value, key)
        self.assertIn("No GU claim is promoted", self.text)
        self.assertIn("accepted_receipt_count: 0", self.text)


if __name__ == "__main__":
    unittest.main()
