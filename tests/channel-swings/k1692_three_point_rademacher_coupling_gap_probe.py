#!/usr/bin/env python3
"""Hostile mutations for K1692."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def valid(data):
    coeff, decision = data.get("coefficients", {}), data.get("decision", {})
    return all([
        data.get("claim_id") == "K1692",
        coeff.get("three_point_c") == "1/4",
        coeff.get("rademacher_c") == "31/60",
        "(576/5)" in coeff.get("difference", ""),
        decision.get("strict_for_each_fixed_shape_and_sufficiently_small_positive_g") is True,
        decision.get("strict_after_global_shape_optimization_proved") is False,
        decision.get("finite_strength_scalar_optimizer_identified") is False,
        "not uniform over C" in data.get("scope_guard", ""),
    ])


def main():
    source = json.loads((ROOT / "lab/process/k1692-three-point-rademacher-coupling-gap.json").read_text())
    mutations = [
        (("claim_id",), "K1691"),
        (("coefficients", "three_point_c"), "31/60"),
        (("coefficients", "rademacher_c"), "1/4"),
        (("coefficients", "difference"), "0"),
        (("decision", "strict_for_each_fixed_shape_and_sufficiently_small_positive_g"), False),
        (("decision", "strict_after_global_shape_optimization_proved"), True),
        (("decision", "finite_strength_scalar_optimizer_identified"), True),
        (("scope_guard",), "uniform over C"),
    ]
    assert valid(source)
    for number, (path, value) in enumerate(mutations, 1):
        changed = copy.deepcopy(source)
        cursor = changed
        for key in path[:-1]:
            cursor = cursor[key]
        cursor[path[-1]] = value
        assert not valid(changed), number
        print(f"REJECT {number:02d}: hostile mutation")
    print(f"RESULT: REJECTED {len(mutations)}/{len(mutations)}")


if __name__ == "__main__":
    main()
