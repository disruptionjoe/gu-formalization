#!/usr/bin/env python3
"""Fail-closed scope audit for Resolver Wave H.

This gate preserves the chosen local J fixture / source-owned bundle
reduction / actual global Theta-Z / source-Euler distinctions. It does not
reproduce the Clifford, matrix, Sage, or first-jet calculations.
"""
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "explorations/cycle-gates-and-audits/resolver-wave-h-public-native-combined-port-disposition-2026-08-03.json"
REPORT = ROOT / "explorations/resolver-wave-h-public-native-combined-port-2026-08-03.md"


def main() -> None:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    report = REPORT.read_text(encoding="utf-8")

    assert data["named_gate"] == "RESOLVER-WAVE-H-PUBLIC-NATIVE-REDUCTION-THETA-Z-DESCENT-AND-TOTAL-EULER"
    assert data["gate_after"] == "LOCAL_CHOSEN_J_MOVING_REDUCTION_AND_COMBINED_PORT_FIXTURE"
    assert data["route_disposition"] == "CONTINUE"
    assert data["hostile_review_status"] in {"PENDING", "PASS_AFTER_REPAIRS", "PASS"}

    layer0 = data["layer_0"]
    assert layer0["relation"] == "REAL_FORM_FORK_WITH_CHOSEN_LOCAL_J_FIXTURE_NOT_SOURCE_OR_BUNDLE_IDENTITY"
    assert layer0["J_red"] == "CHOSEN_LOCAL_U_OVER_SP_TYPE_REDUCTION_FIELD_SOURCE_OWNERSHIP_SILENT"
    assert set(layer0["J_red_distinct_from"]) == {
        "P1", "P2", "P3", "epsilon_src", "epsilon_IG", "Theta_Z"
    }
    assert layer0["T_omega"] == "TENSORIAL_CONNECTION_DIFFERENCE_NOT_CONNECTION"
    assert layer0["epsilon_src_equals_epsilon_IG"] == "UNCERTAIN"

    reduction = data["public_native_reduction"]
    assert reduction["typed_domain"] == "REAL_PUBLIC_uK_NATIVE_GRADES_REAL_COMPLEMENTARY_GRADES_IMAGINARY"
    assert reduction["unrestricted_complex_Clifford_domain"] is False
    assert reduction["fixed_locus_statement"] == "Fix(rho_J)_intersect_uK_equals_sp(K,J)"
    assert reduction["public_real_dimension"] == 16384
    assert reduction["native_real_dimension"] == 8256
    assert reduction["complement_real_dimension"] == 8128
    assert reduction["public_one_form_dimension"] == 229376
    assert reduction["native_one_form_dimension"] == 115584
    assert reduction["R_real_linear_idempotent"] is True
    assert reduction["R_complex_linear"] is False
    assert reduction["image_K_anti_right_H"] is True
    assert reduction["fixed_R_full_public_U_equivariant"] is False
    assert reduction["moving_J_public_U_covariant"] is True
    assert reduction["R_Lie_algebra_homomorphism"] is False
    assert reduction["connection_curvature_functor"] is False
    assert reduction["public_covariance_codomain"] == "MOVES_FROM_sp(K,J)_TO_sp(K,J_h)"
    assert reduction["J_ownership_and_dynamics"] == "SOURCE_SILENT_OPEN"
    assert reduction["bundle_globalization"] == "OPEN_U_OVER_SP_REDUCTION_SECTION"

    port = data["combined_port"]
    assert port["Chevalley_reinclusion_explicit"] is True
    assert port["rank"] == 252
    assert port["kernel_dimension"] == 229124
    assert port["idempotent"] is True
    assert port["local_real_fixed_density_trace_pairing_self_adjoint"] is True
    assert port["Reynolds_q6_Pext_adjoint_decomposition_checked"] is True
    assert port["public_complement_killed"] is True
    assert port["grade10_near_miss_killed"] is True

    tilted = data["moving_tilted_fixture"]
    assert tilted["scope"] == "CHOSEN_A0_EQUALS_0_LOCAL_FIRST_JET_FIXED_COINDEX"
    assert tilted["public_mover_K_unitary"] is True
    assert tilted["public_mover_right_H"] is False
    assert tilted["left_combined_Psrc"] == "BASIC"
    assert tilted["right_combined_Psrc"] == "Ad(h^-1)-COVARIANT"
    assert tilted["frozen_frame_control"] == "FAILS_AS_REQUIRED"
    assert tilted["paired_frame_law"] == "STIPULATED_LOCAL_FIXTURE_NOT_SOURCE_DERIVED"
    assert tilted["general_tau_A0_bridge"] == "OPEN"

    variation = data["moving_variation"]
    assert variation["exact_symbolic_derivative_matches"] is True
    assert variation["differentiated_idempotence"] is True
    assert variation["derivative_live"] is True
    assert variation["auxiliary_projector_chain_fixture"] is True
    assert variation["auxiliary_quadratic_derivative"] == "-4"
    assert variation["displayed_I1B_plus_IF_varied"] is False
    assert variation["actual_Euler_covector_constructed"] is False
    assert variation["global_density_Krein_adjoint"] == "OPEN"

    observation = data["projector_kernel_observation"]
    assert observation["projector_zero_kernel_nonzero_control"] is True
    assert observation["active_transverse_Euler_covector"] == "NOT_CONSTRUCTED"
    assert observation["RL_equals_1_implies_no_leakage"] is False
    assert observation["physical_no_leakage"] == "OPEN"

    global_boundary = data["global_boundary"]
    assert all(value == "OPEN" for value in global_boundary.values())

    assert data["assertion_counts"] == {
        "exact": 26,
        "numeric_native_controls": 9,
        "independent_Sage": 1,
        "source_receipts": 8,
        "type_level": 23,
        "planted": 12,
        "total": 79,
    }
    assert all(data["external_datum"][key] == "unchanged_unused"
               for key in ("P1", "P2", "P3"))
    assert data["external_datum"]["may_manufacture_J_Theta_BV_or_domain"] is False
    assert data["next_gate"]["id"] == "RESOLVER-WAVE-I-ACTUAL-METX-ZORRO-THETA-DESCENT"

    for token in (
        "REAL-FORM-FORK",
        "Lie-algebra homomorphism",
        "same composite",
        "delta S_{\\rm loc}=-4",
        "chosen local reduction fixture",
        "extra local `U/Sp`-type reduction field",
        "not a variation of the displayed `I1B+IF` source",
        "actual nonconstant `Met(X)`/Zorro overlap construction",
        "nonzero kernel vector annihilated by the projector",
        "RL=1",
        "P1/P2/P3 remain unchanged and unused",
        "RESOLVER-WAVE-I-ACTUAL-METX-ZORRO-THETA-DESCENT",
    ):
        assert token in report, f"report missing scope token {token!r}"

    for forbidden in (
        "public u is identical to native sp",
        "r_j is a lie-algebra homomorphism",
        "local moving covariance proves global descent",
        "theta_z is constructed globally",
        "rl=1 proves no leakage",
        "p1/p2/p3 construct the reduction",
        "wave h constructs a mass",
    ):
        assert forbidden not in report.lower()

    print("resolver_wave_h_scope_audit: PASS")
    print("  chosen-J fixture, typed public carrier, combined tilted Psrc, projector first jet, source-Euler, Theta-Z, no-leakage, and datum fences retained")


if __name__ == "__main__":
    main()
