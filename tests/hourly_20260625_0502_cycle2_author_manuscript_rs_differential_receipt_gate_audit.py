#!/usr/bin/env python3
"""Audit AuthorManuscriptRSDifferentialReceiptGate_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0502-cycle2-author-manuscript-rs-differential-receipt-gate.md"
)

EXPECTED_HASH = "3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4"
EXPECTED_OBJECT_ID = "AcquiredAuthorManuscriptObject_V1:GU-MEDIA-2021-DRAFT-RELEASE"
EXPECTED_REQUIRED_OBJECT = "source.action_or_operator for d_RS,-1"


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 9\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing AuthorManuscriptRSDifferentialReceiptGate_V1 JSON")
    return json.loads(match.group(1))


class AuthorManuscriptRSDifferentialReceiptGateAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "AuthorManuscriptRSDifferentialReceiptGate_V1",
        )
        self.assertEqual(self.summary["run"], "hourly-20260625-0502")
        self.assertEqual(self.summary["cycle"], 2)
        self.assertEqual(self.summary["lane"], 3)
        identity = self.summary["artifact_identity"]
        self.assertEqual(
            identity["owned_path"],
            "explorations/hourly-20260625-0502-cycle2-author-manuscript-rs-differential-receipt-gate.md",
        )
        self.assertEqual(
            identity["companion_audit"],
            "tests/hourly_20260625_0502_cycle2_author_manuscript_rs_differential_receipt_gate_audit.py",
        )
        self.assertEqual(identity["artifact_id"], "AuthorManuscriptRSDifferentialReceiptGate_V1")
        self.assertIn("RS:d_RS_minus_1", identity["row_id"])

    def test_manuscript_object_id_and_hash(self) -> None:
        manuscript = self.summary["acquired_author_manuscript_object"]
        self.assertEqual(manuscript["object_id"], EXPECTED_OBJECT_ID)
        self.assertEqual(manuscript["source_id"], "GU-MEDIA-2021-DRAFT-RELEASE")
        self.assertEqual(manuscript["acquisition_state"], "acquired_remote_public_pdf")
        self.assertEqual(manuscript["sha256"], EXPECTED_HASH)
        self.assertEqual(manuscript["checksum_or_archive_id"], f"sha256:{EXPECTED_HASH}")
        self.assertEqual(manuscript["page_count_observed"], 69)
        self.assertTrue(manuscript["hash_verified_this_lane"])

    def test_rs_required_object_and_candidate_status(self) -> None:
        self.assertEqual(self.summary["family"], "RS")
        self.assertEqual(self.summary["rs_required_object"], EXPECTED_REQUIRED_OBJECT)
        candidate = self.summary["candidate_row"]
        self.assertEqual(candidate["family"], "RS")
        self.assertEqual(candidate["required_object"], EXPECTED_REQUIRED_OBJECT)
        self.assertEqual(candidate["candidate_status"], "quarantined_locator_candidate")
        self.assertEqual(candidate["row_status"], "underdefined")
        self.assertEqual(
            candidate["acceptance_status"],
            "not_accepted_missing_source_emitted_RS_rule_and_identity_check",
        )
        self.assertFalse(candidate["accepted_receipt"])
        self.assertFalse(candidate["proof_restart_allowed"])
        self.assertFalse(candidate["claim_promotion_allowed"])
        self.assertGreaterEqual(len(candidate["strongest_positive_locators"]), 4)

    def test_receipt_and_restart_gate(self) -> None:
        self.assertEqual(self.summary["accepted_receipts"], [])
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])
        identity_check = self.summary["family_identity_check"]
        self.assertTrue(identity_check["required"])
        self.assertEqual(identity_check["status"], "not_runnable")
        self.assertIn("d_RS,-1", identity_check["reason"])

    def test_first_obstruction(self) -> None:
        obstruction = self.summary["first_obstruction"]
        self.assertEqual(
            obstruction["id"],
            "missing_source_emitted_RS_differential_action_or_operator_for_d_RS_minus_1",
        )
        self.assertTrue(obstruction["missing"])
        self.assertIn("source space target space degree", obstruction["description"])
        self.assertIn("No source-emitted RS differential/action/operator rule", self.text)

    def test_source_term_checks_and_forbidden_promotions(self) -> None:
        checks = self.summary["source_term_checks"]
        self.assertEqual(checks["BRST_hits"], 0)
        self.assertEqual(checks["Noether_hits"], 0)
        self.assertEqual(checks["Rarita_hits"], 8)
        self.assertEqual(checks["Schwinger_hits"], 8)
        promotions = self.summary["no_claim_promotions"]
        for key, value in promotions.items():
            self.assertFalse(value, key)
        self.assertIn("Forbidden promotions", self.text)


if __name__ == "__main__":
    unittest.main()
