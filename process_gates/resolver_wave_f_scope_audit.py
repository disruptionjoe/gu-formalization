#!/usr/bin/env python3
"""Fail-closed scope audit for Resolver Wave F.

This gate preserves the exterior-projector / generic-source-port /
downstream-weight / total-Euler / KO-basepoint distinctions. It does not
reproduce the mathematical probe or promote a scientific verdict.
"""
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "explorations/cycle-gates-and-audits/resolver-wave-f-source-port-action-ownership-disposition-2026-08-03.json"
REPORT = ROOT / "explorations/resolver-wave-f-source-port-action-ownership-2026-08-03.md"


def main() -> None:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    report = REPORT.read_text(encoding="utf-8")

    assert data["named_gate"] == "RESOLVER-WAVE-F-ACTUAL-SOURCE-SHIAB-FERMION-EULER-WEIGHT-SELECTION"
    assert data["gate_after"] == "OPEN_REBASED_COMPONENT_PROJECTOR_BUILT"
    assert data["route_disposition"] == "REBASE"
    assert data["hostile_review_status"] in {
        "PENDING_REPAIRED_HOSTILE_RERUN",
        "PASS_AFTER_REPAIRS",
    }

    layer0 = data["layer0"]
    assert layer0["source_epsilon_equals_soldering_epsilon_IG"] is False
    assert layer0["theta_Z_equals_n1_distortion_theta"] is False
    assert layer0["grade6_is_connection_value"] is True
    assert layer0["effective_real252_is_connection_value"] is False
    assert layer0["already_grade6_exterior_input_equals_generic_native_adjoint"] is False
    assert layer0["canonical_1_over_9_equals_full20_half_weight"] is False
    assert layer0["projected_Euler_equals_consistent_truncation"] is False
    assert layer0["vectorlike_chi0_equals_canonical_KO_basepoint"] is False

    port = data["exterior_component_projector"]
    assert port["input_type"] == "Cstar_tensor_Lambda6_Cstar"
    assert port["formula"] == "Pext_0=j5*(1/9)*pi_Lambda5V*delta"
    assert port["q6_from_generic_native_adjoint"] == "OPEN_FORMULA_ONLY"
    assert port["delta_j5"] == "9I"
    assert port["observer_coefficients"] == [4, 5]
    assert port["rank"] == 252
    assert port["all_image_blades_checked"] == 252
    assert port["off_image_fixture_checked"] is True
    assert port["idempotent_on_checked_carrier"] is True
    assert port["full_Krein_self_adjointness"] == "NOT_INDEPENDENTLY_CERTIFIED"
    assert port["full_grade6_dimension"] == 3003
    assert port["internal_grade6_dimension"] == 210
    assert port["grade6_K_class"] == "anti"
    assert port["grade6_right_H"] is True
    assert port["complex_126_halves_are_conjugate"] is True
    assert port["raw_positive_Frobenius_allowed"] is False

    moving = data["moving_port"]
    assert moving["actual_source_U_Theta_epsilon"] == "OPEN"
    assert moving["two_leg_transport"] == "PASS_EXTERIOR_SIGNED_PERMUTATION_FIXTURE"
    assert moving["split_stabilizer_lift_invariance"] == "ONE_EXPLICIT_SIGNED_PERMUTATION_PASS"
    assert moving["three_patch_cocycle"] == "CONSTANT_SIGNED_PERMUTATION_COMPOSITION_PASS"
    assert moving["dP_commutator"] == "ONE_INTERNAL_FIVE_PROJECTOR_CHAIN_FIXTURE"
    assert moving["coarse_epsilon_plane_owns_internal_split"] is False
    assert moving["epsilon_src_is_serious_candidate"] is True
    assert moving["epsilon_src_tilted_qsplit_descent"] == "OPEN"
    assert moving["theta_Z_actual_Y14_overlap"] == "OPEN"
    assert moving["public_complex_to_native_Sp_reduction"] == "OPEN"
    assert moving["total_Euler_tangent_to_Sp_fixed_locus"] == "OPEN"
    assert moving["global_source_to_active_port"] == "OPEN"
    assert moving["frozen_projector_control"] == "FAILS_AS_REQUIRED"

    weight = data["downstream_full20_weight"]
    assert weight["distinct_from_exterior_component_projector"] is True
    assert weight["real_exterior_Hom_dimension"] == 4
    assert weight["star_even_subansatz_dimension"] == 2
    assert weight["one_simple_blade_clean_ratio"] == "[2:1]"
    assert weight["one_simple_blade_clean_lambda"] == "1/2"
    assert weight["representation_wide_extension"] == "OPEN"
    assert weight["rectangular_map_source_status"] == "SOURCE_SILENT"
    assert weight["displayed_kappa_contains_weight_field"] is False
    assert weight["zero_selector_ideal_interpretation"] == "FIELD_ABSENT_ACTION_BLIND_NOT_EULER_FLAT"
    assert weight["displayed_kappa_implies_a_minus_2b"] is False
    assert weight["displayed_kappa_selector_verdict"] == "REFUTED_DIRECT_SELECTION_ONLY"
    assert weight["complete_Shiab_fermion_selector_verdict"] == "NOT_EVALUABLE"
    assert weight["ownership_verdict"] == "STAR_EVEN_SUBANSATZ_SOURCE_SILENT_UNSELECTED"

    euler = data["source_euler"]
    assert euler["density_to_primal_global_Riesz"] == "OPEN"
    assert euler["active_projected_equation"] == "OPEN_PENDING_ACTUAL_PORT"
    assert euler["transverse_equation"] == "OPEN"
    assert euler["moving_Shiab_restriction"] == "OPEN"
    assert euler["total_fermion_residual"] == "OPEN"
    assert euler["full_G2_Y_P0"] == "OPEN"
    assert euler["stationary_VEV"] == "OPEN"
    assert euler["mass"] == "OPEN"

    auxiliary = data["auxiliary_rival"]
    assert auxiliary["scope"] == "ISOLATED_ZERO_JET_ONE_BLADE_STAR_EVEN_COMPARATOR"
    assert auxiliary["can_force_representative_clean_ratio"] is True
    assert auxiliary["direct_Euler_variation_checked"] is True
    assert auxiliary["isolated_integration_by_parts_boundary_term"] == "ZERO"
    assert auxiliary["coupled_nonpropagation"] == "OPEN"
    assert auxiliary["source_derived"] is False
    assert auxiliary["required"] is False
    assert auxiliary["verdict"] == "AUXILIARY_CAN_FORCE_REPRESENTATIVE_ONLY"

    basepoint = data["chi0_basepoint_audit"]
    assert basepoint["e_hat_0_is_auxiliary_family_zero"] is True
    assert basepoint["rank_zero_implies_reduced_KO_zero"] is False
    assert basepoint["arbitrary_physical_chi0_is_canonical_basepoint"] is False
    assert basepoint["count_inference"] is False

    assert data["assertion_counts"] == {
        "exact_or_deterministic_native": 29,
        "independent_Sage": 1,
        "source_receipts": 4,
        "type_level": 12,
        "planted": 13,
        "total": 59,
    }
    assert all(data["external_datum"][key] == "unchanged_unused"
               for key in ("P1", "P2", "P3"))
    assert data["next_gate"]["id"] == "RESOLVER-WAVE-G-Q6-NATIVE-SP-TILTED-SOURCE-PORT-AND-TRANSVERSE-EULER"

    for token in (
        "Pext^0 = j5 (1/9)",
        "already been typed as a grade-six exterior symbol",
        "tensorial difference of two affine connections; adjoint-valued source one-form before projection",
        "candidate `(P_source)^! E=0` after `q6`, Riesz, and source transport are built",
        "ADJOINT-TO-GRADE-SIX q6: OPEN / FORMULA ONLY",
        "DOWNSTREAM REAL EXTERIOR HOM: DIMENSION 4",
        "AUXILIARY_CAN_FORCE",
        "transverse equation",
        "vectorlike `chi=0`",
        "P1/P2/P3 remain unchanged and unused",
        "RESOLVER-WAVE-G-Q6-NATIVE-SP-TILTED-SOURCE-PORT-AND-TRANSVERSE-EULER",
    ):
        assert token in report, f"report missing scope token {token!r}"

    for forbidden in (
        "the displayed source kappa term selects lambda=1/2",
        "epsilon_src is epsilon_ig",
        "the local signed-permutation fixture is the actual y14 atlas",
        "auxiliary is required",
        "chi=0 forces p3",
        "open -> partial_constructed",
        "| projected Euler equation | `P252^! E=0`",
    ):
        assert forbidden not in report.lower()

    print("resolver_wave_f_scope_audit: PASS")
    print("  grade-six exterior projector, missing q6/source U, four-dimensional real Hom, total Euler, auxiliary, KO basepoint, and datum fences retained")


if __name__ == "__main__":
    main()
