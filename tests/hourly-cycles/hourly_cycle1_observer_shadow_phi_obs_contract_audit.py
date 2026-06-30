#!/usr/bin/env python3
"""Audit the Cycle 1 Phi_obs observer-shadow contract artifact.

This is a structural contract audit, not a proof. It checks that the artifact
keeps finite Connes control in its target-facing role, requires concrete
Phi_obs fields, records the exact-channel versus replacement-shadow decision,
and does not promote SM gauge, Higgs, or generation claims to derivations.
"""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "explorations" / "hourly-cycle1-observer-shadow-phi-obs-contract-2026-06-24.md"

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Exact finite Connes-channel vs replacement-shadow decision",
    "## 3. What was derived directly from repo sources",
    "## 4. Strongest positive contract",
    "## 5. First exact obstruction or missing proof object",
    "## 6. Impact for Type II1/SM selector claims",
    "## 7. Next meaningful proof or computation",
    "## 8. Machine-readable JSON summary",
]

REQUIRED_PHI_OBS_FIELDS = {
    "observer_algebra_or_gauge_object",
    "chiral_fermion_representation_list",
    "generation_decomposition",
    "real_structure_and_grading_signs",
    "dirac_and_first_order_control",
    "higgs_scalar_and_action_status",
    "anomaly_freed_hopkins_input",
    "substrate_mode_policy",
    "target_data_provenance",
    "replacement_tests",
    "rollback_conditions",
}

REQUIRED_PROVENANCE_KEYS = {
    "A_F",
    "G_SM_Z6",
    "K_SM_T1",
    "T3_generations",
    "Higgs",
    "Anomaly_shadow",
    "Spectral_action",
}

FORBIDDEN_PROMOTION_PATTERNS = [
    r"\bSM gauge group is derived\b",
    r"\bthe SM gauge group has been derived\b",
    r"\bHiggs sector is derived\b",
    r"\bthe Higgs sector has been derived\b",
    r"\bthree generations are derived\b",
    r"\bType II1 selects three generations\b",
    r"\bStandard Model is derived\b",
    r"\bthe Standard Model has been derived\b",
    r"\bSM gauge/Higgs/generations are derived\b",
]


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing Phi_obs contract artifact: {DOC}") from exc


def extract_json_summary(text: str) -> dict[str, Any]:
    marker = "## 8. Machine-readable JSON summary"
    if marker not in text:
        raise AssertionError("missing JSON summary heading")
    tail = text.split(marker, 1)[1]
    match = re.search(r"```json\s*(\{.*?\})\s*```", tail, flags=re.DOTALL)
    if not match:
        raise AssertionError("missing fenced JSON summary block")
    return json.loads(match.group(1))


class PhiObsContractAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_json_summary(cls.text)

    def test_required_sections_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_finite_connes_control_not_primary_substrate_axiom(self) -> None:
        self.assertIn(
            "Finite Connes control is not a primary GU substrate axiom.",
            self.text,
        )
        self.assertEqual(
            self.summary["finite_connes_control_role"],
            "target_facing_certificate_not_primary_GU_substrate_axiom",
        )
        self.assertIn(
            "finite_Connes_control_treated_as_primary_GU_substrate_axiom",
            self.summary["rollback_conditions"],
        )

    def test_phi_obs_decision_fields_are_explicit(self) -> None:
        decision = self.summary["phi_obs_decision"]
        self.assertIs(decision["exact_finite_connes_channel"], False)
        self.assertIs(decision["replacement_shadow_declared"], False)
        self.assertEqual(decision["current_status"], "contract_only_underdefined")
        self.assertIn("requires_explicit_Phi_obs", decision["allowed_current_claim"])

    def test_phi_obs_contract_requires_all_fields(self) -> None:
        contract = self.summary["phi_obs_contract"]
        self.assertEqual(
            set(contract["required_fields"]),
            REQUIRED_PHI_OBS_FIELDS,
        )
        self.assertEqual(
            set(contract["allowed_modes"]),
            {"exact_finite_connes_channel", "replacement_shadow"},
        )
        for status in ["derived", "derived_relative", "hosted", "imported", "failed", "open"]:
            self.assertIn(status, contract["status_vocabulary"])

    def test_target_data_provenance_ledger_is_present_and_nonpromoting(self) -> None:
        ledger = self.summary["target_data_provenance_current"]
        self.assertEqual(set(ledger), REQUIRED_PROVENANCE_KEYS)
        self.assertIn("missing", ledger["A_F"])
        self.assertIn("missing", ledger["G_SM_Z6"])
        self.assertIn("not_selected", ledger["T3_generations"])
        self.assertIn("hosted", ledger["Higgs"])
        self.assertNotEqual(ledger["G_SM_Z6"], "derived")
        self.assertNotEqual(ledger["T3_generations"], "derived")
        self.assertNotEqual(ledger["Higgs"], "derived")

    def test_forbidden_target_inputs_are_machine_readable(self) -> None:
        forbidden = set(self.summary["forbidden_target_inputs"])
        for item in [
            "A_F",
            "finite_CC_tuple",
            "G_SM_Z6",
            "central_Z6",
            "K_SM",
            "n_equals_3",
            "C3",
            "index_3",
            "D4_arms",
            "three_projections",
            "dim_H_F_96",
            "ordinary_anomaly_free_SM_shadow",
            "physical_Higgs_data",
        ]:
            self.assertIn(item, forbidden)

    def test_first_missing_objects_are_named(self) -> None:
        missing = self.summary["first_missing_objects"]
        self.assertIn("P0_choose_exact_finite_Connes_channel_or_declared_replacement_shadow", missing)
        self.assertIn("FC_EPSILON_for_exact_channel_KO6_contact", missing)
        self.assertIn("A_F_selector_without_forbidden_target_input", missing)
        self.assertIn("REPLACEMENT_CODOMAIN_for_non_CC_shadow", missing)

    def test_no_sm_gauge_higgs_or_generations_derivation_is_claimed(self) -> None:
        self.assertIs(self.summary["no_observer_facing_sm_derivation_claim"], True)
        impacts = self.summary["selector_claim_impacts"]
        self.assertEqual(impacts["SM_GAUGE"], "not_derived")
        self.assertIn("open", impacts["HIGGS"])
        self.assertIn("not_selected", impacts["GENERATIONS"])
        for pattern in FORBIDDEN_PROMOTION_PATTERNS:
            self.assertIsNone(re.search(pattern, self.text), pattern)

    def test_rollback_conditions_cover_target_smuggling(self) -> None:
        rollback = set(self.summary["rollback_conditions"])
        for condition in [
            "target_data_used_as_selector_input",
            "n2_or_n4_replacement_proof_still_works",
            "extra_observer_modes_without_anomaly_computation",
            "Higgs_slot_without_physical_projection_and_action",
            "FC_EPSILON_fails_for_exact_CC_contact",
        ]:
            self.assertIn(condition, rollback)


if __name__ == "__main__":
    unittest.main(verbosity=2)
