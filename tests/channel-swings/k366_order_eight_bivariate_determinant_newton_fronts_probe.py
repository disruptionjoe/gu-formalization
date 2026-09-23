#!/usr/bin/env python3
"""Replay K366 and reject mutations of its exact two-scale fronts."""

from __future__ import annotations

import copy
import importlib.util
import json
import math
import sys
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PRODUCER = HERE / "k366_order_eight_bivariate_determinant_newton_fronts.py"
PUBLISHED = ROOT / "lab/process/k366-order-eight-bivariate-determinant-newton-fronts.json"


spec = importlib.util.spec_from_file_location("k366_probe_backend", PRODUCER)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load K366 producer")
backend = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = backend
spec.loader.exec_module(backend)


def rejected(payload: dict) -> bool:
    try:
        backend.validate_payload(payload)
    except AssertionError:
        return True
    return False


def main() -> int:
    rebuilt = backend.build()
    published = json.loads(PUBLISHED.read_text())
    histogram = Counter(len(row["pareto_maximal_newton_front"]) for row in rebuilt["bivariate_front_bank"])
    controls = [
        rebuilt == published,
        rebuilt["fixed_control"]["comparable_template_pairs"] == 146,
        rebuilt["fixed_control"]["scalar_optimal_nesting_obstructions"] == 12,
        histogram == Counter({1: 60, 2: 81, 3: 5}),
        all(sum(point["permutation_count"] for point in row["permutation_exponent_support"]) == math.factorial(row["rank"]) for row in rebuilt["bivariate_front_bank"]),
        rebuilt["newton_front_contract"]["same_permutation_coupling_preserved"],
        not rebuilt["newton_front_contract"]["occurrencewise_absolute_value_used"],
        not rebuilt["decision"]["uniform_integrand_weighted_boundary_majorant_complete"],
        all(rebuilt["release_test"].values()),
    ]
    mutations = []
    for mutate in (
        lambda p: p["fixed_control"].__setitem__("comparable_template_pairs", 145),
        lambda p: p["fixed_control"].__setitem__("scalar_optimal_nesting_obstructions", 11),
        lambda p: p["fixed_control"].__setitem__("maximum_kernel_derivative_order_available", 7),
        lambda p: p["bivariate_front_bank"].pop(),
        lambda p: p["bivariate_front_bank"][0]["permutation_exponent_support"][0].__setitem__("permutation_count", 99),
        lambda p: p["newton_front_contract"].__setitem__("same_permutation_coupling_preserved", False),
        lambda p: p["newton_front_contract"].__setitem__("occurrencewise_absolute_value_used", True),
        lambda p: p["newton_front_contract"].__setitem__("one_false_scalar_exponent_substituted", True),
        lambda p: p["decision"].__setitem__("zero_inclusive_numerical_determinant_envelope_complete", True),
        lambda p: p["release_test"].__setitem__("uniform_strip_bound_not_overclaimed", False),
    ):
        candidate = copy.deepcopy(rebuilt)
        mutate(candidate)
        mutations.append(rejected(candidate))
    if not all(controls) or not all(mutations):
        raise AssertionError("K366 probe failed")
    print(f"K366 probe: {sum(controls)}/{len(controls)} controls passed; {sum(mutations)}/{len(mutations)} hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
