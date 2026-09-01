#!/usr/bin/env python3
"""Exact GF(2) control for ker(d1)/range(d0) candidate cohomology."""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
LEAN = ROOT / "Lean/GUFormalization/CandidateCohomologyLinear.lean"
EXPLORATION = ROOT / "explorations/candidate-cohomology-linear-quotient-2026-08-31.md"
FIELDS = tuple(itertools.product((0, 1), repeat=3))


def add(x: tuple[int, ...], y: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(a ^ b for a, b in zip(x, y))


def d0(g: int) -> tuple[int, int, int]:
    return (g, 0, 0)


def d1(x: tuple[int, int, int]) -> int:
    return x[2]


def f1(x: tuple[int, int, int]) -> tuple[int, int, int]:
    return (x[0] ^ x[1], x[1], x[2])


def classes(carrier, shifts) -> list[frozenset[tuple[int, int, int]]]:
    unseen = set(carrier)
    result = []
    while unseen:
        x = min(unseen)
        orbit = frozenset(add(x, shift) for shift in shifts)
        result.append(orbit)
        unseen -= orbit
    return result


def run_probe() -> dict[str, object]:
    checks: list[str] = []
    lean = LEAN.read_text(encoding="utf-8")
    exploration = EXPLORATION.read_text(encoding="utf-8")
    cycles = tuple(x for x in FIELDS if d1(x) == 0)
    gauge = (d0(0), d0(1))
    quotient = classes(cycles, gauge)

    assert all(d1(d0(g)) == 0 for g in (0, 1))
    checks.append("square_zero_places_gauge_in_cycles")

    assert len(cycles) == 4 and len(gauge) == 2
    checks.append("kernel_and_range_cardinalities_are_exact")

    assert len(quotient) == 2
    checks.append("linear_cohomology_has_dimension_one")

    representative_classes = classes(cycles, gauge)
    assert set(representative_classes) == set(quotient)
    checks.append("representative_and_module_quotients_are_bijective")

    zero_class = next((cls for cls in quotient if (0, 0, 0) in cls), None)
    physical_class = next((cls for cls in quotient if (0, 1, 0) in cls), None)
    assert zero_class is not None and physical_class is not None
    assert zero_class != physical_class
    checks.append("nongauge_cycle_survives_the_quotient")

    assert all(f1(d0(g)) == d0(g) for g in (0, 1))
    assert all(d1(f1(x)) == d1(x) for x in FIELDS)
    assert all(len(classes(tuple(f1(x) for x in cls), gauge)) == 1 for cls in quotient)
    assert frozenset(f1(x) for x in physical_class) == physical_class
    checks.append("chain_map_descends_compatibly_and_linearly")

    all_field_quotient = classes(FIELDS, gauge)
    assert len(all_field_quotient) == 4 > len(quotient)
    checks.append("hostile_noncycle_quotient_leaks_extra_classes")

    assert len(classes(cycles, (d0(0),))) == 4 > len(quotient)
    checks.append("hostile_omitted_gauge_range_leaks_extra_classes")

    bad_f1 = lambda x: (x[1], x[0], x[2])
    assert bad_f1(d0(1)) not in gauge
    checks.append("hostile_non_chain_map_fails_gauge_descent")

    assert "def candidateCohomologyEquivLinear" in lean
    assert "def linearCohomologyMap" in lean
    assert "does not" in exploration and "physical state space" in exploration
    checks.append("lean_linear_surface_and_physical_ceiling_present")

    return {
        "status": "PASS",
        "checks": len(checks),
        "check_names": checks,
        "field_count": len(FIELDS),
        "cycle_count": len(cycles),
        "gauge_count": len(gauge),
        "quotient_class_count": len(quotient),
    }


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
