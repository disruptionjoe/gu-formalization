#!/usr/bin/env python3
"""Audit the Cycle 2 RS quotient transport builder artifact.

The audit checks that the artifact specifies a machine-readable builder for
the RS quotient transport gate while preserving the d_RS,-1 obstruction and
quarantining rank/generation claims.
"""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-cycle2-rs-quotient-transport-builder-2026-06-25.md"
)


REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. What Was Derived Directly From Repo Sources",
    "## 3. Strongest Positive Construction Attempt",
    "## 4. First Exact Obstruction Or Missing Proof Object",
    "## 5. Constructive Next Object",
    "## 6. Impact On GU Claim",
    "## 7. Next Meaningful Proof/Computation Step",
    "## 8. Machine-Readable JSON Summary",
]

REQUIRED_TOP_LEVEL_FIELDS = {
    "witness_id",
    "source_witness",
    "projection_witness",
    "finality_witness",
    "loss_witness",
    "transport_decision",
    "provenance_ledger",
    "rollback_conditions",
    "rank_claim_quarantine",
}

REQUIRED_EFFECT_LAYERS = {"source", "projection", "finality", "loss"}

REQUIRED_DECISIONS = {
    "MISSING_SOURCE_WITNESS",
    "RAW_ONLY_NOT_PHYSICAL_QUOTIENT",
    "MISSING_PROJECTION_FINALITY",
    "MISSING_LOSS_LEDGER",
    "NON_ELLIPTIC_OR_UNPROVED_SYMBOL_COMPLEX",
    "COMPLEX_ONLY_H_STRUCTURE_MISSING",
    "BACKGROUND_UNDERDEFINED",
    "K3_CONTROL_ONLY",
    "TRANSPORT_READY_FOR_SYMBOL_INDEX",
}

REQUIRED_LEDGER_ENTRIES = {
    "source_operator_or_action",
    "module_definitions",
    "right_H_structure",
    "connection",
    "raw_symbol_relation",
    "physical_projection_definition",
    "symbol_exactness_or_ellipticity_certificate",
    "H_linear_trace_or_index_certificate",
    "background_F_ch2_selection",
    "K3_Y14_or_APS_bridge",
    "forbidden_target_input_absence",
}

REQUIRED_LOSSES = {
    "gauge_image_loss",
    "ghost_antighost_subtraction",
    "gamma_trace_constraint_loss",
    "complex_to_H_conversion",
    "source_selected_F_ch2_dependence",
    "APS_eta_h_spectral_flow_terms_if_boundary_used",
}

REQUIRED_ROLLBACK_CONDITIONS = {
    "claims_rank_3_or_generation_count_without_source_derived_physical_RS_index",
    "claims_rank_4_from_target_index_or_normalization",
    "claims_rank_8_without_transport_ready_certificate",
    "identifies_Pi_raw_with_Pi_RS_phys_without_d_RS_minus_1_source_witness",
    "promotes_raw_rank_96C_to_physical_effective_rank",
    "uses_raw_projected_gauge_image_32C_as_loss_without_finality_witness",
    "omits_ghost_antighost_or_gauge_fixing_terms_while_claiming_BRST_finality",
    "converts_complex_rank_to_H_rank_without_H_linear_trace_certificate",
    "assumes_F_ch2_background_without_source_selection",
    "uses_K3_control_without_same_operator_Y14_bridge_or_APS_corrections",
    "uses_forbidden_target_values_as_builder_inputs",
}

FORBIDDEN_POSITIVE_PATTERNS = [
    r"\bthree generations\s+(is|are|were|have been|has been)\s+derived\b",
    r"\bfour generations\s+(is|are|were|have been|has been)\s+derived\b",
    r"\brank\s*3\s+(is|has been)\s+(promoted|justified|proved|derived|closed)\b",
    r"\brank\s*4\s+(is|has been)\s+(promoted|justified|proved|derived|closed)\b",
    r"\brank\s*8\s+(is|has been)\s+(promoted|justified|proved|derived|closed)\b",
    r"\braw\s*96_C\s+(is|has been)\s+(the\s+)?(physical|effective)\s+rank\b",
    r"\bPi_raw\s*=\s*Pi_RS\^phys\b",
]


