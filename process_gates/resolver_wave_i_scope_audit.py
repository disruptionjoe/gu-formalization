#!/usr/bin/env python3
"""Fail-closed scope audit for Resolver Wave I.

This gate preserves the local Theta reconstruction / global source-owned
Theta, raw C* / raised C, chosen (9,5) / live rival (7,7), associated
projector family / actual source Euler distinctions. It does not reproduce
the symbolic, Clifford, or 128-by-128 calculations.
"""
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "explorations/cycle-gates-and-audits/resolver-wave-i-actual-metx-zorro-theta-descent-disposition-2026-08-03.json"
REPORT = ROOT / "explorations/resolver-wave-i-actual-metx-zorro-theta-descent-2026-08-03.md"


def main() -> None:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    report = REPORT.read_text(encoding="utf-8")

    assert data["named_gate"] == "RESOLVER-WAVE-I-ACTUAL-METX-ZORRO-THETA-DESCENT"
    assert data["gate_after"] == "LOCAL_NONLINEAR_METX_THETA_RECONSTRUCTION_AND_RIESZ_PORTED_SPIN_FIXTURE"
    assert data["route_disposition"] == "CONTINUE"
    assert data["hostile_review_status"] == "PASS_AFTER_REPAIRS"

    layer0 = data["layer_0"]
    assert layer0["source_chimeric_order"] == "V10_PLUS_HSTAR4"
    assert layer0["computational_Clifford_order"] == "HSTAR4_PLUS_V10_EXPLICIT_SWAP"
    assert layer0["tautological_metric"] == "h_ARBITRARY_FIBRE_POINT_DISTINCT_FROM_g_obs"
    assert layer0["Gamma_equals_A0"] == "UNCERTAIN_WHICH_OBSERVER_ZORRO_OR_Y_CONNECTION"
    assert layer0["Theta_source_identity"] == "SOURCE_SILENT_RECONSTRUCTION_NOT_GLOBAL_IDENTITY"
    assert layer0["raw_source_leg"] == "CSTAR_COVECTOR_TRANSFORMS_BY_O_INVERSE_TRANSPOSE"
    assert layer0["projector_leg"] == "RIESZ_RAISED_C_VECTOR_TRANSFORMS_BY_O"
    assert layer0["imposter_128"] == "A9F_SPIN_HALF_HINGE_UNTOUCHED_AND_UNTESTED"

    atlas = data["nonlinear_atlas"]
    assert atlas["charts"] == 3
    assert atlas["nonzero_Hessians"] is True
    assert atlas["integrable_inverses_exact"] is True
    assert atlas["full_total_space_first_jet_chain_rule"] is True
    assert atlas["Theta_operator_identity_01_12_02_and_triple"] is True
    assert atlas["omitted_Hessian_plant_fails"] is True
    assert atlas["det_Sym2_B"] == "(det_B)^5"
    assert atlas["forward_total_determinant"] == "(det_B)^4=1/1296"

    theta = data["zorro_candidate"]
    assert theta["observer_Christoffels_match_transformation_rule"] is True
    assert theta["kappa_tensorial"] is True
    assert theta["alpha_tensorial"] is True
    assert theta["raw_hdot_tensorial"] is False
    assert theta["wrong_sign_Gamma_nonlinear_descent"] is False
    assert theta["global_source_owned_Theta_Z"] == "OPEN"

    metric = data["metric_and_density"]
    assert metric["raw_vertical_signature"] == [7, 3]
    assert metric["trace_reversed_vertical_signature"] == [6, 4]
    assert metric["chosen_Wave_H_total_signature"] == [9, 5]
    assert metric["live_rival_7_7_relation"] == "UNDER_DETERMINED_REAL_FORM_FORK_UNTESTED_NOT_KILLED"
    assert metric["metric_determinant_squared_Jacobian_law"] is True
    assert metric["absolute_density_Jacobian_law"] is True

    spin = data["spin_descent"]
    assert spin["pointwise_at_one_triple_overlap"] is True
    assert spin["Spin_positive_triple_cocycle"] is True
    assert spin["minus_sign_is_planted_inconsistency_not_global_w2"] is True
    assert spin["global_spin_structure"] == "OPEN"

    port = data["source_port_descent"]
    assert port["raw_transport"] == "CSTAR_DUAL_O_INVERSE_TRANSPOSE_PLUS_CLIFFORD_ADJOINT"
    assert port["raised_transport"] == "C_VECTOR_O_PLUS_CLIFFORD_ADJOINT"
    assert port["musical_intertwiner"] == "sharp_eta*O^-T=O*sharp_eta"
    assert port["raw_projector"] == "flat_eta*Psrc_raised*sharp_eta"
    assert port["both_tilted_connections_assembled_on_each_chart"] is False
    assert port["projector_rank"] == 252
    assert port["all_252_image_basis_vectors_intertwine"] is True
    assert port["representative_kernel_sectors_intertwine"] is True
    assert port["wrong_vector_law_on_raw_leg_fails"] is True
    assert port["actual_128x128_J_H_and_K_preserved"] is True
    assert port["full_public_UK_J_invariance"] is False

    assert data["assertion_counts"] == {
        "exact": 43,
        "numeric_128x128": 1,
        "source_receipts": 7,
        "type_level": 13,
        "planted": 13,
        "total": 77,
    }
    assert all(data["external_datum"][key] == "unchanged_unused"
               for key in ("P1", "P2", "P3"))
    assert data["external_datum"]["may_manufacture_Theta_source_ownership_Euler_or_domain"] is False
    assert all(value == "OPEN" for value in data["global_boundary"].values())
    assert data["next_gate"]["id"] == "RESOLVER-WAVE-J-DESCENDED-SOURCE-ACTION-TOTAL-EULER-AND-WARD"

    for token in (
        "connection-dependent candidate",
        "raw source first leg",
        "Riesz-raised",
        "O(s)^{-T}",
        "P_{\\rm raw}=\\flat_\\eta P_{\\rm raised}\\sharp_\\eta",
        "live rival/public `(7,7)`",
        "planted inconsistent lift",
        "every one of the 252 selected image basis vectors",
        "source-silent",
        "P1/P2/P3 remain unchanged and unused",
        "RESOLVER-WAVE-J-DESCENDED-SOURCE-ACTION-TOTAL-EULER-AND-WARD",
    ):
        assert token in report, f"report missing scope token {token!r}"

    for forbidden in (
        "theta_z is source-owned",
        "gamma is identical to a0",
        "the (7,7) branch is killed",
        "raw source covectors transform by o ",
        "the minus sign proves nonzero w2",
        "wave i varies the source action",
        "rl=1 proves no leakage",
        "p1/p2/p3 construct theta",
    ):
        assert forbidden not in report.lower()

    print("resolver_wave_i_scope_audit: PASS")
    print("  local Theta reconstruction, raw/raised Riesz port, chosen/rival real-form, Spin-sign, source-Euler, no-leakage, and datum fences retained")


if __name__ == "__main__":
    main()
