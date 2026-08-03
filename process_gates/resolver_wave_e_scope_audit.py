#!/usr/bin/env python3
"""Fail-closed scope audit for Resolver Wave E.

This gate checks the source/full-20/weight/Euler fences. It does not reproduce
the native matrix calculation or promote any scientific verdict.
"""
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "explorations/cycle-gates-and-audits/resolver-wave-e-source-owned-moving-252-full20-disposition-2026-08-03.json"
REPORT = ROOT / "explorations/resolver-wave-e-source-owned-moving-252-full20-placement-2026-08-03.md"


def main() -> None:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    report = REPORT.read_text(encoding="utf-8")

    assert data["named_gate"] == "RESOLVER-WAVE-E-SOURCE-OWNED-MOVING-252-FULL20-PLACEMENT"
    assert data["gate_after"] == "PARTIAL_CONSTRUCTED"
    assert data["route_disposition"] == "CONTINUE"
    assert data["hostile_review_status"] == "PASS_AFTER_REPAIRS"

    source = data["source_carrier"]
    assert source["primary_route"] == "T_omega_bulk_ad_valued_one_form"
    assert source["T_omega_equals_Delta_A"] is False
    assert source["source_epsilon_equals_soldering_epsilon"] is False
    assert source["zorro_splitting_required"] is True
    assert source["source_to_native_95_port"] == "OPEN"
    assert source["joined_source_active_252_arrow"] == "OPEN"

    full14 = data["full14_contraction"]
    assert full14["delta_j5"] == "9I"
    assert full14["observer_coefficients"] == [4, 5]
    assert full14["vertical_only_delta_j5"] == "5I"
    assert full14["vertical_only_is_full_symmetry"] is False

    weight = data["full20_weight_family"]
    assert weight["rectangular_map_source_status"] == "SOURCE_SILENT"
    assert weight["unweighted_reconstruction_lambda"] == "1"
    assert weight["unweighted_has_low_R16"] is True
    assert weight["representative_unique_no_low_R_lambda"] == "1/2"
    assert weight["representative_half_weight_rank"] == 128
    assert weight["representative_target_support_dimension"] == 1152
    assert weight["representative_is_surjective_to_support"] is False
    assert weight["representation_wide_half_weight"] == "OPEN"
    assert weight["source_selected_lambda"] is None

    pairing = data["pairing"]
    assert pairing["diagonal_direct_sum_K_reciprocal_built"] is True
    assert pairing["full_G2_reciprocal"] == "OPEN"
    assert pairing["K_right_H"] is True
    assert pairing["C_reverse_support_checked"] is True
    assert pairing["C_right_H_checked"] is True
    assert pairing["coarse_direct_S_X_type_survivors"] == ["1"]
    assert pairing["total_G2_Y_P0_placement"] == "OPEN"
    assert pairing["arbitrary_M3C_right_H_with_trivial_provenance_reality"] is False

    descent = data["moving_descent"]
    assert descent["three_frame_constant_conjugation"] == "PASS"
    assert descent["transition_cocycle"] == "COBOUNDARY_FIXTURE_PASS"
    assert descent["actual_Y14_atlas_and_zorro_overlap"] == "OPEN"

    euler = data["source_euler"]
    assert euler["displayed_source_kappa_term"] == "SOURCE_OWNED"
    assert euler["active_j5_restriction"] == "CONDITIONAL_ON_SOURCE_TO_ACTIVE_PORT_AND_KAPPA1"
    assert euler["joined_source_active_252_arrow"] == "OPEN"
    assert euler["full14_exterior_adjoint"] == "PASS"
    assert euler["isolated_kappa_direct_equals_pulled"] is True
    assert euler["flat_curvature_fixture"] == "NOT_CONSTRUCTED"
    assert euler["affine_action_comparator_Ward_Green"] == "PASS"
    assert euler["ward_green_coupled_to_moving_projector"] is False
    assert euler["complement_Hessian_blocks"] == "OPEN"
    assert euler["complete_total_Euler_coefficient"] == "OPEN"
    assert euler["stationary_VEV"] == "OPEN"
    assert euler["mass"] == "OPEN"

    assert data["assertion_counts"]["total"] == 53
    assert data["assertion_counts"]["planted"] == 8
    assert data["source_collision"]["half_weight_selector"] == "SOURCE-SILENT"
    assert all(data["external_datum"][key] == "unchanged_unused"
               for key in ("P1", "P2", "P3"))
    assert data["next_gate"]["id"] == "RESOLVER-WAVE-F-ACTUAL-SOURCE-SHIAB-FERMION-EULER-WEIGHT-SELECTION"

    for token in (
        "4 horizontal + 5 vertical",
        "lambda=1/2",
        "JOINED SOURCE-TO-ACTIVE 252 EULER ARROW: OPEN",
        "COMPLETE TOTAL EULER COEFFICIENT: OPEN",
        "P1/P2/P3 remain unchanged and unused",
        "RESOLVER-WAVE-F-ACTUAL-SOURCE-SHIAB-FERMION-EULER-WEIGHT-SELECTION",
    ):
        assert token in report, f"report missing scope token {token!r}"

    for forbidden in (
        "the source selects lambda=1/2",
        "source-faithful",
        "wave e derives a mass",
        "the three-frame coboundary fixture is the actual y14 atlas",
    ):
        assert forbidden not in report.lower()

    print("resolver_wave_e_scope_audit: PASS")
    print("  native/source port, representative half-weight, G2/P0, total-Euler, VEV/mass, and datum fences retained")


if __name__ == "__main__":
    main()
