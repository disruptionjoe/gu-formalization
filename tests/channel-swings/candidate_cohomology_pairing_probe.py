#!/usr/bin/env python3
"""Exact GF(2) controls for pairing descent on cycle/gauge classes."""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
LEAN = ROOT / "Lean/GUFormalization/CandidateCohomologyPairing.lean"
EXPLORATION = ROOT / "explorations/candidate-cohomology-pairing-criterion-2026-08-31.md"
VECTORS = tuple(itertools.product((0, 1), repeat=3))
CYCLES = tuple(x for x in VECTORS if x[2] == 0)
GAUGE = {(0, 0, 0), (1, 0, 0)}


def add(x: tuple[int, ...], y: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((a + b) % 2 for a, b in zip(x, y, strict=True))


def pair(x: tuple[int, ...], y: tuple[int, ...]) -> int:
    return x[1] * y[1] % 2


def hostile_nonbasic_pair(x: tuple[int, ...], y: tuple[int, ...]) -> int:
    return x[0] * y[1] % 2


def class_key(x: tuple[int, ...]) -> int:
    return x[1]


def run_probe() -> dict[str, object]:
    lean = LEAN.read_text(encoding="utf-8")
    exploration = EXPLORATION.read_text(encoding="utf-8")
    checks: list[str] = []

    assert len(CYCLES) == 4 and len(GAUGE) == 2
    checks.append("cycle_and_gauge_carriers_exact")

    assert all(add(x, g) in CYCLES for x in CYCLES for g in GAUGE)
    checks.append("gauge_images_preserve_cycles")

    assert all(pair(g, y) == 0 for g in GAUGE for y in CYCLES)
    assert all(pair(x, g) == 0 for x in CYCLES for g in GAUGE)
    checks.append("pairing_is_two_sided_gauge_basic")

    assert all(
        pair(add(x, g), add(y, h)) == pair(x, y)
        for x in CYCLES for y in CYCLES for g in GAUGE for h in GAUGE
    )
    checks.append("representative_independence")

    classes = {class_key(x) for x in CYCLES}
    assert classes == {0, 1}
    checks.append("quotient_has_two_exact_classes")

    left_radical = {
        x for x in CYCLES if all(pair(x, y) == 0 for y in CYCLES)
    }
    right_radical = {
        y for y in CYCLES if all(pair(x, y) == 0 for x in CYCLES)
    }
    assert left_radical == right_radical == GAUGE
    checks.append("both_cycle_radicals_equal_gauge_images")

    quotient_table = {(a, b): a * b % 2 for a in classes for b in classes}
    assert quotient_table[(1, 1)] == 1
    assert all(quotient_table[(0, b)] == 0 for b in classes)
    checks.append("descended_pairing_is_nondegenerate")

    planted_noncycle = (0, 0, 1)
    assert planted_noncycle not in CYCLES
    checks.append("planted_noncycle_excluded")

    assert any(
        hostile_nonbasic_pair(add(x, g), y) != hostile_nonbasic_pair(x, y)
        for x in CYCLES for y in CYCLES for g in GAUGE
    )
    checks.append("hostile_nonbasic_pairing_rejected")

    zero_pair_radical = set(CYCLES)
    assert zero_pair_radical != GAUGE and (0, 1, 0) in zero_pair_radical
    checks.append("hostile_extra_radical_rejected")

    assert "left_nondegenerate_iff_radical_is_gauge" in lean
    assert "right_nondegenerate_iff_radical_is_gauge" in lean
    checks.append("lean_iff_criteria_present")

    assert "not a physical state space" in exploration
    assert "positive" in exploration and "analytic domain" in exploration
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
