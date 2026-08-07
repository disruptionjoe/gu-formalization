#!/usr/bin/env python3
"""Fail-closed scope audit for the R2B2B2H2 I2B second jet."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "lab/process/pw2fr2b2b2h2-i2b-second-residual-primalizer-pairing-registry.json"
REPORT = ROOT / "explorations/pw2fr2b2b2h2-complete-i2b-second-residual-primalizer-pairing-2026-08-04.md"


def main() -> None:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    report = REPORT.read_text(encoding="utf-8")

    assert data["status"] == "CONDITIONAL_ACTIVE_FIXED_BACKGROUND_I2B_SECOND_RESIDUAL_PRIMALIZER_PAIRING_JET_CLOSED__GLOBAL_SOURCE_EPSILON_CURVATURE_GRAPH_OPEN"
    jet = data["residual_primalizer_pairing_jet"]
    assert jet["base_residual_coordinates"] == 13
    assert jet["base_full_carrier_norm"] == "981/64"
    assert jet["fixed_residual_pairing_jet"] == ["981/64", "0", "4293/128", "0"]
    assert jet["first_pairing_slots"] == "2_OF_2_MATCH_ACCEPTED_DSTAR"
    assert jet["mixed_action"] == "-103/256"
    assert jet["live_family_count"] == 3
    assert jet["direct_equals_five_family_sum"] is True
    assert data["admission"]["global_source_epsilon_curvature_graph"] == "OPEN"
    assert data["admission"]["complete_I1_A4"] == "NOT_ASSEMBLED"
    assert data["admission"]["projective_kappa1"] == "NOT_RUN"
    assert data["external_datum"] == "P1_P2_P3_UNCHANGED_AND_UNUSED"
    assert data["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
    assert data["third_lane_gate"] == "TG-1 AND TG-2 AND TG-3 = NOT_PROMOTED"

    for token in (
        "CONDITIONAL_ACTIVE_FIXED_BACKGROUND_I2B_SECOND_RESIDUAL_PRIMALIZER_PAIRING_JET_CLOSED",
        "D_rs I2B = -103/256",
        "P_g(E0,E0) = (981/64, 0, 4293/128, 0)",
        "does **not** construct the global",
        "P1/P2/P3 remain unchanged and unused",
        "FORMALLY_SEPARATE_INSIDE_ERIC_LANE",
        "TG-1 AND TG-2 AND TG-3",
    ):
        assert token in report, token

    for forbidden in (
        "complete i1 a4 bank passes",
        "complete i2b c4 bank passes",
        "kappa1 is selected",
        "third lane promoted",
        "physics verdict proved",
    ):
        assert forbidden not in report.lower(), forbidden

    print("pw2fr2b2b2h2_i2b_second_residual_primalizer_pairing_scope_audit: PASS")
    print("  scoped second-jet closure and global-curvature/C4 boundary retained")


if __name__ == "__main__":
    main()
