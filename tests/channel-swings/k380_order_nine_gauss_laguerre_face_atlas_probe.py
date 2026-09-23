#!/usr/bin/env python3
"""Independent replay and hostile mutations for K380."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PRODUCER = Path(__file__).with_name("k380_order_nine_gauss_laguerre_face_atlas.py")
STORED = ROOT / "lab/process/k380-order-nine-gauss-laguerre-face-atlas.json"


def load():
    spec = importlib.util.spec_from_file_location("k380_probe_target", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K380 producer")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load()
    stored = json.loads(STORED.read_text())
    if stored != module.build():
        raise AssertionError("deterministic K380 replay differs")
    checks = [
        stored["fixed_control"]["paths"] == 256,
        stored["fixed_control"]["coherent_groups"] == 20,
        stored["fixed_control"]["upper_triangle_gram_entries"] == 2368,
        stored["fixed_control"]["ordered_quadratic_terms"] == 4480,
        stored["fixed_control"]["maximum_species_determinant_rank"] == 5,
        stored["positive_product_gauss_laguerre_rule"]["product_weight"] == f"1/{256**20}",
        stored["radial_angular_replay"]["node_replays_all_twenty_times_at_1_over_256"],
        stored["cumulative_time_face_atlas"]["upper_triangle_entries_covered"] == 2368,
        stored["cumulative_time_face_atlas"]["unique_kernel_zero_masks"] > 0,
        stored["cumulative_time_face_atlas"]["unique_row_coalescence_masks"] > 0,
        stored["cumulative_time_face_atlas"]["unique_column_coalescence_masks"] > 0,
        stored["remainder_interface"]["pure_second_derivative_axes"] == 20,
        not stored["decision"]["complete_order_nine_integral_emitted"],
    ]
    if not all(checks):
        raise AssertionError("K380 control failed")
    mutations = [
        lambda p: p["fixed_control"].__setitem__("paths", 255),
        lambda p: p["fixed_control"].__setitem__("coherent_groups", 19),
        lambda p: p["fixed_control"].__setitem__("upper_triangle_gram_entries", 2367),
        lambda p: p["fixed_control"].__setitem__("ordered_quadratic_terms", 4479),
        lambda p: p["fixed_control"].__setitem__("maximum_species_determinant_rank", 4),
        lambda p: p["positive_product_gauss_laguerre_rule"].__setitem__("axis_node", "1/255"),
        lambda p: p["positive_product_gauss_laguerre_rule"].__setitem__("axis_weight", "1/255"),
        lambda p: p["positive_product_gauss_laguerre_rule"]["peano_kernel"].__setitem__("nonnegative", False),
        lambda p: p["cumulative_time_face_atlas"].__setitem__("upper_triangle_entries_covered", 2367),
        lambda p: p["cumulative_time_face_atlas"].__setitem__("occurrencewise_absolute_value_permitted", True),
        lambda p: p["remainder_interface"].__setitem__("pure_second_derivative_axes", 18),
        lambda p: p["release_test"].__setitem__("complete_order_nine_integral_emitted", True),
    ]
    rejected = 0
    for mutation in mutations:
        candidate = copy.deepcopy(stored)
        mutation(candidate)
        try:
            module.validate_payload(candidate)
        except AssertionError:
            rejected += 1
    if rejected != len(mutations):
        raise AssertionError("K380 hostile mutation survived")
    print(f"K380 order-nine face-atlas probe passed ({sum(checks)}/{len(checks)} controls; {rejected}/{len(mutations)} hostile mutations rejected)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
