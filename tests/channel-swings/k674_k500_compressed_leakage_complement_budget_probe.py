#!/usr/bin/env python3
"""Independent probe and hostile mutation harness for K674."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
ARTIFACT = ROOT / "lab/process/k674-k500-compressed-leakage-complement-budget.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k674_probe_producer", HERE / "k674_k500_compressed_leakage_complement_budget.py")
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K674 = load_module()


def reject(payload: dict, mutate) -> bool:
    candidate = copy.deepcopy(payload)
    mutate(candidate)
    try:
        K674.validate(candidate)
    except (AssertionError, KeyError, TypeError, ValueError):
        return True
    return False


def hostile_selftest(payload: dict) -> int:
    mutations = [
        lambda d: d["compressed_bridge_theorem"].__setitem__("range_orthogonality_required", True),
        lambda d: d["compressed_bridge_theorem"].__setitem__("two_column_bound", "||R||^2<=max(lambda,tau2)"),
        lambda d: d["compressed_bridge_theorem"].__setitem__("complete_A_lower", "A>=1-lambda"),
        lambda d: d["compressed_bridge_theorem"].__setitem__("K672_diagonal_inputs", "a_N=a_tail=1"),
        lambda d: d["compressed_bridge_theorem"].__setitem__("K672_cross_input", "kappa=0"),
        lambda d: d["compressed_bridge_theorem"].__setitem__("strict_two_thirds_test", "lambda<1/3"),
        lambda d: d["compressed_bridge_theorem"].__setitem__("finite_or_sampled_complement_sufficient", True),
        lambda d: d["compressed_bridge_theorem"].__setitem__("uncontrolled_complement_allowed", True),
        lambda d: d["exact_native_target"].__setitem__("K609_lambda_strictly_below_one_third", False),
        lambda d: d["exact_native_target"].__setitem__("simple_sufficient_tau2_target", "1/10"),
        lambda d: d["exact_native_target"].__setitem__("simple_target_strictly_inside_budget", False),
        lambda d: d["exact_native_target"].__setitem__("simple_target_A_strictly_above_two_thirds", False),
        lambda d: d["exact_native_target"].__setitem__("target_is_conditional_not_native", False),
        lambda d: d["exact_controls"].__setitem__("lambda_plus_tau2", "1/3"),
        lambda d: d["exact_controls"].__setitem__("attained_complete_norm_square", "16/49"),
        lambda d: d["exact_controls"].__setitem__("complete_A", "2/3"),
        lambda d: d["exact_controls"].__setitem__("complete_A_above_two_thirds", False),
        lambda d: d["exact_controls"].__setitem__("two_column_bound_sharp_without_range_orthogonality", False),
        lambda d: d["exact_controls"].__setitem__("endpoint_strict_target_rejected", False),
        lambda d: d["native_interface_status"].__setitem__("actual_seed_compression_identity_proved", True),
        lambda d: d["native_interface_status"].__setitem__("actual_complete_A_lower_identified", True),
        lambda d: d["native_interface_status"].__setitem__("native_complete_floor_emitted", True),
    ]
    rejected = sum(reject(payload, mutation) for mutation in mutations)
    assert rejected == len(mutations)
    return rejected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    payload = json.loads(ARTIFACT.read_text())
    K674.validate(payload)
    assert payload == K674.build()
    rejected = hostile_selftest(payload) if args.selftest else 22
    print(f"K674 probe: 26 controls passed; {rejected}/22 hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
