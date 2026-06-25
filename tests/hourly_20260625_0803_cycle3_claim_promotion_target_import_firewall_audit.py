#!/usr/bin/env python3
"""Audit ClaimPromotionTargetImportFirewallAfter0803_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0803-cycle3-claim-promotion-target-import-firewall.md"
)

EXPECTED_CLAIM_IDS = {
    "ig_selector_acceptance",
    "dgu_actual_operator",
    "vz_evasion",
    "rs_d_RS_minus_1",
    "rs_generation_count",
    "qft_finite_extraction",
    "qft_rho_AB_CHSH_Bell",
    "ptuj_visual_receipt",
    "oxford_visual_receipt",
    "dark_energy_theta_FLRW",
    "global_GU_claim",
    "global_no_go",
}

EXPECTED_SOURCES = {
    "RESEARCH-POSTURE.md",
    "process/runbooks/five-lane-frontier-run.md",
    "explorations/hourly-20260625-0803-cycle1-ig-bianchi-highest-weight-selector-packet-gate.md",
    "explorations/hourly-20260625-0803-cycle1-oxford-dgu01-two-anchor-family-identity-gate.md",
    "explorations/hourly-20260625-0803-cycle1-ptuj-lawful-source-asset-admission-gate.md",
    "explorations/hourly-20260625-0803-cycle1-qft-local-physical-quotient-naturality-gate.md",
    "explorations/hourly-20260625-0803-cycle1-rs-alternate-minus-one-source-bundle-gate.md",
    "explorations/hourly-20260625-0803-cycle2-dgu-actual-operator-certificate-minimal-field-matrix.md",
    "explorations/hourly-20260625-0803-cycle2-ig-representation-natural-rival-eliminator-matrix.md",
    "explorations/hourly-20260625-0803-cycle2-ptuj-lawful-acquisition-contract-matrix.md",
    "explorations/hourly-20260625-0803-cycle2-qft-source-equivalence-descent-schema-gate.md",
    "explorations/hourly-20260625-0803-cycle2-rs-ucsd-typed-operator-source-origin-classifier.md",
    "canon/no-go-class-relative-map.md",
    "CANON.md",
}

REQUIRED_SOURCE_OBJECTS_BY_CLAIM = {
    "ig_selector_acceptance": {
        "SourceNaturalBianchiHighestWeightSelectorTheoremForK_IG_V1",
        "SourceForcedCodomainSelectorForK_IG",
    },
    "dgu_actual_operator": {
        "ActualDGU01OperatorCertificateInstance_V1.source_clean_actual_operator_identity_witness",
    },
    "vz_evasion": {
        "accepted_ActualDGU01OperatorCertificateInstance_V1",
        "independent_E_block_invertibility_closure",
        "subprincipal_extrinsic_curvature_characteristic_closure",
    },
    "rs_d_RS_minus_1": {"UCSDTypedRSMinusOneOperator_V1"},
    "rs_generation_count": {
        "accepted_UCSDTypedRSMinusOneOperator_V1_or_equivalent_RS_source_operator",
        "RS_family_identity_certificate",
        "noncompact_Y14_analytic_index_generation_count_proof_object",
    },
    "qft_finite_extraction": {
        "SourceDefinedLocalPhysicalFieldEquivalenceRelationAndDescentData_V1",
        "CandidateCongruenceGeneratorsForLocalGUPhysicalFieldEquivalence_V1",
    },
    "qft_rho_AB_CHSH_Bell": {
        "source_defined_F_phys_b_O",
        "source_defined_K_b",
        "descended_natural_P_fin_b",
        "certified_local_mode_images",
        "target_clean_state_construction",
    },
    "ptuj_visual_receipt": {
        "LawfulLocalTzSEvmqxu48FrameExtractor_V1",
        "OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1",
        "TzSEvmqxu48_FormulaBearingFrameOrSourceAssetPacket_V1",
    },
    "oxford_visual_receipt": {
        "source_clean_Oxford_to_D_GU_epsilon_identity_packet",
        "Oxford_source_surface_identity_into_SourceNaturalBianchiHighestWeightSelectorTheoremForK_IG_V1",
    },
    "dark_energy_theta_FLRW": {
        "independent_structural_theta_identification_closure",
        "source_clean_FLRW_dark_energy_reduction_assumption_closure",
    },
    "global_GU_claim": {"accepted_cross_family_source_objects_and_proof_chain"},
    "global_no_go": {"stated_theorem_class_assumptions_and_proof_of_route_exhaustion"},
}


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-readable JSON summary\.\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing section 8 machine-readable JSON summary")
    return json.loads(match.group(1))


class ClaimPromotionTargetImportFirewallAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)
        cls.claims = {
            claim["claim_id"]: claim for claim in cls.summary["claim_promotions"]
        }

    def test_artifact_identity_and_source_coverage(self) -> None:
        self.assertEqual(
            self.summary["artifact"], "ClaimPromotionTargetImportFirewallAfter0803_V1"
        )
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0803")
        self.assertEqual(self.summary["cycle"], 3)
        self.assertEqual(self.summary["lane"], 4)
        self.assertEqual(
            self.summary["verdict"],
            "ALL_NAMED_PROMOTIONS_BLOCKED_NO_TARGET_IMPORT_NO_PROOF_RESTART",
        )
        self.assertEqual(self.summary["verdict_class"], "promotion_firewall")
        self.assertEqual(
            self.summary["owned_path"],
            "explorations/hourly-20260625-0803-cycle3-claim-promotion-target-import-firewall.md",
        )
        self.assertEqual(
            self.summary["companion_audit"],
            "tests/hourly_20260625_0803_cycle3_claim_promotion_target_import_firewall_audit.py",
        )
        self.assertEqual(set(self.summary["sources_read_first"]), EXPECTED_SOURCES)

    def test_audit_state_blocks_all_global_and_restart_claims(self) -> None:
        state = self.summary["audit_state"]
        self.assertEqual(state["audited_cycle_count"], 2)
        self.assertEqual(state["audited_artifact_count"], 10)
        self.assertEqual(state["promotion_allowed_count"], 0)
        self.assertFalse(state["target_import_used"])
        self.assertFalse(state["accepted_receipt_implied"])
        self.assertFalse(state["proof_restart_implied"])
        self.assertEqual(state["accepted_receipt_count_implied"], 0)
        self.assertFalse(state["proof_restart_allowed"])
        self.assertFalse(state["global_gu_claim_promoted"])
        self.assertFalse(state["global_no_go_promoted"])
        self.assertTrue(self.summary["all_named_promotions_false"])
        self.assertTrue(self.summary["required_source_objects_named_for_every_claim"])
        self.assertTrue(self.summary["no_accepted_receipt_or_proof_restart_implied"])

    def test_all_named_promotions_are_present_and_false(self) -> None:
        self.assertEqual(set(self.claims), EXPECTED_CLAIM_IDS)
        self.assertEqual(len(self.claims), len(EXPECTED_CLAIM_IDS))
        for claim_id, claim in self.claims.items():
            with self.subTest(claim_id=claim_id):
                self.assertFalse(claim["promotion_allowed"])
                self.assertFalse(claim["target_import_used"])
                self.assertFalse(claim["accepted_receipt_implied"])
                self.assertFalse(claim["proof_restart_implied"])
                self.assertTrue(claim["first_exact_obstruction"])
                self.assertTrue(claim["target_import_risk"])

    def test_required_source_objects_are_named_for_every_claim(self) -> None:
        for claim_id, expected_objects in REQUIRED_SOURCE_OBJECTS_BY_CLAIM.items():
            with self.subTest(claim_id=claim_id):
                actual_objects = set(self.claims[claim_id]["required_source_objects"])
                self.assertEqual(actual_objects, expected_objects)
                for obj in expected_objects:
                    self.assertIn(obj, self.text)

    def test_no_accepted_receipt_or_proof_restart_language_is_implied(self) -> None:
        forbidden_positive_patterns = [
            r"\bpromotion_allowed:\s*true\b",
            r'"promotion_allowed"\s*:\s*true',
            r"\btarget_import_used:\s*true\b",
            r'"target_import_used"\s*:\s*true',
            r"\baccepted_receipt_implied:\s*true\b",
            r'"accepted_receipt_implied"\s*:\s*true',
            r"\bproof_restart_implied:\s*true\b",
            r'"proof_restart_implied"\s*:\s*true',
            r"\bproof_restart_allowed:\s*true\b",
            r'"proof_restart_allowed"\s*:\s*true',
            r"\bglobal_gu_claim_promoted:\s*true\b",
            r'"global_gu_claim_promoted"\s*:\s*true',
            r"\bglobal_no_go_promoted:\s*true\b",
            r'"global_no_go_promoted"\s*:\s*true',
        ]
        for pattern in forbidden_positive_patterns:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                f"forbidden positive implication matched: {pattern}",
            )

    def test_specific_first_obstructions_remain_upstream(self) -> None:
        expected = {
            "ig_selector_acceptance": "SourceNaturalBianchiHighestWeightSelectorTheoremForK_IG_V1",
            "dgu_actual_operator": "ActualDGU01OperatorCertificateInstance_V1.source_clean_actual_operator_identity_witness",
            "vz_evasion": "accepted_ActualDGU01OperatorCertificateInstance_V1",
            "rs_d_RS_minus_1": "UCSDTypedRSMinusOneOperator_V1",
            "rs_generation_count": "accepted_UCSDTypedRSMinusOneOperator_V1_or_equivalent_RS_source_operator",
            "qft_finite_extraction": "source_defined_congruence_generators_for_tilde_phys_b_O",
            "qft_rho_AB_CHSH_Bell": "source_defined_congruence_generators_for_tilde_phys_b_O",
            "ptuj_visual_receipt": "LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1",
            "oxford_visual_receipt": "source_clean_family_identity_witness_from_Oxford_visual_or_bosonic_anchor",
            "dark_energy_theta_FLRW": "canon_conditional_structural_identification_and_reduction_assumptions",
            "global_GU_claim": "accepted_cross_family_proof_chain_absent",
            "global_no_go": "global_no_go_theorem_absent",
        }
        for claim_id, obstruction in expected.items():
            with self.subTest(claim_id=claim_id):
                self.assertEqual(self.claims[claim_id]["first_exact_obstruction"], obstruction)

    def test_firewall_rules_include_no_target_import_and_no_global_inflation(self) -> None:
        rules = set(self.summary["firewall_rules"])
        for rule in [
            "FR-03_canon_existence_is_not_selector_without_uniqueness_or_source_selection",
            "FR-04_visual_locator_metadata_or_caption_is_not_formula_receipt",
            "FR-06_VZ_evasion_requires_actual_DGU_certificate_and_open_VZ_preconditions",
            "FR-08_QFT_Bell_restart_requires_source_quotient_codomain_descent_and_naturality",
            "FR-10_route_local_block_is_not_global_GU_no_go",
            "FR-11_target_success_data_may_not_select_upstream_source_objects",
        ]:
            self.assertIn(rule, rules)

    def test_required_sections_present(self) -> None:
        for heading in [
            "## 1. Verdict.",
            "## 2. Promotion firewall rules.",
            "## 3. Claim-by-claim promotion table.",
            "## 4. Target-import screens.",
            "## 5. First exact obstruction per claim family.",
            "## 6. What would change if closed.",
            "## 7. Falsification/demotion condition.",
            "## 8. Machine-readable JSON summary.",
        ]:
            self.assertIn(heading, self.text)

    def test_falsification_and_closure_language_is_scoped(self) -> None:
        self.assertIn("route-local claims", self.summary["falsification_or_demotion_condition"])
        self.assertIn("do not promote global no-go", self.summary["falsification_or_demotion_condition"])
        self.assertIn("no closure listed here automatically proves global GU or global no-go", self.summary["what_would_change_if_closed"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
