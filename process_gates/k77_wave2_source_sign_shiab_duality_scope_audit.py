#!/usr/bin/env python3
"""Fail-closed scope audit for the K77 source-sign reconciliation packet."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "lab/process/k77-wave2-source-sign-shiab-duality-reconciliation.json"
REPORT = ROOT / "explorations/k77-wave2-source-sign-shiab-duality-reconciliation-2026-08-04.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-04-k77-wave2-source-sign-shiab-duality-review.md"
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

    expected = (
        "PARTIAL__NATIVE_EVEN_SHIAB_HOM0__DEGREE_REALITY_SAT_REQUIRES_ONE_ODD_COVECTOR__"
        "EXACT_Q_REPAIRS_BUILT__OWNERSHIP_ADJOINT_WARD_OPEN"
    )
    assert registry["gate_status"] == expected

    receipt = registry["source_receipt"]
    assert receipt["toe_2025_contraction_2_to_1_then_star"] == "SOURCE_CONFIRMS"
    assert receipt["toe_2025_cyclic_d_squared"] == "SOURCE_UNRELEASED"
    assert receipt["released_sign_correction"] == "SOURCE_SILENT"

    branches = registry["branch_results"]
    native = branches["native_ambient_even_shiab"]
    assert native["complex_hom_same_half"] == 0
    assert native["complex_hom_opposite_half"] == 2
    degree = branches["degree_sensitive_duality_reality"]
    assert degree["barred_row_only_solutions"] == 0
    assert degree["full_row_and_column_sign_solutions"] == 2
    assert degree["bare_half_spinor_flip_hom"] == 0
    assert degree["vector_supplied_half_spinor_flip_hom"] == 1
    q = branches["additional_odd_covector"]
    assert q["fixture_span_dimension"] == 2
    assert q["moving_transition"] == "PASS"
    assert q["fixed_q_transition_plant"] == "FAILS_AS_REQUIRED"

    surplus = registry["constraint_surplus"]
    assert surplus["surplus"] == -14
    assert surplus["current_selecting_constraint_rank"] == 0

    fixture = registry["exact_fixture"]
    assert fixture == {
        "source": 7,
        "type": 15,
        "exact": 22,
        "planted": 5,
        "total": 49,
        "failures": 0,
        "sage_version": "10.9",
    }

    assert registry["review_contract"]["hostile_review"] == "COMPLETE__ONE_MATERIAL_LAYER0_REPAIR"
    assert registry["external_datum"] == {
        "P1": "UNUSED__CAN_ORIENT_ONLY_AFTER_Q_LINE_EXISTS",
        "P2": "UNUSED__Q_LINE_IS_RECEIVER_HYPOTHESIS_NOT_IDENTIFICATION",
        "P3": "UNUSED",
    }
    assert registry["next_gate"]["id"] == "K77_D916_Q_RECEIVER_OWNERSHIP_ADJOINT_WARD_SELECTION"
    assert registry["next_gate"]["wave3_admitted"] is False
    assert all(value is False for value in registry["status_boundary"].values())

    wave2 = campaign["waves"][1]
    frontier = campaign["frontier"]
    assert wave2["status"] == expected
    assert wave2["result_ref"].endswith("k77-wave2-source-sign-shiab-duality-reconciliation-2026-08-04.md")
    assert "SOURCE_NATIVE_EVEN_SHIAB_D7_HOM_ZERO" in wave2["emitted"]
    assert "Q_RECEIVER_OWNERSHIP_AND_DEGREE_REALITY_VS_LEFT_RIGHT_SHIAB_PLACEMENT" in wave2["carried_debt"]
    assert frontier["completed_waves"] == [1]
    assert frontier["partial_waves"] == [2]
    assert frontier["next_wave"] == 2
    assert frontier["next_required_build"] == "K77_D916_Q_RECEIVER_OWNERSHIP_ADJOINT_WARD_SELECTION"

    for token in (
        "three-way fork",
        "dim hom(lambda2 v tensor s+, v tensor s+) = 0",
        "exactly two sign solutions",
        "same `q`-type object",
        "surplus is `-14`",
        "p1 is not consumed here",
        "wave 3 does not open",
    ):
        assert token in report, f"missing report token: {token}"

    for token in (
        "repaired_partial__three_branches_converge_on_one_q_type_receiver",
        "allowing both row and column degree conventions yields two exact solutions",
        "fixed-`q` transition plant fails",
        "summary outruns the executable artifact",
        "actual pushed gu commit",
        "p1/p2/p3: unused",
    ):
        assert token in review, f"missing review token: {token}"

    for token in (
        "successor collision: the released 2025 spoken explanation",
        "source-corrects-signs: none found",
        "contracted back to a one-form",
        "additional moving odd tensor",
    ):
        assert token in source, f"missing source token: {token}"

    print("k77_wave2_source_sign_shiab_duality_scope_audit: PASS")
    print("  native even Hom=0; full degree-reality SAT and modified Shiab converge on one source-unowned moving odd covector; Wave 2 remains partial")


if __name__ == "__main__":
    main()
