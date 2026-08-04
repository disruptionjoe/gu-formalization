#!/usr/bin/env python3
"""Fail-closed scope audit for the K77 trace-q ownership/adjoint/Ward packet."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "lab/process/k77-wave2-q-receiver-trace-adjoint-ward-selection.json"
REPORT = ROOT / "explorations/k77-wave2-q-receiver-trace-adjoint-ward-selection-2026-08-04.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-04-k77-wave2-q-receiver-trace-adjoint-ward-review.md"
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

    expected = (
        "PARTIAL__TRACE_REVERSED_TAUTOLOGICAL_Q_GEOMETRY_OWNED__"
        "LEFT_RIGHT_ADJOINT_EXCHANGE_AND_CURRENTS_EXACT__"
        "WARD_DOES_NOT_SELECT_COEFFICIENT__ZERO_ORDER_REALITY_FULL_H_OPEN"
    )
    assert registry["gate_status"] == expected

    source = registry["source_receipt"]
    assert source["trace_reversal"] == "SOURCE_CONFIRMS"
    assert source["distinguished_metric_fibre_direction"] == "SOURCE_CONFIRMS"
    assert source["trace_q_in_d916"] == "SOURCE_SILENT"
    assert source["unique_left_right_selection"] == "SOURCE_SILENT"
    assert "NOT_Q_PLACEMENT_SELECTION" in source["commutator_or_i_anticommutator_freedom"]

    ownership = registry["ownership"]
    assert ownership["free_q"] == "REPLACED_CONDITIONALLY_BY_TAUTOLOGICAL_TRACE_SECTION"
    assert ownership["global_metric_bundle_naturality"] == "EXACT"
    assert ownership["trace_reversal_load_bearing"] is True
    assert ownership["observation_vector_required"] is False
    assert ownership["P1_orientation_required"] is False
    assert ownership["full_fixed_source_group"].startswith("OPEN")

    placement = registry["placement_results"]
    assert placement["left"] == "EXACT_NONZERO"
    assert placement["right"] == "EXACT_NONZERO"
    assert placement["fixture_sensitivity_rank"] == 2
    assert placement["ward_selection_rank"] == 0
    assert placement["unique_coefficient"] == "OPEN"

    surplus = registry["constraint_surplus"]
    assert surplus["prior_free_q_projective_parameters"] == 13
    assert surplus["current_free_q_projective_parameters"] == 0
    assert surplus["left_right_projective_parameters"] == 1
    assert surplus["current_selecting_constraint_rank"] == 0
    assert surplus["surplus"] == -1

    assert registry["exact_fixture"] == {
        "source": 6,
        "type": 20,
        "exact": 25,
        "planted": 5,
        "total": 56,
        "failures": 0,
    }
    assert registry["external_datum"] == {
        "P1": "UNUSED__CANONICAL_RADIAL_TRACE_SECTION_HAS_OWN_SIGN",
        "P2": "UNUSED",
        "P3": "UNUSED",
        "new_q_datum": False,
    }
    assert registry["next_gate"]["id"] == "K77_D916_TRACE_Q_COEFFICIENT_ZERO_ORDER_REALITY_SELECTION"
    assert registry["next_gate"]["wave3_admitted"] is False
    assert all(value is False for value in registry["status_boundary"].values())

    wave2 = campaign["waves"][1]
    frontier = campaign["frontier"]
    assert wave2["status"] == expected
    assert wave2["result_ref"].endswith("k77-wave2-q-receiver-trace-adjoint-ward-selection-2026-08-04.md")
    for token in (
        "TAUTOLOGICAL_TRACE_Q_GEOMETRY_OWNER",
        "LEFT_RIGHT_MULTIINDEX_KREIN_ADJOINT_EXCHANGE",
        "WARD_COEFFICIENT_SELECTION_RANK_ZERO",
        "Q_RECEIVER_CONSTRAINT_SURPLUS_IMPROVED_TO_MINUS_1",
    ):
        assert token in wave2["emitted"]
    assert "TRACE_Q_LEFT_RIGHT_COEFFICIENT_SELECTION" in wave2["carried_debt"]
    assert frontier["completed_waves"] == [1]
    assert frontier["partial_waves"] == [2]
    assert frontier["next_wave"] == 2
    assert frontier["next_required_build"] == "K77_D916_TRACE_Q_COEFFICIENT_ZERO_ORDER_REALITY_SELECTION"

    for token in (
        "q_g=\\frac12g",
        "13 -> 0",
        "-14 -> -1",
        "ward covariance cannot choose the placement",
        "source-silent",
        "p1 is not consumed",
        "wave 3 does not open",
    ):
        assert token in report, f"missing report token: {token}"

    for token in (
        "repaired_partial__trace_q_owns_receiver__ward_leaves_one_coefficient",
        "floating inversion",
        "actual even spin-connection generator",
        "coefficient/lie-algebra factor",
        "surplus is `-1`",
        "p1/p2/p3: unused",
        "wave 3: not admitted",
    ):
        assert token in review, f"missing review token: {token}"

    print("k77_wave2_q_receiver_trace_adjoint_ward_scope_audit: PASS")
    print("  trace-reversed tautological q is geometry-owned conditionally; adjoint/currents are exact; Ward leaves one coefficient and Wave 2 remains partial")


if __name__ == "__main__":
    main()
