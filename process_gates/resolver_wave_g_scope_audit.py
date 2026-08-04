#!/usr/bin/env python3
"""Fail-closed scope audit for Resolver Wave G.

This gate preserves the local-native-q6 / public-source-port / moving-frame /
global-descent / total-Euler distinctions. It does not reproduce the algebra.
"""
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "explorations/cycle-gates-and-audits/resolver-wave-g-q6-native-tilted-source-port-disposition-2026-08-03.json"
REPORT = ROOT / "explorations/resolver-wave-g-q6-native-tilted-source-port-2026-08-03.md"


def main() -> None:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    report = REPORT.read_text(encoding="utf-8")

    assert data["named_gate"] == "RESOLVER-WAVE-G-Q6-NATIVE-SP-TILTED-SOURCE-PORT-AND-TRANSVERSE-EULER"
    assert data["gate_after"] == "PARTIAL_NATIVE_Q6_AND_LOCAL_TILTED_SCHEMA_CONSTRUCTED"
    assert data["route_disposition"] == "CONTINUE"
    assert data["hostile_review_status"] in {"PENDING", "PASS_AFTER_REPAIRS", "PASS"}

    q6 = data["fixed_native_q6"]
    assert q6["native_grades"] == [2, 3, 6, 7, 10, 11, 14]
    assert q6["native_coefficient_dimension"] == 8256
    assert q6["all_clifford_blades_checked"] == 16384
    assert q6["grade6_blades_fixed"] == 3003
    assert q6["cross_grade_blades_killed"] == 5253
    assert q6["one_form_rank"] == 42042
    assert q6["one_form_kernel_dimension"] == 73542
    assert q6["fixed_coefficient_pairing_self_adjoint"] is True
    assert q6["global_density_Krein_adjoint"] == "OPEN"

    hom = data["intertwiner_census"]
    assert hom["coefficientwise_Hom_dimension"] == 1
    assert hom["one_form_Hom_dimension"] == 5
    assert hom["per_input_grade"]["6"] == 4
    assert hom["per_input_grade"]["10"] == 1
    assert hom["Spin_equivariance_alone_selects_q6"] is False
    assert hom["grade10_near_miss_annihilated"] is True

    active = data["rank252_composite"]
    assert active["rank"] == 252
    assert active["composite_kernel_dimension"] == 115332
    assert active["all_internal_five_blade_images_checked"] == 252
    assert active["Pext_fixed_pairing_self_adjoint"] is True
    assert active["normalization"] == "1/9"
    assert active["complex_126_halves_independent_real_fields"] is False

    mover = data["full_Sp_mover"]
    assert mover["generator_grade"] == 3
    assert mover["X_squared"] == 0
    assert mover["native_K_anti_right_H"] is True
    assert mover["finite_g_K_unitary"] is True
    assert mover["fixed_q6_full_Sp_equivariant"] is False
    assert mover["moving_q6_covariant"] is True

    tilted = data["tilted_source"]
    assert tilted["scope"] == "CHOSEN_A0_EQUALS_0_LOCAL_CONVENTION_FIXTURE"
    assert tilted["left_tilted_T"] == "invariant"
    assert tilted["right_tilted_T"] == "Ad(h^-1)-equivariant"
    assert tilted["untilted_left_control"] == "fails_as_required"
    assert tilted["wrong_Maurer_Cartan_side_control"] == "fails_as_required"
    assert tilted["tau_homomorphism_fixture"] == "PASS"
    assert tilted["semidirect_associativity_fixture"] == "PASS"
    assert tilted["frame_surrogate_type"] == "GL2_LEFT_FRAME_FIXTURE_ONLY_NOT_CLIFFORD_NOT_THETA_Z"
    assert tilted["combined_Psrc_Tomega_naturality"] == "NOT_TESTED"

    global_port = data["global_port"]
    assert global_port["epsilon_src_invents_split"] is False
    assert global_port["coarse_epsilon_plane_invents_split"] is False
    assert global_port["actual_Theta_Z_coindex"] == "OPEN"
    assert global_port["nonconstant_overlap_descent"] == "OPEN"
    assert global_port["public_U_to_native_Sp_reduction"] == "OPEN"
    assert global_port["total_Euler_tangency_to_native_fixed_locus"] == "OPEN"
    assert global_port["local_Psrc"] == "FORMULA_ONLY_UNINSTANTIATED"
    assert global_port["status"] == "LOCAL_SCHEMA_ONLY"

    variation = data["variational_boundary"]
    assert variation["fixed_q6_order"] == 0
    assert variation["fixed_q6_independent_Green_current"] is False
    assert variation["source_variation_domain"] == "UNDECLARED"
    assert variation["diagnostic_Euler_split_equals_restricted_action_variation"] is False
    assert variation["active_Euler_complete"] is False
    assert variation["transverse_Euler_complete"] is False
    assert variation["RL_equals_1_implies_no_leakage"] is False

    assert data["assertion_counts"] == {
        "exact": 29,
        "independent_Sage": 3,
        "source_receipts": 6,
        "type_level": 17,
        "planted": 9,
        "total": 64,
    }
    assert all(data["external_datum"][key] == "unchanged_unused"
               for key in ("P1", "P2", "P3"))
    assert data["next_gate"]["id"] == "RESOLVER-WAVE-H-PUBLIC-NATIVE-REDUCTION-THETA-Z-DESCENT-AND-TOTAL-EULER"

    for token in (
        "Pi_6^{\\rm ad}",
        "Spin equivariance does not select the map",
        "fixed grade-six projector is not full-`Sp` equivariant",
        "left tilted factor then",
        "GL(2)` frame surrogate",
        "combined covariance",
        "public-to-native real-form reduction",
        "source variation domain",
        "active and transverse equations",
        "P1/P2/P3 remain unchanged and unused",
        "RESOLVER-WAVE-H-PUBLIC-NATIVE-REDUCTION-THETA-Z-DESCENT-AND-TOTAL-EULER",
    ):
        assert token in report, f"report missing scope token {token!r}"

    for forbidden in (
        "a0=0` convention displayed in the portal transcript",
        "local native q6 is the public source port",
        "fixed q6 is full-sp equivariant",
        "epsilon_src is epsilon_ig",
        "rl=1 proves no leakage",
        "p1/p2/p3 select q6",
        "wave g constructs a mass",
    ):
        assert forbidden not in report.lower()

    print("resolver_wave_g_scope_audit: PASS")
    print("  native q6, five-intertwiner census, moving q6, chosen tilted fixture, uninstantiated combined port, global descent, Euler, and datum fences retained")


if __name__ == "__main__":
    main()
