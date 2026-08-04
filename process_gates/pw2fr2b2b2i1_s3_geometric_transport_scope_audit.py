#!/usr/bin/env python3
"""Fail-closed scope audit for the R2B2B2I1 S3 geometric certificate."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "lab/process/pw2fr2b2b2i1-s3-geometric-transport-certificate.json"
REPORT = ROOT / "explorations/pw2fr2b2b2i1-s3-geometric-transport-certificate-2026-08-04.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-04-pw2fr2b2b2i1-review.md"
PROBE = ROOT / "tests/channel-swings/pw2fr2b2b2i1_s3_geometric_transport_probe.py"
CAMPAIGN = ROOT / "lab/process/eric-curt-ten-wave-campaign.json"


def main() -> None:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    campaign = json.loads(CAMPAIGN.read_text(encoding="utf-8"))
    report = REPORT.read_text(encoding="utf-8")
    review = REVIEW.read_text(encoding="utf-8")
    probe = PROBE.read_text(encoding="utf-8")

    assert data["status"] == "BOTH_S3_GENERATORS_CERTIFIED_ON_UNIVERSAL_OWNER_CONORMAL_GEOMETRIC_TRANSPORT_LAYER"
    counts = data["universal_counts"]
    assert counts["metric_owners"] == 10
    assert counts["ordered_first_dewitt_owner_derivatives"] == 10
    assert counts["ordered_second_dewitt_owner_derivatives"] == 100
    assert counts["owner_conormal_connection_generators"] == 40
    assert counts["normalized_trace_owner_directions"] == 10
    assert counts["quartic_monomials"] == 35
    assert counts["symmetric_owner_pairs"] == 55
    assert counts["joint_labels"] == 1925
    assert data["joint_orbit_census"] == {"1": 2, "3": 115, "6": 263}
    assert data["burnside_fixed_counts"] == {
        "identity": 1925,
        "each_of_three_transpositions": 117,
        "each_of_two_three_cycles": 2,
    }
    assert data["candidate_representatives_per_bank"] == 380
    assert data["candidate_reduction"] == 1545
    assert data["unconditional_fallback_cells_per_bank"] == 1925

    admission = data["admission"]
    assert admission["finite_S3_action"] == "ADMITTED"
    assert admission["universal_owner_conormal_geometric_transport"] == "CERTIFIED"
    assert admission["Phi_Hodge_Shiab_transport"] == "NOT_UNIVERSALLY_CERTIFIED"
    assert admission["residual_primalizer_action_transport"] == "NOT_UNIVERSALLY_CERTIFIED"
    assert admission["complete_I1_A4"] == "NOT_PROMOTED"
    assert admission["complete_I2B_C4"] == "NOT_PROMOTED"
    assert admission["multiindex_Green_Helmholtz"] == "NOT_ADMITTED"
    assert data["reduction_engine"] == "ADMITTED_NOT_PROMOTED"
    assert data["external_datum"] == "P1_P2_P3_UNCHANGED_AND_UNUSED"
    assert data["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
    assert data["third_lane_gate"] == "TG-1 AND TG-2 AND TG-3 = NOT_PROMOTED"
    assert data["next_gate"] == "PW2F-R2B2B2I1-REMAINING-EVALUATOR-LAYERS-ON-ORBIT-REPRESENTATIVES-PLUS-DENSE-HELDOUTS-THEN-SEPARATE-C4-BANKS"

    evidence = data["evidence"]
    assert evidence["probe"] == PROBE.relative_to(ROOT).as_posix()
    assert evidence["exploration"] == REPORT.relative_to(ROOT).as_posix()
    assert evidence["hostile_review"] == REVIEW.relative_to(ROOT).as_posix()
    assert evidence["scope_audit"] == Path(__file__).relative_to(ROOT).as_posix()

    checkpoint = campaign["latest_successor_checkpoint"]
    for key in ("gate", "status", "curt_track", "third_lane_gate", "next_gate"):
        assert checkpoint[key] == data[key]
    assert checkpoint["external_datum"] == "P1/P2/P3 UNCHANGED AND UNUSED"
    assert "1,925-cell fallback remains live" in checkpoint["scope"]
    assert "unbuilt and unpromoted" in checkpoint["scope"]

    required_tokens = (
        "BOTH_S3_GENERATORS_CERTIFIED_ON_UNIVERSAL_OWNER_CONORMAL_GEOMETRIC_TRANSPORT_LAYER",
        "{1:2, 3:115, 6:263}",
        "1,925-cell fallback remains live",
        "Phi`/Hodge/Shiab, residual, moving primalizer",
        "P1/P2/P3 remain unchanged and unused",
        "FORMALLY_SEPARATE_INSIDE_ERIC_LANE",
        "TG-1 AND TG-2 AND TG-3",
    )
    for token in required_tokens:
        assert token in report or token in review, token

    for token in (
        "candidate_representatives_per_bank",
        "drop the 1,925-cell fallback before remaining evaluator-layer certification",
        "Phi/Hodge/Shiab/residual/primalizer/action equivariance remains unexecuted",
        "I1 A4 and I2B C4 remain separate, incomplete",
        "Curt remains FORMALLY_SEPARATE_INSIDE_ERIC_LANE",
        "TG-1 AND TG-2 AND TG-3 remains NOT_PROMOTED",
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

    print("pw2fr2b2b2i1_s3_geometric_transport_scope_audit: PASS")
    print("  S3 geometry, live fallback, open evaluator layers, separate banks, Curt, and TG boundary retained")


if __name__ == "__main__":
    main()
