#!/usr/bin/env python3
"""Fail-closed scope audit for Resolver Wave D.

This gate checks disposition and Layer-0 fences. It does not reproduce the
exterior algebra, Weyl characters, or native matrix calculations and moves no
scientific status.
"""
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "explorations/cycle-gates-and-audits/resolver-wave-d-native-126-disposition-2026-08-03.json"
REPORT = ROOT / "explorations/resolver-wave-d-native-126-connection-placement-2026-08-03.md"


def main() -> None:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    report = REPORT.read_text(encoding="utf-8")

    assert data["named_gate"] == "RESOLVER-WAVE-D-NATIVE-126-CONNECTION-PLACEMENT"
    assert data["gate_after"] == "PARTIAL_CONSTRUCTED"
    assert data["route_disposition"] == "CONTINUE"
    assert data["hostile_review_status"] == "PASS_AFTER_REPAIRS"

    carrier = data["connection_carrier"]
    assert carrier["native_grade"] == 6
    assert carrier["K_adjoint_class"] == "K_ANTI_SELF_ADJOINT"
    assert carrier["right_H_linear"] is True
    assert carrier["raw_grade5_connection_allowed"] is False
    assert carrier["scalar_phase_repair_native_Sp_allowed"] is False

    exterior = data["exterior_map"]
    assert exterior["domain"] == "V10* tensor Lambda6(V10*)"
    assert exterior["target"] == "Lambda5(V10*)"
    assert exterior["domain_dimension"] == 2100
    assert exterior["target_dimension_real"] == 252
    assert exterior["complex_hodge_halves"] == ["126+", "126-"]
    assert exterior["delta_rank"] == 252
    assert exterior["wedge_rank"] == 120
    assert exterior["joint_kernel_dimension"] == 1728
    assert exterior["delta_j5"] == "5I"
    assert exterior["observer_split_coefficients"] == [4, 5]

    pairing = data["pairing"]
    assert pairing["bare_K_grade5"] == "HERMITIAN_SURVIVES"
    assert pairing["bare_C_plus_grade5"] == "ALTERNATING_SURVIVES"
    assert pairing["bare_C_minus_grade5"] == "ALTERNATING_SURVIVES"
    assert pairing["total_P0_rho_Y_kernel_built"] is False
    assert pairing["provenance_can_reverse_bare_verdict"] is True

    full20 = data["full20"]
    assert full20["written_c_rho_type"] == "S_TO_S"
    assert full20["one_form_output_comparator_type"] == "S_TO_V_TENSOR_S"
    assert full20["chosen_representative_one_form_output_has_one_144_component_per_source"] is True
    assert full20["chosen_representative_one_form_output_has_imGamma_16_companion_per_source"] is True
    assert full20["chosen_representative_one_form_output_has_low_R_16_companion_per_source"] is True
    assert full20["one_form_output_is_pure_144_map"] is False
    assert full20["written_c_rho_identified_with_one_form_output"] is False
    assert full20["physical_full20_placement_built"] is False

    source = data["symmetry_and_source"]
    assert source["local_Spin64_component_built"] is True
    assert source["moving_epsilon_full_Sp_descent_built"] is False
    assert source["source_selects_nonzero_grade6"] is False
    assert source["vev_built"] is False and source["mass_built"] is False

    assert data["assertion_counts"]["total"] == 70
    assert data["assertion_counts"]["planted_or_hostile"] == 11
    assert data["source_collision"]["curvature_map_projection_corrected_to_contraction"] == "SOURCE-CORRECTS"
    assert data["source_collision"]["exact_Vstar_Lambda6_to_Lambda5_map"] == "SOURCE-SILENT"
    assert all(data["external_datum"][key] == "unchanged_unused"
               for key in ("P1", "P2", "P3"))
    assert data["next_gate"]["id"] == "RESOLVER-WAVE-E-SOURCE-OWNED-MOVING-252-FULL20-PLACEMENT"

    for token in (
        "OPEN -> PARTIAL_CONSTRUCTED",
        "4 phi from the horizontal legs + 5 phi from the vertical legs = 9 phi",
        "source packet's",
        "P1/P2/P3 remain unchanged and unused",
        "RESOLVER-WAVE-E-SOURCE-OWNED-MOVING-252-FULL20-PLACEMENT",
    ):
        assert token in report, f"report missing scope token {token!r}"

    for forbidden in (
        "the one-form-output comparator is the written c_rho",
        "the real 252 is two independent real fields",
        "wave d derives a mass",
    ):
        assert forbidden not in report.lower()

    print("resolver_wave_d_scope_audit: PASS")
    print("  local 252, total-kernel, full-20-map, source, VEV, mass, and datum fences retained")


if __name__ == "__main__":
    main()
