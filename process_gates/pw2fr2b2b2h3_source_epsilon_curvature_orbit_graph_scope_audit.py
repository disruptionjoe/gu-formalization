#!/usr/bin/env python3
"""Fail-closed scope audit for the R2B2B2H3 source-epsilon orbit graph."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "lab/process/pw2fr2b2b2h3-source-epsilon-curvature-orbit-graph-registry.json"
REPORT = ROOT / "explorations/pw2fr2b2b2h3-source-epsilon-curvature-orbit-graph-2026-08-04.md"


def main() -> None:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    report = REPORT.read_text(encoding="utf-8")

    assert data["status"] == "CONDITIONAL_ACTIVE_LOCAL_SOURCE_EPSILON_CONNECTION_CURVATURE_OPERATOR_ORBIT_GRAPH_CLOSED__GLOBAL_REAL_FORM_BUNDLE_MORPHISM_OPEN"
    fixture = data["connection_curvature_fixture"]
    assert fixture["curvature_conjugacy"] == "EXACT_BEFORE_COEFFICIENT_EXTRACTION"
    assert fixture["mixed_curvature_nonzero_entries"] == 4
    assert fixture["omitted_maurer_cartan_defect_nonzero_entries"] == 4
    orbit = data["active_source_orbit"]
    assert orbit["curvature_coordinates"] == [360, 132, 121, 121]
    assert orbit["residual_coordinates"] == [13, 2, 2, 2]
    assert orbit["explicit_moved_operator_equals_transported_residual"] is True
    assert orbit["residual_norm_jet"] == ["981/64", "0", "0", "0"]
    assert data["admission"]["global_source_to_active_real_form_bundle_morphism"] == "OPEN"
    assert data["admission"]["complete_I1_A4"] == "NOT_ASSEMBLED"
    assert data["admission"]["projective_kappa1"] == "NOT_RUN"
    assert data["external_datum"] == "P1_P2_P3_UNCHANGED_AND_UNUSED"
    assert data["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
    assert data["third_lane_gate"] == "TG-1 AND TG-2 AND TG-3 = NOT_PROMOTED"

    for token in (
        "CONDITIONAL_ACTIVE_LOCAL_SOURCE_EPSILON_CONNECTION_CURVATURE_OPERATOR_ORBIT_GRAPH_CLOSED",
        "F(B_epsilon) = epsilon^-1 F(Gamma) epsilon",
        "(360, 132, 121, 121)",
        "(981/64, 0, 0, 0)",
        "not the complete global H3",
        "P1/P2/P3 remain unchanged and unused",
        "FORMALLY_SEPARATE_INSIDE_ERIC_LANE",
        "TG-1 AND TG-2 AND TG-3",
    ):
        assert token in report, token

    for forbidden in (
        "global bundle morphism closed",
        "complete i1 a4 bank passes",
        "complete i2b c4 bank passes",
        "kappa1 is selected",
        "third lane promoted",
        "physics verdict proved",
    ):
        assert forbidden not in report.lower(), forbidden

    print("pw2fr2b2b2h3_source_epsilon_curvature_orbit_graph_scope_audit: PASS")
    print("  conditional local orbit closure and global real-form/C4 boundary retained")


if __name__ == "__main__":
    main()
