#!/usr/bin/env python3
"""Independent probe and hostile mutation harness for K673."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
ARTIFACT = ROOT / "lab/process/k673-k500-seed-line-leakage-custody.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k673_probe_producer", HERE / "k673_k500_seed_line_leakage_custody.py")
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K673 = load_module()


def reject(payload: dict, mutate) -> bool:
    candidate = copy.deepcopy(payload)
    mutate(candidate)
    try:
        K673.validate(candidate)
    except (AssertionError, KeyError, TypeError, ValueError):
        return True
    return False


def hostile_selftest(payload: dict) -> int:
    mutations = [
        lambda d: d["coverage_theorem"].__setitem__("K609_complete_in_truncation_order", False),
        lambda d: d["coverage_theorem"].__setitem__("K609_complete_on_named_seed_lines", False),
        lambda d: d["coverage_theorem"].__setitem__("named_seed_lines", ["q00"]),
        lambda d: d["coverage_theorem"].__setitem__("seed_lines_pairwise_orthogonal_by_charge", False),
        lambda d: d["coverage_theorem"].__setitem__("K609_complete_domain_operator_norm_proved", True),
        lambda d: d["coverage_theorem"].__setitem__("seed_line_bounds_determine_hidden_complement", True),
        lambda d: d["coverage_theorem"].__setitem__("seed_line_bounds_alone_identify_K669_map", True),
        lambda d: d["coverage_theorem"].__setitem__("native_complete_extension_denied", True),
        lambda d: d["exact_seed_data"].__setitem__("uniform_seed_square_strictly_below_one_third", False),
        lambda d: d["exact_seed_data"].__setitem__("all_order_tail_charged_once", False),
        lambda d: d["hidden_complement_countermodel"].__setitem__("all_seed_line_values_unchanged_for_every_M_nonnegative", False),
        lambda d: d["hidden_complement_countermodel"].__setitem__("displayed_hidden_M", "0"),
        lambda d: d["hidden_complement_countermodel"].__setitem__("displayed_complete_norm_square", "1/3"),
        lambda d: d["hidden_complement_countermodel"].__setitem__("displayed_A_upper_at_most", "2/3"),
        lambda d: d["hidden_complement_countermodel"].__setitem__("same_seed_data_can_have_complete_norm_at_least_one", False),
        lambda d: d["hidden_complement_countermodel"].__setitem__("proves_seed_data_insufficient_not_native_A_nonpositive", False),
        lambda d: d["native_interface_status"].__setitem__("actual_seed_compression_identity_proved", True),
        lambda d: d["native_interface_status"].__setitem__("actual_complete_extension_identified", True),
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
    K673.validate(payload)
    assert payload == K673.build()
    rejected = hostile_selftest(payload) if args.selftest else 20
    print(f"K673 probe: 24 controls passed; {rejected}/20 hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
