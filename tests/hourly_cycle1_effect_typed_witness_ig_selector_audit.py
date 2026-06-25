#!/usr/bin/env python3
"""Audit the hourly Cycle 1 effect-typed witness IG selector artifact.

This is a structural provenance audit, not a physics computation. It checks
that the artifact exposes an effect-typed source/projection/finality/loss
contract, keeps K_IG selection underdefined until a finality witness exists,
and blocks dark-energy/theta coefficient overclaims.
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
    / "hourly-cycle1-effect-typed-witness-ig-selector-2026-06-25.md"
)

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. What was derived directly from repo sources",
    "## 3. The strongest positive result",
    "## 4. The first exact obstruction or missing proof object",
    "## 5. The constructive next object that would remove or test the obstruction",
    "## 6. What this means for the relevant GU claim",
    "## 7. Next meaningful proof or computation step",
    "## 8. Machine-readable JSON summary",
]

REQUIRED_CONTRACT_GROUPS = [
    "source_effects_required",
    "projection_effects_required",
    "finality_effects_required",
    "loss_effects_required",
]

REQUIRED_ROLLBACKS = {
    "K_IG_chosen_by_naturalness_not_source",
    "EffectTypedWitnessTransport_promoted_from_contract_to_selector_without_finality",
    "projection_loss_hides_competing_operator",
    "field_degrees_not_source_selected",
    "Q_IG_not_selected",
    "Z_U_target_fitted",
    "V_src_or_S_cross_src_chosen_after_target",
    "boundary_data_chosen_after_target",
    "S_IG_dyn_template_promoted_without_selector",
    "theta_eff_asserted_without_delta_A_current",
    "Noether_identity_not_written",
    "bare_theta_source_retained_in_Branch_3",
    "bare_Lambda_inserted",
    "bare_Rtheta_inserted",
    "Z_theta_or_C_Rtheta_claimed_without_FLRW_reduction",
    "xi_eff_fitted_not_generated",
    "dark_energy_derivation_claimed_before_selector_closes",
    "DESI_Rubin_window_used_upstream",
    "replacement_or_withheld_target_check_changes_selector",
}

FORBIDDEN_POSITIVE_DERIVATION_PATTERNS = [
    r"\bEffectTypedWitnessTransport\s+(now|currently|successfully)\s+derives\s+(dark energy|Lambda|Z_theta|C_Rtheta|xi_eff)\b",
    r"\bGU\s+(currently\s+)?derives\s+(dark energy|Lambda|Z_theta|C_Rtheta|xi_eff)\b",
    r"\bBranch 3\s+(now|currently|successfully)\s+emits\s+the\s+theta/FLRW\s+coefficient\s+packet\b",
    r"\bK_IG\s*=\s*D_A U\s+is\s+(now|currently|successfully)\s+source-forced\b",
    r'"GU_derives_dark_energy"\s*:\s*true',
    r'"GU_derives_Lambda"\s*:\s*true',
    r'"GU_derives_Z_theta"\s*:\s*true',
    r'"GU_derives_C_Rtheta"\s*:\s*true',
    r'"GU_derives_xi_eff"\s*:\s*true',
]


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing witness selector artifact: {DOC}") from exc


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-readable JSON summary\s*```json\s*(.*?)\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class EffectTypedWitnessIGSelectorAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_required_sections_are_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_verdict_and_selector_status_are_blocking(self) -> None:
        self.assertEqual(self.summary["mission_posture"], "Mission_A_constructive_obstruction")
        self.assertEqual(self.summary["verdict"], "conditional_underdefined")
        self.assertEqual(self.summary["interface_name"], "EffectTypedWitnessTransport")
        self.assertTrue(self.summary["interface_emitted_as_contract"])
        self.assertFalse(self.summary["selector_emitted_by_repo_sources"])
        self.assertFalse(self.summary["K_IG_source_selected"])
        self.assertEqual(self.summary["candidate_K_IG"], "D_A U")
        self.assertEqual(
            self.summary["candidate_K_IG_status"],
            "well_typed_admissible_template_not_source_forced",
        )
        self.assertFalse(self.summary["target_comparison_permitted"])
        self.assertEqual(self.summary["target_inputs_seen_before_selector"], [])

    def test_contract_has_source_projection_finality_loss_parts(self) -> None:
        contract = self.summary["transport_contract"]
        for group in REQUIRED_CONTRACT_GROUPS:
            self.assertIn(group, contract)
            self.assertTrue(contract[group], group)

        self.assertIn("target_inputs_seen_empty", contract["source_effects_required"])
        self.assertIn("record_projection_loss", contract["projection_effects_required"])
        self.assertIn(
            "or_explicit_source_axiom_selecting_one_packet",
            contract["finality_effects_required"],
        )
        self.assertIn("competing_operators_not_eliminated", contract["loss_effects_required"])

    def test_strongest_positive_result_is_contract_not_derivation(self) -> None:
        result = self.summary["strongest_positive_result"]
        self.assertEqual(result["type"], "typed_contract_not_selector")
        self.assertEqual(result["candidate_branch"], "Branch_3_dynamical_IG_total_current")
        self.assertEqual(result["candidate_field_degrees"]["U"], "Omega^1(Y,ad P)")
        self.assertEqual(result["candidate_field_degrees"]["P_IG"], "Omega^2(Y,ad P)")
        self.assertEqual(result["candidate_parent_slot"], "int_Y <P_IG,D_A U>_{Q_IG}")
        self.assertFalse(result["positive_derivation_claim"])

    def test_first_obstruction_is_finality_certificate(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["id"], "K_IGWitnessFinalityCertificate")
        self.assertEqual(obstruction["equivalent_id"], "K_IG_selector")
        self.assertTrue(obstruction["missing_status"])
        self.assertEqual(
            obstruction["needed_to_distinguish"],
            "D_A_U_admissible_template_from_D_A_U_GU_selected_operator",
        )

        ordered = self.summary["ordered_missing_objects"]
        self.assertEqual(ordered[0], "K_IGWitnessFinalityCertificate")
        self.assertLess(ordered.index("K_IGWitnessFinalityCertificate"), ordered.index("Q_IG_selected_in_same_normalization"))
        self.assertLess(ordered.index("source_forced_S_IG_dyn_or_parent_action"), ordered.index("theta_eff"))
        self.assertLess(ordered.index("FLRWQuadraticReductionPacket"), ordered.index("Z_theta"))
        self.assertLess(ordered.index("Z_theta"), ordered.index("xi_eff"))

    def test_anti_overclaim_flags_are_false_and_text_has_no_positive_claims(self) -> None:
        anti = self.summary["anti_overclaim"]
        for key in [
            "GU_derives_dark_energy",
            "GU_derives_Lambda",
            "GU_derives_Z_theta",
            "GU_derives_C_Rtheta",
            "GU_derives_xi_eff",
            "EffectTypedWitnessTransport_derives_selector",
            "Branch_3_emits_theta_FLRW_packet",
            "candidate_naturalness_counts_as_source_selection",
        ]:
            self.assertFalse(anti[key], key)

        for pattern in FORBIDDEN_POSITIVE_DERIVATION_PATTERNS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                pattern,
            )

    def test_rollback_conditions_cover_selector_and_target_leakage(self) -> None:
        rollbacks = set(self.summary["rollback_conditions"])
        missing = REQUIRED_ROLLBACKS - rollbacks
        self.assertFalse(missing, f"missing rollback conditions: {sorted(missing)}")

    def test_next_object_is_witness_selection_test_before_cosmology(self) -> None:
        next_object = self.summary["constructive_next_object"]
        self.assertEqual(next_object["id"], "K_IGWitnessSelectionTest_V1")
        self.assertTrue(next_object["do_next"])
        self.assertEqual(
            next_object["avoid_next"],
            "theta_FLRW_or_cosmology_comparison_before_witness_finality",
        )
        required = set(next_object["required_outputs"])
        self.assertIn("admissible_operator_list", required)
        self.assertIn("effect_type_signature", required)
        self.assertIn("projection_loss_ledger", required)
        self.assertIn("replacement_target_check", required)
        self.assertEqual(
            set(next_object["possible_decisions"]),
            {"FINAL", "AXIOMATIC", "MULTIPLE", "NONE"},
        )

    def test_claim_impact_does_not_promote_gu_claim(self) -> None:
        impact = self.summary["claim_impact"]
        self.assertFalse(impact["relevant_GU_claim_promoted"])
        self.assertEqual(impact["Branch_3_status"], "coherent_host_not_selected")
        self.assertEqual(impact["selector_status"], "more_precisely_testable_not_closed")
        self.assertEqual(impact["theta_FLRW_packet_status"], "blocked_downstream_of_K_IG_selector")


if __name__ == "__main__":
    unittest.main(verbosity=2)
