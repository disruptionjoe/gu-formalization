#!/usr/bin/env python3
"""Fail-closed scope audit for the I2 resumable third-size-six certificate."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "lab/process/pw2fr2b2b2i2-resumable-full-evaluator-coverage.json"
REPORT = ROOT / "explorations/pw2fr2b2b2i2-resumable-third-size6-full-evaluator-certificate-2026-08-05.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-05-pw2fr2b2b2i2-resumable-third-size6-review.md"
PROBE = ROOT / "tests/channel-swings/pw2fr2b2b2i2_resumable_third_size6_full_evaluator_probe.py"
CAMPAIGN = ROOT / "lab/process/eric-curt-ten-wave-campaign.json"
COUNCIL = ROOT / "lab/process/post-b2c15r3-multidisciplinary-council-next-ten-waves.json"


def main() -> None:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    campaign = json.loads(CAMPAIGN.read_text(encoding="utf-8"))
    council = json.loads(COUNCIL.read_text(encoding="utf-8"))
    report = REPORT.read_text(encoding="utf-8")
    review = REVIEW.read_text(encoding="utf-8")
    probe = PROBE.read_text(encoding="utf-8")

    assert data["gate"] == "PW2F-R2B2B2I2-RESUMABLE-THIRD-UNCOVERED-SIZE6-FULL-EVALUATOR"
    assert data["status"] == "THIRD_UNCOVERED_SIZE6_CERTIFIED__DURABLE_6_OF_380__UNIVERSAL_374_OPEN__DENSE_HELDOUTS_0_OF_6_EXECUTED"
    assert data["run_id"] == "historical-investigation"
    assert data["resumption_contract"]["next_resume_index"] == 6
    assert data["resumption_contract"]["shard_unit"] == "ONE_COMPLETE_CANONICAL_S3_ORBIT"
    assert data["coverage"] == {
        "joint_labels": 1925,
        "canonical_representatives": 380,
        "durable_representatives_predecessor": 5,
        "new_size_six_representatives_certified": 1,
        "durable_representatives_certified": 6,
        "remaining_representatives": 374,
        "representative_coverage": "6/380",
        "selected_orbit_coverage": "6/6_LABELS",
        "dense_heldouts_preregistered": 6,
        "dense_heldouts_executed": 0,
    }

    entries = data["coverage_chain"]["entries"]
    assert len(entries) == 3
    assert [entry["coverage_index"] for entry in entries] == [4, 5, 6]
    assert entries[0]["representative"] == {
        "owner_pair": [0, 0],
        "quartic_point": [0, 0, 1, 3],
    }
    assert [row["mixed_action"] for row in entries[0]["labels"]] == [
        "-523/144", "-1379/288", "-523/144",
        "-1235/288", "3499/288", "3643/288",
    ]
    assert entries[1]["representative"] == {
        "owner_pair": [0, 0],
        "quartic_point": [0, 0, 2, 2],
    }
    assert [row["mixed_action"] for row in entries[1]["labels"]] == [
        "-31/144", "-697/144", "-31/144",
        "-409/144", "871/72", "1015/72",
    ]

    entry = entries[2]
    assert entry["representative"] == {
        "owner_pair": [0, 0],
        "quartic_point": [0, 0, 3, 1],
    }
    assert entry["orbit_size"] == 6
    assert entry["predecessor_ledger_revision"] == "93fb3c01d4c4ab40d6d4035bdd6063aae8dcdfab"
    assert entry["predecessor_ledger_sha256"] == "2f7a2aad5d1d76dd544d2bba5454ecaea1c905bea4685e2b05cda9f1917b8c9d"
    assert [row["mixed_action"] for row in entry["labels"]] == [
        "749/144", "-1499/288", "749/144",
        "-203/288", "3379/288", "4675/288",
    ]

    heldouts = data["dense_heldout_bank"]
    assert len(heldouts["seeds"]) == 6
    assert heldouts["lattice_exclusion"] == "6/6"
    assert heldouts["closed_nontrivial_S3_orbits"] == "6/6"
    assert heldouts["executed"] == "0/6"

    checks = data["exact_checks"]
    assert checks["dependency_hashes"] == "2/2"
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
    assert checks["mixed_action_fingerprint"] == [
        "749/144", "-1499/288", "749/144", "-203/288", "3379/288", "4675/288",
    ]
    assert checks["summary"] == "26 exact + 2 source + 9 type + 7 planted = 44 PASS"

    assert data["constraint_parameter_ledger"]["fitted_parameters"] == 0
    assert data["constraint_parameter_ledger"]["raw_transport_equalities"] == 336
    assert data["admission"]["remaining_full_evaluator_transport"] == "OPEN_374_OF_380_REPRESENTATIVES"
    assert data["admission"]["dense_universal_heldouts"] == "PREREGISTERED_6__EXECUTED_0"
    assert data["admission"]["complete_I1_A4"] == "NOT_PROMOTED"
    assert data["admission"]["complete_I2B_C4"] == "NOT_PROMOTED"
    assert data["reduction_engine"] == "ADMITTED_NOT_PROMOTED"
    assert data["unconditional_fallback_cells_per_bank"] == 1925
    assert data["external_datum"] == "P1_P2_P3_UNCHANGED_AND_UNUSED"
    assert data["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
    assert data["third_lane_gate"] == "TG-1 AND TG-2 AND TG-3 = NOT_PROMOTED"
    assert data["next_gate"].endswith("REMAINING-374-REPRESENTATIVE-FULL-EVALUATOR-COVERAGE-PLUS-EXECUTE-DENSE-HELDOUTS-THEN-SEPARATE-C4-BANKS")

    evidence = data["evidence"]
    assert evidence["probe"] == PROBE.relative_to(ROOT).as_posix()
    assert evidence["exploration"] == REPORT.relative_to(ROOT).as_posix()
    assert evidence["hostile_review"] == REVIEW.relative_to(ROOT).as_posix()
    assert evidence["scope_audit"] == Path(__file__).relative_to(ROOT).as_posix()

    for checkpoint in (campaign["latest_successor_checkpoint"], council["latest_successor_checkpoint"]):
        for key in ("gate", "status", "curt_track", "third_lane_gate", "next_gate"):
            assert checkpoint[key] == data[key]
        assert checkpoint["external_datum"] == "P1/P2/P3 UNCHANGED AND UNUSED"
        assert "6/380" in checkpoint["scope"]
        assert "374" in checkpoint["scope"]
        assert "heldout" in checkpoint["scope"]
        assert "1,925-cell fallback remains live" in checkpoint["scope"]

    for token in (
        "6/380", "other `374`", "0/6` executed", "1,925-cell fallback stays live",
        "749/144", "4675/288", "P1/P2/P3",
        "FORMALLY_SEPARATE_INSIDE_ERIC_LANE", "TG-1 AND TG-2 AND TG-3",
    ):
        assert token in report or token in review, token

    for token in (
        "representative_coverage=6/380", "remaining_representatives=374/380",
        "dense_heldouts_preregistered=6/6__executed=0/6",
        "FALLBACK=1925_CELLS_PER_BANK_REMAINS_LIVE",
        "Curt remains FORMALLY_SEPARATE_INSIDE_ERIC_LANE",
        "TG-1 AND TG-2 AND TG-3 remains NOT_PROMOTED",
        "PLANT promote the 380-representative engine from partial coverage",
        "PLANT count frozen dense heldouts as executed",
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

    print("pw2fr2b2b2i2_resumable_third_size6_scope_audit: PASS")
    print("  append-only 6/380 coverage, heldouts 0/6, remaining 374, live fallback, separate banks, Curt, and TG boundary retained")


if __name__ == "__main__":
    main()
