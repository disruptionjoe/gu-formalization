#!/usr/bin/env python3
"""Audit AuthorManuscriptAcquisitionRow_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0203-cycle3-author-manuscript-acquisition-row.md"
)

REQUIRED_FAMILIES = {"IG", "RS", "QFT", "DGU_VZ"}
REQUIRED_PROVENANCE = {"local_or_archive_path", "checksum_or_archive_id"}


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 9\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing AuthorManuscriptAcquisitionRow_V1 JSON")
    return json.loads(match.group(1))


class AuthorManuscriptAcquisitionRowAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity(self) -> None:
        self.assertEqual(self.summary["artifact"], "AuthorManuscriptAcquisitionRow_V1")
        self.assertEqual(
            self.summary["artifact_identity"]["owned_path"],
            "explorations/hourly-20260625-0203-cycle3-author-manuscript-acquisition-row.md",
        )
        self.assertEqual(
            self.summary["artifact_identity"]["companion_audit"],
            "tests/hourly_20260625_0203_cycle3_author_manuscript_acquisition_row_audit.py",
        )
        self.assertEqual(
            self.summary["artifact_identity"]["row_id"],
            "AuthorManuscriptAcquisitionRow_V1:GU-MEDIA-2021-DRAFT-RELEASE",
        )

    def test_source_and_current_state(self) -> None:
        self.assertEqual(self.summary["source_id"], "GU-MEDIA-2021-DRAFT-RELEASE")
        row = self.summary["current_row"]
        self.assertEqual(row["source_id"], "GU-MEDIA-2021-DRAFT-RELEASE")
        self.assertEqual(row["current_state"], "not_acquired")
        self.assertFalse(row["author_manuscript_acquired"])
        self.assertFalse(row["manuscript_receipt_rows_evaluable"])
        self.assertIn(
            "AcquiredAuthorManuscriptObject_V1",
            row["required_before_receipt_rows_can_be_evaluated"],
        )

    def test_release_page_is_not_receipt(self) -> None:
        surface = self.summary["source_surface"]
        row = self.summary["current_row"]
        self.assertFalse(surface["release_page_accepted_as_receipt"])
        self.assertFalse(row["release_page_accepted_as_receipt"])
        self.assertEqual(
            surface["release_page_allowed_use"],
            "chronology_and_acquisition_pointer_only",
        )

    def test_required_provenance_includes_path_and_checksum(self) -> None:
        provenance = set(self.summary["required_provenance"])
        self.assertTrue(REQUIRED_PROVENANCE.issubset(provenance))
        obstruction_fields = set(self.summary["first_exact_obstruction"]["required_fields"])
        self.assertTrue(REQUIRED_PROVENANCE.issubset(obstruction_fields))
        requirement = self.summary["checksum_archive_requirement"]
        self.assertFalse(requirement["release_page_link_only_satisfies_requirement"])

    def test_family_query_plan_covers_all_required_families(self) -> None:
        plan = self.summary["family_query_plan_after_acquisition"]
        self.assertEqual(set(plan), REQUIRED_FAMILIES)
        for family, entry in plan.items():
            with self.subTest(family=family):
                self.assertIn("required_object", entry)
                self.assertGreaterEqual(len(entry["query_targets"]), 4)

    def test_proof_restart_not_allowed(self) -> None:
        self.assertFalse(self.summary["current_row"]["proof_restart_allowed"])
        self.assertFalse(self.summary["restart_policy"]["proof_restart_allowed"])
        self.assertIn(
            "perform_family_mathematical_identity_check",
            self.summary["restart_policy"]["steps_before_restart"],
        )

    def test_no_claim_promotion(self) -> None:
        promotions = self.summary["no_claim_promotions"]
        for key, value in promotions.items():
            self.assertFalse(value, key)
        self.assertFalse(self.summary["current_row"]["claim_promotion_allowed"])
        forbidden = " ".join(self.summary["forbidden_promotions"])
        self.assertIn("release page accepted as manuscript receipt", forbidden)
        self.assertIn("family proof restart from acquisition metadata", forbidden)
        self.assertIn("No GU claim is promoted.", self.text)


if __name__ == "__main__":
    unittest.main()
