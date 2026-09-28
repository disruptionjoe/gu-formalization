#!/usr/bin/env python3
"""Deterministic replay and hostile controls for K558."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = Path(__file__).with_name("k558_orders_eleven_twelve_positive_peano_contract.py")
STORED = ROOT / "lab/process/k558-orders-eleven-twelve-positive-peano-contract.json"


def load():
    spec = importlib.util.spec_from_file_location("k558_probe_target", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K558 producer")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load()
    stored = json.loads(STORED.read_text())
    if stored != module.build():
        raise AssertionError("deterministic K558 replay differs")
    rows = stored["order_contracts"]
    checks = [
        stored["one_axis_identity"]["kernel_nonnegative"],
        stored["one_axis_identity"]["kernel_continuous_at_node"],
        stored["one_axis_identity"]["kernel_zero_order_at_origin"] == 2,
        stored["one_axis_identity"]["kernel_mass"] == "1/33554432",
        [row["order"] for row in rows] == [11, 12],
        [len(row["tensor_telescoping"]["axis_contracts"]) for row in rows] == [24, 26],
        all(not row["tensor_telescoping"]["mixed_derivatives_required"] for row in rows),
        all(row["tensor_telescoping"]["node_jet_substitution_for_global_integral_forbidden"] for row in rows),
        not stored["decision"]["complete_order_eleven_remainder_numerically_bounded"],
        not stored["decision"]["complete_order_twelve_remainder_numerically_bounded"],
        not stored["decision"]["complete_order_eleven_integral_emitted"],
        not stored["decision"]["complete_order_twelve_integral_emitted"],
    ]
    if not all(checks):
        raise AssertionError("K558 control failed")
    mutations = [
        lambda p: p["fixed_control"].__setitem__("combined_native_axes", 49),
        lambda p: p["fixed_control"].__setitem__("combined_axis_entry_evaluations", 2413151),
        lambda p: p["one_axis_identity"].__setitem__("kernel_nonnegative", False),
        lambda p: p["one_axis_identity"].__setitem__("kernel_continuous_at_node", False),
        lambda p: p["one_axis_identity"].__setitem__("kernel_zero_order_at_origin", 1),
        lambda p: p["one_axis_identity"].__setitem__("kernel_mass", "1/16777216"),
        lambda p: p["order_contracts"].pop(),
        lambda p: p["order_contracts"][0]["tensor_telescoping"].__setitem__("mixed_derivatives_required", True),
        lambda p: p["order_contracts"][1]["tensor_telescoping"].__setitem__("pure_second_directional_terms", 25),
        lambda p: p["order_contracts"][0]["tensor_telescoping"]["axis_contracts"].pop(),
        lambda p: p["order_contracts"][0]["tensor_telescoping"].__setitem__("node_jet_substitution_for_global_integral_forbidden", False),
        lambda p: p["order_contracts"][1]["tensor_telescoping"].__setitem__("global_entrywise_supremum_before_group_assembly_forbidden", False),
        lambda p: p["order_contracts"][0]["decision"].__setitem__("complete_axis_remainder_numerically_bounded", True),
        lambda p: p["order_contracts"][1]["decision"].__setitem__("complete_integral_emitted", True),
        lambda p: p["decision"].__setitem__("complete_order_eleven_integral_emitted", True),
        lambda p: p["decision"].__setitem__("complete_order_twelve_integral_emitted", True),
        lambda p: p["decision"].__setitem__("native_K152_interval_emitted", True),
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
        raise AssertionError(f"K558 hostile rejection changed: {rejected}/{len(mutations)}")
    print(f"K558 probe passed {len(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
