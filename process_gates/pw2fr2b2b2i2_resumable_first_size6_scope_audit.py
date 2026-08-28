#!/usr/bin/env python3
"""Fail-closed scope audit for the I2 resumable first-size-six certificate."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "lab/process/pw2fr2b2b2i2-resumable-full-evaluator-coverage.json"
REPORT = ROOT / "explorations/pw2fr2b2b2i2-resumable-first-size6-full-evaluator-certificate-2026-08-05.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-05-pw2fr2b2b2i2-resumable-first-size6-review.md"
PROBE = ROOT / "tests/channel-swings/pw2fr2b2b2i2_resumable_first_size6_full_evaluator_probe.py"


def main() -> None:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    report = REPORT.read_text(encoding="utf-8")
    review = REVIEW.read_text(encoding="utf-8")
    probe = PROBE.read_text(encoding="utf-8")

    assert data["run_id"] == "historical-investigation"
    assert data["resumption_contract"]["ledger_style"] == "APPEND_ONLY_CERTIFICATE_CHAIN"
    assert data["resumption_contract"]["next_resume_index"] >= 4
    assert data["resumption_contract"]["shard_unit"] == "ONE_COMPLETE_CANONICAL_S3_ORBIT"
    assert data["coverage_chain"]["base"] == {
        "representatives_certified": 3,
        "representative_coverage": "3/380",
        "certificate": "lab/process/pw2fr2b2b2i2-affine-first-size3-full-evaluator-certificate.json",
    }

    entries = data["coverage_chain"]["entries"]
    assert [entry["coverage_index"] for entry in entries] == list(
        range(4, 4 + len(entries))
    )
    entry = entries[0]
    assert entry["coverage_index"] == 4
    assert entry["representative"] == {
        "owner_pair": [0, 0],
        "quartic_point": [0, 0, 1, 3],
    }
    assert entry["orbit_size"] == 6
    actions = [row["mixed_action"] for row in entry["labels"]]
    assert actions == [
        "-523/144", "-1379/288", "-523/144",
        "-1235/288", "3499/288", "3643/288",
    ]

    heldouts = data["dense_heldout_bank"]
    assert len(heldouts["seeds"]) == 6
    assert heldouts["lattice_exclusion"] == "6/6"
    assert heldouts["closed_nontrivial_S3_orbits"] == "6/6"
    assert heldouts["executed"] == "0/6"

    checks = data["exact_checks"]
    assert checks["selected_orbit_generator_edges"] == "12/12"
    assert checks["selected_orbit_nonself_edges"] == "12/12"
    for key in (
        "geometry_slots", "Phi1_slots", "Phi2_slots", "Hodge_slots",
        "residual_slots", "moving_primalizer_slots", "action_slots",
    ):
        assert checks[key] == "48/48"
    for key in (
        "mixed_residual_liveness", "mixed_primalizer_liveness",
        "mixed_action_liveness", "moving_Hodge_product_rule_controls",
    ):
        assert checks[key] == "6/6"
    assert checks["summary"] == "26 exact + 2 source + 9 type + 7 planted = 44 PASS"

    assert data["constraint_parameter_ledger"]["fitted_parameters"] == 0
    assert data["constraint_parameter_ledger"]["raw_transport_equalities"] == 336
    assert data["admission"]["resumable_coverage_ledger"] == "ADMITTED_APPEND_ONLY"
    assert data["admission"]["dense_universal_heldouts"] == "PREREGISTERED_6__EXECUTED_0"
    assert data["admission"]["complete_I1_A4"] == "NOT_PROMOTED"
    assert data["admission"]["complete_I2B_C4"] == "NOT_PROMOTED"
    assert data["reduction_engine"] == "ADMITTED_NOT_PROMOTED"
    assert data["unconditional_fallback_cells_per_bank"] == 1925
    assert data["external_datum"] == "P1_P2_P3_UNCHANGED_AND_UNUSED"
    assert data["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
    assert data["third_lane_gate"] == "TG-1 AND TG-2 AND TG-3 = NOT_PROMOTED"
    assert "PW2F-R2B2B2I2-RESUMABLE-REMAINING-376-REPRESENTATIVE-FULL-EVALUATOR-COVERAGE-PLUS-EXECUTE-DENSE-HELDOUTS-THEN-SEPARATE-C4-BANKS" in report

    assert all(path.is_file() for path in (PROBE, REPORT, REVIEW))

    for token in (
        "RESUMABLE_LEDGER_CREATED__FIRST_UNCOVERED_SIZE6_CERTIFIED__DURABLE_4_OF_380__UNIVERSAL_376_OPEN__DENSE_HELDOUTS_0_OF_6_EXECUTED",
        "4/380", "other `376` representatives", "0/6` executed",
        "1,925-cell fallback stays live", "-523/144", "3643/288",
        "P1/P2/P3", "FORMALLY_SEPARATE_INSIDE_ERIC_LANE",
        "TG-1 AND TG-2 AND TG-3",
    ):
        assert token in report or token in review, token

    for token in (
        "representative_coverage=4/380",
        "remaining_representatives=376/380",
        "dense_heldouts_preregistered=6/6__executed=0/6",
        "FALLBACK=1925_CELLS_PER_BANK_REMAINS_LIVE",
        "Curt remains FORMALLY_SEPARATE_INSIDE_ERIC_LANE",
        "TG-1 AND TG-2 AND TG-3 remains NOT_PROMOTED",
        "PLANT promote the 380-representative engine from 4/380 coverage",
        "PLANT count preregistered dense heldouts as executed",
    ):
        assert token in probe, token

    combined = "\n".join((report, review)).lower()
    for forbidden in (
        "380-representative engine is promoted", "complete i1 a4 bank passes",
        "complete i2b c4 bank passes", "green/helmholtz is admitted",
        "dense heldouts pass", "curt track merged", "third lane promoted",
        "physics verdict proved",
    ):
        assert forbidden not in combined, forbidden

    print("pw2fr2b2b2i2_resumable_first_size6_scope_audit: PASS")
    print("  append-only 4/380 coverage, heldouts 0/6, remaining 376, live fallback, separate banks, Curt, and TG boundary retained")


if __name__ == "__main__":
    main()
