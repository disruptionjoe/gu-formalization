#!/usr/bin/env python3
"""Fail-closed wiring and scope audit for the GU functional-channel reset."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def strict(path):
    def pairs(items):
        keys = [key for key, _ in items]
        if len(keys) != len(set(keys)):
            raise ValueError(f"duplicate key in {path}")
        return dict(items)
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=pairs)


contract_path = ROOT / "lab/process/functional-channel-operating-contract-v1.0.json"
contract = strict(contract_path)
human = (ROOT / "lab/process/functional-channel-operating-contract-v1.0.md").read_text(encoding="utf-8")
agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
lanes = (ROOT / "LANES.yaml").read_text(encoding="utf-8")
operating = (ROOT / "lab/process/OPERATING-MODEL.md").read_text(encoding="utf-8")
context_pack = (ROOT / "lab/process/agent-context-pack.md").read_text(encoding="utf-8")
synthesis = (ROOT / "explorations/precontract-waves-0abc-synthesis-2026-08-05.md").read_text(encoding="utf-8")

assert contract["status"] == "RATIFIED"
assert contract["purpose_lanes_preserved"] == ["1", "2", "3", "A"]
assert contract["functional_channels_are_not_lanes"] is True
assert set(contract["channels"]) == {"BUILD", "COMPOSE", "SOURCE", "VERIFY"}
assert contract["dispatch"]["fixed_percentages"] is False
assert contract["durability_level"] == "OWNER_LOCAL_MANDATORY_CONTEXT_PLUS_MACHINE_TESTED_CONTRACT"
assert contract["fleet_runner_interpretation_change"] == "NOT_CHANGED_IN_THIS_RUN"
assert contract["standing_ledger"]["owner"] == "COMPOSE_CHANNEL_WITH_LANE_A_RECONCILIATION"
assert contract["channels"]["COMPOSE"]["cadence"]["after_material_build_outputs"] == 3
assert contract["channels"]["SOURCE"]["return_codes"] == [
    "SOURCE-CONFIRMS", "SOURCE-CORRECTS", "SOURCE-SILENT"
]
assert contract["over_determined"]["finder_may_adjudicate"] is False
assert contract["over_determined"]["independent_owner_required"] is True
assert contract["channels"]["VERIFY"]["unchanged_replay_is_progress"] is False
assert contract["channels"]["VERIFY"]["hostile_charges"] == [
    "SUMMARY_OUTRUNS_ARTIFACT", "DEFENDS_SUPERSEDED_OR_MISTYPED_OBJECT"
]
symplectic = contract["channels"]["VERIFY"]["conditional_specialist_lenses"]["SYMPLECTIC_GEOMETRY"]
assert "PHYSICAL_TRANSITION" in symplectic["trigger"]
assert symplectic["forbidden_promotion"] == "UNREDUCED_DENSITY_IS_NOT_A_PHYSICAL_TRANSITION"

for ref in [
    "lab/process/functional-channel-operating-contract-v1.0.md",
    "lab/process/functional-channel-operating-contract-v1.0.json",
]:
    assert ref in lanes
assert 'manifest_revision: 4' in lanes
assert 'contract_version: "2.0"' in lanes
assert 'id: functional-channel-contract-v1' in lanes
assert "functional-channel-operating-contract-v1.0.md" in agents
assert "GU-COSMO-DYNAMIC-01" in agents
assert "functional-channel-operating-contract-v1.0.md" in operating
assert "functional-channel-operating-contract-v1.0.md" in context_pack
assert "GU-COSMO-DYNAMIC-01" in context_pack
assert "conditional-physics-ledger-v0.28.json" in lanes
assert contract["standing_ledger"]["ref"].endswith("conditional-physics-ledger-v0.28.json")
assert contract["standing_ledger"]["human_ref"].endswith("conditional-physics-ledger-v0.28.md")
assert contract["standing_ledger"]["action_owner_directive"].startswith("CURVATURE_SQUARED_IS_NOT_AN_OWNER")
assert contract["standing_ledger"]["first_order_boundary_directive"].startswith("SELECTED_PRIMITIVE_EPSILON")
assert "HODGE_PHI_CLIFFORD_PAIRING_FRAME_NATURAL" in contract["standing_ledger"]["moving_gimmel_frame_directive"]
assert "LOCAL_PRINCIPAL_GAUGE_ROTATED_LEVI_CIVITA_SOLDERING" in contract["standing_ledger"]["moving_gimmel_frame_directive"]
assert "CONSTRUCT_SECOND_OBSERVATION_SOLDERING_JETS" in contract["standing_ledger"]["moving_gimmel_frame_directive"]

assert "The finder of an over-determined row escalates it and may not adjudicate it" in human
assert "found over-determined row is valuable" in human
assert "forced fitting is forbidden" in human
assert "There are no fixed channel percentages" in human
assert "unchanged packet" in human
assert "summary outruns the artifact" in human
assert "superseded or mistyped" in human
assert "include a symplectic-geometry lens" in human
assert "An unreduced density is not a physical transition" in human
assert "ledger_row_changes: none" in human
assert "Thin automation triggers" in human

donor = contract["cross_theory_mechanism_donor_policy"]
assert donor["standing_role"] == "BOUNDED_COMPOSE_CHECKPOINT__NOT_A_LANE"
assert donor["selection_cap"] == 2
assert donor["selected_ports"] == ["NCG-CONTROL", "STRING-LINF"]
assert donor["wrong_type_is_not_gap"] is True
assert donor["frg_admission"] == "STABLE_ACTION_NUMERATOR_FIELD_CONTENT_AND_COMMON_DOMAIN_REQUIRED"
assert "Cross-theory mechanism donors" in human
assert "wrong-type object is not relabelled" in human
assert "A free level or period choice is a new datum" in human

directive = contract["active_scientific_directives"][0]
assert directive["id"] == "GU-COSMO-DYNAMIC-01"
assert directive["owner"] == "SOURCE_PLUS_COMPOSE__INDEPENDENT_FROM_NEXT_BUILD_FINDER"
assert directive["primary_row_on_hold"] is None
assert directive["status"] == "INTRINSIC_HOMOGENEOUS_WARD_EXACT__MOVING_SHIAB_LOAD_BEARING__FULL_DIRECT_MOVING_PREBOUNDARY_CLASS_OPEN__Q1_OPEN__GLOBAL_PROJECTOR_CONDITIONAL__SUPER_IG_GLOBAL_DESCENT_OPEN"
assert directive["source_return"] == "SOURCE-SILENT"
assert directive["release_condition_met"] is True
assert directive["successor_rows"] == ["LT-GR2a", "LT-GR2b", "LT-GR2c", "LT-GR2d", "LT-GR2e"]
assert len(set(directive["required_layer0_objects"])) == 7
assert "LITERAL_CONSTANT_LAMBDA_G" in directive["required_layer0_objects"]
assert "VARIABLE_OLIVE_VARPI_AUGMENTED_TORSION_VEV" in directive["required_layer0_objects"]
assert directive["forbidden_collapse"] == "EINSTEIN_RECOVERY_DOES_NOT_IMPLY_DYNAMIC_COSMOLOGICAL_SECTOR_RECOVERY"
assert "SECOND_OBSERVATION_AND_SOLDERING_JETS" in directive["next_gate"]
assert "FULL_NONLINEAR_EULER_PRESYMPLECTIC_CLASS" in directive["next_gate"]
assert "SECOND_LAYER_OWNER_MAP_REMAINS_SEPARATE" in directive["next_gate"]
assert "FINITE_TREE_SPECTRAL_KREIN_MAJORANT_POSITIVE" in directive["current_evidence_boundary"]
assert "NO_MULTIPLICATIVE_SCALAR_SIGN_EXTENDS_FREE_P" in directive["current_evidence_boundary"]
assert "FIXED_CONSTANT_SCALAR_BACKGROUND_SELECTED_ACTION_TT_HESSIAN_HAS_UNIQUE_POSITIVE_SPECTRAL_C" in directive["current_evidence_boundary"]
assert "FIRST_C_CORRECTION_FOUR_COEFFICIENTS_CONSTRAINT_RANK_FOUR_ZERO_FREEDOM" in directive["current_evidence_boundary"]
assert "BACKGROUND_NOT_PROVED_STATIONARY" in directive["current_evidence_boundary"]
assert "FULL_THREE_FIELD_CUBIC_HESSIAN_ZERO_AT_ZERO_FIELD" in directive["current_evidence_boundary"]
assert "REAL_ODD_CONTINUUM_ENERGY_DENOMINATOR_SHELLS_EXACT" in directive["current_evidence_boundary"]
assert "Q0Q0_COMPACT_CORE_BULK_NUMERATOR_ZERO_ON_FREE_SHELL" in directive["current_evidence_boundary"]
assert "Q0QM_HH_ONLY_NUMERATOR_NONZERO" in directive["current_evidence_boundary"]
assert "FULL_PENCIL_FIELD_REDEFINITION_COMPLETION_ZERO_ON_ALL_FREE_SHELLS" in directive["current_evidence_boundary"]
assert "INTRINSIC_AUGMENTED_TORSION_D3_TRACE_136_OVER_3_TRACELESS_MINUS_56_OVER_3" in directive["current_evidence_boundary"]
assert "INTRINSIC_THETA_RAD_Q0QM_ZERO" in directive["current_evidence_boundary"]
assert "INTRINSIC_THETA_RAD_QMQM_NONZERO" in directive["current_evidence_boundary"]
assert "STATIONARY_BULK_PULLBACK_USES_FIRST_SECOND_LIFT_JETS" in directive["current_evidence_boundary"]
assert "TWO_CONNECTION_DIFFERENCE_RANK24_KERNEL_DIAGONAL24" in directive["current_evidence_boundary"]
assert "PRINCIPAL_DIAGONAL_GAUGE_RANK0" in directive["current_evidence_boundary"]
assert "LOWER_ORDER_HOMOGENEOUS_WARD_BV_PREBOUNDARY_OPEN" in directive["current_evidence_boundary"]
assert "INTRINSIC_HOMOGENEOUS_WARD_ZERO_91_OF_91" in directive["current_evidence_boundary"]
assert "MOVING_SHIAB_LOAD_BEARING" in directive["current_evidence_boundary"]
assert "FROZEN_SHIAB_DEFECTS4" in directive["current_evidence_boundary"]
assert "NO_Q1_POLE_OR_PHYSICAL_SHEET_RESULT_BOOKED" in directive["current_evidence_boundary"]
assert "LOCAL_TT_GIMMEL_DENSITY_D1_ZERO" in directive["latest_build_evidence"]
assert "HODGE_PHI_CLIFFORD_PAIRING_FRAME_NATURAL" in directive["latest_build_evidence"]
assert "LC_SOLDERING_RANK10" in directive["latest_build_evidence"]
assert "COMPLETE_FIRST_JET_OBSERVATION_NO_LEAKAGE" in directive["latest_build_evidence"]
assert "FORMAL_ADJOINT_METRIC_EULER_NONZERO" in directive["latest_build_evidence"]
assert "MOVING_SECTION_TERM_NONZERO" in directive["latest_build_evidence"]
assert "UNRESTRICTED_PREBOUNDARY_NONZERO" in directive["latest_build_evidence"]
assert "FULL_NONLINEAR_SECOND_JET_OPEN" in directive["latest_build_evidence"]
assert "NO_FIFTH_QUOTIENT" in directive["latest_build_evidence"]
assert "FULL_NONLINEAR_ACTION_FOCK_COMMON_DOMAIN_LOOP_UV_C_OPEN" in directive["current_evidence_boundary"]
assert "ALL_FINITE_LOCAL_CONSTANT_MODE_COMPLETIONS_NOSCREEN_OR_ARE_UNSOLVABLE" in directive["current_evidence_boundary"]
assert "NORMALIZED_GLOBAL_PROJECTOR_SCREENS_CONSTANT_SHIFTS_EXACTLY" in directive["current_evidence_boundary"]
assert "NOT_DERIVED_OR_IDENTIFIED_WITH_P2" in directive["current_evidence_boundary"]
assert "NOT_DEFAULT_ODD_ACTION" in directive["current_evidence_boundary"]
assert "one pole\ntotal" in human
assert "z*(alpha_II*kappa_1-z)" in human
assert "t=-kappa_1/312" in human
assert "rank 100" in human
assert "100*kappa_1/117" in human
assert "124*kappa_1/117" in human
assert "opposite the Einstein pole" in human
assert "T_reduced=E_g^direct+(D_g A)^!J_A" in human
assert "rank ten on\ntimelike, spacelike and null" in human
assert "P=I+2L/m^2" in human
assert "No scalar sign" in human
assert "K(0)=0" in human
assert "normalized global projector" in human
assert "not identified with P2" in human
assert "declines an odd action" in human
assert "SOURCE-SILENT" in human
assert "four first-order matrix entries" in human
assert "Generic Jordan walls" in human
assert "compact-core\n`theta-q0-q0` bulk numerator is exactly zero" in human
assert "mixed\n`theta-q0-qm` numerator is not selected" in human
assert "Only its unique nonzero reduced class may advance to Q1" in human
assert "remains circular" in human
assert "the Einstein equation was recovered” is not a completion result" in human
assert "historical Einstein" in human

assert "Subsequent ratification" in synthesis
assert "not ratified **in this\nRun**" in synthesis
assert set(contract["non_effects"]) >= {
    "NO_SCHEDULER_CHANGE", "NO_TRIGGER_CHANGE", "NO_ACTIVATION_GRANT_CHANGE",
    "NO_LANE_COUNT_CHANGE", "NO_CANON_CHANGE",
    "NO_EXTERNAL_P1_P2_P3_CHANGE", "NO_PUBLIC_POSTURE_CHANGE"
}

print("PASS: functional channels and v0.28 ledger preserve local principal physical-response closure without nonlinear stationarity, BV/BFV or physics promotion")
