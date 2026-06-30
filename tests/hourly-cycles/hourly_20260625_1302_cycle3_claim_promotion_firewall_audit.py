#!/usr/bin/env python3
"""Audit ClaimPromotionFirewallAfter1302_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-1302-cycle3-claim-promotion-firewall.md"
)

EXPECTED_CLAIMS = {
    "ptuj_formula_receipt",
    "ig_K_IG_selector_theorem",
    "dgu_actual_operator_certificate",
    "dgu_vz_replay",
    "rs_d_RS_minus_1",
    "rs_generation_restart",
    "qft_F_phys",
    "qft_P_fin",
    "qft_rho_AB_CHSH",
    "dark_energy_generation_global_GU_claims",
    "global_no_go",
    "target_import_derived_promotion",
}

EXPECTED_SOURCES = {
    "RESEARCH-POSTURE.md",
    "process/runbooks/five-lane-frontier-run.md",
    "explorations/hourly-20260625-1302-cycle1-dgu-identity-witness.md",
    "explorations/hourly-20260625-1302-cycle1-ig-selector-theorem.md",
    "explorations/hourly-20260625-1302-cycle1-ptuj-extractor-branch.md",
    "explorations/hourly-20260625-1302-cycle1-qft-congruence-generators.md",
    "explorations/hourly-20260625-1302-cycle1-rs-ucsd-frame-packet.md",
    "explorations/hourly-20260625-1302-cycle2-dgu-identity-field-protocol-gate.md",
    "explorations/hourly-20260625-1302-cycle2-ig-d7-multiplicity-audit-gate.md",
    "explorations/hourly-20260625-1302-cycle2-ptuj-toolchain-manifest-gate.md",
    "explorations/hourly-20260625-1302-cycle2-qft-gauge-action-restriction-stability-gate.md",
    "explorations/hourly-20260625-1302-cycle2-rs-ucsd-frame-acquisition-contract.md",
    "explorations/hourly-20260625-0803-cycle3-claim-promotion-target-import-firewall.md",
}

REQUIRED_OBJECT_SNIPPETS = {
    "ptuj_formula_receipt": "TzSEvmqxu48_FormulaBearingFrameOrSourceAssetPacket_V1",
    "ig_K_IG_selector_theorem": "VerifiedMultiplicityAndHighestWeightSelectorPacketForShiabHomSpace_V1",
    "dgu_actual_operator_certificate": "ActualDGU01IdentityWitness_V1",
    "dgu_vz_replay": "ActualDGU01OperatorCertificateInstance_V1",
    "rs_d_RS_minus_1": "UCSDTypedRSMinusOneOperator_V1",
    "rs_generation_restart": "noncompact_Y14_analytic_index_generation_count_proof_object",
    "qft_F_phys": "LocalGaugeActionGroupoidOnObservedRawGUFields_V1",
    "qft_P_fin": "SourceDefinedLocalPhysicalFieldEquivalenceRelationAndDescentData_V1",
    "qft_rho_AB_CHSH": "target_clean_state_construction",
    "dark_energy_generation_global_GU_claims": "cross_family_proof_chains",
    "global_no_go": "route_exhaustion_proof",
    "target_import_derived_promotion": "recorded_non_import_proof",
}


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 5\. Machine-readable JSON summary\.\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary")
    return json.loads(match.group(1))


class ClaimPromotionFirewallAfter1302Audit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)
        cls.claims = {
            claim["claim_id"]: claim for claim in cls.summary["claim_families"]
        }

    def test_artifact_identity(self) -> None:
        self.assertEqual(self.summary["artifact"], "ClaimPromotionFirewallAfter1302_V1")
        self.assertEqual(self.summary["run_id"], "hourly-20260625-1302")
        self.assertEqual(self.summary["cycle"], 3)
        self.assertEqual(self.summary["lane"], 4)
        self.assertEqual(
            self.summary["verdict"],
            "ALL_NAMED_PROMOTIONS_BLOCKED_NO_TARGET_IMPORT",
        )
        self.assertEqual(self.summary["verdict_class"], "promotion_firewall")
        self.assertEqual(
            self.summary["owned_path"],
            "explorations/hourly-20260625-1302-cycle3-claim-promotion-firewall.md",
        )
        self.assertEqual(
            self.summary["companion_audit"],
            "tests/hourly_20260625_1302_cycle3_claim_promotion_firewall_audit.py",
        )

    def test_sources_and_claim_families_are_complete(self) -> None:
        self.assertEqual(set(self.summary["sources_read_first"]), EXPECTED_SOURCES)
        self.assertEqual(set(self.claims), EXPECTED_CLAIMS)
        self.assertEqual(len(self.claims), 12)
        self.assertTrue(self.summary["all_named_claim_families_present"])

    def test_required_summary_booleans(self) -> None:
        self.assertEqual(self.summary["promotions_allowed"], 0)
        self.assertEqual(self.summary["promotions_blocked"], 12)
        self.assertFalse(self.summary["target_import_used"])
        self.assertFalse(self.summary["major_GU_claim_promoted"])
        self.assertFalse(self.summary["global_no_go_promoted"])

        state = self.summary["audit_state"]
        self.assertEqual(state["promotions_allowed"], 0)
        self.assertEqual(state["promotions_blocked"], 12)
        self.assertFalse(state["target_import_used"])
        self.assertFalse(state["target_import_used_to_select_source_object"])
        self.assertFalse(state["target_import_used_to_restart_proof"])
        self.assertFalse(state["accepted_receipt_implied"])
        self.assertFalse(state["proof_restart_implied"])
        self.assertFalse(state["major_GU_claim_promoted"])
        self.assertFalse(state["global_no_go_promoted"])

    def test_every_claim_blocks_promotion_and_target_import(self) -> None:
        for claim_id, claim in self.claims.items():
            with self.subTest(claim_id=claim_id):
                self.assertEqual(claim["decision"], "blocked")
                self.assertFalse(claim["promotion_allowed"])
                self.assertFalse(claim["target_import_used"])
                self.assertIn(
                    REQUIRED_OBJECT_SNIPPETS[claim_id],
                    claim["required_missing_object"],
                )

    def test_named_claim_families_appear_in_plain_english_sections(self) -> None:
        required_plain_terms = [
            "PTUJ formula receipt",
            "IG `K_IG` selector theorem",
            "DGU actual operator certificate",
            "DGU/VZ replay",
            "RS `d_RS,-1`",
            "RS generation restart",
            "QFT `F_phys`",
            "QFT `P_fin`",
            "QFT `rho_AB` / CHSH",
            "dark-energy / generation / global GU claims",
            "global no-go",
            "target-import-derived promotion",
        ]
        for term in required_plain_terms:
            with self.subTest(term=term):
                self.assertIn(term, self.text)

    def test_disallowed_positive_promotion_phrases_are_absent(self) -> None:
        forbidden_patterns = [
            r"\bpromotion_allowed\s*:\s*true\b",
            r'"promotion_allowed"\s*:\s*true',
            r"\btarget_import_used\s*:\s*true\b",
            r'"target_import_used"\s*:\s*true',
            r"\bmajor_GU_claim_promoted\s*:\s*true\b",
            r'"major_GU_claim_promoted"\s*:\s*true',
            r"\bglobal_no_go_promoted\s*:\s*true\b",
            r'"global_no_go_promoted"\s*:\s*true',
            r"\bproof_restart_allowed\s*:\s*true\b",
            r"\baccepted_receipt_count\s*:\s*[1-9]\d*\b",
            r"\bpromotions_allowed\s*:\s*[1-9]\d*\b",
            r"\bmajor GU claim is promoted\b",
            r"\bglobal no-go is promoted\b",
            r"\bformula receipt is accepted\b",
            r"\bVZ replay is allowed\b",
            r"\bgeneration restart is allowed\b",
            r"\bCHSH recovery is established\b",
        ]
        for pattern in forbidden_patterns:
            with self.subTest(pattern=pattern):
                self.assertIsNone(
                    re.search(pattern, self.text, flags=re.IGNORECASE),
                    f"forbidden promotion phrase matched: {pattern}",
                )

    def test_required_sections_present(self) -> None:
        for heading in [
            "## 1. Verdict.",
            "## 2. Promotion table with claim, current status, required missing object, decision.",
            "## 3. Target-import firewall checks.",
            "## 4. Allowed next actions vs forbidden promotions.",
            "## 5. Machine-readable JSON summary.",
        ]:
            self.assertIn(heading, self.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
