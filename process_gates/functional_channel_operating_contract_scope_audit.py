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
assert "conditional-physics-ledger-v0.38.json" in lanes
assert contract["standing_ledger"]["ref"].endswith("conditional-physics-ledger-v0.38.json")
assert contract["standing_ledger"]["human_ref"].endswith("conditional-physics-ledger-v0.38.md")
assert contract["standing_ledger"]["action_owner_directive"].startswith("CURVATURE_SQUARED_IS_NOT_AN_OWNER")
assert contract["standing_ledger"]["first_order_boundary_directive"].startswith("SELECTED_PRIMITIVE_EPSILON")
assert "HODGE_PHI_CLIFFORD_PAIRING_FRAME_NATURAL" in contract["standing_ledger"]["moving_gimmel_frame_directive"]
assert "LOCAL_PRINCIPAL_GAUGE_ROTATED_LEVI_CIVITA_SOLDERING" in contract["standing_ledger"]["moving_gimmel_frame_directive"]
assert "SECOND_SPIN_LEVI_CIVITA_JET" in contract["standing_ledger"]["moving_gimmel_frame_directive"]
assert "ACTION_SPIN_LC_RANK9_KERNEL_KK" in contract["standing_ledger"]["moving_gimmel_frame_directive"]
assert "TAUTOLOGICAL_PHI1_FULL_SLOT_RESPONSE_ZERO" in contract["standing_ledger"]["moving_gimmel_frame_directive"]
assert "SOURCE_VARIABLES_G_VARPI_T_EQUALS_VARPI_MINUS_BLC" in contract["standing_ledger"]["moving_gimmel_frame_directive"]
assert "ZERO_JET_SOURCE_HESSIAN_RANK24_NULLITY10_GAUGE4_NONGAUGE6" in contract["standing_ledger"]["moving_gimmel_frame_directive"]
assert "SELECTED_GRAPH_CURVATURE_GAIN_MINUS1_OVER26" in contract["standing_ledger"]["moving_gimmel_frame_directive"]
assert "NONNULL_KERNEL_GAUGE4" in contract["standing_ledger"]["moving_gimmel_frame_directive"]
assert "NULL_KERNEL_GAUGE4_PHYSICAL2" in contract["standing_ledger"]["moving_gimmel_frame_directive"]
assert "SAME_GRADE_CL2_DBT_EULER_ZERO_ON_HORIZONTAL24_AND_FULL1274" in contract["standing_ledger"]["moving_gimmel_frame_directive"]
assert "ADJACENT_GRADE_CL1_HCL2_EULER_RANKS_12_12_11" in contract["standing_ledger"]["moving_gimmel_frame_directive"]
assert "CURRENT_34_VARIABLE_TRUNCATION_NOT_ACTION_INVARIANT" in contract["standing_ledger"]["moving_gimmel_frame_directive"]
assert "GRADE1_HESSIAN_RANK196_INERTIA97_99" in contract["standing_ledger"]["moving_gimmel_frame_directive"]
assert "FULL_CURVATURE_PLUS_DBT_SOURCE_CROSS_RANKS13_15_15" in contract["standing_ledger"]["moving_gimmel_frame_directive"]
assert "SCHUR_RANKS13_15_14" in contract["standing_ledger"]["moving_gimmel_frame_directive"]
assert "N2_KERNEL_GAUGE4_PLUS_HELICITY1_DOUBLE_NOT_HELICITY2" in contract["standing_ledger"]["moving_gimmel_frame_directive"]
assert "N2_LOCAL_PRINCIPAL_GREEN_FLUX_RANK2_DEFINITE_GAUGE_DESCENDING" in contract["standing_ledger"]["moving_gimmel_frame_directive"]
assert "I2B_GAUSS_PROJECTED_RANK100_INERTIA54_46" in contract["standing_ledger"]["moving_gimmel_frame_directive"]
assert "ORTHOGONAL_CL2_LEAKAGE2_OVER39" in contract["standing_ledger"]["moving_gimmel_frame_directive"]
assert "FULL_1274_BY_100_RESIDUAL_TARGET_PRIMARY" in contract["standing_ledger"]["moving_gimmel_frame_directive"]

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
assert "Next-Run execution method, ratified by Joe on 2026-08-06" in human
assert "Randomized\n   witnesses may locate blocks but never certify a null" in human
assert "Only exact helicity two opens" in human
assert "NEXT-RUN METHOD" in context_pack
assert "representation theory, variational PDE, symplectic" in context_pack

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
assert directive["status"] == "N2_HELICITY1_NOT_SPIN2__I2B_GAUSS_PROJECTED_COMPONENT_EXACT__FULL_RESIDUAL_LEAKAGE_LIVE__FULL_RESIDUAL_TARGET_PRIMARY__COMMON_DOMAIN_ODD_BV_BFV_OPEN__Q1_OPEN__GLOBAL_PROJECTOR_CONDITIONAL__SUPER_IG_GLOBAL_DESCENT_OPEN"
assert directive["source_return"] == "SOURCE-SILENT"
assert directive["release_condition_met"] is True
assert directive["successor_rows"] == ["LT-GR2a", "LT-GR2b", "LT-GR2c", "LT-GR2d", "LT-GR2e"]
next_method = directive["next_run_method"]
assert next_method["target"] == "COMPLETE_1274_BY_100_RESIDUAL_PULLBACK_WITH_OTHER_CLIFFORD_GRADES_AND_COMOVING_EPSILON_FRAME_OBSERVATION"
assert next_method["ordered_steps"] == [
    "DECOMPOSE_TARGET_BY_CLIFFORD_GRADE_AND_OBSERVER_STABILIZER_TYPE",
    "PROVE_TYPE_FORCED_ZERO_BLOCKS_WITHOUT_REUSING_THE_KILLED_FULL_SPIN_SCALAR_SHORTCUT",
    "ASSEMBLE_SPARSE_EXACT_NONZERO_BLOCKS_WITH_COMOVING_EPSILON_FRAME_AND_OBSERVATION_INCLUDED_FROM_START",
    "CERTIFY_COMPLETENESS_AND_CLASSIFY_THE_2_OVER_39_LEAKAGE_AS_CANCELLED_GAUGE_OR_SURVIVING_INVARIANT",
    "COMPARE_THE_COMPLETE_QUADRATIC_INVARIANT_SPAN_WITH_OBSERVER_FULL_II",
    "ONLY_IF_CARRIER_TYPE_SURVIVES_DERIVE_EULER_PREBOUNDARY_AND_NULL_LITTLE_GROUP_HELICITY",
    "ONLY_IF_HELICITY_TWO_SURVIVES_OPEN_COMMON_KREIN_DOMAIN_AND_ODD_BV_BFV",
]
assert next_method["exact_computation_policy"].startswith("REPRESENTATION_BLOCKED_SPARSE_EXACT_FIRST")
assert next_method["mandatory_reviews"] == [
    "DIFFERENTIAL_GEOMETRY", "REPRESENTATION_THEORY", "VARIATIONAL_PDE",
    "SYMPLECTIC_GEOMETRY", "KREIN_OPERATOR_THEORY", "SOURCE_CRITICISM",
]
assert "NO_GLOBAL_DOMAIN_CAMPAIGN_BEFORE_EXACT_HELICITY_TWO" in next_method["stop_conditions"]
assert "SOURCE_REINSPECT_MOVING_LEVI_CIVITA_AUGMENTED_TORSION_EPSILON_AND_OBSERVATION_GUIDANCE" in next_method["parallel_source_compose"]
assert len(set(directive["required_layer0_objects"])) == 7
assert "LITERAL_CONSTANT_LAMBDA_G" in directive["required_layer0_objects"]
assert "VARIABLE_OLIVE_VARPI_AUGMENTED_TORSION_VEV" in directive["required_layer0_objects"]
assert directive["forbidden_collapse"] == "EINSTEIN_RECOVERY_DOES_NOT_IMPLY_DYNAMIC_COSMOLOGICAL_SECTOR_RECOVERY"
assert "BUILD_FULL_1274_BY_100_RESIDUAL_TARGET" in directive["next_gate"]
assert "FULL_I2B_QUADRATIC_CUBIC_EULER_PREBOUNDARY_HELICITY" in directive["next_gate"]
assert "COMMON_RIGHT_H_KREIN_DOMAIN" in directive["next_gate"]
assert "ODD_BV_BFV" in directive["next_gate"]
assert "ONLY_IF_HELICITY2_SURVIVES" in directive["next_gate"]
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
assert "N2_HELICITY1_NOT_SPIN2" in directive["current_evidence_boundary"]
assert "N2_LOCAL_GREEN_FLUX_LIVE" in directive["current_evidence_boundary"]
assert "I2B_GAUSS_PROJECTED_COMPONENT_EXACT" in directive["current_evidence_boundary"]
assert "FULL_RESIDUAL_LEAKAGE_LIVE" in directive["current_evidence_boundary"]
assert "FULL_1274_BY_100_RESIDUAL_TARGET_PRIMARY" in directive["current_evidence_boundary"]
assert "LOCAL_TT_GIMMEL_DENSITY_D1_ZERO" in directive["latest_build_evidence"]
assert "HODGE_PHI_CLIFFORD_PAIRING_FRAME_NATURAL" in directive["latest_build_evidence"]
assert "ACTION_SPIN_LC_RANK9_KERNEL_KK" in directive["latest_build_evidence"]
assert "COMPLETE_FIRST_JET_OBSERVATION_NO_LEAKAGE" in directive["latest_build_evidence"]
assert "SECOND_SPIN_LEVI_CIVITA_JET_EXACT_NONZERO" in directive["latest_build_evidence"]
assert "OBSERVATION_PURE_SECTION_D2_ZERO_SECTION_FIELD_CROSS_D2_NONZERO" in directive["latest_build_evidence"]
assert "NONLINEAR_FORMAL_ADJOINT_EULER_PREBOUNDARY_OWNER_EXACT" in directive["latest_build_evidence"]
assert "STATIONARY_SELECTED_METRIC_HESSIAN_CAUSAL_RANKS_9_9_6" in directive["latest_build_evidence"]
assert "DIFFEO_CROSS_RANK3" in directive["latest_build_evidence"]
assert "METRIC_ONLY_WARD_AND_DIAGNOSTIC_COUPLED_RETYPE_SCOPED" in directive["latest_build_evidence"]
assert "TAUTOLOGICAL_PHI1_FULL_SLOT_RESPONSE_ZERO" in directive["latest_build_evidence"]
assert "SOURCE_VARIABLES_G_VARPI_T_EQUALS_VARPI_MINUS_BLC" in directive["latest_build_evidence"]
assert "ZERO_JET_SOURCE_HESSIAN_RANK24_NULLITY10_GAUGE4_NONGAUGE6" in directive["latest_build_evidence"]
assert "BOTH_WARD_BLOCKS_EXACT" in directive["latest_build_evidence"]
assert "SELECTED_GRAPH_CURVATURE_GAIN_MINUS1_OVER26" in directive["latest_build_evidence"]
assert "NONNULL_TOTAL_RANK30_KERNEL_GAUGE4" in directive["latest_build_evidence"]
assert "NULL_TOTAL_RANK28_KERNEL_GAUGE4_PHYSICAL2" in directive["latest_build_evidence"]
assert "SAME_GRADE_CL2_DBT_EULER_ZERO_ON_HORIZONTAL24_AND_FULL1274" in directive["latest_build_evidence"]
assert "ADJACENT_GRADE_CL1_HCL2_EULER_RANKS_12_12_11" in directive["latest_build_evidence"]
assert "PARITY_COMPLETED_OFFDIAGONAL_RANKS_24_24_22" in directive["latest_build_evidence"]
assert "CURRENT_34_VARIABLE_TRUNCATION_NOT_ACTION_INVARIANT" in directive["latest_build_evidence"]
assert "N2_KERNEL_GAUGE4_PLUS_HELICITY1_DOUBLE" in directive["latest_build_evidence"]
assert "GRADE1_HESSIAN_RANK196_INERTIA97_99" in directive["latest_build_evidence"]
assert "FULL_CURVATURE_PLUS_DBT_SOURCE_CROSS_RANKS13_15_15" in directive["latest_build_evidence"]
assert "SCHUR_RANKS13_15_14" in directive["latest_build_evidence"]
assert "UNIQUE_POSITIVE_N2_TWO_EXTRA_MODE_LOCUS_APPROX3_175378" in directive["latest_build_evidence"]
assert "N2_ROTATION_POLYNOMIAL_X2_PLUS1_NOT_X2_PLUS4" in directive["latest_build_evidence"]
assert "N2_LOCAL_PRINCIPAL_GREEN_FLUX_RANK2_DEFINITE_GAUGE_DESCENDING" in directive["latest_build_evidence"]
assert "N2_SPIN2_ROUTE_KILLED" in directive["latest_build_evidence"]
assert "I2B_GAUSS_INSERTION_ISOMETRY_RANK100" in directive["latest_build_evidence"]
assert "GAUSS_PROJECTED_INERTIA54_46" in directive["latest_build_evidence"]
assert "ORTHOGONAL_CL2_LEAKAGE2_OVER39" in directive["latest_build_evidence"]
assert "I2B_GAUSS_WRONG_TYPE" in directive["latest_build_evidence"]
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

print("PASS: functional channels and v0.38 ledger preserve predecessor theorems, retain the N2 helicity-one kill, type the projected Gauss block and its live Cl2 leakage, and route the full residual target without residue or quotient promotion")
