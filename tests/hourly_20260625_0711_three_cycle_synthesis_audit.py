#!/usr/bin/env python3
"""Audit the 0711 three-cycle synthesis closeout."""

from __future__ import annotations

import argparse
import json
import re
import sys
import unittest
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0711-three-cycle-fifteen-hole-synthesis.md"
)

EXPECTED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Fifteen-hole Result Table",
    "## 3. Closed/conditional/blocked/failed/no-go",
    "## 4. Next frontier objects",
    "## 5. Sequential versus parallel",
    "## 6. Wrapper assessment",
    "## 7. Verification summary",
    "## 8. Final mathematical/category review",
    "## 9. Machine-readable JSON summary",
]

EXPECTED_CYCLE3_ARTIFACTS = {
    "ProofRestartReadinessClassifierAfter0711_V1",
    "ReceiptTransitionMatrixAfter0711_V1",
    "AlternateSourceBundleMatrixAfter0711_V1",
    "ActualDGU01OperatorCertificateFieldBlockerAfter0711_V1",
    "Hourly20260625_0711_ThreeCycleFifteenHoleSynthesis_V1",
}


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing synthesis artifact: {DOC}") from exc


def extract_summary(text: str) -> dict[str, Any]:
    match = re.search(
        r"## 9\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class ThreeCycleSynthesisAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_required_sections_present(self) -> None:
        for heading in EXPECTED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_identity_and_actual_closeout_verdict(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "Hourly20260625_0711_ThreeCycleFifteenHoleSynthesis_V1",
        )
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0711")
        self.assertEqual(self.summary["cycle"], 3)
        self.assertEqual(self.summary["lane"], 5)
        self.assertEqual(
            self.summary["verdict"],
            "FIFTEEN_QUALITY_HOLES_ZERO_ACCEPTED_RECEIPTS_NO_PROOF_RESTART",
        )
        self.assertEqual(self.summary["verdict_class"], "three_cycle_closeout")
        self.assertNotIn("placeholder", self.summary["verdict"].lower())

    def test_fifteen_holes_and_cycle_distribution(self) -> None:
        holes = self.summary["holes"]
        self.assertEqual(len(holes), 15)
        self.assertEqual([hole["hole"] for hole in holes], list(range(1, 16)))

        by_cycle = {1: 0, 2: 0, 3: 0}
        for hole in holes:
            by_cycle[hole["cycle"]] += 1
        self.assertEqual(by_cycle, {1: 5, 2: 5, 3: 5})

        cycle3 = {hole["artifact"] for hole in holes if hole["cycle"] == 3}
        self.assertEqual(cycle3, EXPECTED_CYCLE3_ARTIFACTS)

    def test_receipts_restart_and_promotions_are_closed(self) -> None:
        decision = self.summary["run_level_decision"]
        self.assertEqual(decision["accepted_receipt_count"], 0)
        self.assertEqual(decision["accepted_for_routing_count"], 0)
        self.assertEqual(decision["family_identity_checks_passed"], 0)
        self.assertFalse(decision["proof_restart_allowed"])
        self.assertFalse(decision["claim_promotion_allowed"])
        self.assertFalse(decision["major_GU_claim_promoted"])
        self.assertFalse(decision["global_no_go_promoted"])

        for hole in self.summary["holes"]:
            self.assertEqual(hole["accepted_receipt_count"], 0)
            self.assertFalse(hole["proof_restart_allowed"])

    def test_cycle3_records_actual_matrices(self) -> None:
        holes = {hole["artifact"]: hole for hole in self.summary["holes"]}
        transition = holes["ReceiptTransitionMatrixAfter0711_V1"]
        self.assertEqual(transition["normalized_candidate_rows"], 39)
        self.assertEqual(transition["status"], "blocked_transition_matrix")

        bundle = holes["AlternateSourceBundleMatrixAfter0711_V1"]
        self.assertFalse(bundle["global_no_go_promoted"])
        self.assertEqual(bundle["next_object"], "alternate_primary_source_bundles")

        dgu = holes["ActualDGU01OperatorCertificateFieldBlockerAfter0711_V1"]
        self.assertEqual(dgu["accepted_certificate_fields"], 0)
        self.assertFalse(dgu["VZ_evasion_promoted"])

    def test_result_counts_are_conservative(self) -> None:
        counts = self.summary["result_counts"]
        self.assertEqual(counts["closed_full_receipts"], 0)
        self.assertEqual(counts["closed_substeps"], 1)
        self.assertEqual(counts["conditional"], 1)
        self.assertEqual(counts["no_go"], 0)
        self.assertEqual(counts["global_no_go_blocked"], 1)
        self.assertGreaterEqual(counts["blocked"], 9)

    def test_next_frontier_objects_include_required_families(self) -> None:
        next_objects = set(self.summary["next_frontier_objects"])
        for required in [
            "LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1",
            "PrimarySourceOrRecoveredNotes_BianchiHighestWeightShiabSelectorPacket_V1",
            "OxfordBosonicTwoAnchorDGU01FamilyIdentityPacket_V1",
            "ActualDGU01OperatorCertificateInstance_V1",
            "AlternatePrimarySourceRSMinusOneRuleSearchBundle_V1",
            "LocalPhysicalFieldQuotientAndNaturalityLemma_V1",
            "GlobalNegativeReceiptBundle_V1",
        ]:
            self.assertIn(required, next_objects)

    def test_wrapper_assessment_records_quality_improvement_without_promotion(self) -> None:
        wrapper = self.summary["wrapper_assessment"]
        self.assertTrue(wrapper["improved_quality"])
        for evidence in [
            "cycle2_consumed_cycle1_obstructions",
            "cycle3_blocked_receipt_inflation",
            "transition_matrix_found_zero_accepted_routes",
            "alternate_source_matrix_preserved_scoped_failure_boundaries",
        ]:
            self.assertIn(evidence, wrapper["evidence"])
        self.assertIn("source_capture_and_family_identity", wrapper["material_change_to_next_goals"])

    def test_final_category_review_invariants(self) -> None:
        review = self.summary["final_category_review"]
        for key in [
            "source_hosted_visual_not_family_identity",
            "bosonic_equation_not_actual_DGU_01",
            "hosted_shiab_not_source_forced_selector",
            "mixed_spinor_ad_not_RS_minus_one",
            "finite_carrier_not_QFT_extraction",
            "metadata_caption_thumbnail_not_receipt",
            "scoped_negative_not_global_no_go",
        ]:
            self.assertTrue(review[key], key)
        self.assertFalse(review["target_import_used"])

    def test_text_contains_no_disallowed_global_promotion_phrasing(self) -> None:
        forbidden_patterns = [
            r"major GU claim is promoted",
            r"proof restart is allowed",
            r"global_no_go_promoted:\s*true",
            r'"global_no_go_promoted"\s*:\s*true',
            r"accepted_receipt_count:\s*[1-9]",
        ]
        for pattern in forbidden_patterns:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                f"forbidden promotion phrase matched: {pattern}",
            )


def audit_summary() -> dict[str, Any]:
    text = read_doc()
    summary = extract_summary(text)
    return {
        "document": str(DOC.relative_to(REPO_ROOT)),
        "artifact": summary["artifact"],
        "verdict": summary["verdict"],
        "hole_count": len(summary["holes"]),
        "accepted_receipt_count": summary["run_level_decision"]["accepted_receipt_count"],
        "proof_restart_allowed": summary["run_level_decision"]["proof_restart_allowed"],
        "global_no_go_promoted": summary["run_level_decision"]["global_no_go_promoted"],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Audit the 0711 three-cycle synthesis.")
    parser.add_argument("--json", action="store_true", help="Print audit summary as JSON.")
    args, _remaining = parser.parse_known_args(argv)

    if args.json:
        print(json.dumps(audit_summary(), indent=2, sort_keys=True))
        return 0

    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(ThreeCycleSynthesisAudit)
    )
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
