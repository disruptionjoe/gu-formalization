#!/usr/bin/env python3
"""Fail-closed scope audit for the I2 affine and first-size-three certificate."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "lab/process/pw2fr2b2b2i2-affine-first-size3-full-evaluator-certificate.json"
REPORT = ROOT / "explorations/pw2fr2b2b2i2-affine-first-size3-full-evaluator-certificate-2026-08-05.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-05-pw2fr2b2b2i2-affine-first-size3-review.md"
PROBE = ROOT / "tests/channel-swings/pw2fr2b2b2i2_affine_first_size3_full_evaluator_probe.py"
CAMPAIGN = ROOT / "lab/process/eric-curt-ten-wave-campaign.json"
COUNCIL = ROOT / "lab/process/post-b2c15r3-multidisciplinary-council-next-ten-waves.json"


def main() -> None:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    campaign = json.loads(CAMPAIGN.read_text(encoding="utf-8"))
    council = json.loads(COUNCIL.read_text(encoding="utf-8"))
    report = REPORT.read_text(encoding="utf-8")
    review = REVIEW.read_text(encoding="utf-8")
    probe = PROBE.read_text(encoding="utf-8")

    assert data["gate"] == "PW2F-R2B2B2I2-AFFINE-FIRST-MOVING-FIRST-SIZE3-FULL-EVALUATOR"
    assert data["status"] == "AFFINE_FIRST_MOVING_CERTIFIED__FIRST_SIZE3_ORBIT_CERTIFIED__DURABLE_3_OF_380__UNIVERSAL_377_OPEN"
    assert data["run_id"] == "historical-investigation"
    assert data["coverage"] == {
        "joint_labels": 1925,
        "canonical_representatives": 380,
        "fixed_representatives_predecessor": 2,
        "size_three_representatives_total": 115,
        "new_size_three_representatives_certified": 1,
        "durable_representatives_certified": 3,
        "remaining_representatives": 377,
        "representative_coverage": "3/380",
        "selected_orbit_coverage": "3/3_LABELS",
    }

    affine = data["affine_first_moving"]
    for key, expected in {
        "basis_cases": "50/50",
        "dense_affine_span_controls": "2/2",
        "generator_edges": "100/100",
        "geometry_edges": "100/100",
        "moving_shiab_family_edges": "800/800",
        "residual_edges": "100/100",
        "moving_primalizer_edges": "100/100",
        "action_derivative_edges": "100/100",
        "trace_nonzero_cases": "50/50",
        "action_nonzero_cases": "20/50",
        "old_forward_lift_control": "PASS",
    }.items():
        assert affine[key] == expected

    assert data["selected_size3_orbit"]["representative"] == {
        "owner_pair": [0, 0],
        "quartic_point": [0, 0, 0, 4],
    }
    assert [row["mixed_action"] for row in data["selected_size3_orbit"]["labels"]] == [
        "-727/144", "-727/144", "107/9"
    ]

    checks = data["exact_checks"]
    assert checks["selected_orbit_generator_edges"] == "6/6"
    assert checks["selected_orbit_nonself_edges"] == "5/6"
    for key in ("geometry_slots", "Phi1_slots", "Phi2_slots", "Hodge_slots", "residual_slots", "moving_primalizer_slots", "action_slots"):
        assert checks[key] == "24/24"
    for key in ("mixed_residual_liveness", "mixed_primalizer_liveness", "mixed_action_liveness", "moving_Hodge_product_rule_controls"):
        assert checks[key] == "3/3"
    assert checks["summary"] == "33 exact + 2 source + 9 type + 7 planted = 51 PASS"

    assert data["constraint_parameter_ledger"]["fitted_parameters"] == 0
    assert data["constraint_parameter_ledger"]["raw_transport_equalities"] == 1368
    assert data["admission"]["remaining_full_evaluator_transport"] == "OPEN_377_OF_380_REPRESENTATIVES"
    assert data["admission"]["complete_I1_A4"] == "NOT_PROMOTED"
    assert data["admission"]["complete_I2B_C4"] == "NOT_PROMOTED"
    assert data["reduction_engine"] == "ADMITTED_NOT_PROMOTED"
    assert data["unconditional_fallback_cells_per_bank"] == 1925
    assert data["external_datum"] == "P1_P2_P3_UNCHANGED_AND_UNUSED"
    assert data["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
    assert data["third_lane_gate"] == "TG-1 AND TG-2 AND TG-3 = NOT_PROMOTED"
    assert data["next_gate"].endswith("REMAINING-377-REPRESENTATIVE-FULL-EVALUATOR-COVERAGE-THEN-SEPARATE-C4-BANKS")

    evidence = data["evidence"]
    assert evidence["probe"] == PROBE.relative_to(ROOT).as_posix()
    assert evidence["exploration"] == REPORT.relative_to(ROOT).as_posix()
    assert evidence["hostile_review"] == REVIEW.relative_to(ROOT).as_posix()
    assert evidence["scope_audit"] == Path(__file__).relative_to(ROOT).as_posix()

    for checkpoint in (campaign["latest_successor_checkpoint"], council["latest_successor_checkpoint"]):
        for key in ("gate", "status", "curt_track", "third_lane_gate", "next_gate"):
            assert checkpoint[key] == data[key]
        assert checkpoint["external_datum"] == "P1/P2/P3 UNCHANGED AND UNUSED"
        assert "3/380" in checkpoint["scope"]
        assert "377" in checkpoint["scope"]
        assert "1,925-cell fallback remains live" in checkpoint["scope"]

    for token in (
        "3/380", "other `377` representatives", "1,925-cell fallback stays live",
        "-727/144", "107/9", "P1/P2/P3 remain unchanged and unused",
        "FORMALLY_SEPARATE_INSIDE_ERIC_LANE", "TG-1 AND TG-2 AND TG-3",
    ):
        assert token in report or token in review, token

    for token in (
        "representative_coverage=3/380",
        "remaining_representatives=377/380",
        "FALLBACK=1925_CELLS_PER_BANK_REMAINS_LIVE",
        "Curt remains FORMALLY_SEPARATE_INSIDE_ERIC_LANE",
        "TG-1 AND TG-2 AND TG-3 remains NOT_PROMOTED",
        "PLANT promote the 380-representative engine from 3/380 coverage",
        "PLANT replace the 1,925-cell fallback before the other 377 representatives",
    ):
        assert token in probe, token

    combined = "\n".join((report, review)).lower()
    for forbidden in (
        "380-representative engine is promoted", "complete i1 a4 bank passes",
        "complete i2b c4 bank passes", "green/helmholtz is admitted",
        "curt track merged", "third lane promoted", "physics verdict proved",
    ):
        assert forbidden not in combined, forbidden

    print("pw2fr2b2b2i2_affine_first_size3_full_evaluator_scope_audit: PASS")
    print("  affine layer, 3/380 coverage, remaining 377, live fallback, separate banks, Curt, and TG boundary retained")


if __name__ == "__main__":
    main()