def artifact_text() -> str:
    return ARTIFACT.read_text(encoding="utf-8")


def extract_summary(text: str) -> dict[str, object]:
    for block in re.findall(r"```json\s*(.*?)\s*```", text, re.DOTALL):
        data = json.loads(block)
        if data.get("artifact") == "EFFECT_TYPED_WITNESS_TRANSPORT_RS_QUOTIENT_BUILDER":
            return data
    raise AssertionError("RS quotient transport builder JSON summary not found")


class HourlyCycle2RSQuotientTransportBuilderAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = artifact_text()
        cls.summary = extract_summary(cls.text)

    def test_required_deliverable_headings_are_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_builder_is_specified_but_not_transport_ready(self) -> None:
        self.assertTrue(self.summary["builder_contract_specified"])
        self.assertFalse(self.summary["builder_instance_transport_ready"])
        self.assertEqual(
            self.summary["current_transport_decision"],
            "MISSING_SOURCE_WITNESS",
        )
        self.assertIn(
            "D_RS_MINUS_1",
            self.summary["verdict"],
        )

    def test_first_obstruction_is_source_d_rs_minus_1(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["id"], "d_RS,-1")
        self.assertEqual(obstruction["required_type"], "SourceWitness")
        self.assertEqual(
            obstruction["required_map"],
            "Ghost_RS,H^src -> Field_RS,H^src",
        )
        self.assertEqual(
            obstruction["status"],
            "MISSING_SOURCE_DEFINED_H_LINEAR_GAUGE_BRST_DIFFERENTIAL",
        )
        self.assertFalse(obstruction["raw_principal_sample_sufficient"])
        self.assertIn("Projection", obstruction["why_first"])

    def test_source_context_preserves_raw_only_status(self) -> None:
        context = self.summary["source_derived_context"]
        self.assertTrue(context["raw_gamma_trace_projector_available"])
        self.assertEqual(context["raw_rank_C_Pi_raw_E_plus_Pi_raw"], 96)
        self.assertEqual(context["raw_projected_gauge_image_rank_C"], 32)
        self.assertFalse(context["pi_rs_phys_defined"])
        self.assertFalse(context["physical_quotient_brst_defined"])
        self.assertFalse(context["d_RS_minus_1_defined"])
        self.assertFalse(context["H_linear_trace_defined"])
        self.assertFalse(context["source_selected_F_ch2_defined"])
        self.assertFalse(context["same_operator_K3_Y14_or_APS_bridge_defined"])

    def test_builder_contract_has_required_fields_layers_and_decisions(self) -> None:
        contract = self.summary["builder_contract"]
        self.assertEqual(set(contract["required_top_level_fields"]), REQUIRED_TOP_LEVEL_FIELDS)
        self.assertEqual(set(contract["effect_layers"]), REQUIRED_EFFECT_LAYERS)
        self.assertEqual(set(contract["allowed_decisions"]), REQUIRED_DECISIONS)
        self.assertEqual(
            contract["decision_order"],
            [
                "target_quarantine",
                "source_witness",
                "projection_witness",
                "finality_witness",
                "loss_witness",
                "transport_ready",
            ],
        )

    def test_witness_contracts_cover_source_projection_finality_loss(self) -> None:
        witnesses = self.summary["witness_contracts"]
        self.assertEqual(set(witnesses), {
            "source_witness",
            "projection_witness",
            "finality_witness",
            "loss_witness",
        })
        source = witnesses["source_witness"]
        self.assertEqual(source["object_id"], "d_RS,-1")
        self.assertEqual(source["domain"], "Ghost_RS,H^src")
        self.assertEqual(source["codomain"], "Field_RS,H^src")
        self.assertTrue(source["must_be_right_H_linear"])
        self.assertTrue(source["must_be_connection_compatible"])
        self.assertTrue(source["must_be_source_derived"])
        self.assertTrue(source["must_absent_target_inputs"])
        self.assertEqual(source["current_status"], "MISSING")

        projection = witnesses["projection_witness"]
        self.assertFalse(projection["may_identify_Pi_raw_with_Pi_RS_phys_without_source_witness"])
        self.assertEqual(projection["current_status"], "BLOCKED_BY_SOURCE_WITNESS")

        finality = witnesses["finality_witness"]
        self.assertTrue(finality["requires_BRST_complex_or_gauge_fixed_block"])
        self.assertTrue(finality["requires_symbol_exactness_or_ellipticity"])
        self.assertTrue(finality["requires_H_linear_trace_or_index"])
        self.assertTrue(finality["requires_background_and_bridge_status"])
        self.assertEqual(finality["current_status"], "BLOCKED_BY_SOURCE_WITNESS")

        loss = witnesses["loss_witness"]
        self.assertEqual(set(loss["tracked_losses_required"]), REQUIRED_LOSSES)
        self.assertEqual(loss["current_status"], "BLOCKED_BY_SOURCE_WITNESS")

    def test_provenance_ledger_and_rollback_conditions_are_complete(self) -> None:
        ledger = self.summary["provenance_ledger"]
        self.assertTrue(ledger["required"])
        self.assertEqual(set(ledger["entries_required"]), REQUIRED_LEDGER_ENTRIES)
        self.assertEqual(
            ledger["current_status"],
            "INCOMPLETE_MISSING_SOURCE_OPERATOR_AND_D_RS_MINUS_1",
        )
        self.assertEqual(set(self.summary["rollback_conditions"]), REQUIRED_ROLLBACK_CONDITIONS)

    def test_rank_quarantine_blocks_targets_and_generations(self) -> None:
        quarantine = self.summary["rank_claim_quarantine"]
        self.assertEqual(quarantine["status"], "ACTIVE")
        for forbidden in [
            "ind_H(D_RS)=8",
            "rank_H(E_RS^eff)=4",
            "total_ind_H(D_GU)=24",
            "three_generations",
            "four_generations",
            "normalization_chosen_after_target_comparison",
            "physical_DOF_count_as_analytic_index",
        ]:
            self.assertIn(forbidden, quarantine["forbidden_construction_inputs"])
        self.assertFalse(quarantine["rank_3_claim_allowed_now"])
        self.assertFalse(quarantine["rank_4_claim_allowed_now"])
        self.assertFalse(quarantine["rank_8_claim_allowed_now"])
        self.assertFalse(quarantine["three_generations_derived"])
        self.assertFalse(quarantine["four_generations_derived"])
        self.assertEqual(quarantine["raw_96C_status"], "RAW_ONLY_CONTEXT")
        self.assertEqual(quarantine["raw_32C_status"], "RAW_ONLY_CONTEXT")
        for pattern in FORBIDDEN_POSITIVE_PATTERNS:
            self.assertIsNone(re.search(pattern, self.text, re.IGNORECASE))

    def test_positive_construction_is_contract_only_and_names_next_object(self) -> None:
        positive = self.summary["strongest_positive_construction"]
        self.assertEqual(positive["status"], "CONTRACT_ONLY")
        self.assertIn(
            "source_witness_for_d_RS_minus_1_supplied",
            positive["would_be_ready_if"],
        )
        self.assertEqual(
            positive["current_block"],
            "source_witness_for_d_RS_minus_1_supplied",
        )
        self.assertEqual(
            self.summary["constructive_next_object"],
            "D_RS_MINUS_1_SOURCE_CERTIFICATE",
        )
        self.assertEqual(
            self.summary["handoff_gate"],
            "RS_SYMBOL_INDEX_CONTRACT_ONLY_AFTER_TRANSPORT_READY_FOR_SYMBOL_INDEX",
        )


def main() -> int:
    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(
            HourlyCycle2RSQuotientTransportBuilderAuditTests
        )
    )
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
