#!/usr/bin/env python3
"""Audit AcquiredAuthorManuscriptObjectVerification_V1."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0301-cycle1-author-manuscript-object-verification.md"
)
PDF_PATH = REPO_ROOT / "Geometric_UnityDraftApril1st2021.pdf"
EXPECTED_SHA256 = "3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4"
EXPECTED_PAGE_COUNT = 69


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing AcquiredAuthorManuscriptObjectVerification_V1 JSON")
    return json.loads(match.group(1))


class AuthorManuscriptObjectVerificationAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "AcquiredAuthorManuscriptObjectVerification_V1",
        )
        self.assertEqual(self.summary["source_id"], "GU-MEDIA-2021-DRAFT-RELEASE")
        self.assertEqual(
            self.summary["artifact_identity"]["owned_path"],
            "explorations/hourly-20260625-0301-cycle1-author-manuscript-object-verification.md",
        )
        self.assertEqual(
            self.summary["artifact_identity"]["companion_audit"],
            "tests/hourly_20260625_0301_cycle1_author_manuscript_object_verification_audit.py",
        )

    def test_local_pdf_path_and_checksum(self) -> None:
        self.assertTrue(PDF_PATH.exists(), "root PDF is missing")
        obj = self.summary["local_source_object"]
        self.assertTrue(obj["exists"])
        self.assertEqual(obj["local_or_archive_path"], "Geometric_UnityDraftApril1st2021.pdf")
        self.assertEqual(Path(obj["absolute_path"]), PDF_PATH)
        self.assertEqual(obj["checksum_algorithm"], "sha256")
        self.assertEqual(obj["checksum_or_archive_id"], EXPECTED_SHA256)
        actual = hashlib.sha256(PDF_PATH.read_bytes()).hexdigest()
        self.assertEqual(actual, EXPECTED_SHA256)

    def test_page_count_and_metadata_fields_recorded(self) -> None:
        pdf = self.summary["pdf_inspection"]
        self.assertEqual(pdf["page_count"], EXPECTED_PAGE_COUNT)
        self.assertEqual(pdf["pypdf"]["page_count"], EXPECTED_PAGE_COUNT)
        self.assertEqual(pdf["pymupdf"]["page_count"], EXPECTED_PAGE_COUNT)
        pypdf_meta = pdf["pypdf"]["metadata"]
        pymupdf_meta = pdf["pymupdf"]["metadata"]
        self.assertEqual(pypdf_meta["/Creator"], "TeX")
        self.assertEqual(pypdf_meta["/Producer"], "pdfTeX-1.40.21")
        self.assertEqual(pypdf_meta["/CreationDate"], "D:20210401162628Z")
        self.assertEqual(pymupdf_meta["format"], "PDF 1.5")
        self.assertEqual(pymupdf_meta["creator"], "TeX")
        self.assertEqual(pymupdf_meta["producer"], "pdfTeX-1.40.21")

    def test_text_extraction_status_recorded(self) -> None:
        pdf = self.summary["pdf_inspection"]
        for library in ("pypdf", "pymupdf"):
            extraction = pdf[library]["text_extraction"]
            with self.subTest(library=library):
                self.assertEqual(extraction["attempted_pages"], EXPECTED_PAGE_COUNT)
                self.assertEqual(extraction["nonempty_pages"], EXPECTED_PAGE_COUNT)
                self.assertGreater(extraction["total_extracted_chars"], 100000)
                self.assertEqual(extraction["failures"], [])
        self.assertIn("Geometric Unity: Author", self.summary["local_source_object"]["object_identity_text"])

    def test_state_transition_is_acquired_pending_query(self) -> None:
        transition = self.summary["state_transition"]
        self.assertEqual(transition["previous_state"], "not_acquired")
        self.assertEqual(transition["current_state"], "acquired_pending_query")
        self.assertTrue(transition["transition_allowed"])
        provenance = self.summary["provenance_status"]
        self.assertTrue(provenance["local_or_archive_path_recorded"])
        self.assertTrue(provenance["checksum_or_archive_id_recorded"])
        self.assertFalse(provenance["family_query_log_recorded"])

    def test_no_family_receipt_promotion(self) -> None:
        no_promotion = self.summary["no_family_receipt_promotion"]
        for key, value in no_promotion.items():
            self.assertFalse(value, key)
        self.assertIn("This is a provenance/acquisition gate only.", self.text)
        self.assertIn("not a family receipt", self.text)
        self.assertIn("not permission to restart", self.text)

    def test_remaining_obstruction_is_family_query_log(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["id"], "FamilyQueryLogForAcquiredAuthorManuscript_V1")
        self.assertTrue(obstruction["missing"])
        required = set(obstruction["required_before_receipt_promotion"])
        self.assertIn("family_specific_query_log", required)
        self.assertIn("family_mathematical_identity_check", required)


if __name__ == "__main__":
    unittest.main()
