#!/usr/bin/env python3
"""Audit the Cycle 2 author-manuscript QFT finite projector receipt gate."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0502-cycle2-author-manuscript-qft-finite-projector-receipt-gate.md"
)

EXPECTED_SHA256 = "3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4"
REQUIRED_QUERY_TERMS = {
    "P_fin",
    "P fin",
    "F_phys",
    "K_b",
    "projector",
    "projection",
    "finite",
    "source extraction",
    "extraction",
    "local representative",
    "representative",
    "quantization",
    "quantum",
    "Fock",
    "Hilbert",
    "field",
    "operator",
    "Lagrangian",
    "Euler",
    "Dirac",
    "Yang-Mills",
    "QFT",
    "finite-dimensional",
    "finite dimensional",
    "mode",
    "modes",
    "source-side",
    "source side",
}


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 9\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary")
    return json.loads(match.group(1))


class AuthorManuscriptQFTFiniteProjectorReceiptGateAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "AuthorManuscriptQFTFiniteProjectorReceiptGate_V1",
        )
        identity = self.summary["artifact_identity"]
        self.assertEqual(identity["run_id"], "hourly-20260625-0502")
        self.assertEqual(identity["cycle"], 2)
        self.assertEqual(identity["lane"], 4)
        self.assertEqual(
            identity["owned_path"],
            "explorations/hourly-20260625-0502-cycle2-author-manuscript-qft-finite-projector-receipt-gate.md",
        )
        self.assertEqual(
            identity["companion_audit"],
            "tests/hourly_20260625_0502_cycle2_author_manuscript_qft_finite_projector_receipt_gate_audit.py",
        )
        self.assertEqual(
            identity["object_id"],
            "AuthorManuscriptQFTFiniteProjectorReceiptGate_V1:GU-MEDIA-2021-DRAFT-RELEASE:QFT",
        )

    def test_manuscript_object_id_and_hash(self) -> None:
        manuscript = self.summary["manuscript_object"]
        self.assertEqual(self.summary["source_id"], "GU-MEDIA-2021-DRAFT-RELEASE")
        self.assertEqual(
            manuscript["object_id"],
            "AcquiredAuthorManuscriptObject_V1:GU-MEDIA-2021-DRAFT-RELEASE",
        )
        self.assertEqual(manuscript["artifact"], "AcquiredAuthorManuscriptObject_V1")
        self.assertEqual(manuscript["acquisition_state"], "acquired_remote_public_pdf")
        self.assertEqual(manuscript["sha256"], EXPECTED_SHA256)
        self.assertEqual(manuscript["checksum_or_archive_id"], f"sha256:{EXPECTED_SHA256}")
        self.assertTrue(manuscript["hash_verified_this_lane"])
        self.assertEqual(manuscript["content_length_bytes"], 2087649)
        self.assertEqual(manuscript["page_count_observed"], 69)

    def test_qft_required_object_and_equivalents(self) -> None:
        self.assertEqual(self.summary["family"], "QFT")
        self.assertEqual(
            self.summary["qft_required_object"],
            "P_fin^b: F_phys^b(O) -> K_b",
        )
        equivalents = set(self.summary["equivalent_required_objects"])
        for required in [
            "finite_source_extraction_projector",
            "local_representative_map_into_K_b",
            "finite_physical_field_to_source_mode_extraction_map",
            "source_side_finite_QFT_projector_rule",
        ]:
            self.assertIn(required, equivalents)

    def test_query_scope_and_terms_are_preserved(self) -> None:
        scope = self.summary["query_scope"]
        self.assertEqual(scope["surface"], "acquired_2021_author_manuscript_pdf_text")
        self.assertIn("PyMuPDF", scope["method"])
        self.assertIn("QFT finite source projector", scope["scope_note"])
        self.assertEqual(set(self.summary["query_terms"]), REQUIRED_QUERY_TERMS)
        self.assertEqual(set(self.summary["query_results"]), REQUIRED_QUERY_TERMS)

    def test_negative_blocked_status_requirements(self) -> None:
        self.assertEqual(self.summary["status"], "blocked_negative")
        self.assertTrue(self.summary["negative_result_scoped"])
        self.assertEqual(self.summary["accepted_receipts"], [])
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])
        self.assertIn("blocked negative", self.text.lower())

    def test_exact_qft_tokens_are_absent_and_adjacent_terms_are_not_accepted(self) -> None:
        results = self.summary["query_results"]
        for exact in ["P_fin", "P fin", "F_phys", "K_b", "projector"]:
            self.assertEqual(results[exact]["hit_count"], 0, exact)
            self.assertFalse(results[exact]["accepted_locator"], exact)
        for adjacent in ["projection", "finite", "QFT", "quantization", "mode"]:
            self.assertGreater(results[adjacent]["hit_count"], 0, adjacent)
            self.assertFalse(results[adjacent]["accepted_locator"], adjacent)

    def test_acceptance_criteria_require_domain_target_map_and_import_screen(self) -> None:
        criteria = self.summary["acceptance_criteria"]
        self.assertIn("F_phys", criteria["must_emit_domain"])
        self.assertIn("K_b", criteria["must_emit_target"])
        self.assertIn("projector", criteria["must_emit_map"])
        self.assertTrue(criteria["must_be_source_side"])
        self.assertTrue(criteria["must_pass_import_screen"])

    def test_first_obstruction(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["id"], "SourceProjectorPFinBFromAuthorManuscript")
        self.assertTrue(obstruction["missing"])
        self.assertEqual(obstruction["required_object"], "P_fin^b: F_phys^b(O) -> K_b")
        self.assertIn("no manuscript locator emits P_fin", obstruction["description"])
        self.assertTrue(obstruction["source_side_before_proof_side"])

    def test_strongest_positive_attempt_is_quarantined_not_receipt(self) -> None:
        attempt = self.summary["strongest_positive_qft_construction_attempt"]
        self.assertEqual(
            attempt["status"],
            "quarantined_locator_cluster_not_accepted_receipt",
        )
        locators = {entry["locator"] for entry in attempt["locators"]}
        self.assertIn("PDF p. 54 equation (12.1) finite/infinite dimension region", locators)
        self.assertIn("PDF p. 55 equations (12.2)-(12.3)", locators)
        self.assertIn("PDF p. 60 Section 12.8", locators)
        for entry in attempt["locators"]:
            self.assertIn("why_not_accepted", entry)

    def test_constructive_next_object_and_forbidden_promotions(self) -> None:
        next_object = self.summary["constructive_next_object"]
        self.assertEqual(next_object["id"], "AuthorManuscriptQFTFiniteProjectorLocatorRow_V1")
        for field in [
            "source_id",
            "manuscript_object_id",
            "sha256",
            "locator",
            "emitted_rule_type",
            "domain",
            "target",
            "map",
            "local_mode_records",
            "import_screen",
            "receipt_decision",
        ]:
            self.assertIn(field, next_object["required_fields"])

        forbidden = set(self.summary["forbidden_promotions"])
        for claim in [
            "manuscript_supplies_P_fin_b",
            "manuscript_supplies_finite_source_extraction_projector",
            "manuscript_supplies_local_representative_map_into_K_b",
            "manuscript_proves_source_derived_QFT_state_space_extraction",
            "manuscript_derives_finite_QFT_covariance_rho_AB_Bell_CHSH",
        ]:
            self.assertIn(claim, forbidden)

    def test_next_computation_stays_source_side_until_receipt_exists(self) -> None:
        next_step = self.summary["next_meaningful_proof_or_source_computation"]
        self.assertEqual(next_step["source_computation"], "manual_page_window_QFT_projector_pass")
        self.assertEqual(next_step["target_object"], "AuthorManuscriptQFTFiniteProjectorLocatorRow_V1")
        self.assertEqual(next_step["proof_computation_if_source_row_accepted"], "SourceModeQuotientPacket_for_K_b")
        self.assertFalse(next_step["proof_restart_currently_allowed"])
        self.assertIn("PDF p. 54 equation (12.1)", next_step["page_windows"])
        self.assertIn("PDF p. 60 Sections 12.8-12.9", next_step["page_windows"])


if __name__ == "__main__":
    unittest.main()
