#!/usr/bin/env python3
"""Exact GF(2) control for the additive co-Yoneda equivalence."""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
LEAN = ROOT / "Lean/GUFormalization/GroupActionBurnsideCoYoneda.lean"
EXPLORATION = ROOT / "explorations/group-action-burnside-co-yoneda-2026-08-31.md"
GENERATORS = tuple((middle, x, y) for middle in (0, 1) for x in (0, 1) for y in (0, 1))
INDEX = {generator: i for i, generator in enumerate(GENERATORS)}


def vector(*generators: tuple[int, int, int]) -> int:
    value = 0
    for generator in generators:
        value ^= 1 << INDEX[generator]
    return value


def echelon(rows: list[int]) -> dict[int, int]:
    pivots: dict[int, int] = {}
    for row in rows:
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return pivots


def in_span(value: int, rows: list[int]) -> bool:
    pivots = echelon(rows)
    while value:
        pivot = value.bit_length() - 1
        if pivot not in pivots:
            return False
        value ^= pivots[pivot]
    return True


def relations(*, left: bool = True, right: bool = True, balance: bool = True) -> list[int]:
    rows: list[int] = []
    for middle in (0, 1):
        if left:
            for x, xp, y in itertools.product((0, 1), repeat=3):
                rows.append(vector((middle, x ^ xp, y), (middle, x, y), (middle, xp, y)))
        if right:
            for x, y, yp in itertools.product((0, 1), repeat=3):
                rows.append(vector((middle, x, y ^ yp), (middle, x, y), (middle, x, yp)))
    if balance:
        for x, y in itertools.product((0, 1), repeat=2):
            rows.append(vector((1, x, y), (0, x, y)))
    return rows


def compose(generator: tuple[int, int, int]) -> int:
    _middle, x, y = generator
    return x * y


def section(value: int) -> int:
    return 0 if value == 0 else vector((1, 1, 1))


def run_probe() -> dict[str, object]:
    checks: list[str] = []
    lean = LEAN.read_text(encoding="utf-8")
    exploration = EXPLORATION.read_text(encoding="utf-8")
    rows = relations()

    assert len(GENERATORS) - len(echelon(rows)) == 1
    checks.append("additive_coend_and_target_both_dimension_one")

    assert compose((1, 1, 1)) == 1
    checks.append("composition_is_nonzero_and_therefore_isomorphism")

    assert compose((1, 1, 1)) == 1 and section(1) == vector((1, 1, 1))
    checks.append("canonical_identity_leg_section_is_right_inverse")

    assert all(in_span(vector(g) ^ section(compose(g)), rows) for g in GENERATORS)
    checks.append("every_generator_reduces_to_canonical_composite")

    assert in_span(vector((0, 1, 1)) ^ vector((1, 1, 1)), rows)
    checks.append("middle_object_choice_is_killed_by_balance")

    no_balance = relations(balance=False)
    assert not in_span(vector((0, 1, 1)) ^ vector((1, 1, 1)), no_balance)
    checks.append("hostile_missing_balance_breaks_left_inverse")

    assert len(GENERATORS) - len(echelon(relations(left=False))) > 1
    assert len(GENERATORS) - len(echelon(relations(right=False))) > 1
    checks.append("hostile_missing_additivity_breaks_injectivity")

    assert compose((1, 1, 0)) == 0
    checks.append("hostile_zero_second_leg_is_not_a_section")

    assert "def additiveCoYonedaEquiv" in lean
    assert "coYonedaSection_comp_additiveBalancedCompose" in lean
    checks.append("lean_two_sided_inverse_surface_present")

    assert "not a biset bicategory" in exploration and "Mackey 2-functor" in exploration
    checks.append("higher_categorical_claim_ceiling_present")

    return {
        "status": "PASS",
        "checks": len(checks),
        "check_names": checks,
        "generators": len(GENERATORS),
        "relation_rank": len(echelon(rows)),
        "quotient_dimension": len(GENERATORS) - len(echelon(rows)),
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
