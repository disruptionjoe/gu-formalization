#!/usr/bin/env python3
"""Fail-closed scope audit for the R2B2B2H mixed-Shiab operator jet."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "lab/process/pw2fr2b2b2h-mixed-shiab-second-jet-registry.json"
REPORT = ROOT / "explorations/pw2fr2b2b2h-mixed-shiab-second-jet-2026-08-04.md"


def main() -> None:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    report = REPORT.read_text(encoding="utf-8")

    assert data["status"] == "CONDITIONAL_ACTIVE_MIXED_SHIAB_OPERATOR_JET_CLOSED__DISTINCT_I2B_SECOND_PRIMALIZER_OPEN"
    jet = data["operator_jet"]
    assert jet["moving_Clifford_relations"] == "196_OF_196_PAIRS_PASS_THROUGH_RS"
    assert jet["first_Hodge_slots"] == "2_OF_2_MATCH_ACCEPTED_DSTAR"
    assert jet["Hodge_square"] == "SIGN_MINUS_ONE_THROUGH_RS"
    assert jet["first_Shiab_slots"] == "BASE_PLUS_2_OF_2_MATCH_ACCEPTED_CONSTRUCTORS"
    assert jet["mixed_Shiab_coordinates"] == 515
    assert data["admission"]["complete_I1_A4"] == "NOT_ASSEMBLED"
    assert data["admission"]["distinct_I2B_second_primalizer_pairing"] == "OPEN"
    assert data["admission"]["projective_kappa1"] == "NOT_RUN"
    assert data["external_datum"] == "P1_P2_P3_UNCHANGED_AND_UNUSED"
    assert data["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
    assert data["third_lane_gate"] == "TG-1 AND TG-2 AND TG-3 = NOT_PROMOTED"

    for token in (
        "CONDITIONAL_ACTIVE_MIXED_TRACE_PHI_HODGE_SHIAB_OPERATOR_JET_CLOSED",
        "mixed Shiab slot is live in 515 sparse coordinates",
        "does **not** assemble the 35-monomial `I1 A4`",
        "complete second residual-primalizer/pairing jet",
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

    print("pw2fr2b2b2h_mixed_shiab_second_jet_scope_audit: PASS")
    print("  operator-jet closure and separate I2B/bank boundary retained")


if __name__ == "__main__":
    main()
