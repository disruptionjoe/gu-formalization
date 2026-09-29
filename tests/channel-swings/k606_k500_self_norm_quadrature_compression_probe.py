#!/usr/bin/env python3
"""Deterministic replay and hostile mutations for K606."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "tests/channel-swings/k606_k500_self_norm_quadrature_compression.py"
ARTIFACT = ROOT / "lab/process/k606-k500-self-norm-quadrature-compression.json"


def load():
    spec = importlib.util.spec_from_file_location("k606_probe_source", SOURCE)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load()
    payload = module.build()
    module.validate(payload)
    assert payload == json.loads(ARTIFACT.read_text())
    closure = payload["closure"]
    checks = [
        payload["total_positivity_theorem"]["strict_total_positivity"],
        payload["total_positivity_theorem"]["within_determinant_interference_preserved"],
        payload["cauchy_schwarz_theorem"]["diagonal_bounds_are_still_numerically_required"],
        closure["mapped_nonzero_classes"] == 39438,
        closure["unique_positive_diagonal_self_norms"] == 1614,
        closure["unique_N_self_norms"] == 291,
        closure["unique_B_F_self_norms"] == 1323,
        closure["direct_cross_integrals_eliminated"] == 37824,
        not closure["missing_self_endpoints"],
        payload["exact_controls"]["same_order_two_by_two_determinant_positive"],
        payload["decision"]["all_nonzero_K604_classes_mapped"],
        not payload["decision"]["complete_K500_uniform_leakage_emitted"],
    ]
    mutations = [
        lambda p: p["total_positivity_theorem"].__setitem__("strict_total_positivity", False),
        lambda p: p["total_positivity_theorem"].__setitem__("within_determinant_interference_preserved", False),
        lambda p: p["total_positivity_theorem"].__setitem__("exact_zero_mixed_classes_remain_zero", 0),
        lambda p: p["cauchy_schwarz_theorem"].__setitem__("diagonal_bounds_are_still_numerically_required", False),
        lambda p: p["cauchy_schwarz_theorem"].__setitem__("determinants_are_not_expanded_or_replaced_by_occurrencewise_absolute_values", False),
        lambda p: p["closure"].__setitem__("mapped_nonzero_classes", 39437),
        lambda p: p["closure"].__setitem__("missing_self_endpoints", [["bad", 0]]),
        lambda p: p["closure"].__setitem__("unique_positive_diagonal_self_norms", 1615),
        lambda p: p["closure"].__setitem__("unique_N_self_norms", 292),
        lambda p: p["closure"].__setitem__("unique_B_F_self_norms", 1322),
        lambda p: p["closure"].__setitem__("direct_cross_integrals_eliminated", 0),
        lambda p: p["exact_controls"].__setitem__("same_order_two_by_two_determinant_positive", False),
        lambda p: p["decision"].__setitem__("complete_self_norm_closure_emitted", False),
        lambda p: p["decision"].__setitem__("all_nonzero_K604_classes_mapped", False),
        lambda p: p["decision"].__setitem__("outward_diagonal_values_emitted", True),
        lambda p: p["decision"].__setitem__("complete_finite_K456_moments_emitted", True),
        lambda p: p["decision"].__setitem__("complete_K500_uniform_leakage_emitted", True),
        lambda p: p["decision"].__setitem__("native_noncyclic_floor_emitted", True),
        lambda p: p["decision"].__setitem__("K473_released", True),
        lambda p: p["decision"].__setitem__("native_K152_interval_emitted", True),
    ]
    rejected = 0
    for mutate in mutations:
        changed = copy.deepcopy(payload)
        mutate(changed)
        try:
            module.validate(changed)
        except AssertionError:
            rejected += 1
    assert all(checks) and rejected == len(mutations)
    print(f"K606 exact controls: {sum(checks)}/{len(checks)} passed")
    print(f"K606 hostile mutations: {rejected}/{len(mutations)} rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
