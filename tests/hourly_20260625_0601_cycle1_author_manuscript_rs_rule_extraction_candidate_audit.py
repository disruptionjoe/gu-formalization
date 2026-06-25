#!/usr/bin/env python3
"""Audit AuthorManuscriptRSRuleExtractionCandidate_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0601-cycle1-author-manuscript-rs-rule-extraction-candidate.md"
)

EXPECTED_REQUIRED_OBJECT = "source.action_or_operator for d_RS,-1"


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing AuthorManuscriptRSRuleExtractionCandidate_V1 JSON")
    return json.loads(match.group(1))


class AuthorManuscriptRSRuleExtractionCandidateAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity_and_required_object(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "AuthorManuscriptRSRuleExtractionCandidate_V1",
        )
        self.assertEqual(self.summary["run"], "hourly-20260625-0601")
        self.assertEqual(self.summary["cycle"], 1)
        self.assertEqual(self.summary["family"], "RS")
        self.assertEqual(self.summary["rs_required_object"], EXPECTED_REQUIRED_OBJECT)
        self.assertIn("AuthorManuscriptRSRuleExtractionCandidate_V1", self.text)
        self.assertIn("d_RS,-1", self.text)

        identity = self.summary["artifact_identity"]
        self.assertEqual(
            identity["owned_path"],
            "explorations/hourly-20260625-0601-cycle1-author-manuscript-rs-rule-extraction-candidate.md",
        )
        self.assertEqual(
            identity["companion_audit"],
            "tests/hourly_20260625_0601_cycle1_author_manuscript_rs_rule_extraction_candidate_audit.py",
        )
        self.assertIn("RS:d_RS_minus_1", identity["row_id"])

    def test_pass_scope_covers_required_formula_neighborhoods(self) -> None:
        scope = self.summary["pass_scope"]
        self.assertEqual(scope["source_file"], "Geometric_UnityDraftApril1st2021.pdf")
        for locator in [
            "9.16",
            "9.22",
            "10.1",
            "10.10",
            "11.1",
            "11.4",
            "12.9",
            "12.22",
        ]:
            self.assertIn(locator, scope["checked_locators"])
            self.assertIn(locator, self.text)
        self.assertGreaterEqual(self.summary["typed_rows_checked"], 20)

    def test_zero_accepted_receipts_and_no_restart(self) -> None:
        self.assertEqual(self.summary["accepted_receipts"], [])
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])

        candidate = self.summary["candidate_row"]
        self.assertEqual(candidate["required_object"], EXPECTED_REQUIRED_OBJECT)
        self.assertEqual(candidate["accepted_receipt_count"], 0)
        self.assertFalse(candidate["accepted_receipt"])
        self.assertFalse(candidate["proof_restart_allowed"])
        self.assertFalse(candidate["claim_promotion_allowed"])

    def test_no_proof_restart_unless_accepted_receipt_and_identity(self) -> None:
        identity_check = self.summary["family_identity_check"]
        self.assertTrue(identity_check["required"])
        self.assertEqual(identity_check["status"], "not_runnable")
        self.assertIn("zero accepted RS source receipts", identity_check["reason"])
        self.assertIn("No proof restart is allowed.", self.text)

    def test_strongest_positive_row_is_not_accepted(self) -> None:
        strongest = self.summary["strongest_positive_row"]
        self.assertEqual(strongest["locator"], "10.10")
        self.assertEqual(strongest["decision"], "not_accepted")
        self.assertIn("unstable", strongest["reason"])
        self.assertIn("10.10", self.text)
        self.assertIn("not accepted", self.text)

    def test_final_demotion_and_obstruction(self) -> None:
        self.assertEqual(
            self.summary["verdict"],
            "FAIL_FOR_RS_DIFFERENTIAL_RECEIPT_ZERO_ACCEPTED_RS_RECEIPTS",
        )
        self.assertEqual(self.summary["verdict_class"], "fail")
        obstruction = self.summary["first_obstruction"]
        self.assertEqual(
            obstruction["id"],
            "missing_stable_RS_only_source_rule_for_d_RS_minus_1",
        )
        self.assertIn("source space, target space, degree/slot", obstruction["description"])
        self.assertEqual(obstruction["first_decisive_failed_row"], "10.10")

        demotion = self.summary["final_demotion"]
        self.assertEqual(demotion["from"], "quarantined_locator_candidate")
        self.assertEqual(demotion["to"], "fail_for_RS_differential_receipt")
        self.assertFalse(demotion["global_no_go"])
        self.assertIn("fail_for_RS_differential_receipt", self.text)

    def test_no_claim_promotions(self) -> None:
        promotions = self.summary["no_claim_promotions"]
        for key, value in promotions.items():
            self.assertIs(value, False, key)
        self.assertFalse(promotions["RS_generation_count_proof_restart"])
        self.assertFalse(promotions["equation_10_10_accepted_as_RS_differential"])
        self.assertIn("This artifact does not close those routes.", self.text)


if __name__ == "__main__":
    unittest.main()
