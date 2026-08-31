#!/usr/bin/env python3
"""Exact GF(2) control for the additive balanced coend presentation."""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
LEAN = ROOT / "Lean/GUFormalization/GroupActionBurnsideAdditiveCoend.lean"
EXPLORATION = ROOT / "explorations/group-action-burnside-additive-coend-2026-08-31.md"
GENERATORS = tuple((middle, x, y) for middle in (0, 1) for x in (0, 1) for y in (0, 1))
INDEX = {generator: i for i, generator in enumerate(GENERATORS)}


def vector(*generators: tuple[int, int, int]) -> int:
    value = 0
    for generator in generators:
        value ^= 1 << INDEX[generator]
    return value


def rank(rows: list[int]) -> int:
    pivots: dict[int, int] = {}
    for row in rows:
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return len(pivots)


def relation_rows(*, left: bool = True, right: bool = True, balance: bool = True) -> list[int]:
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


def quotient_dimension(rows: list[int]) -> int:
    return len(GENERATORS) - rank(rows)


def run_probe() -> dict[str, object]:
    checks: list[str] = []
    lean = LEAN.read_text(encoding="utf-8")
    exploration = EXPLORATION.read_text(encoding="utf-8")

    full_rows = relation_rows()
    assert quotient_dimension(full_rows) == 1
    checks.append("biadditive_balanced_quotient_has_dimension_one")

    assert quotient_dimension(relation_rows(balance=False)) == 2
    checks.append("hostile_missing_middle_balance_rejected")

    assert quotient_dimension(relation_rows(left=False)) > 1
    checks.append("hostile_missing_left_additivity_rejected")

    assert quotient_dimension(relation_rows(right=False)) > 1
    checks.append("hostile_missing_right_additivity_rejected")

    set_quotient_generators = 4
    assert set_quotient_generators > quotient_dimension(full_rows)
    checks.append("set_quotient_is_strictly_too_large_additively")

    evaluators = []
    for values in itertools.product((0, 1), repeat=len(GENERATORS)):
        if all(sum(((values[i] if row >> i & 1 else 0) for i in range(len(GENERATORS))), 0) % 2 == 0 for row in full_rows):
            evaluators.append(values)
    assert len(evaluators) == 2
    checks.append("exactly_two_F2_biadditive_balanced_evaluators")

    assert len(evaluators) == 2 ** quotient_dimension(full_rows)
    checks.append("universal_factorization_count_matches")

    nonzero = next((values for values in evaluators if any(values)), None)
    assert nonzero is not None
    assert nonzero[INDEX[(0, 1, 1)]] == nonzero[INDEX[(1, 1, 1)]] == 1
    assert all(nonzero[INDEX[(middle, x, y)]] == x * y for middle, x, y in GENERATORS)
    checks.append("surviving_generator_is_the_bilinear_tensor_class")

    assert "inductive AdditiveCoendRelation" in lean
    assert "AdditiveBalancedEvaluator.descend_unique" in lean
    assert "def additiveBalancedCompose" in lean
    checks.append("lean_additive_universal_surface_present")

    assert "not a biset bicategory" in exploration and "Mackey 2-functor" in exploration
    checks.append("categorical_claim_ceiling_present")

    return {
        "status": "PASS",
        "checks": len(checks),
        "check_names": checks,
        "generators": len(GENERATORS),
        "relation_rank": rank(full_rows),
        "quotient_dimension": quotient_dimension(full_rows),
        "balanced_evaluators": len(evaluators),
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
