#!/usr/bin/env python3
"""Fail-closed scope audit for the actual-carrier D916 rival packet."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "lab/process/k77-wave2-actual-draft916-blockwise-adjoint-descent.json"
REPORT = ROOT / "explorations/k77-wave2-actual-draft916-k77-blockwise-adjoint-descent-2026-08-04.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-04-k77-wave2-actual-draft916-blockwise-review.md"
SOURCE = ROOT / "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md"
CAMPAIGN = ROOT / "lab/process/k77-post-b2-next-eight-wave-campaign.json"


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)


def normalized(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def main() -> None:
    registry = load_json(REGISTRY)
    campaign = load_json(CAMPAIGN)
    report = normalized(REPORT)
    review = normalized(REVIEW)
    source = normalized(SOURCE)

    expected_status = (
        "PARTIAL__CONDITIONAL_TOTAL_GRADED_D916_RIVAL_BUILT__"
        "SOURCE_SIGN_IDENTIFICATION_FULL_CONNECTION_VARIATION_AND_FULL_H_DESCENT_OPEN"
    )
    assert registry["gate_status"] == expected_status

    receipt = registry["source_receipt"]
    assert receipt["section_112_page"] == 51
    assert receipt["section_112_field_signs"] == "SOURCE_STATES_AMBIENT_HALF_SPINOR"
    assert receipt["shia_b_family"].endswith("PREFERRED_SELECTION_NOT_LOCATED")

    collision = registry["source_sign_collision"]
    assert collision["selected_ambient_j_parities"] == {
        "PHI_D": -1,
        "D": 1,
        "MINUS_D_TIMES": 1,
    }
    assert collision["uniform_same_or_cross_row_duality_solutions"] == 0
    assert collision["disposition"].endswith("SOURCE_IDENTIFICATION_NOT_ESTABLISHED")

    built = registry["built_now"]
    assert built["rolled_auxiliary_grading"] == "BALANCED_960_960"
    assert built["formal_adjoint"].endswith("FULL_PHI_D_MULTIINDEX_OPEN")
    assert built["current"].endswith("COMPLETE_SHARED_CORE_OPEN")
    assert built["superig"].endswith("FULL_H_OPEN")

    correction = registry["superig_correction"]
    assert correction["failure"] == "NONCOMPACT_SPIN_EQUIVARIANCE_DEFECT"
    assert correction["repair"] == "INVERSE_TRACE_METRIC_WEIGHTS_MINUS_ETA_A_ETA_B"
    assert correction["full_source_h_descent"] == "OPEN"

    fixture = registry["exact_fixture"]
    assert fixture == {
        "source": 8,
        "type": 23,
        "exact": 39,
        "planted": 9,
        "total": 79,
        "failures": 0,
    }

    next_gate = registry["next_gate"]
    assert next_gate["id"] == "K77_D916_SOURCE_SIGN_DUALITY_SHIAB_PARITY_RECONCILIATION"
    assert len(next_gate["branches"]) == 3
    assert next_gate["wave3_admitted"] is False
    assert len(registry["remaining_wave2_burden"]) == 6

    assert registry["review_contract"]["hostile_review"] == "COMPLETE__MATERIAL_SCOPE_REPAIR__WAVE2_PARTIAL"
    assert registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"}
    assert all(value is False for value in registry["status_boundary"].values())

    wave2 = campaign["waves"][1]
    frontier = campaign["frontier"]
    assert wave2["status"] == expected_status
    assert frontier["completed_waves"] == [1]
    assert frontier["partial_waves"] == [2]
    assert frontier["next_wave"] == 2
    assert frontier["next_required_build"] == "K77_D916_SOURCE_SIGN_DUALITY_SHIAB_PARITY_RECONCILIATION"

    for token in (
        "smallest exact reason",
        "section 11.2 explicitly places",
        "no value of `kappa` fits",
        "inverse trace metric",
        "one nontrivial real-spin connection direction",
        "wave 2 remains",
        "p1/p2/p3 use",
    ):
        assert token in report, f"missing report token: {token}"

    for token in (
        "repaired_partial__conditional_rival_passes",
        "reverses the one-form labels",
        "no convention fits",
        "fails exact noncompact generators",
        "complete shared-core rederivation",
        "8 source + 23 type + 39 exact + 9 planted = 79 pass",
    ):
        assert token in review, f"missing review token: {token}"

    for token in (
        "section 11.2",
        "zeta_minus in omega1(s_minus)",
        "layer0-collision / not-established",
        "construction-selected-rival",
    ):
        assert token in source, f"missing source token: {token}"

    print("k77_wave2_actual_draft916_blockwise_scope_audit: PASS")
    print("  conditional total-graded rival retained; source-sign reconciliation, complete common variation, full-H descent, observation, physics, and datum use remain open")


if __name__ == "__main__":
    main()
