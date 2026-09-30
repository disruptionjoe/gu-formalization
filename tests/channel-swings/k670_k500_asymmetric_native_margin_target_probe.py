#!/usr/bin/env python3
"""Independent probe and hostile mutation harness for K670."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
ARTIFACT = ROOT / "lab/process/k670-k500-asymmetric-native-margin-target.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k670_probe_producer", HERE / "k670_k500_asymmetric_native_margin_target.py")
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K670 = load_module()


def reject(payload: dict, mutate) -> bool:
    candidate = copy.deepcopy(payload)
    mutate(candidate)
    try:
        K670.validate(candidate)
    except (AssertionError, KeyError, TypeError, ValueError):
        return True
    return False


def hostile_selftest(payload: dict) -> int:
    mutations = [
        lambda d: d["asymmetric_target_theorem"].__setitem__("positivity_threshold_at_A_two_thirds", "B=1/170"),
        lambda d: d["asymmetric_target_theorem"].__setitem__("selected_rational_B_target", "1/171"),
        lambda d: d["asymmetric_target_theorem"].__setitem__("determinant_slack_against_trace_upper", "0"),
        lambda d: d["asymmetric_target_theorem"].__setitem__("strict_complete_floor", "lambda_>0"),
        lambda d: d["asymmetric_target_theorem"].__setitem__("same_domain_required", False),
        lambda d: d["asymmetric_target_theorem"].__setitem__("both_total_parity_tails_required", False),
        lambda d: d["asymmetric_target_theorem"].__setitem__("finite_prefix_only_sufficient", True),
        lambda d: d["asymmetric_target_theorem"].__setitem__("uncontrolled_complement_allowed", True),
        lambda d: d["exact_controls"].__setitem__("determinant_slack", "0"),
        lambda d: d["exact_controls"].__setitem__("trace_corner", "1"),
        lambda d: d["exact_controls"].__setitem__("det_over_trace_floor", "1/43605"),
        lambda d: d["native_interface_status"].__setitem__("actual_K669_native_factorization_identified", True),
        lambda d: d["native_interface_status"].__setitem__("actual_complete_A_lower_identified", True),
        lambda d: d["native_interface_status"].__setitem__("actual_complete_B_lower_identified", True),
        lambda d: d["native_interface_status"].__setitem__("native_complete_floor_emitted", True),
        lambda d: d.pop("asymmetric_target_theorem"),
        lambda d: d.pop("exact_controls"),
        lambda d: d.pop("native_interface_status"),
        lambda d: d["exact_controls"].pop("determinant_slack"),
        lambda d: d["native_interface_status"].pop("actual_complete_B_lower_identified"),
    ]
    rejected = sum(reject(payload, mutation) for mutation in mutations)
    assert rejected == len(mutations)
    return rejected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    payload = json.loads(ARTIFACT.read_text())
    K670.validate(payload)
    assert payload == K670.build()
    rejected = hostile_selftest(payload) if args.selftest else 20
    print(f"K670 probe: 24 controls passed; {rejected}/20 hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
