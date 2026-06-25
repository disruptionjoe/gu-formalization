#!/usr/bin/env python3
"""Audit NegativeReceiptQuarantinePolicy_V1.

The audit parses the embedded JSON summary and checks the cycle 2 policy
contract: negative receipts require complete acquired source scope plus a query
log, weak source surfaces cannot become negative receipts, target-facing DESI
language cannot select GU objects, generated excerpts cannot be accepted, and no
claim is promoted.
"""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0203-cycle2-negative-receipt-quarantine-policy.md"
)

EXPECTED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Direct Source Derivations",
    "## 3. Status Transition Rules: missing -> quarantined -> rejected -> negative_receipt -> accepted_for_routing",
    "## 4. Source-Kind Policy Table for Cycle 1 Surfaces",
    "## 5. Target-Import Controls",
    "## 6. Strongest Positive Result",
    "## 7. First Exact Obstruction",
    "## 8. GU Claim Impact and Forbidden Promotions",
    "## 9. Machine-Readable JSON Summary",
]

REQUIRED_STATUS_VOCABULARY = {
    "missing",
    "quarantined",
    "rejected",
    "negative_receipt",
    "accepted_for_routing",
}

NEVER_NEGATIVE_SURFACES = {
    "outline_only",
    "metadata_only",
    "release_metadata_only",
    "generated_transcript_excerpt",
    "indexed_transcript_without_repo_local_text",
    "unacquired_author_manuscript",
    "repo_reconstruction_artifact",
    "literature_index",
}


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing policy artifact: {DOC}") from exc


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 9\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class NegativeReceiptQuarantinePolicyAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_required_sections_present(self) -> None:
        for heading in EXPECTED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_artifact_identity(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "NegativeReceiptQuarantinePolicy_V1",
        )
        self.assertEqual(self.summary["version"], "2026-06-25")
        self.assertEqual(self.summary["run"], "hourly-20260625-0203")
        self.assertEqual(self.summary["cycle"], 2)
        self.assertEqual(self.summary["lane"], 4)
        identity = self.summary["artifact_identity"]
        self.assertEqual(
            identity["owned_path"],
            "explorations/hourly-20260625-0203-cycle2-negative-receipt-quarantine-policy.md",
        )
        self.assertEqual(
            identity["companion_audit"],
            "tests/hourly_20260625_0203_cycle2_negative_receipt_quarantine_policy_audit.py",
        )

    def test_status_vocabulary_includes_required_terms(self) -> None:
        self.assertEqual(set(self.summary["status_vocabulary"]), REQUIRED_STATUS_VOCABULARY)
        transition_rules = self.summary["status_transition_rules"]
        self.assertEqual(set(transition_rules), REQUIRED_STATUS_VOCABULARY)
        self.assertIs(transition_rules["missing"]["absence_is_evidence"], False)
        self.assertIs(transition_rules["quarantined"]["proof_restart_allowed"], False)
        self.assertIs(transition_rules["negative_receipt"]["promotion_allowed"], False)
        self.assertIs(
            transition_rules["accepted_for_routing"]["claim_promotion_allowed_at_intake"],
            False,
        )

    def test_negative_receipt_requires_complete_surface_and_query_log(self) -> None:
        requirements = self.summary["negative_receipt_requirements"]
        required_true_fields = [
            "complete_acquired_source_surface",
            "declared_source_scope",
            "query_log_required",
            "family_specific_query_terms_required",
            "notation_variants_required",
            "inspected_hits_and_false_positive_decisions_required",
            "exact_required_object_absence_required",
            "target_import_forbidden",
        ]
        for field in required_true_fields:
            self.assertIs(requirements[field], True, field)
        self.assertIs(requirements["promotion_allowed"], False)
        self.assertEqual(requirements["restart_gate"], "blocked")

    def test_outline_and_metadata_only_cannot_be_negative_receipts(self) -> None:
        blocked_surfaces = set(
            self.summary["surfaces_that_cannot_be_negative_receipts_without_more_acquisition"]
        )
        self.assertTrue(NEVER_NEGATIVE_SURFACES <= blocked_surfaces)

        policy_by_surface = {
            row["surface"]: row for row in self.summary["cycle1_source_kind_policy"]
        }
        for surface in [
            "TOE_Jaimungal_outline_timestamps",
            "metadata_only",
            "generated_transcript_excerpt",
            "2021_draft_release_page_without_manuscript_text",
            "repo_reconstruction_artifact",
        ]:
            self.assertIn(surface, policy_by_surface)
            self.assertIs(policy_by_surface[surface]["can_become_negative_receipt"], False)
            self.assertIs(policy_by_surface[surface]["can_become_accepted_for_routing"], False)

    def test_target_import_controls_block_desi_selection(self) -> None:
        controls = self.summary["target_import_controls"]
        self.assertIs(controls["DESI_target_language_can_select_IG_or_DGU_object"], False)
        self.assertIs(controls["dark_energy_target_language_can_select_IG_or_DGU_object"], False)
        self.assertIs(controls["target_data_can_select_RS_or_QFT_object"], False)
        self.assertIs(controls["source_side_object_must_precede_target_comparison"], True)
        self.assertIs(
            controls["negative_receipt_query_log_must_include_source_side_object_terms"],
            True,
        )

    def test_generated_transcript_excerpt_cannot_be_accepted(self) -> None:
        controls = self.summary["target_import_controls"]
        self.assertIs(controls["generated_transcript_excerpt_can_be_accepted"], False)
        policy_by_surface = {
            row["surface"]: row for row in self.summary["cycle1_source_kind_policy"]
        }
        generated = policy_by_surface["generated_transcript_excerpt"]
        self.assertEqual(generated["current_status"], "quarantined")
        self.assertIn("primary audio video or official transcript", generated["control"])

    def test_no_claim_promotion(self) -> None:
        promotions = self.summary["no_claim_promotions"]
        for key, value in promotions.items():
            self.assertIs(value, False, key)
        self.assertIn("No GU claim is promoted.", self.text)
        self.assertIn("Forbidden promotions", self.text)

    def test_first_obstruction_is_negative_receipt_instance(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["id"], "NegativeReceiptInstance_V1")
        self.assertIs(obstruction["missing_for_all_cycle1_surfaces"], True)
        self.assertIn("complete acquired scope", obstruction["description"])
        self.assertIn("query log", obstruction["description"])


if __name__ == "__main__":
    unittest.main()
