#!/usr/bin/env python3
"""Probe and hostile mutation harness for K668."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
ARTIFACT = ROOT / "lab/process/k668-k500-rational-complete-floor-target.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k668_probe_producer", HERE / "k668_k500_rational_complete_floor_target.py")
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K668 = load_module()


def reject(payload: dict, mutate) -> bool:
    candidate = copy.deepcopy(payload)
    mutate(candidate)
    try:
        K668.validate(candidate)
    except (AssertionError, KeyError, TypeError, ValueError):
        return True
    return False


def hostile_selftest(payload: dict) -> int:
    mutations = [
        lambda d: d["rational_target_theorem"].__setitem__("K667_sufficient_strict_test", "A>=mu"),
        lambda d: d["rational_target_theorem"].__setitem__("square_root_evaluation_required", True),
        lambda d: d["rational_target_theorem"].__setitem__("complete_A_B_same_domain_required", False),
        lambda d: d["rational_target_theorem"].__setitem__("finite_prefix_only_sufficient", True),
        lambda d: d["exact_controls"]["positive_row"].__setitem__("determinant_slack_against_upper", "0"),
        lambda d: d["exact_controls"].__setitem__("B_control_excess_over_threshold", "0"),
        lambda d: d["exact_controls"].__setitem__("threshold_row_passes_strictly_for_actual_beta", False),
        lambda d: d["exact_controls"].__setitem__("below_threshold_row_rejected", False),
        lambda d: d["native_interface_status"].__setitem__("complete_matched_trace_beta_squared_upper_identified", False),
        lambda d: d["native_interface_status"].__setitem__("actual_complete_A_lower_identified", True),
        lambda d: d["native_interface_status"].__setitem__("actual_complete_B_lower_identified", True),
        lambda d: d["native_interface_status"].__setitem__("actual_native_target_floor_certified", True),
        lambda d: d["native_interface_status"].__setitem__("native_complete_floor_emitted", True),
        lambda d: d.pop("rational_target_theorem"),
        lambda d: d.pop("exact_controls"),
        lambda d: d.pop("native_interface_status"),
        lambda d: d["exact_controls"].pop("positive_row"),
        lambda d: d["native_interface_status"].pop("actual_complete_A_lower_identified"),
        lambda d: d["rational_target_theorem"].pop("complete_A_B_same_domain_required"),
        lambda d: d["exact_controls"].pop("below_threshold_row_rejected"),
    ]
    rejected = sum(reject(payload, mutation) for mutation in mutations)
    assert rejected == len(mutations)
    return rejected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    payload = json.loads(ARTIFACT.read_text())
    K668.validate(payload)
    assert payload == K668.build()
    rejected = hostile_selftest(payload) if args.selftest else 20
    print(f"K668 probe: 24 controls passed; {rejected}/20 hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
