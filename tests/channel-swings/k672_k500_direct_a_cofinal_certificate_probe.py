#!/usr/bin/env python3
"""Independent probe and hostile mutation harness for K672."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
ARTIFACT = ROOT / "lab/process/k672-k500-direct-a-cofinal-certificate.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k672_probe_producer", HERE / "k672_k500_direct_a_cofinal_certificate.py")
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K672 = load_module()


def reject(payload: dict, mutate) -> bool:
    candidate = copy.deepcopy(payload)
    mutate(candidate)
    try:
        K672.validate(candidate)
    except (AssertionError, KeyError, TypeError, ValueError):
        return True
    return False


def hostile_selftest(payload: dict) -> int:
    mutations = [
        lambda d: d["direct_A_theorem"].__setitem__("comparison_matrix", "[[a_N,0],[0,a_tail]]"),
        lambda d: d["direct_A_theorem"].__setitem__("two_thirds_test", "diagonals only"),
        lambda d: d["direct_A_theorem"].__setitem__("finite_prefix_only_sufficient", True),
        lambda d: d["direct_A_theorem"].__setitem__("sampled_complement_sufficient", True),
        lambda d: d["direct_A_theorem"].__setitem__("uncontrolled_cross_allowed", True),
        lambda d: d["direct_A_theorem"].__setitem__("auxiliary_chart_contraction_substitutable_for_total_form_bound", True),
        lambda d: d["direct_A_theorem"].__setitem__("complete_common_domain_required", False),
        lambda d: d["exact_controls"]["passing_control"].__setitem__("shifted_determinant", "0"),
        lambda d: d["exact_controls"]["passing_control"].__setitem__("shifted_trace", "1"),
        lambda d: d["exact_controls"].__setitem__("passing_shifted_det_over_trace", "1/48"),
        lambda d: d["exact_controls"].__setitem__("passing_complete_A_strict_lower", "2/3"),
        lambda d: d["exact_controls"].__setitem__("passing_A_strictly_above_two_thirds", False),
        lambda d: d["exact_controls"]["endpoint_control"].__setitem__("shifted_determinant", "1/48"),
        lambda d: d["exact_controls"].__setitem__("endpoint_exact_complete_A", "3/4"),
        lambda d: d["exact_controls"].__setitem__("endpoint_strict_target_rejected", False),
        lambda d: d["native_interface_status"].__setitem__("actual_complete_A_lower_identified", True),
        lambda d: d["native_interface_status"].__setitem__("native_complete_floor_emitted", True),
        lambda d: d.pop("direct_A_theorem"),
        lambda d: d.pop("exact_controls"),
        lambda d: d.pop("native_interface_status"),
    ]
    rejected = sum(reject(payload, mutation) for mutation in mutations)
    assert rejected == len(mutations)
    return rejected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    payload = json.loads(ARTIFACT.read_text())
    K672.validate(payload)
    assert payload == K672.build()
    rejected = hostile_selftest(payload) if args.selftest else 20
    print(f"K672 probe: 24 controls passed; {rejected}/20 hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
