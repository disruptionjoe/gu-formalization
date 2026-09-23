#!/usr/bin/env python3
"""Independent replay and hostile controls for K344."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = Path(__file__).with_name("k344_order_eight_gauss_laguerre_face_atlas.py")
STORED = ROOT / "lab/process/k344-order-eight-gauss-laguerre-face-atlas.json"


def load():
    spec = importlib.util.spec_from_file_location("k344_probe_target", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K344 producer")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load()
    stored = json.loads(STORED.read_text())
    rebuilt = module.build()
    if stored != rebuilt:
        raise AssertionError("deterministic K344 replay differs")
    checks = [
        stored["fixed_control"]["paths"] == 192,
        stored["fixed_control"]["coherent_groups"] == 23,
        stored["fixed_control"]["upper_triangle_gram_entries"] == 1296,
        stored["positive_product_gauss_laguerre_rule"]["axis_node"] == "1/256",
        stored["positive_product_gauss_laguerre_rule"]["node_count"] == 1,
        stored["positive_product_gauss_laguerre_rule"]["peano_kernel"]["nonnegative"],
        stored["radial_angular_replay"]["node_replays_all_eighteen_times_at_1_over_256"],
        stored["cumulative_time_face_atlas"]["upper_triangle_entries_covered"] == 1296,
        stored["cumulative_time_face_atlas"]["unique_kernel_zero_masks"] > 0,
        stored["cumulative_time_face_atlas"]["unique_row_coalescence_masks"] > 0,
        stored["cumulative_time_face_atlas"]["unique_column_coalescence_masks"] > 0,
        stored["remainder_interface"]["pure_second_derivative_axes"] == 18,
        not stored["remainder_interface"]["mixed_derivatives_required"],
        not stored["decision"]["complete_order_eight_integral_emitted"],
        not stored["release_test"]["native_K152_interval_emitted"],
    ]
    if not all(checks):
        raise AssertionError("K344 control failed")
    mutations = [
        lambda p: p["fixed_control"].__setitem__("paths", 191),
        lambda p: p["fixed_control"].__setitem__("coherent_groups", 22),
        lambda p: p["fixed_control"].__setitem__("upper_triangle_gram_entries", 1295),
        lambda p: p["positive_product_gauss_laguerre_rule"].__setitem__("axis_node", "1/255"),
        lambda p: p["positive_product_gauss_laguerre_rule"].__setitem__("axis_weight", "1/255"),
        lambda p: p["positive_product_gauss_laguerre_rule"].__setitem__("product_weight", "1/256"),
        lambda p: p["positive_product_gauss_laguerre_rule"].__setitem__("all_weights_strictly_positive", False),
        lambda p: p["positive_product_gauss_laguerre_rule"]["peano_kernel"].__setitem__("nonnegative", False),
        lambda p: p["cumulative_time_face_atlas"].__setitem__("upper_triangle_entries_covered", 1295),
        lambda p: p["cumulative_time_face_atlas"].__setitem__("complete_group_quadratic_form_precedes_absolute_enclosure", False),
        lambda p: p["cumulative_time_face_atlas"].__setitem__("occurrencewise_absolute_value_permitted", True),
        lambda p: p["remainder_interface"].__setitem__("pure_second_derivative_axes", 17),
        lambda p: p["remainder_interface"].__setitem__("mixed_derivatives_required", True),
        lambda p: p["decision"].__setitem__("native_order_eight_positive_value_rule_emitted", False),
        lambda p: p["decision"].__setitem__("group_level_node_evaluator_emitted", True),
        lambda p: p["decision"].__setitem__("complete_order_eight_remainder_emitted", True),
        lambda p: p["decision"].__setitem__("complete_order_eight_integral_emitted", True),
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
        raise AssertionError(f"K344 hostile rejection changed: {rejected}/{len(mutations)}")
    print(f"K344 probe passed {len(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
