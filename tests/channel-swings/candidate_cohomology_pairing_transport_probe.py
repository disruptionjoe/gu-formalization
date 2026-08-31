#!/usr/bin/env python3
"""Exact finite control for pairing-preserving quotient transport."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
LEAN = ROOT / "Lean/GUFormalization/CandidateCohomologyPairingTransport.lean"
EXPLORATION = ROOT / "explorations/candidate-cohomology-pairing-transport-2026-08-31.md"
SOURCE = (0, 1)
TARGET = ("gauge", "physical")
EQUIV = {0: "gauge", 1: "physical"}
ZERO_SOURCE = 0
ZERO_TARGET = "gauge"


def source_pair(x: int, y: int) -> int:
    return x * y % 2


def target_pair(x: str, y: str) -> int:
    return int(x == "physical" and y == "physical")


def nondegenerate(carrier, zero, pair) -> tuple[bool, bool]:
    left = all(
        x == zero or any(pair(x, y) != 0 for y in carrier)
        for x in carrier
    )
    right = all(
        y == zero or any(pair(x, y) != 0 for x in carrier)
        for y in carrier
    )
    return left, right


def run_probe() -> dict[str, object]:
    checks: list[str] = []
    lean = LEAN.read_text(encoding="utf-8")
    exploration = EXPLORATION.read_text(encoding="utf-8")

    assert set(EQUIV) == set(SOURCE) and set(EQUIV.values()) == set(TARGET)
    checks.append("quotient_equivalence_is_bijective")

    assert EQUIV[ZERO_SOURCE] == ZERO_TARGET
    checks.append("zero_class_is_preserved")

    assert all(
        target_pair(EQUIV[x], EQUIV[y]) == source_pair(x, y)
        for x in SOURCE for y in SOURCE
    )
    checks.append("pairing_is_preserved")

    source_nd = nondegenerate(SOURCE, ZERO_SOURCE, source_pair)
    target_nd = nondegenerate(TARGET, ZERO_TARGET, target_pair)
    assert source_nd == target_nd == (True, True)
    checks.append("left_nondegeneracy_transports")
    checks.append("right_nondegeneracy_transports")

    hostile_zero_swap = {0: "physical", 1: "gauge"}
    assert hostile_zero_swap[ZERO_SOURCE] != ZERO_TARGET
    checks.append("hostile_zero_moving_equivalence_rejected")

    hostile_pair = lambda x, y: int(x == "gauge" and y == "gauge")
    assert any(
        hostile_pair(EQUIV[x], EQUIV[y]) != source_pair(x, y)
        for x in SOURCE for y in SOURCE
    )
    checks.append("hostile_nonisometric_equivalence_rejected")

    degenerate = lambda _x, _y: 0
    assert nondegenerate(TARGET, ZERO_TARGET, degenerate) == (False, False)
    checks.append("hostile_extra_radical_detected")

    assert "leftNondegenerate_iff" in lean and "rightNondegenerate_iff" in lean
    checks.append("lean_transport_iff_theorems_present")

    assert "not a physical isometry" in exploration
    checks.append("physical_claim_ceiling_present")

    return {"status": "PASS", "checks": len(checks), "check_names": checks}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    result = run_probe()
    if args.selftest:
        print(f"PASS {result['checks']}/{result['checks']}")
    else:
        print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
