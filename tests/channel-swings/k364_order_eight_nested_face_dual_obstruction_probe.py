#!/usr/bin/env python3
"""Replay K364 and reject mutations of its exact nested-dual obstruction."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PRODUCER = HERE / "k364_order_eight_nested_face_dual_obstruction.py"
PUBLISHED = ROOT / "lab/process/k364-order-eight-nested-face-dual-obstruction.json"


spec = importlib.util.spec_from_file_location("k364_probe_backend", PRODUCER)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load K364 producer")
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
    controls = [
        rebuilt == published,
        rebuilt["fixed_control"]["same_rank_comparable_template_pairs"] == 146,
        rebuilt["obstruction_summary"]["pairs_without_monotone_optimal_integer_gauge_duals"] == 12,
        rebuilt["obstruction_summary"]["forced_inner_overextraction_histogram"] == {"0": 134, "1": 12},
        rebuilt["confluent_derivative_demand"]["maximum_kernel_derivative_order_required"] == 8,
        rebuilt["decision"]["naive_monotone_optimal_scalar_dual_reuse_rejected"],
        not rebuilt["nested_dual_contract"]["determinant_failure_claimed"],
        not rebuilt["decision"]["uniform_integrand_weighted_boundary_majorant_complete"],
        all(rebuilt["release_test"].values()),
    ]
    mutations = []
    for mutate in (
        lambda p: p["fixed_control"].__setitem__("same_rank_comparable_template_pairs", 145),
        lambda p: p["obstruction_summary"].__setitem__("pairs_without_monotone_optimal_integer_gauge_duals", 11),
        lambda p: p["obstruction_summary"].__setitem__("forced_inner_overextraction_histogram", {"0": 146}),
        lambda p: p["confluent_derivative_demand"].__setitem__("maximum_kernel_derivative_order_required", 7),
        lambda p: p["decision"].__setitem__("naive_monotone_optimal_scalar_dual_reuse_rejected", False),
        lambda p: p["decision"].__setitem__("uniform_integrand_weighted_boundary_majorant_complete", True),
        lambda p: p["release_test"].__setitem__("exactly_12_optimal_scalar_nesting_obstructions", False),
        lambda p: p["comparable_pair_bank"].pop(),
        lambda p: p["comparable_pair_bank"][0].__setitem__("minimum_forced_inner_overextraction", 2),
        lambda p: p["fixed_control"].__setitem__("K363_epsilon", "1/32"),
    ):
        candidate = copy.deepcopy(rebuilt)
        mutate(candidate)
        mutations.append(rejected(candidate))
    if not all(controls) or not all(mutations):
        raise AssertionError("K364 probe failed")
    print(f"K364 probe: {sum(controls)}/{len(controls)} controls passed; {sum(mutations)}/{len(mutations)} hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
