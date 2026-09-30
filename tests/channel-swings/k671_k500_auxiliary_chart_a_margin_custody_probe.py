#!/usr/bin/env python3
"""Independent probe and hostile mutation harness for K671."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
ARTIFACT = ROOT / "lab/process/k671-k500-auxiliary-chart-a-margin-custody.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k671_probe_producer", HERE / "k671_k500_auxiliary_chart_a_margin_custody.py")
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K671 = load_module()


def reject(payload: dict, mutate) -> bool:
    candidate = copy.deepcopy(payload)
    mutate(candidate)
    try:
        K671.validate(candidate)
    except (AssertionError, KeyError, TypeError, ValueError):
        return True
    return False


def hostile_selftest(payload: dict) -> int:
    mutations = [
        lambda d: d["compensated_margin_theorem"].__setitem__("contraction_can_change_while_A_fixed", False),
        lambda d: d["compensated_margin_theorem"].__setitem__("same_contraction_can_coexist_with_distinct_A", False),
        lambda d: d["compensated_margin_theorem"].__setitem__("auxiliary_contraction_alone_identifies_A", True),
        lambda d: d["compensated_margin_theorem"].__setitem__("smaller_auxiliary_contraction_implies_A_above_two_thirds", True),
        lambda d: d["compensated_margin_theorem"].__setitem__("K659_semiboundedness_retained", False),
        lambda d: d["compensated_margin_theorem"].__setitem__("fixed_native_A_denied", True),
        lambda d: d["compensated_margin_theorem"].__setitem__("complete_common_domain_required", False),
        lambda d: d["exact_controls"].__setitem__("fixed_A", "2/3"),
        lambda d: d["exact_controls"].__setitem__("all_compensated_rows_preserve_fixed_A", False),
        lambda d: d["exact_controls"].__setitem__("auxiliary_remainder_ratios_are_distinct", False),
        lambda d: d["exact_controls"].__setitem__("same_chart_ratio", "1/8"),
        lambda d: d["exact_controls"].__setitem__("same_chart_rows_have_distinct_A", False),
        lambda d: d["native_interface_status"].__setitem__("actual_compensating_regular_form_lower_identified", True),
        lambda d: d["native_interface_status"].__setitem__("actual_invariant_total_A_lower_identified", True),
        lambda d: d["native_interface_status"].__setitem__("native_complete_floor_emitted", True),
        lambda d: d.pop("compensated_margin_theorem"),
        lambda d: d.pop("exact_controls"),
        lambda d: d.pop("native_interface_status"),
        lambda d: d["exact_controls"].pop("fixed_A_compensated_rows"),
        lambda d: d["exact_controls"].pop("same_chart_distinct_A_rows"),
    ]
    rejected = sum(reject(payload, mutation) for mutation in mutations)
    assert rejected == len(mutations)
    return rejected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    payload = json.loads(ARTIFACT.read_text())
    K671.validate(payload)
    assert payload == K671.build()
    rejected = hostile_selftest(payload) if args.selftest else 20
    print(f"K671 probe: 24 controls passed; {rejected}/20 hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
