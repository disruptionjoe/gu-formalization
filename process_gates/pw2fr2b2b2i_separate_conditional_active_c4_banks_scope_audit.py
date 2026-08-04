#!/usr/bin/env python3
"""Fail-closed scope audit for the R2B2B2I C4-bank coverage decision."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "lab/process/pw2fr2b2b2i-separate-conditional-active-c4-banks-registry.json"
REPORT = ROOT / "explorations/pw2fr2b2b2i-separate-conditional-active-c4-banks-2026-08-04.md"


def main() -> None:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    report = REPORT.read_text(encoding="utf-8")

    assert data["status"] == "SEPARATE_CONDITIONAL_ACTIVE_C4_BANK_PROMOTION_BLOCKED_ON_UNIVERSAL_OWNER_CONORMAL_COVERAGE__PARAMETRIC_H_H2_FORMULAS_RETAINED"
    requirement = data["bank_requirement"]
    assert requirement["metric_owner_count"] == 10
    assert requirement["symmetric_owner_pair_count"] == 55
    assert requirement["homogeneous_quartic_monomial_count"] == 35
    assert requirement["uncompressed_cells_per_bank"] == 1925
    coverage = data["accepted_coverage"]
    assert coverage["shared_exercised_pair"] == [3, 7]
    assert coverage["owner_pair_gap"] == 54
    assert coverage["quartic_lattice_gap"] == 34
    assert coverage["parameterized_constructors_retained"] is True
    assert coverage["universal_symmetry_reduction"] == "NOT_PROVED"
    assert coverage["complete_I1_A4"] == "NOT_PROMOTED"
    assert coverage["complete_I2B_C4"] == "NOT_PROMOTED"
    assert data["admission"]["bank_nonexistence"] == "NOT_CLAIMED"
    assert data["admission"]["multiindex_Green_Helmholtz"] == "NOT_ADMITTED"
    assert data["external_datum"] == "P1_P2_P3_UNCHANGED_AND_UNUSED"
    assert data["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
    assert data["third_lane_gate"] == "TG-1 AND TG-2 AND TG-3 = NOT_PROMOTED"

    for token in (
        "SEPARATE_CONDITIONAL_ACTIVE_C4_BANK_PROMOTION_BLOCKED_ON_UNIVERSAL_OWNER_CONORMAL_COVERAGE",
        "55 * 35 = 1,925",
        "Parameterization makes a universal successor",
        "not a mathematical obstruction",
        "does not prove either bank zero, inconsistent, or nonexistent",
        "P1/P2/P3 remain unchanged and unused",
        "FORMALLY_SEPARATE_INSIDE_ERIC_LANE",
        "TG-1 AND TG-2 AND TG-3",
    ):
        assert token in report, token

    for forbidden in (
        "complete i1 a4 bank passes",
        "complete i2b c4 bank passes",
        "bank nonexistence proved",
        "kappa1 is selected",
        "third lane promoted",
        "physics verdict proved",
    ):
        assert forbidden not in report.lower(), forbidden

    print("pw2fr2b2b2i_separate_conditional_active_c4_banks_scope_audit: PASS")
    print("  universal coverage blocker, separate banks, and nonexistence boundary retained")


if __name__ == "__main__":
    main()
