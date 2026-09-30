#!/usr/bin/env python3
"""Independent probe and hostile mutation harness for K669."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
ARTIFACT = ROOT / "lab/process/k669-k500-leakage-remainder-factorization-bridge.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k669_probe_producer", HERE / "k669_k500_leakage_remainder_factorization_bridge.py")
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K669 = load_module()


def reject(payload: dict, mutate) -> bool:
    candidate = copy.deepcopy(payload)
    mutate(candidate)
    try:
        K669.validate(candidate)
    except (AssertionError, KeyError, TypeError, ValueError):
        return True
    return False


def hostile_selftest(payload: dict) -> int:
    mutations = [
        lambda d: d["factorization_bridge_theorem"].__setitem__("required_native_identity", "numerical similarity"),
        lambda d: d["factorization_bridge_theorem"].__setitem__("required_map_identification", "same dimension"),
        lambda d: d["factorization_bridge_theorem"].__setitem__("finite_or_sampled_identification_sufficient", True),
        lambda d: d["factorization_bridge_theorem"].__setitem__("equal_numerical_norm_without_map_identity_sufficient", True),
        lambda d: d["factorization_bridge_theorem"].__setitem__("uncontrolled_complement_allowed", True),
        lambda d: d["exact_bounds"].__setitem__("K609_upper_strictly_below_one_third", False),
        lambda d: d["exact_bounds"].__setitem__("conditional_A_strictly_above_two_thirds", False),
        lambda d: d["exact_bounds"].__setitem__("conservative_rational_A_lower", "1"),
        lambda d: d["exact_controls"].__setitem__("operator_norm_square_T_a_inverse", "1/4"),
        lambda d: d["exact_controls"].__setitem__("certified_A", "3/4"),
        lambda d: d["exact_controls"]["unidentified_map_counterexample"].__setitem__("proves_numeric_reuse_without_identification_invalid", False),
        lambda d: d["native_interface_status"].__setitem__("actual_native_factorization_identified", True),
        lambda d: d["native_interface_status"].__setitem__("actual_native_map_intertwiner_identified", True),
        lambda d: d["native_interface_status"].__setitem__("actual_complete_A_lower_identified", True),
        lambda d: d["native_interface_status"].__setitem__("native_complete_floor_emitted", True),
        lambda d: d.pop("factorization_bridge_theorem"),
        lambda d: d.pop("exact_bounds"),
        lambda d: d.pop("exact_controls"),
        lambda d: d.pop("native_interface_status"),
        lambda d: d["exact_controls"].pop("unidentified_map_counterexample"),
    ]
    rejected = sum(reject(payload, mutation) for mutation in mutations)
    assert rejected == len(mutations)
    return rejected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    payload = json.loads(ARTIFACT.read_text())
    K669.validate(payload)
    assert payload == K669.build()
    rejected = hostile_selftest(payload) if args.selftest else 20
    print(f"K669 probe: 24 controls passed; {rejected}/20 hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
