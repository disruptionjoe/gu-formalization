#!/usr/bin/env python3
"""Structural certificate for the Jacobson/B5 five-source twenty-seat sweep."""

from __future__ import annotations

import copy
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "lab/process/jacobson-b5-twenty-seat-priority-sweep-2026-08-21.json"
SOURCE_IDS = {"2411.00267", "2405.10307", "2403.02119", "2212.10608", "2208.11706"}
CLASSIFICATIONS = {"EXACT_PORT", "METHOD_PORT", "ANALOGY_ONLY", "WRONG_TYPE", "ALREADY_PRESENT"}
REQUIRED_SEAT = {
    "id", "group", "lens", "evidence_mode", "confidence", "classification",
    "strongest_applicability", "strongest_objection", "cheapest_decisive_test",
    "kill_condition", "required_artifact", "forbidden_inference", "priority", "vote",
}


def no_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def validate(data):
    assert data["artifact"] == "JACOBSON_B5_TWENTY_SEAT_PRIORITY_SWEEP"
    assert "not_twenty_independent_ai_vendors" in data["independence_notice"]
    assert {source["id"] for source in data["sources"]} == SOURCE_IDS
    assert len(data["sources"]) == 5
    assert all(source["classification"] in CLASSIFICATIONS for source in data["sources"])
    assert len(data["selected_method_ports"]) <= 2
    assert all(port["classification"] == "METHOD_PORT" for port in data["selected_method_ports"])

    seats = data["seats"]
    assert len(seats) == 20
    assert len({seat["id"] for seat in seats}) == 20
    assert sum(seat["group"] == "science_council" for seat in seats) == 10
    assert sum(seat["group"] == "variant_specialists" for seat in seats) == 10
    for seat in seats:
        assert REQUIRED_SEAT <= seat.keys()
        assert all(seat[field] not in (None, "") for field in REQUIRED_SEAT)
        assert seat["classification"] in CLASSIFICATIONS

    outliers = data["specialist_outliers"]
    assert outliers
    assert all(item["disposition"] in {"SELECTED", "DEFERRED", "REJECTED"} for item in outliers)
    assert all(item["revival_trigger"] for item in outliers)
    priority = data["priority_decision"]
    assert priority["effect"] == "REFINED"
    assert priority["prior_condition"] == "B5-PHYSICAL-PAIRING-OWNER-PACKET"
    assert priority["next_condition"] == "B5-SIGNATURE-TYPED-REDUCED-PHASE-SPACE-BVBFV-OWNER-PACKET"
    assert len(priority["downstream_battery"]) == 6
    assert "no_physical_pairing" in priority["claim_ceiling"]


def expect_failure(data, mutation):
    trial = copy.deepcopy(data)
    mutation(trial)
    try:
        validate(trial)
    except (AssertionError, KeyError, ValueError):
        return
    raise AssertionError("planted invalid registry unexpectedly passed")


def main():
    data = json.loads(REGISTRY.read_text(), object_pairs_hook=no_duplicate_keys)
    validate(data)
    expect_failure(data, lambda trial: trial["seats"].append(copy.deepcopy(trial["seats"][0])))
    expect_failure(data, lambda trial: trial["seats"][0].pop("forbidden_inference"))
    expect_failure(data, lambda trial: trial["selected_method_ports"].append(copy.deepcopy(trial["selected_method_ports"][0])))
    print("5 primary sources + 20 seats + 3 planted rejections = PASS")


if __name__ == "__main__":
    main()
