"""Audit the Cycle 3 RS source differential origin screen.

This audit checks that the artifact decides the source-origin question for
``d_RS,-1`` without promoting raw RS symbol data into a physical quotient,
H-index, rank, or generation claim.
"""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "explorations" / "hourly-cycle3-rs-source-differential-origin-screen-2026-06-25.md"

REQUIRED_SECTIONS = [
    "## 1. Verdict",
    "## 2. What Was Derived Directly From Repo Sources",
    "## 3. Strongest Positive Construction Attempt",
    "## 4. First Exact Obstruction Or Missing Proof Object",
    "## 5. Constructive Next Object",
    "## 6. Impact On GU Claim",
    "## 7. Next Meaningful Proof/Computation Step",
    "## 8. Machine-Readable JSON Summary",
]

REQUIRED_EFFECT_LAYERS = {"source", "projection", "finality", "loss"}

FORBIDDEN_PROMOTION_PATTERNS = [
    r"\bphysical rank is derived\b",
    r"\bH-index is derived\b",
    r"\brank 3 is derived\b",
    r"\brank 4 is derived\b",
    r"\brank 8 is derived\b",
    r"\bthree generations are derived\b",
    r"\bfour generations are derived\b",
    r"\bPi_raw\s*=\s*Pi_RS\^phys\b",
    r"\braw principal symbol proves d_RS,-1\b",
]


def extract_json_summary(text: str) -> dict[str, object]:
    pattern = re.compile(r"```json\n(?P<body>\{.*?\})\n```", re.DOTALL)
    for match in pattern.finditer(text):
        data = json.loads(match.group("body"))
        if data.get("artifact") == "HOURLY_CYCLE3_RS_SOURCE_DIFFERENTIAL_ORIGIN_SCREEN":
            return data
    raise AssertionError("Cycle 3 RS source differential origin JSON summary not found")


