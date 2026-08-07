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
current_ledger_ref = contract["standing_ledger"]["ref"]
current_human_ref = contract["standing_ledger"]["human_ref"]
assert current_ledger_ref in lanes
assert current_human_ref in lanes
assert tuple(map(int, current_ledger_ref.removesuffix(".json").rsplit("v", 1)[1].split("."))) >= (0, 49)
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
assert "FULL_CL2_TARGET_1274_BY_100_NNZ640" in contract["standing_ledger"]["moving_gimmel_frame_directive"]
assert "MASSLESS_HELICITY2" in contract["standing_ledger"]["moving_gimmel_frame_directive"]
assert "MASSIVE_SO3_SPIN2_DIM5_CASIMIR_MINUS6" in contract["standing_ledger"]["moving_gimmel_frame_directive"]
assert "RESTRICTED_SCALAR_1157_OVER3589_NOT_CHARACTERISTIC" in contract["standing_ledger"]["moving_gimmel_frame_directive"]
assert "V043_COVECTOR_SLOT_PROXY_RANK4_RETRACTED_AS_ACTION_TARGET" in contract["standing_ledger"]["moving_gimmel_frame_directive"]
assert "ACTUAL_INDEPENDENT_CONNECTION_LIFT_RANK3_KERNEL_E0" in contract["standing_ledger"]["moving_gimmel_frame_directive"]
assert "CONNECTION_ONLY_DUPSILON_WELD_IMPOSSIBLE_AT_CURRENT_PRINCIPAL_GRADE" in contract["standing_ledger"]["moving_gimmel_frame_directive"]
assert "SOURCE_NORMAL_JET_AND_TOTAL_METRIC_SECTION_DERIVATIVE_ON_E0_PRIMARY" in contract["standing_ledger"]["moving_gimmel_frame_directive"]
assert "FULL_SELECTED_SHIAB_RANK1274_ISOMORPHISM" in contract["standing_ledger"]["moving_gimmel_frame_directive"]
assert "UNIQUE_SPLIT_PREIMAGES_FAIL_PRINCIPAL_BIANCHI" in contract["standing_ledger"]["moving_gimmel_frame_directive"]
assert "CL2_SOURCE8281_OUTPUT_GRADES1_5_TARGET_GRADE2_ZERO" in contract["standing_ledger"]["moving_gimmel_frame_directive"]
assert "DIRECT_GCR_AND_SINGLE_Q_OWNER_KILLED" in contract["standing_ledger"]["moving_gimmel_frame_directive"]
assert "ODD_SOURCE_OWNER_PRIMARY" in contract["standing_ledger"]["moving_gimmel_frame_directive"]

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
assert "Predecessor execution method, ratified by Joe on 2026-08-06" in human
assert "Current execution method" in human
assert "Randomized witnesses may locate blocks but never certify a null" in human
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
assert directive["status"] == "NONNULL_KOSZUL_ODD_SUPPORT28_PLUS117_EXACT__DIRECT_CL2_GCR_OWNER_KILLED__SINGLE_Q_ADAPTER_KILLED__ODD_SOURCE_OWNER_OPEN__NULL_SCREEN_OPEN__TOTAL_BIANCHI_OPEN__BACKGROUND_SUBTRACTION_UNOWNED__MASSLESS_CONSTRAINT_COMPLEX_OPEN__COUPLED_NONZERO_FERMION_HESSIAN_OPEN__COMMON_DOMAIN_ODD_BV_BFV_OPEN__Q1_OPEN"
assert "SOURCE-CONFIRMS" in directive["source_return"] and "SOURCE-SILENT" in directive["source_return"]
assert directive["release_condition_met"] is True
assert directive["successor_rows"] == ["LT-GR2a", "LT-GR2b", "LT-GR2c", "LT-GR2d", "LT-GR2e"]
next_method = directive["next_run_method"]
assert next_method["target"] == "SOURCE_NATIVE_ODD_CURVATURE_OR_RICHER_SOLDERING_OWNER_AND_NULL_SCREEN"
assert next_method["ordered_steps"] == [
    "PRESERVE_EXACT_MASSLESS_HELICITY2_AND_MASSIVE_SO3_SPIN2_DIM5_SUBBLOCK",
    "DO_NOT_ADD_AN_INDEPENDENT_OBSERVATION_ACTION_FIELD__METRIC_AND_GRAPH_SECTION_SHARE_ONE_TANGENT",
    "DO_NOT_TREAT_A_DIFFERENCE_OF_GRAM_FORMS_AS_THE_GRAM_OF_A_RESIDUAL_DIFFERENCE",
    "PRESERVE_THE_EXACT_ODD_CL1_SUPPORT28_PLUS117_SPLIT_AND_SELECTED_SHIAB_RECONSTRUCTION",
    "DO_NOT_IDENTIFY_ODD_CL1_PACKETS_WITH_CLASSICAL_CL2_GAUSS_CODAZZI_RICCI_CURVATURE",
    "CONSTRUCT_SOURCE_NATIVE_ODD_AUGMENTED_TORSION_OR_TRANSLATION_CURVATURE_OWNER_OR_A_RICHER_MOVING_EPSILON_SOLDERING_MAP",
    "CONSTRUCT_A_NULL_CHARACTERISTIC_SCREEN_OR_GAUGE_QUOTIENT_WITHOUT_NONNULL_NORMALIZATION",
    "ASSEMBLE_J1_LIE_XI_A_GAUGE_ROTATED_LEVI_CIVITA_MOVING_HODGE_SHIAB_GRAPH_AND_OWNED_BACKGROUND_TERMS",
    "TEST_TOTAL_DIFFERENTIAL_BIANCHI_AND_RAW_DUPSILON_NATURALITY_ON_ALL_FOUR_GRAPH_COLUMNS",
    "REQUIRE_AN_EXPLICIT_ACTION_OR_COUNTERTERM_OWNER_BEFORE_ANY_BACKGROUND_SUBTRACTION",
    "ONLY_IF_THAT_PASSES_EXTEND_TO_TRANSVERSE_SOURCE_VARIABLES",
    "DERIVE_THE_OFF_TT_SPIN0_CHARACTERISTIC_POLYNOMIAL_ONLY_ON_THE_DESCENDED_QUOTIENT",
    "ONLY_THEN_ASSEMBLE_AND_DESCEND_THE_MASSLESS_CONSTRAINT_COMPLEX",
    "CLASSIFY_EVERY_REMAINING_MASSLESS_QUOTIENT_CLASS_WITHOUT_RECOUNTING_MASSIVE_SPIN2_PARTNERS",
    "ONLY_AFTER_BOSONIC_QUOTIENT_COUPLE_SEPARATELY_TYPED_NONZERO_FERMION_HESSIAN",
    "ONLY_AFTER_COMPLETE_QUOTIENT_OPEN_COMMON_KREIN_DOMAIN_AND_ODD_BV_BFV",
]
assert next_method["exact_computation_policy"].startswith("REPRESENTATION_BLOCKED_SPARSE_EXACT_FIRST")
assert next_method["mandatory_reviews"] == [
    "DIFFERENTIAL_GEOMETRY", "REPRESENTATION_THEORY", "VARIATIONAL_PDE",
    "SYMPLECTIC_GEOMETRY", "KREIN_OPERATOR_THEORY", "SOURCE_CRITICISM",
]
assert "NO_TT_SUBQUOTIENT_PROMOTION_TO_COMPLETE_PHYSICAL_SPECTRUM" in next_method["stop_conditions"]
assert "NO_REPRESENTATION_FORCED_MASSIVE_SPIN2_CARRIER_PROMOTED_TO_POSITIVE_PHYSICAL_STATES" in next_method["stop_conditions"]
assert "SOURCE_RETURN_CONFIRMS_GAUSS_COMPATIBLE_TWO_CONNECTION_ARENA_AND_IS_SILENT_ON_A_K77_GCR_TO_ODD_CURVATURE_OWNER_MAP__REINSPECT_ONLY_IF_NEW_COLLISION" in next_method["parallel_source_compose"]
assert len(set(directive["required_layer0_objects"])) == 7
assert "LITERAL_CONSTANT_LAMBDA_G" in directive["required_layer0_objects"]
assert "VARIABLE_OLIVE_VARPI_AUGMENTED_TORSION_VEV" in directive["required_layer0_objects"]
assert directive["forbidden_collapse"] == "EINSTEIN_RECOVERY_DOES_NOT_IMPLY_DYNAMIC_COSMOLOGICAL_SECTOR_RECOVERY"
assert "CONSTRUCT_SOURCE_NATIVE_ODD_AUGMENTED_TORSION_OR_TRANSLATION_CURVATURE_PACKET" in directive["next_gate"]
assert "RICHER_MOVING_EPSILON_SOLDERING_OWNER" in directive["next_gate"]
assert "CONSTRUCT_NULL_SCREEN" in directive["next_gate"]
assert "RAW_UPSILON_NATURALITY" in directive["next_gate"]
assert "THEN_TEST_TOTAL_BIANCHI" in directive["next_gate"]
assert "ONLY_AFTER_COMPLETE_QUOTIENT_OPEN_COMMON_KREIN_DOMAIN_AND_ODD_BV_BFV" in next_method["ordered_steps"]
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
assert "FULL_1274_BY_100_RESIDUAL_TARGET_COMPLETE" in directive["current_evidence_boundary"]
assert "FULL_CL2_TARGET_1274_BY_100_RANK100_NNZ640" in directive["current_full_cl2_evidence"]
assert "MASSLESS_HELICITY2" in directive["current_full_cl2_evidence"]
assert "MASSIVE_SO3_SPIN2_DIM5_CASIMIR_MINUS6" in directive["current_full_cl2_evidence"]
assert "SPIN0_POLYNOMIAL_OPEN" in directive["current_full_cl2_evidence"]
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
assert "TT_MASS2_1922_OVER3589" in directive["latest_build_evidence"]
assert "MASSLESS_HELICITY2" in directive["latest_build_evidence"]
assert "MASSIVE_SO3_SPIN2_DIM5_CASIMIR_MINUS6" in directive["latest_build_evidence"]
assert "TT_PREBOUNDARY_NONZERO" in directive["latest_build_evidence"]
assert "BACKGROUND_SUBTRACTED_OFF_TT_SPIN0_AND_MASSLESS_CONSTRAINT_COMPLEX_OPEN" in directive["latest_build_evidence"]
assert "V043_PROXY_WELD_VALID_ONLY_ON_COVECTOR_SLOT_CARRIER" in directive["latest_build_evidence"]
assert "ACTUAL_INDEPENDENT_CONNECTION_LIFT_RANK3_KERNEL_E0" in directive["latest_build_evidence"]
assert "METRIC_WARD_LOAD_NONZERO_ON_E0" in directive["latest_build_evidence"]
assert "CONNECTION_ONLY_WELD_IMPOSSIBLE" in directive["latest_build_evidence"]
assert "INDEPENDENT_OBSERVATION_COLUMN_REJECTED" in directive["latest_build_evidence"]
assert "SOURCE_NORMAL_JET_TOTAL_METRIC_SECTION_DERIVATIVE_OPEN" in directive["latest_build_evidence"]
assert "FULL_SELECTED_SHIAB_RANK1274_ISOMORPHISM" in directive["latest_build_evidence"]
assert "PRINCIPAL_BIANCHI_RANKS14_14_14_14" in directive["latest_build_evidence"]
assert "SPLIT_JET_IDENTIFICATION_REJECTED" in directive["latest_build_evidence"]
assert "CL2_SOURCE8281_OUTPUT_GRADES1_5_TARGET_GRADE2_ZERO" in directive["latest_build_evidence"]
assert "DIRECT_GCR_AND_SINGLE_Q_OWNER_KILLED" in directive["latest_build_evidence"]
assert "ODD_SOURCE_OWNER_PRIMARY" in directive["latest_build_evidence"]
assert "ODD_CL1_SUPPORTS_7_7_7_7_TOTAL28" in directive["latest_nonnull_koszul_evidence"]
assert "ODD_CL1_TRANSVERSE_SUPPORTS_51_22_22_22_TOTAL117" in directive["latest_nonnull_koszul_evidence"]
assert "CL2_SOURCE8281_NONZERO_OUTPUT_GRADES1_5_TARGET_GRADE2_ZERO" in directive["latest_nonnull_koszul_evidence"]
assert "SINGLE_Q_CONTRACTION_RANK13_CANNOT_SUPPLY_Q_COMPONENT" in directive["latest_nonnull_koszul_evidence"]
assert "NULL_AUXILIARY_SCREEN_DEPENDENT" in directive["latest_nonnull_koszul_evidence"]
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

print("PASS: functional channels and v0.49 ledger preserve the exact odd packet, reject the wrong-type GCR and single-q owners, and route odd-source plus null-screen completion without residue or quotient promotion")
