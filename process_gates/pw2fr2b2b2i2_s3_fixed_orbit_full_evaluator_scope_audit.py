#!/usr/bin/env python3
"""Fail-closed scope audit for the R2B2B2I2 fixed-orbit certificate."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "lab/process/pw2fr2b2b2i2-s3-fixed-orbit-full-evaluator-certificate.json"
REPORT = ROOT / "explorations/pw2fr2b2b2i2-s3-fixed-orbit-full-evaluator-certificate-2026-08-05.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-05-pw2fr2b2b2i2-fixed-orbit-review.md"
PROBE = ROOT / "tests/channel-swings/pw2fr2b2b2i2_s3_fixed_orbit_full_evaluator_probe.py"
CAMPAIGN = ROOT / "lab/process/eric-curt-ten-wave-campaign.json"
COUNCIL = ROOT / "lab/process/post-b2c15r3-multidisciplinary-council-next-ten-waves.json"


def main() -> None:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    campaign = json.loads(CAMPAIGN.read_text(encoding="utf-8"))
    council = json.loads(COUNCIL.read_text(encoding="utf-8"))
    report = REPORT.read_text(encoding="utf-8")
    review = REVIEW.read_text(encoding="utf-8")
    probe = PROBE.read_text(encoding="utf-8")

    assert data["status"] == "FULL_EVALUATOR_CERTIFIED_ON_COMPLETE_S3_FIXED_ORBIT_STRATUM__UNIVERSAL_378_OPEN"
    assert data["gate"] == "PW2F-R2B2B2I2-S3-FIXED-ORBIT-FULL-EVALUATOR"
    assert data["run_id"] == "RUN-20260805-054616-gu-formalization-pw2fr2b2b2i2-fixed-orbit-full-evaluator"

    coverage = data["coverage"]
    assert coverage == {
        "joint_labels": 1925,
        "canonical_representatives": 380,
        "fixed_orbit_representatives": 2,
        "fixed_orbit_representatives_certified": 2,
        "remaining_representatives": 378,
        "representative_coverage": "2/380",
        "fixed_orbit_coverage": "2/2",
    }
    assert data["fixed_representatives"] == [
        {
            "owner_pair": [9, 9],
            "quartic_point": [0, 0, 0, 4],
            "mixed_action": "215/8",
        },
        {
            "owner_pair": [9, 9],
            "quartic_point": [1, 1, 1, 1],
            "mixed_action": "87/16",
        },
    ]

    checks = data["exact_checks"]
    for key in (
        "geometry_slots",
        "Phi1_slots",
        "Phi2_slots",
        "Hodge_slots",
        "residual_slots",
        "moving_primalizer_slots",
        "action_slots",
    ):
        assert checks[key] == "16/16"
    assert checks["mixed_residual_liveness"] == "2/2"
    assert checks["mixed_primalizer_liveness"] == "2/2"
    assert checks["mixed_action_liveness"] == "2/2"
    assert checks["moving_Hodge_product_rule_controls"] == "2/2"
    assert checks["old_forward_lift_control"] == "PASS"
    assert checks["summary"] == "19 exact + 2 source + 8 type + 6 planted = 35 PASS"

    ledger = data["constraint_parameter_ledger"]
    assert ledger["fitted_parameters"] == 0
    assert ledger["raw_transport_equalities"] == 112
    assert ledger["independent_constraint_rank"] == "NOT_COMPUTED"
    assert ledger["physical_surplus"] == "NOT_APPLICABLE_AT_EVALUATOR_TRANSPORT_SCOPE"

    admission = data["admission"]
    assert admission["fixed_orbit_full_evaluator_transport"] == "CERTIFIED_2_OF_2_FIXED_REPRESENTATIVES"
    assert admission["remaining_full_evaluator_transport"] == "OPEN_378_OF_380_REPRESENTATIVES"
    assert admission["complete_I1_A4"] == "NOT_PROMOTED"
    assert admission["complete_I2B_C4"] == "NOT_PROMOTED"
    assert admission["multiindex_Green_Helmholtz"] == "NOT_ADMITTED"
    assert data["reduction_engine"] == "ADMITTED_NOT_PROMOTED"
    assert data["unconditional_fallback_cells_per_bank"] == 1925
    assert data["external_datum"] == "P1_P2_P3_UNCHANGED_AND_UNUSED"
    assert data["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
    assert data["third_lane_gate"] == "TG-1 AND TG-2 AND TG-3 = NOT_PROMOTED"
    assert data["next_gate"] == "PW2F-R2B2B2I2-RESUMABLE-REMAINING-378-REPRESENTATIVE-FULL-EVALUATOR-COVERAGE-THEN-SEPARATE-C4-BANKS"

    evidence = data["evidence"]
    assert evidence["probe"] == PROBE.relative_to(ROOT).as_posix()
    assert evidence["exploration"] == REPORT.relative_to(ROOT).as_posix()
    assert evidence["hostile_review"] == REVIEW.relative_to(ROOT).as_posix()
    assert evidence["scope_audit"] == Path(__file__).relative_to(ROOT).as_posix()

    for checkpoint in (
        campaign["latest_successor_checkpoint"],
        council["latest_successor_checkpoint"],
    ):
        for key in ("gate", "status", "curt_track", "third_lane_gate", "next_gate"):
            assert checkpoint[key] == data[key]
        assert checkpoint["external_datum"] == "P1/P2/P3 UNCHANGED AND UNUSED"
        assert "2/380" in checkpoint["scope"]
        assert "378" in checkpoint["scope"]
        assert "1,925-cell fallback remains live" in checkpoint["scope"]

    required_tokens = (
        "FULL_EVALUATOR_CERTIFIED_ON_COMPLETE_S3_FIXED_ORBIT_STRATUM__UNIVERSAL_378_OPEN",
        "2/380",
        "other `378` remain open",
        "1,925-cell fallback stays live",
        "215/8",
        "87/16",
        "P1/P2/P3 remain unchanged and unused",
        "FORMALLY_SEPARATE_INSIDE_ERIC_LANE",
        "TG-1 AND TG-2 AND TG-3",
    )
    for token in required_tokens:
        assert token in report or token in review, token

    for token in (
        "representative_coverage=2/380",
        "remaining_representatives=378/380",
        "FALLBACK=1925_CELLS_PER_BANK_REMAINS_LIVE",
        "Curt remains FORMALLY_SEPARATE_INSIDE_ERIC_LANE",
        "TG-1 AND TG-2 AND TG-3 remains NOT_PROMOTED",
        "PLANT promote the 380-representative engine from 2/380 coverage",
        "PLANT replace the 1,925-cell fallback before the other 378 representatives",
    ):
        assert token in probe, token

    combined = "\n".join((report, review)).lower()
    for forbidden in (
        "380-representative engine is promoted",
        "complete i1 a4 bank passes",
        "complete i2b c4 bank passes",
        "green/helmholtz is admitted",
        "curt track merged",
        "third lane promoted",
        "physics verdict proved",
    ):
        assert forbidden not in combined, forbidden

    print("pw2fr2b2b2i2_s3_fixed_orbit_full_evaluator_scope_audit: PASS")
    print("  2/380 fixed stratum, remaining 378, live fallback, separate banks, Curt, and TG boundary retained")


if __name__ == "__main__":
    main()
