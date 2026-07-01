#!/usr/bin/env python3
"""Audit AuthorManuscriptQFTFiniteExtractionReceiptSearch_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0301-cycle2-manuscript-qft-finite-extraction-receipt.md"
)

EXPECTED_HEADINGS = [
    "## 1. Verdict",
    "## 2. What Was Derived Directly From Repo Sources",
    "## 3. The Strongest Positive Result",
    "## 4. The First Exact Obstruction Or Missing Proof Object",
    "## 5. The Constructive Next Object That Would Remove Or Test The Obstruction",
    "## 6. What This Means For The Relevant GU Claim",
    "## 7. Next Meaningful Proof Or Computation Step",
    "## 8. Manuscript Query Rows",
    "## 9. Machine-Readable JSON Summary",
]

EXPECTED_QUERY_FAMILIES = {
    "exact_projector_symbols",
    "finite",
    "quantization",
    "hilbert_state",
    "local_representative",
    "projector_projection",
    "physical_field_content",
    "mode_algebra",
    "covariance_pullback",
    "observer_observable",
    "zero_one_form",
    "carrier_quotient",
}

REQUIRED_NO_PROMOTIONS = {
    "QFT_P_fin_b_supplied",
    "finite_QFT_recovery_derived",
    "local_representative_selected",
    "K_b_defined_or_selected",
    "local_observable_extraction_defined",
    "Gram_CHSH_Bell_rho_AB_recovery_restarted",
    "proof_restart_allowed_now",
}


def read_artifact() -> str:
    try:
        return ARTIFACT.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing artifact: {ARTIFACT}") from exc


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 9\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class AuthorManuscriptQFTFiniteExtractionReceiptAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_artifact()
        cls.summary = extract_summary(cls.text)
        cls.query_families = {
            row["family"]: row for row in cls.summary["searched_query_families"]
        }
        cls.candidate_rows = cls.summary["candidate_rows"]

    def test_required_sections_present(self) -> None:
        for heading in EXPECTED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_artifact_identity_and_source(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "AuthorManuscriptQFTFiniteExtractionReceiptSearch_V1",
        )
        self.assertEqual(self.summary["version"], "2026-06-25")
        self.assertEqual(self.summary["run"], "hourly-20260625-0301")
        self.assertEqual(self.summary["cycle"], 2)
        self.assertEqual(self.summary["lane"], 4)
        self.assertEqual(self.summary["verdict_class"], "underdefined")
        self.assertEqual(
            self.summary["artifact_identity"]["owned_path"],
            "explorations/hourly-20260625-0301-cycle2-manuscript-qft-finite-extraction-receipt.md",
        )
        self.assertEqual(
            self.summary["artifact_identity"]["companion_audit"],
            "tests/hourly_20260625_0301_cycle2_manuscript_qft_finite_extraction_receipt_audit.py",
        )
        source = self.summary["source"]
        self.assertEqual(source["source_id"], "GU-MEDIA-2021-DRAFT-RELEASE")
        self.assertEqual(source["source_object"], "Geometric_UnityDraftApril1st2021.pdf")
        self.assertEqual(source["page_count"], 69)
        self.assertIn("ligature-normalized", source["query_scope"])

    def test_all_required_query_families_are_logged(self) -> None:
        self.assertEqual(set(self.query_families), EXPECTED_QUERY_FAMILIES)
        required_terms = {
            "exact_projector_symbols": ["P_fin", "F_phys", "K_b"],
            "finite": ["finite", "finite dimensional", "finite-dimensional"],
            "quantization": ["quantization", "quantize", "quantized", "quantum field theory"],
            "hilbert_state": ["Hilbert", "Hilbert space", "state"],
            "local_representative": ["local representative", "representative"],
            "projector_projection": ["projector", "projection", "projection map"],
            "physical_field_content": ["physical field", "field content"],
            "mode_algebra": ["mode", "algebra"],
            "covariance_pullback": ["covariance", "pullback", "pull back"],
            "observer_observable": ["observer", "observable", "measurement"],
            "zero_one_form": ["zero-form", "one-form", "1-form"],
            "carrier_quotient": ["carrier", "quotient"],
        }
        for family, terms in required_terms.items():
            query_text = " ".join(self.query_families[family]["queries"])
            for term in terms:
                self.assertIn(term, query_text, family)

    def test_page_locators_cover_positive_context_clusters(self) -> None:
        locators = {
            locator
            for row in self.summary["searched_query_families"]
            for locator in row["page_locators"]
        }
        for required in ["p.16", "p.17", "p.25", "p.26", "p.31", "p.33", "p.49", "p.54", "p.56", "p.58", "p.64"]:
            self.assertIn(required, locators)
        self.assertEqual(self.query_families["exact_projector_symbols"]["page_locators"], [])

    def test_zero_accepted_receipts_and_no_restart(self) -> None:
        self.assertEqual(self.summary["required_qft_object"], "P_fin^b: F_phys^b(O) -> K_b")
        self.assertIs(self.summary["required_object_emitted"], False)
        self.assertIs(self.summary["equivalent_finite_extraction_rule_emitted"], False)
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertEqual(self.summary["accepted_receipts"], [])
        self.assertIs(self.summary["accepted_for_routing"], False)
        self.assertIs(self.summary["proof_restart_allowed"], False)
        self.assertIs(self.summary["claim_promotion_allowed"], False)
        self.assertIs(self.summary["finite_qft_recovery_promoted"], False)
        for row in self.candidate_rows:
            self.assertIs(row["accepted_for_routing"], False, row["row_id"])

    def test_target_import_guard_flags_are_clean_and_nonpromotional(self) -> None:
        target_import = self.summary["target_import"]
        self.assertEqual(target_import["target_data_seen"], [])
        self.assertIs(target_import["target_import_detected"], False)
        forbidden = set(target_import["forbidden_qft_targets_not_used_for_selection"])
        for term in ["Gram", "CHSH", "Bell", "rho_AB", "finite_QFT_recovery"]:
            self.assertIn(term, forbidden)

    def test_first_obstruction_is_finite_extraction_map(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["id"], "FiniteLocalQFTExtractionMap_V1")
        self.assertIs(obstruction["missing"], True)
        self.assertIn("P_fin^b", obstruction["description"])
        self.assertIn("F_phys^b(O)", obstruction["description"])
        self.assertIn("K_b", obstruction["description"])
        self.assertIn("source", obstruction["description"])
        self.assertIn("codomain", obstruction["description"])

    def test_constructive_next_object_has_required_fields(self) -> None:
        next_object = self.summary["constructive_next_object"]
        self.assertEqual(next_object["id"], "FiniteLocalQFTExtractionMapSpec_V1")
        self.assertEqual(
            set(next_object["required_fields"]),
            {
                "observation_context",
                "source_space",
                "operation",
                "codomain",
                "naturality",
                "non_import_condition",
                "finite_stability_test",
            },
        )

    def test_no_qft_proof_promotion(self) -> None:
        promotions = self.summary["no_claim_promotions"]
        self.assertEqual(set(promotions), REQUIRED_NO_PROMOTIONS)
        for key, value in promotions.items():
            self.assertIs(value, False, key)
        self.assertIn("It does not support:", self.text)
        self.assertIn("The 2021 manuscript supplies P_fin^b.", self.text)
        self.assertIn("The manuscript derives finite QFT recovery.", self.text)


if __name__ == "__main__":
    unittest.main()