class HourlyCycle3RSSourceDifferentialOriginScreenAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.data = extract_json_summary(cls.text)

    def test_required_sections_present(self) -> None:
        for section in REQUIRED_SECTIONS:
            self.assertIn(section, self.text)

    def test_verdict_blocks_on_source_origin_not_raw_symbol(self) -> None:
        self.assertEqual(
            self.data["verdict"],
            "BLOCKED_RAW_PRINCIPAL_SYMBOL_ONLY__SOURCE_DERIVED_D_RS_MINUS_1_NOT_SUPPLIED",
        )
        self.assertEqual(self.data["decision_for_current_sources"], "FAIL_SOURCE_DERIVATION_GATE")
        screened = self.data["screened_object"]
        self.assertEqual(screened["id"], "d_RS,-1")
        self.assertEqual(screened["required_map"], "Ghost_RS,H^src -> Field_RS,H^src")
        self.assertEqual(screened["current_status"], "NOT_SUPPLIED")

    def test_source_context_distinguishes_raw_symbol_from_source_theorem(self) -> None:
        context = self.data["source_derived_context"]
        self.assertTrue(context["raw_gamma_trace_projectors_available"])
        self.assertTrue(context["raw_principal_gauge_symbol_available"])
        self.assertEqual(context["raw_principal_gauge_symbol"], "epsilon -> xi tensor epsilon")
        self.assertTrue(context["reconstruction_grade_nabla_epsilon_gauge_language_available"])
        self.assertTrue(context["typed_operator_action_spine_available_as_host"])
        self.assertFalse(context["actual_D_GU_source_closed_operator_certificate_available"])
        self.assertFalse(context["action_or_source_theorem_derived_d_RS_minus_1_available"])
        self.assertFalse(context["BRST_complex_or_gauge_fixed_finality_available"])
        self.assertFalse(context["Pi_RS_phys_defined"])

    def test_strongest_positive_construction_remains_candidate_shape_only(self) -> None:
        attempt = self.data["strongest_positive_construction_attempt"]
        self.assertEqual(
            attempt["candidate_formula"],
            "d_candidate(epsilon)=Pi_gamma_free(nabla^A epsilon)",
        )
        self.assertEqual(attempt["candidate_principal_symbol"], "P_plus(xi tensor epsilon)")
        self.assertTrue(attempt["uses_repo_raw_symbol"])
        self.assertTrue(attempt["uses_AF4_reconstruction_gauge_phrase"])
        self.assertEqual(attempt["status"], "CANDIDATE_SHAPE_ONLY_NOT_SOURCE_DERIVED")
        for required in [
            "primary_GU_action_operator_or_EL_derives_the_symmetry",
            "right_H_linearity_is_proved_from_source_connection",
            "BRST_complex_or_gauge_fixed_elliptic_block_is_supplied",
            "loss_ledger_is_complete_and_target_free",
        ]:
            self.assertIn(required, attempt["would_pass_if"])

    def test_first_obstruction_is_source_action_or_operator(self) -> None:
        obstruction = self.data["first_exact_obstruction"]
        self.assertEqual(
            obstruction["field"],
            "RS_SOURCE_ORIGIN_CERTIFICATE.source_action_or_operator",
        )
        self.assertEqual(obstruction["status"], "MISSING")
        self.assertIn("No current repo source derives d_RS,-1", obstruction["description"])
        self.assertIn("Projection, finality, loss", obstruction["why_first"])
        self.assertIn("raw principal symbol epsilon -> xi tensor epsilon", obstruction["not_enough"])
        self.assertIn("reconstruction-grade psi_a ~ psi_a + nabla_a epsilon statement", obstruction["not_enough"])

    def test_constructive_next_certificate_has_required_sections_and_decisions(self) -> None:
        next_object = self.data["constructive_next_object"]
        self.assertEqual(next_object["id"], "RS_D_MINUS_1_SOURCE_ORIGIN_CERTIFICATE_V1")
        self.assertEqual(
            set(next_object["required_sections"]),
            {
                "source_action_or_operator",
                "ghost_module",
                "field_module",
                "differential",
                "source_symmetry",
                "projection_semantics",
                "finality",
                "loss",
                "target_quarantine",
            },
        )
        for status in [
            "ACCEPT_SOURCE_DERIVED_D_RS_MINUS_1",
            "FAIL_SOURCE_ACTION_OR_OPERATOR_MISSING",
            "FAIL_ONLY_RAW_PRINCIPAL_SYMBOL",
            "FAIL_ONLY_RECONSTRUCTION_GAUGE_PROSE",
            "FAIL_NO_BRST_OR_GAUGE_FIXED_FINALITY",
            "INVALID_TARGET_INPUT",
        ]:
            self.assertIn(status, next_object["decision_statuses"])

    def test_effect_layers_are_present_and_blocked_correctly(self) -> None:
        layers = self.data["effect_layers"]
        self.assertEqual(set(layers), REQUIRED_EFFECT_LAYERS)
        self.assertEqual(layers["source"]["status"], "MISSING_SOURCE_DERIVATION")
        self.assertTrue(layers["source"]["raw_symbol_available"])
        self.assertFalse(layers["source"]["source_theorem_available"])
        self.assertEqual(layers["projection"]["status"], "BLOCKED_BY_SOURCE")
        self.assertFalse(layers["projection"]["Pi_RS_phys_defined"])
        self.assertFalse(layers["projection"]["may_identify_Pi_raw_with_Pi_RS_phys"])
        self.assertEqual(layers["finality"]["status"], "BLOCKED_BY_SOURCE")
        self.assertFalse(layers["finality"]["BRST_complex_available"])
        self.assertFalse(layers["finality"]["gauge_fixed_elliptic_block_available"])
        self.assertFalse(layers["finality"]["symbol_exact_or_elliptic_all_nonzero_xi"])
        self.assertEqual(layers["loss"]["status"], "BLOCKED_BY_SOURCE")
        self.assertFalse(layers["loss"]["complete_loss_ledger_available"])

    def test_rank_quarantine_is_active_and_covers_requested_claims(self) -> None:
        quarantine = self.data["rank_quarantine"]
        self.assertEqual(quarantine["status"], "ACTIVE")
        for key in [
            "promote_physical_rank_now",
            "promote_H_index_now",
            "promote_rank_3_now",
            "promote_rank_4_now",
            "promote_rank_8_now",
            "promote_generation_count_now",
        ]:
            self.assertFalse(quarantine[key])
        for forbidden in [
            "physical_rank_target",
            "H_index_target",
            "rank_3",
            "rank_4",
            "rank_8",
            "three_generations",
            "four_generations",
            "raw_projector_rank_as_physical_rank",
            "raw_projected_gauge_image_as_physical_loss",
        ]:
            self.assertIn(forbidden, quarantine["forbidden_inputs"])

    def test_rollback_conditions_cover_source_projection_finality_loss_and_rank(self) -> None:
        rollback = set(self.data["rollback_conditions"])
        for condition in [
            "claims_source_derived_d_RS_minus_1_from_raw_principal_symbol_only",
            "claims_source_derived_d_RS_minus_1_from_AF4_gauge_prose_only",
            "identifies_Pi_raw_with_Pi_RS_phys_without_source_origin_certificate",
            "uses_projected_raw_gauge_image_as_physical_loss_without_BRST_finality",
            "claims_physical_rank_before_RS_D_MINUS_1_SOURCE_ORIGIN_CERTIFICATE_V1_accepts",
            "claims_H_index_before_final_H_linear_Fredholm_object_exists",
            "claims_rank_3_or_rank_4_or_rank_8_before_source_finality",
            "claims_generation_count_before_source_finality",
            "imports_target_normalization_or_generation_value_as_construction_input",
        ]:
            self.assertIn(condition, rollback)

    def test_impact_keeps_gu_branch_open_but_source_origin_blocked(self) -> None:
        impact = self.data["impact_on_GU_claim"]
        self.assertFalse(impact["GU_RS_branch_falsified"])
        self.assertEqual(impact["current_branch_status"], "SOURCE_ORIGIN_BLOCKED")
        self.assertIn("action_or_source_theorem_derived_H_linear_d_RS_minus_1", impact["what_must_exist_if_branch_correct"])
        self.assertEqual(
            impact["next_gate"],
            "fill_RS_D_MINUS_1_SOURCE_ORIGIN_CERTIFICATE_V1_then_rerun_quotient_transport_builder",
        )

    def test_no_forbidden_promotion_language(self) -> None:
        for pattern in FORBIDDEN_PROMOTION_PATTERNS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                msg=f"forbidden promotion pattern present: {pattern}",
            )


if __name__ == "__main__":
    unittest.main()
