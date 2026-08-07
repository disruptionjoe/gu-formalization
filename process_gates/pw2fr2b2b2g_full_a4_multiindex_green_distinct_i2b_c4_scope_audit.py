#!/usr/bin/env python3
"""Fail-closed scope audit for the R2B2B2G admission-blocker result."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "lab/process/pw2fr2b2b2g-full-a4-multiindex-green-distinct-i2b-c4-registry.json"
REPORT = ROOT / "explorations/pw2fr2b2b2g-full-a4-multiindex-green-distinct-i2b-c4-2026-08-03.md"


def main() -> None:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    report = REPORT.read_text(encoding="utf-8")

    assert data["status"] == "REBASE_BLOCKED_ON_MIXED_SHIAB_SECOND_JET_AND_COMPLETE_I2B_PRIMALIZER"
    assert data["trace_transport"]["first_slots_match_full_moving_Phi"] == "6_OF_6_PASS"
    assert data["trace_transport"]["norm_jet"] == ["-1", "0", "0", "0"]
    assert len(data["trace_transport"]["mixed_trace_live"]) == 3
    admission = data["admission"]
    assert admission["moving_Shiab_api"] == "FIRST_ORDER_ONLY_CURVATURE_H_TRACE_MOTION"
    assert admission["mixed_trace_Shiab_input"] == "ABSENT"
    assert admission["full_I1_A4"] == "BLOCKED_ON_MIXED_SHIAB_JET"
    assert admission["distinct_I2B_C4"] == "BLOCKED_ON_COMPLETE_SECOND_RESIDUAL_PRIMALIZER_PAIRING_JET"
    assert admission["projective_kappa1"] == "NOT_RUN"
    assert admission["arbitrary_symmetric_completion"] == "FORBIDDEN"
    assert data["external_datum"] == "P1_P2_P3_UNCHANGED_AND_UNUSED"
    assert data["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
    assert data["third_lane_gate"] == "TG-1 AND TG-2 AND TG-3 = NOT_PROMOTED"

    for token in (
        "does **not** admit interpolation yet",
        "live first-order trace corrections",
        "mixed slot is nevertheless nonzero",
        "BLOCKED_ON_MIXED_SHIAB_JET",
        "BLOCKED_ON_COMPLETE_SECOND_PRIMALIZER_JET",
        "No arbitrary symmetric quartic",
        "P1/P2/P3 remain unchanged and unused",
        "FORMALLY_SEPARATE_INSIDE_ERIC_LANE",
        "TG-1 AND TG-2 AND TG-3",
    ):
        assert token in report, token

    for forbidden in (
        "complete i1 a4 bank passes",
        "complete i2b c4 bank passes",
        "kappa1 is selected",
        "euler obstruction proved",
        "third lane promoted",
    ):
        assert forbidden not in report.lower(), forbidden

    print("pw2fr2b2b2g_full_c4_scope_audit: PASS")
    print("  mixed-Shiab/primalizer blockers and campaign fences retained")


if __name__ == "__main__":
    main()
