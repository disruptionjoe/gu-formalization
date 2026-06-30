#!/usr/bin/env python3
"""Audit AuthorManuscriptIGSelectorReceiptGate_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0502-cycle2-author-manuscript-ig-selector-receipt-gate.md"
)


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 9\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing AuthorManuscriptIGSelectorReceiptGate_V1 JSON")
    return json.loads(match.group(1))


class AuthorManuscriptIGSelectorReceiptGateAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "AuthorManuscriptIGSelectorReceiptGate_V1",
        )
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0502")
        self.assertEqual(self.summary["cycle"], 2)
        self.assertEqual(self.summary["lane"], 2)
        identity = self.summary["artifact_identity"]
        self.assertEqual(
            identity["owned_path"],
            "explorations/hourly-20260625-0502-cycle2-author-manuscript-ig-selector-receipt-gate.md",
        )
        self.assertEqual(
            identity["companion_audit"],
            "tests/hourly_20260625_0502_cycle2_author_manuscript_ig_selector_receipt_gate_audit.py",
        )
        self.assertEqual(
            identity["object_id"],
            "AuthorManuscriptIGSelectorReceiptGate_V1:GU-MEDIA-2021-DRAFT-RELEASE:IG",
        )

    def test_manuscript_object_id_and_hash(self) -> None:
        manuscript = self.summary["manuscript_object"]
        self.assertEqual(
            manuscript["object_id"],
            "AcquiredAuthorManuscriptObject_V1:GU-MEDIA-2021-DRAFT-RELEASE",
        )
        self.assertEqual(
            manuscript["sha256"],
            "3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4",
        )
        self.assertEqual(
            manuscript["checksum_or_archive_id"],
            "sha256:3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4",
        )
        self.assertEqual(manuscript["page_count_observed"], 69)
        self.assertEqual(manuscript["content_length_bytes"], 2087649)
        self.assertTrue(manuscript["pdf_refetched_this_lane"])
        self.assertTrue(manuscript["sha256_verified_this_lane"])
        self.assertFalse(manuscript["repo_local_pdf_written"])

    def test_ig_required_object_and_candidate_status(self) -> None:
        self.assertEqual(self.summary["family"], "IG")
        self.assertEqual(
            self.summary["required_object"],
            "SourceForcedCodomainSelectorForK_IG",
        )
        row = self.summary["candidate_row"]
        self.assertEqual(row["family"], "IG")
        self.assertEqual(row["required_object"], "SourceForcedCodomainSelectorForK_IG")
        self.assertEqual(row["candidate_status"], "quarantined_strong_candidate")
        self.assertEqual(
            row["acceptance_status"],
            "not_accepted_missing_source_forced_selector_and_family_identity",
        )
        self.assertFalse(row["accepted_receipt"])
        self.assertFalse(row["proof_restart_allowed"])
        self.assertFalse(row["claim_promotion_allowed"])
        self.assertTrue(row["candidate_is_source_emitted"])
        self.assertFalse(row["selector_is_source_forced"])
        self.assertFalse(row["family_identity_passed"])
        self.assertIn("Section 8", " ".join(row["candidate_locators"]))
        self.assertIn("Section 5.3-5.4", " ".join(row["candidate_locators"]))
        self.assertIn("Shiab_candidate", " ".join(row["emitted_source_objects"]))

    def test_keating_locator_comparison_stays_non_proof(self) -> None:
        comparison = self.summary["keating_locator_comparison"]
        self.assertTrue(comparison["comparison_only"])
        self.assertFalse(comparison["used_as_proof"])
        self.assertEqual(
            comparison["status"],
            "quarantined_source_side_locator_candidate",
        )
        self.assertIn("neither emits", comparison["relation_to_manuscript"])

    def test_receipt_counts_and_restart_gate(self) -> None:
        self.assertEqual(self.summary["accepted_receipts"], [])
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])
        self.assertIn("proof_restart", self.summary["forbidden_promotions"])
        self.assertIn("accepted_receipt_count: 0", self.text)

    def test_first_obstruction(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(
            obstruction["id"],
            "ManuscriptRepresentationTheoryBianchiSelectorForShiab_V1",
        )
        self.assertTrue(obstruction["missing"])
        self.assertEqual(obstruction["obstruction_type"], "missing_source_object")
        self.assertIn("SourceForcedCodomainSelectorForK_IG", obstruction["description"])
        required = set(obstruction["required_to_accept"])
        self.assertIn("Bianchi_or_representation_theory_selection_rule", required)
        self.assertIn("family_identity_to_SourceForcedCodomainSelectorForK_IG", required)

    def test_constructive_next_object(self) -> None:
        next_object = self.summary["constructive_next_object"]
        self.assertEqual(next_object["id"], "AuthorManuscriptIGSelectorIdentityPacket_V1")
        self.assertEqual(
            next_object["manuscript_object_id"],
            "AcquiredAuthorManuscriptObject_V1:GU-MEDIA-2021-DRAFT-RELEASE",
        )
        self.assertIn("family identity", self.summary["next_meaningful_step"])
        self.assertIn("source intake", self.summary["next_meaningful_step"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
