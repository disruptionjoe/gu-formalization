#!/usr/bin/env python3
"""Deterministic replay and hostile controls for K384."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = Path(__file__).with_name("k384_order_nine_positive_peano_contract.py")
STORED = ROOT / "lab/process/k384-order-nine-positive-peano-contract.json"


def load():
    spec = importlib.util.spec_from_file_location("k384_probe_target", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K384 producer")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load()
    stored = json.loads(STORED.read_text())
    if stored != module.build():
        raise AssertionError("deterministic K384 replay differs")
    rows = stored["tensor_telescoping"]["axis_contracts"]
    checks = [
        stored["one_axis_identity"]["kernel_nonnegative"],
        stored["one_axis_identity"]["kernel_continuous_at_node"],
        stored["one_axis_identity"]["kernel_zero_order_at_origin"] == 2,
        stored["one_axis_identity"]["kernel_mass"] == "1/33554432",
        len(rows) == 20,
        all(row["preceding_axes_fixed_at_node"] + row["following_axes_integrated_exactly"] == 19 for row in rows),
        not stored["tensor_telescoping"]["mixed_derivatives_required"],
        stored["tensor_telescoping"]["pure_second_directional_terms"] == 20,
        stored["tensor_telescoping"]["node_jet_substitution_for_global_integral_forbidden"],
        not stored["decision"]["complete_twenty_axis_remainder_numerically_bounded"],
        not stored["decision"]["complete_order_nine_integral_emitted"],
        not stored["decision"]["rank_five_order_nine_global_cover_released"],
    ]
    if not all(checks):
        raise AssertionError("K384 control failed")
    mutations = [
        lambda p: p["fixed_control"].__setitem__("native_axes", p["fixed_control"]["native_axes"][:-1]),
        lambda p: p["fixed_control"].__setitem__("axis_node", "1/255"),
        lambda p: p["one_axis_identity"].__setitem__("kernel_nonnegative", False),
        lambda p: p["one_axis_identity"].__setitem__("kernel_continuous_at_node", False),
        lambda p: p["one_axis_identity"].__setitem__("kernel_zero_order_at_origin", 1),
        lambda p: p["one_axis_identity"].__setitem__("kernel_mass", "1/16777216"),
        lambda p: p["tensor_telescoping"].__setitem__("mixed_derivatives_required", True),
        lambda p: p["tensor_telescoping"].__setitem__("pure_second_directional_terms", 19),
        lambda p: p["tensor_telescoping"]["axis_contracts"].pop(),
        lambda p: p["tensor_telescoping"].__setitem__("node_jet_substitution_for_global_integral_forbidden", False),
        lambda p: p["tensor_telescoping"].__setitem__("global_entrywise_supremum_before_group_assembly_forbidden", False),
        lambda p: p["decision"].__setitem__("complete_twenty_axis_remainder_formula_emitted", False),
        lambda p: p["decision"].__setitem__("complete_twenty_axis_remainder_numerically_bounded", True),
        lambda p: p["decision"].__setitem__("complete_order_nine_integral_emitted", True),
        lambda p: p["decision"].__setitem__("rank_five_order_nine_global_cover_released", True),
        lambda p: p["release_test"].__setitem__("node_controls_not_promoted", False),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(stored)
        mutate(candidate)
        try:
            module.validate_payload(candidate)
        except AssertionError:
            rejected += 1
    if rejected != len(mutations):
        raise AssertionError(f"K384 hostile rejection changed: {rejected}/{len(mutations)}")
    print(f"K384 probe passed {len(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
