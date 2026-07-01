#!/usr/bin/env python3
"""Audit ManuscriptIGShiabReceiptCandidateSearch_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0301-cycle1-manuscript-ig-shiab-receipt-candidates.md"
)


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing ManuscriptIGShiabReceiptCandidateSearch_V1 JSON")
    return json.loads(match.group(1))


class ManuscriptIGShiabReceiptCandidateSearchAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity_and_source(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "ManuscriptIGShiabReceiptCandidateSearch_V1",
        )
        self.assertEqual(self.summary["run"], "hourly-20260625-0301")
        self.assertEqual(self.summary["cycle"], 1)
        self.assertEqual(self.summary["lane"], 2)
        identity = self.summary["artifact_identity"]
        self.assertEqual(
            identity["owned_path"],
            "explorations/hourly-20260625-0301-cycle1-manuscript-ig-shiab-receipt-candidates.md",
        )
        self.assertEqual(
            identity["companion_audit"],
            "tests/hourly_20260625_0301_cycle1_manuscript_ig_shiab_receipt_candidates_audit.py",
        )
        source = self.summary["source"]
        self.assertEqual(source["source_id"], "GU-MEDIA-2021-DRAFT-RELEASE")
        self.assertEqual(source["source_kind"], "author_manuscript_or_draft")
        self.assertEqual(source["page_count_observed"], 69)
        self.assertEqual(
            source["sha256"],
            "3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4",
        )

    def test_at_least_three_query_families_were_searched(self) -> None:
        families = self.summary["query_families_searched"]
        self.assertGreaterEqual(len(families), 3)
        family_names = {family["family"] for family in families}
        self.assertIn("shiab_ship", family_names)
        self.assertIn("projection_pi", family_names)
        self.assertIn("domain_codomain_selector", family_names)
        for family in families:
            self.assertGreaterEqual(len(family["variants"]), 2, family["family"])
            self.assertIn("hit_pages", family, family["family"])

    def test_candidate_rows_have_required_statuses_and_locators(self) -> None:
        allowed_statuses = {"accepted_for_routing", "quarantined", "rejected", "missing"}
        candidate_rows = self.summary["candidate_rows"]
        self.assertGreaterEqual(len(candidate_rows), 4)
        statuses = {row["candidate_status"] for row in candidate_rows}
        self.assertIn("quarantined", statuses)
        self.assertIn("rejected", statuses)
        self.assertIn("missing", statuses)
        for row in candidate_rows:
            self.assertIn(row["candidate_status"], allowed_statuses)
            self.assertIn(row["acceptance_status"], allowed_statuses)
            if row["candidate_status"] in {"quarantined", "rejected"}:
                self.assertGreater(len(row["page_locators"]), 0, row["row_id"])

    def test_strong_candidate_has_page_level_locators(self) -> None:
        strong = self.summary["candidate_rows"][0]
        self.assertEqual(strong["candidate_status"], "quarantined")
        locators = " ".join(strong["page_locators"])
        self.assertIn("PDF page 41", locators)
        self.assertIn("PDF page 43", locators)
        self.assertIn("PDF page 44", locators)
        self.assertIn("Shiab", strong["short_paraphrase"])
        self.assertFalse(strong["accepted_for_routing"])
        self.assertFalse(strong["family_identity_passed"])

    def test_accepted_receipt_count_and_promotion_flags_are_explicitly_false(self) -> None:
        self.assertEqual(self.summary["accepted_receipts"], [])
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        flags = self.summary["target_import_or_proof_promotion_flags"]
        self.assertFalse(flags["target_data_seen_nonempty"])
        self.assertFalse(flags["target_import_used"])
        self.assertFalse(flags["accepted_for_routing_any"])
        self.assertFalse(flags["proof_restart_allowed"])
        self.assertFalse(flags["claim_promotion_allowed"])
        self.assertIn("accepted_receipt_count: 0", self.text)

    def test_no_non_ig_family_is_claimed(self) -> None:
        scope = self.summary["family_scope"]
        self.assertEqual(scope["families_claimed"], ["IG"])
        self.assertFalse(scope["non_IG_families_claimed"])
        self.assertEqual(scope["required_object"], "SourceForcedCodomainSelectorForK_IG")
        for row in self.summary["candidate_rows"]:
            self.assertEqual(row["family"], "IG")
            self.assertEqual(row["required_object"], "SourceForcedCodomainSelectorForK_IG")
        promotions = self.summary["no_claim_promotions"]
        self.assertFalse(promotions["non_IG_family_claimed"])
        self.assertFalse(promotions["proof_restart_allowed"])

    def test_first_obstruction_and_next_object(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(
            obstruction["id"],
            "ManuscriptRepresentationTheoryBianchiSelectorForShiab_V1",
        )
        self.assertTrue(obstruction["missing"])
        self.assertEqual(obstruction["blocks_acceptance_for"], "SourceForcedCodomainSelectorForK_IG")
        next_object = self.summary["constructive_next_object"]
        self.assertEqual(next_object["id"], "AuthorManuscriptIGSelectorIdentityPacket_V1")
        required = set(next_object["required_fields"])
        self.assertIn("source_forced_selector_rule", required)
        self.assertIn("family_identity_to_SourceForcedCodomainSelectorForK_IG", required)


if __name__ == "__main__":
    unittest.main(verbosity=2)
