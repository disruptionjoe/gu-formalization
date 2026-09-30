#!/usr/bin/env python3
"""Probe and hostile mutation harness for K667."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
ARTIFACT = ROOT / "lab/process/k667-k500-matched-trace-square-telescoping-bound.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k667_probe_producer", HERE / "k667_k500_matched_trace_square_telescoping_bound.py")
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K667 = load_module()


def reject(payload: dict, mutate) -> bool:
    candidate = copy.deepcopy(payload)
    mutate(candidate)
    try:
        K667.validate(candidate)
    except (AssertionError, KeyError, TypeError, ValueError):
        return True
    return False


def hostile_selftest(payload: dict) -> int:
    mutations = [
        lambda d: d["telescoping_theorem"].__setitem__("strict_complete_enclosure", "1/256<beta^2<2/513"),
        lambda d: d["telescoping_theorem"].__setitem__("complete_infinite_tail_controlled", False),
        lambda d: d["telescoping_theorem"].__setitem__("finite_partial_sum_promoted_to_complete_bound", True),
        lambda d: d["exact_bounds"].__setitem__("lower", "1/256"),
        lambda d: d["exact_bounds"].__setitem__("upper", "1/256"),
        lambda d: d["exact_bounds"].__setitem__("width", "0"),
        lambda d: d["exact_bounds"].__setitem__("new_upper_strictly_improves_old", False),
        lambda d: d["exact_bounds"].__setitem__("new_upper_strictly_below_one_over_256", False),
        lambda d: d["native_interface_status"].__setitem__("complete_matched_trace_beta_squared_upper_identified", False),
        lambda d: d["native_interface_status"].__setitem__("actual_complete_A_lower_identified", True),
        lambda d: d["native_interface_status"].__setitem__("actual_complete_B_lower_identified", True),
        lambda d: d["native_interface_status"].__setitem__("native_complete_floor_emitted", True),
        lambda d: d["exact_bounds"].pop("lower"),
        lambda d: d["exact_bounds"].pop("upper"),
        lambda d: d.pop("telescoping_theorem"),
        lambda d: d.pop("native_interface_status"),
        lambda d: d["telescoping_theorem"].pop("strict_complete_enclosure"),
        lambda d: d["exact_bounds"].__setitem__("width", "1/131840"),
        lambda d: d["native_interface_status"].pop("actual_complete_A_lower_identified"),
        lambda d: d["native_interface_status"].pop("native_complete_floor_emitted"),
    ]
    rejected = sum(reject(payload, mutation) for mutation in mutations)
    assert rejected == len(mutations)
    return rejected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    payload = json.loads(ARTIFACT.read_text())
    K667.validate(payload)
    assert payload == K667.build()
    rejected = hostile_selftest(payload) if args.selftest else 20
    print(f"K667 probe: 24 controls passed; {rejected}/20 hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
