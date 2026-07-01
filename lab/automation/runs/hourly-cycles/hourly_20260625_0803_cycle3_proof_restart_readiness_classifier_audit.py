#!/usr/bin/env python3
"""Audit ProofRestartReadinessClassifierAfter0803_V1."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0803-cycle3-proof-restart-readiness-classifier.md"
)

EXPECTED_ROUTES = {"PTUJ_visual", "IG", "DGU_VZ", "RS", "QFT"}
EXPECTED_MISSING_OBJECTS = {
    "PTUJ_visual": "LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1",
    "IG": "SourceNaturalBianchiHighestWeightSelectorTheoremForK_IG_V1",
    "DGU_VZ": "ActualDGU01OperatorCertificateInstance_V1.source_clean_actual_operator_identity_witness",
    "RS": "UCSDTypedRSMinusOneOperator_V1",
    "QFT": "source_defined_congruence_generators_for_tilde_phys_b_O",
}
EXPECTED_NEXT_OBJECTS = {
    "PTUJ_visual": "LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1",
    "IG": "SourceNaturalBianchiHighestWeightSelectorTheoremForK_IG_V1",
    "DGU_VZ": "ActualDGU01OperatorCertificateInstance_V1.source_clean_actual_operator_identity_witness",
    "RS": "UCSDTypedRSMinusOneOperator_V1",
    "QFT": "CandidateCongruenceGeneratorsForLocalGUPhysicalFieldEquivalence_V1",
}
EXPECTED_READ_FIRST = [
    "RESEARCH-POSTURE.md",
    "process/runbooks/five-lane-frontier-run.md",
    "explorations/hourly-20260625-0803-cycle1-ptuj-lawful-source-asset-admission-gate.md",
    "explorations/hourly-20260625-0803-cycle1-ig-bianchi-highest-weight-selector-packet-gate.md",
    "explorations/hourly-20260625-0803-cycle1-oxford-dgu01-two-anchor-family-identity-gate.md",
    "explorations/hourly-20260625-0803-cycle1-rs-alternate-minus-one-source-bundle-gate.md",
    "explorations/hourly-20260625-0803-cycle1-qft-local-physical-quotient-naturality-gate.md",
    "explorations/hourly-20260625-0803-cycle2-ptuj-lawful-acquisition-contract-matrix.md",
    "explorations/hourly-20260625-0803-cycle2-ig-representation-natural-rival-eliminator-matrix.md",
    "explorations/hourly-20260625-0803-cycle2-dgu-actual-operator-certificate-minimal-field-matrix.md",
    "explorations/hourly-20260625-0803-cycle2-rs-ucsd-typed-operator-source-origin-classifier.md",
    "explorations/hourly-20260625-0803-cycle2-qft-source-equivalence-descent-schema-gate.md",
]
REQUIRED_SOURCE_COVERAGE = {
    "PTUJ_visual": {
        "GU-MEDIA-2021-PULL-THAT-UP-JAMIE",
        "GU-POD-2021-KEATING-REVEALED-1",
        "GU-POD-2021-KEATING-REVEALED-2",
        "GU-MEDIA-2021-DRAFT-RELEASE",
    },
    "IG": {
        "canon/shiab-existence-cl95.md",
        "literature/weinstein-ucsd-2025-04-transcript.md",
        "manuscript_Oxford_PTUJ_Keating_selector_surfaces",
    },
    "DGU_VZ": {
        "Oxford_02:35:10_anchor",
        "Oxford_02:36:12_anchor",
        "manuscript_Sections_9_12_and_9_3",
        "literature/weinstein-ucsd-2025-04-transcript.md",
        "canon/no-go-class-relative-map.md",
    },
    "RS": {
        "Geometric_UnityDraftApril1st2021.pdf#page_49_equation_10.10",
        "literature/weinstein-ucsd-2025-04-transcript.md",
        "canon/no-go-class-relative-map.md",
    },
    "QFT": {
        "active-research/signed-readout/theorem-statement-v1-2026-06-23.md",
        "literature/weinstein-ucsd-2025-04-transcript.md",
        "0711_QFT_finite_local_extraction_spec_gate",
    },
}

FORBIDDEN_PROMOTION_TRUE_KEYS = {
    "caption_or_metadata_as_receipt",
    "source_motivation_as_selector_derivation",
    "Oxford_bosonic_anchor_as_actual_DGU_certificate",
    "UCSD_aggregate_operator_as_pure_RS_rule",
    "QFT_schema_as_inhabited_quotient",
    "VZ_evasion_promotion",
    "generation_count_promotion",
    "Bell_or_CHSH_promotion",
    "downstream_physics_claim_promotion",
    "global_no_go_promotion",
}

FORBIDDEN_TEXT_PATTERNS = [
    r"\bproof restart allowed\b",
    r"\bready for proof restart\b",
    r"\baccepted_receipt_count:\s*[1-9]",
    r"\bfamily_identity_checks_passed:\s*[1-9]",
    r"\bVZ evasion is proved\b",
    r"\bgeneration count is proved\b",
    r"\bBell violation is proved\b",
    r"\bQFT recovery is proved\b",
]


def extract_json_summary(text: str) -> dict[str, Any]:
    match = re.search(
        r"## 8\. Machine-readable JSON summary\.\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing section 8 machine-readable JSON summary")
    return json.loads(match.group(1))


class ProofRestartReadinessClassifierAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_json_summary(cls.text)
        cls.routes = {route["route_id"]: route for route in cls.summary["routes"]}

    def test_artifact_identity_and_global_verdict(self) -> None:
        self.assertEqual(
            self.summary["artifact"], "ProofRestartReadinessClassifierAfter0803_V1"
        )
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0803")
        self.assertEqual(self.summary["cycle"], 3)
        self.assertEqual(self.summary["lane"], 1)
        self.assertEqual(
            self.summary["verdict"],
            "GLOBAL_PROOF_RESTART_FORBIDDEN_ZERO_READY_ROUTES",
        )
        self.assertEqual(self.summary["verdict_class"], "blocked_restart_forbidden")
        self.assertEqual(self.summary["global_proof_restart_state"], "forbidden")
        self.assertFalse(self.summary["global_claim_promotion_allowed"])
        self.assertEqual(self.summary["ready_route_count"], 0)
        self.assertEqual(self.summary["classified_route_count"], 5)

    def test_required_sources_read_first_are_exact(self) -> None:
        self.assertEqual(self.summary["read_first_sources"], EXPECTED_READ_FIRST)
        self.assertEqual(
            self.summary["owned_path"],
            "explorations/hourly-20260625-0803-cycle3-proof-restart-readiness-classifier.md",
        )
        self.assertEqual(
            self.summary["companion_audit"],
            "tests/hourly_20260625_0803_cycle3_proof_restart_readiness_classifier_audit.py",
        )

    def test_route_coverage_is_exact(self) -> None:
        self.assertEqual(set(self.routes), EXPECTED_ROUTES)
        self.assertEqual(len(self.summary["routes"]), len(EXPECTED_ROUTES))
        self.assertEqual(
            {row["route_id"] for row in self.summary["next_meaningful_sequential_lanes"]},
            EXPECTED_ROUTES,
        )

    def test_restart_rule_requires_all_four_predicates(self) -> None:
        rule = self.summary["proof_restart_rule"]
        self.assertTrue(rule["accepted_receipt_count_gt_0_required"])
        self.assertTrue(rule["family_identity_checks_passed_gt_0_required"])
        self.assertTrue(rule["target_import_screen_passed_required"])
        self.assertTrue(rule["route_specific_restart_object_present_required"])
        self.assertTrue(rule["all_conditions_required"])

    def test_zero_accepted_receipts_family_identities_and_restarts(self) -> None:
        for route_id, route in self.routes.items():
            self.assertEqual(route["accepted_receipt_count"], 0, route_id)
            self.assertEqual(route["accepted_for_routing_count"], 0, route_id)
            self.assertEqual(route["family_identity_checks_passed"], 0, route_id)
            self.assertFalse(route["route_specific_restart_object_present"], route_id)
            self.assertFalse(route["proof_restart_allowed"], route_id)
            self.assertFalse(route["claim_promotion_allowed"], route_id)
            self.assertFalse(route["target_import_detected"], route_id)
            self.assertEqual(
                route["first_unmet_restart_predicate"],
                "accepted_receipt_count_gt_0",
                route_id,
            )

    def test_first_exact_missing_objects_are_stable(self) -> None:
        for route_id, expected in EXPECTED_MISSING_OBJECTS.items():
            self.assertEqual(
                self.routes[route_id]["first_exact_missing_object"],
                expected,
                route_id,
            )
            self.assertIn(expected, self.text)

    def test_next_sequential_lane_objects_are_exact(self) -> None:
        next_by_route = {
            row["route_id"]: row["next_object"]
            for row in self.summary["next_meaningful_sequential_lanes"]
        }
        self.assertEqual(next_by_route, EXPECTED_NEXT_OBJECTS)

    def test_required_source_coverage_per_route(self) -> None:
        for route_id, required in REQUIRED_SOURCE_COVERAGE.items():
            self.assertTrue(
                required.issubset(set(self.routes[route_id]["required_source_coverage"])),
                route_id,
            )

    def test_route_specific_blocker_fields_are_preserved(self) -> None:
        self.assertEqual(self.routes["IG"]["source_natural_eliminations_today"], 0)
        self.assertFalse(self.routes["IG"]["all_representation_natural_rivals_eliminated"])
        self.assertEqual(self.routes["DGU_VZ"]["accepted_certificate_field_count"], 0)
        self.assertEqual(self.routes["DGU_VZ"]["required_certificate_field_count"], 10)
        self.assertFalse(self.routes["RS"]["typed_source_origin_operator_rule_exists"])
        self.assertFalse(self.routes["RS"]["generation_count_promotion_allowed"])
        self.assertFalse(self.routes["QFT"]["valid_finite_extraction_restart"])
        self.assertFalse(self.routes["QFT"]["valid_qft_state_restart"])

    def test_global_restart_evaluation_matches_route_predicates(self) -> None:
        evaluation = self.summary["global_restart_evaluation"]
        self.assertEqual(evaluation["routes_with_accepted_receipt_count_gt_0"], [])
        self.assertEqual(evaluation["routes_with_family_identity_checks_passed_gt_0"], [])
        self.assertEqual(evaluation["routes_with_route_specific_restart_object_present"], [])
        self.assertEqual(evaluation["routes_ready_for_proof_restart"], [])
        self.assertFalse(evaluation["global_proof_restart_allowed"])
        self.assertEqual(
            set(evaluation["routes_with_target_import_screen_passed"]),
            {"PTUJ_visual", "IG", "RS"},
        )

    def test_no_claim_promotions(self) -> None:
        promotions = self.summary["forbidden_promotions"]
        self.assertEqual(set(promotions), FORBIDDEN_PROMOTION_TRUE_KEYS)
        for key, value in promotions.items():
            self.assertFalse(value, key)
        self.assertFalse(self.summary["global_claim_promotion_allowed"])

    def test_no_forbidden_promotion_text(self) -> None:
        for pattern in FORBIDDEN_TEXT_PATTERNS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                f"forbidden promotion phrase matched: {pattern}",
            )

    def test_classifier_falsification_condition_requires_all_restart_predicates(self) -> None:
        condition = self.summary["classifier_falsification_condition"]
        for required in [
            "accepted_receipt_count_gt_0",
            "family_identity_checks_passed_gt_0",
            "target_import_screen_passed_true",
            "route_specific_restart_object_present_true",
        ]:
            self.assertIn(required, condition)


if __name__ == "__main__":
    unittest.main(verbosity=2)
