#!/usr/bin/env python3
"""Finite controls for all-middle coend balance and universal factorization."""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path

from group_action_burnside_biset_coend_probe import run_probe as fixed_middle_probe


ROOT = Path(__file__).resolve().parents[2]
LEAN = ROOT / "Lean/GUFormalization/GroupActionBurnsideBisetCoend.lean"
EXPLORATION = ROOT / "explorations/group-action-burnside-all-middle-coend-2026-08-31.md"
PAIRS = tuple((middle, value) for middle in ("B0", "B1") for value in (0, 1))
MOVES = tuple((("B1", value), ("B0", value)) for value in (0, 1))


def closure_classes(moves: tuple[tuple[tuple[str, int], tuple[str, int]], ...]):
    parent = {x: x for x in PAIRS}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for left, right in moves:
        a, b = find(left), find(right)
        if a != b:
            parent[b] = a
    buckets: dict[tuple[str, int], set[tuple[str, int]]] = {}
    for x in PAIRS:
        buckets.setdefault(find(x), set()).add(x)
    return tuple(frozenset(values) for values in buckets.values())


def representative(cls: frozenset[tuple[str, int]]) -> tuple[str, int]:
    value = next(iter(cls), None)
    assert value is not None
    return value


def run_probe() -> dict[str, object]:
    checks: list[str] = []
    fixed = fixed_middle_probe()
    assert fixed["status"] == "PASS" and fixed["balanced_double_cosets"] == 2
    checks.append("nonnormal_S3_fixed_middle_control_retained")

    classes = closure_classes(MOVES)
    assert len(classes) == 2
    checks.append("arbitrary_middle_morphism_connects_objects")

    assert {frozenset(x[1] for x in cls) for cls in classes} == {
        frozenset({0}), frozenset({1})
    }
    checks.append("composition_signature_constant_on_balance_classes")

    fixed_middle_classes = closure_classes(())
    assert len(fixed_middle_classes) == 4
    checks.append("hostile_fixed_middle_only_quotient_rejected")

    over_quotient = closure_classes(MOVES + ((("B0", 0), ("B0", 1)),))
    assert len(over_quotient) == 1
    checks.append("hostile_over_quotient_rejected")

    assignments = tuple(itertools.product((0, 1), repeat=len(PAIRS)))
    balanced = []
    for values in assignments:
        evaluator = dict(zip(PAIRS, values, strict=True))
        if all(evaluator[a] == evaluator[b] for a, b in MOVES):
            balanced.append(evaluator)
    quotient_maps = tuple(itertools.product((0, 1), repeat=len(classes)))
    assert len(balanced) == len(quotient_maps) == 4
    checks.append("balanced_evaluators_equal_quotient_maps")

    for evaluator in balanced:
        factored = {index: evaluator[representative(cls)] for index, cls in enumerate(classes)}
        assert all(
            factored[index] == evaluator[pair]
            for index, cls in enumerate(classes) for pair in cls
        )
    checks.append("every_balanced_evaluator_factors")

    assert len({tuple(f[index] for index in range(len(classes))) for f in (
        {i: evaluator[representative(cls)] for i, cls in enumerate(classes)}
        for evaluator in balanced
    )}) == len(balanced)
    checks.append("factorization_is_unique")

    hostile = {pair: int(pair == ("B1", 0)) for pair in PAIRS}
    assert any(hostile[a] != hostile[b] for a, b in MOVES)
    checks.append("nonbalanced_evaluator_rejected")

    lean = LEAN.read_text(encoding="utf-8")
    assert "structure AllMiddlePair" in lean and "inductive AllMiddleMove" in lean
    assert "structure BalancedEvaluator" in lean
    assert "theorem BalancedEvaluator.descend_unique" in lean
    checks.append("lean_all_middle_universal_surface_present")

    exploration = EXPLORATION.read_text(encoding="utf-8")
    assert "set-valued coend" in exploration and "not a Mackey 2-functor" in exploration
    checks.append("categorical_claim_ceiling_present")

    return {
        "status": "PASS",
        "checks": len(checks),
        "check_names": checks,
        "all_middle_classes": len(classes),
        "fixed_middle_classes": len(fixed_middle_classes),
        "over_quotient_classes": len(over_quotient),
        "balanced_evaluators": len(balanced),
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
