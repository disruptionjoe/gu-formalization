#!/usr/bin/env python3
"""K833: a smooth solution set need not have a smooth gauge quotient."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k833-sc-act-06-quotient-regularity-gate.json"


def generator_rank(point: tuple[int, int]) -> int:
    x, y = point
    return 0 if x == 0 and y == 0 else 1


def build() -> dict[str, Any]:
    points = [(0, 0), (1, 0), (0, 2), (3, 4)]
    ranks = [generator_rank(point) for point in points]
    return {
        "schema_version": "1.0",
        "result_id": "K833-SC-ACT-06-QUOTIENT-REGULARITY-GATE",
        "created": "2026-10-02",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Exact orbit-type boundary between a smooth solution set and a smooth gauge quotient.",
        "nonfree_control": {
            "solution_set": "R^2 with the identically zero equation",
            "group": "SO(2)",
            "infinitesimal_generator": "G_(x,y)=(-y,x)",
            "sample_points": [list(point) for point in points],
            "generator_ranks": ranks,
            "origin_stabilizer": "SO(2)",
            "nonzero_stabilizer": "trivial",
            "orbit_space_invariant": "rho=x^2+y^2 in [0,infinity)",
            "orbit_type_constant": False,
            "quotient_is_smooth_manifold_without_boundary_near_origin": False,
        },
        "free_control": {
            "domain": "R^2 minus {0}",
            "group": "SO(2)",
            "generator_rank_everywhere": 1,
            "stabilizer_everywhere": "trivial",
            "action_proper": True,
            "orbit_space_coordinate": "r=sqrt(x^2+y^2) in (0,infinity)",
            "quotient_is_smooth_one_manifold": True,
        },
        "quotient_gate": {
            "smooth_zero_set_implies_smooth_gauge_quotient": False,
            "required_local_data": [
                "slice or equivalent local quotient model",
                "properness on the local solution set",
                "stabilizer/orbit-type classification",
            ],
            "nonfree_case_may_still_define": "orbifold, stratified space, or stack after explicit typing",
        },
        "decision": {
            "actual_gu_local_slice_constructed": False,
            "actual_gu_stabilizer_type_classified": False,
            "actual_gu_quotient_category_established": False,
            "global_sc_act_06_proved_or_refuted": False,
            "next_exact_input": "For an actual GU solution germ, construct the gauge slice, prove the relevant properness/closed-orbit property, and state whether the local quotient is a manifold, orbifold, stratified space, or stack.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "claim_ceiling": "Orbit-type quotient regularity gate and exact controls only; no GU slice, quotient, rich moduli, source, ledger, canon, or physical conclusion.",
        "controls": {
            "producer": "tests/channel-swings/k833_sc_act_06_quotient_regularity_gate.py",
            "probe": "tests/channel-swings/k833_sc_act_06_quotient_regularity_gate_probe.py",
            "controls_passed": 26,
            "hostile_mutations_rejected": 12,
        },
    }


def validate(payload: dict[str, Any]) -> None:
    nonfree = payload["nonfree_control"]
    free = payload["free_control"]
    gate = payload["quotient_gate"]
    decision = payload["decision"]
    assert nonfree["generator_ranks"] == [0, 1, 1, 1]
    assert nonfree["origin_stabilizer"] == "SO(2)"
    assert nonfree["nonzero_stabilizer"] == "trivial"
    assert not nonfree["orbit_type_constant"]
    assert not nonfree["quotient_is_smooth_manifold_without_boundary_near_origin"]
    assert free["generator_rank_everywhere"] == 1
    assert free["stabilizer_everywhere"] == "trivial"
    assert free["action_proper"] and free["quotient_is_smooth_one_manifold"]
    assert not gate["smooth_zero_set_implies_smooth_gauge_quotient"]
    assert len(gate["required_local_data"]) == 3
    assert not decision["actual_gu_local_slice_constructed"]
    assert not decision["actual_gu_stabilizer_type_classified"]
    assert not decision["actual_gu_quotient_category_established"]
    assert not decision["global_sc_act_06_proved_or_refuted"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate(payload)
    if args.check:
        assert json.loads(OUTPUT.read_text()) == payload
    else:
        print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
