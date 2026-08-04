#!/usr/bin/env python3
"""Fail-closed scope audit for Resolver Wave J.

Preserves comparator/native-action, Omega1-port/Omega2-curvature,
covariance/native-Ward, and obstruction/route-selection distinctions.
It does not reproduce the mathematical probe.
"""
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "explorations/cycle-gates-and-audits/resolver-wave-j-descended-source-action-total-euler-ward-disposition-2026-08-03.json"
REPORT = ROOT / "explorations/resolver-wave-j-descended-source-action-total-euler-ward-2026-08-03.md"


def main() -> None:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    report = REPORT.read_text(encoding="utf-8")
    probe = (ROOT / "tests/channel-swings/resolver_wave_j_descended_source_action_total_euler_ward_probe.py").read_text(encoding="utf-8")

    assert data["named_gate"] == "RESOLVER-WAVE-J-DESCENDED-SOURCE-ACTION-TOTAL-EULER-AND-WARD"
    assert data["gate_after"] == "LOCAL_SOURCE_DENSITY_AND_TRANSLATION_COMPARATORS_WITH_COSET_CURVATURE_OBSTRUCTION"
    assert data["route_disposition"] == "REBASE"
    assert data["hostile_review_status"] in {"REPAIRED_PENDING_FINAL_REVIEW", "PASS_AFTER_REPAIRS"}

    layer0 = data["layer_0"]
    assert layer0["descended_fixture"] == "POINTWISE_ALREADY_COMPOSED_SCALAR_DENSITY_COMPARATOR_NOT_I_B1"
    assert layer0["translation_comparator"] == "CYCLIC_COEFFICIENT_TRANSGRESSION_FIXTURE_AT_FIXED_GEOMETRY"
    assert layer0["native_B1_Euler"] == "OPEN_DISTINCT_COVECTOR"
    assert layer0["Ward_comparator"] == "INFINITESIMAL_GL2_CYCLIC_TRACE_COVARIANCE_NOT_NATIVE_WARD"
    assert layer0["Psrc"] == "OMEGA1_TO_OMEGA1_CANDIDATE_OUTPUT_TANGENCY_PORT"
    assert layer0["Shiab"] == "DENSITY_DUAL_OMEGA2_TO_OMEGA13_MAP_UNBUILT_NATIVE"

    density = data["local_density_comparator"]
    assert density["charts"] == 3
    assert density["pairwise_and_triple_transport"] is True
    assert density["native_Shiab_constructed"] is False
    assert density["monolithic_I_B1_constructed"] is False

    translation = data["translation_comparator"]
    assert translation["coefficients"] == ["1/2", "1/3"]
    assert translation["linear_and_quadratic_channels_independent"] is True
    assert translation["native_B1_Euler_constructed"] is False

    comparators = data["green_and_covariance_comparators"]
    assert comparators["boundary_live"] is True
    assert comparators["native_Ward_identity"] == "OPEN"
    assert comparators["native_Green_form_and_domain"] == "OPEN"

    burden = data["degree_and_coset_burdens"]
    assert burden["quadratic_coefficient_degree"] == "OMEGA2_GRADE2"
    assert burden["quadratic_coefficient_fed_to_Psrc"] is False
    assert burden["image_bracket_nonclosure_proved"] is False
    assert burden["R_J_X"] == "0" and burden["R_J_Y"] == "0"
    assert burden["R_J_bracket"] == "-2*e045678"
    assert burden["naive_F_RJA_shortcut"] == "KILLED_WITHOUT_COSET_CORRECTION"
    assert burden["restrict_before_variation"] == "OPEN_PENDING_DEGREE_CORRECT_TEST"
    assert burden["full_public_then_projected_residual"] == "OPEN_PENDING_DEGREE_CORRECT_TEST"
    assert burden["bosonic_tangency"] == "OPEN_NOT_TESTED"
    assert burden["total_tangency"] == "OPEN_NOT_TESTED"

    assert data["moving_geometry_comparators"]["all_joined_in_same_B1_functional"] is False
    assert data["assertion_counts"] == {
        "exact": 18,
        "numeric": 0,
        "source_receipts": 5,
        "type_level": 19,
        "planted": 10,
        "total": 52,
    }
    assert all(data["external_datum"][key] == "unchanged_unused" for key in ("P1", "P2", "P3"))
    assert data["next_gate"]["id"] == "RESOLVER-WAVE-K-NATIVE-SHIAB-MONOLITHIC-B1-VARIATION-AND-PORT-PLACEMENT"

    for token in (
        "did **not** complete its advertised total-Euler/Ward gate",
        "pointwise source-shaped density",
        "cyclic/transgression identities",
        "not a native Ward or Noether theorem",
        "It is an `Omega2` grade-two coefficient",
        "corrected reduced `(a,m)` action remains possible",
        "bosonic and total port tangency remain open and untested",
        "P1/P2/P3 are unchanged and unused",
        "RESOLVER-WAVE-K-NATIVE-SHIAB-MONOLITHIC-B1-VARIATION-AND-PORT-PLACEMENT",
    ):
        assert token in report, f"report missing scope token {token!r}"

    for forbidden in (
        "bosonic tangency fails",
        "postvariation port order selected",
        "the surviving construction order is",
        "the 252 survives as a post-variation",
        "source-corrects-project-before-curvature",
    ):
        assert forbidden not in report.lower(), forbidden

    for stale_probe_claim in (
        "constructs the smallest source-owned action-level object",
        "exact source translation derivative",
        "complete source translation euler contraction",
    ):
        assert stale_probe_claim not in probe.lower(), stale_probe_claim

    print("resolver_wave_j_scope_audit: PASS")
    print("  comparator/native-action, degree, open port-order, tangency, and datum fences retained")


if __name__ == "__main__":
    main()
