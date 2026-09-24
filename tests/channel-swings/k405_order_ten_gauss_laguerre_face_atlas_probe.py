#!/usr/bin/env python3
"""Independent replay and hostile mutations for K405."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PRODUCER = Path(__file__).with_name("k405_order_ten_gauss_laguerre_face_atlas.py")
STORED = ROOT / "lab/process/k405-order-ten-gauss-laguerre-face-atlas.json"


def load():
    spec = importlib.util.spec_from_file_location("k405_probe_target", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K405 producer")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load()
    stored = json.loads(STORED.read_text())
    if stored != module.build():
        raise AssertionError("deterministic K405 replay differs")
    checks = [
        stored["fixed_control"]["paths"] == 480,
        stored["fixed_control"]["coherent_groups"] == 28,
        stored["fixed_control"]["upper_triangle_gram_entries"] == 6890,
        stored["fixed_control"]["ordered_quadratic_terms"] == 13300,
        stored["fixed_control"]["maximum_species_determinant_rank"] == 5,
        stored["positive_product_gauss_laguerre_rule"]["product_weight"] == f"1/{256**22}",
        stored["radial_angular_replay"]["node_replays_all_twenty_two_times_at_1_over_256"],
        stored["cumulative_time_face_atlas"]["upper_triangle_entries_covered"] == 6890,
        stored["cumulative_time_face_atlas"]["unique_kernel_zero_masks"] > 0,
        stored["cumulative_time_face_atlas"]["unique_row_coalescence_masks"] > 0,
        stored["cumulative_time_face_atlas"]["unique_column_coalescence_masks"] > 0,
        stored["remainder_interface"]["pure_second_derivative_axes"] == 22,
        not stored["decision"]["complete_order_ten_integral_emitted"],
    ]
    if not all(checks):
        raise AssertionError("K405 control failed")
    mutations = [
        lambda p: p["fixed_control"].__setitem__("paths", 479),
        lambda p: p["fixed_control"].__setitem__("coherent_groups", 27),
        lambda p: p["fixed_control"].__setitem__("upper_triangle_gram_entries", 6889),
        lambda p: p["fixed_control"].__setitem__("ordered_quadratic_terms", 13299),
        lambda p: p["fixed_control"].__setitem__("maximum_species_determinant_rank", 4),
        lambda p: p["positive_product_gauss_laguerre_rule"].__setitem__("axis_node", "1/255"),
        lambda p: p["positive_product_gauss_laguerre_rule"].__setitem__("axis_weight", "1/255"),
        lambda p: p["positive_product_gauss_laguerre_rule"]["peano_kernel"].__setitem__("nonnegative", False),
        lambda p: p["cumulative_time_face_atlas"].__setitem__("upper_triangle_entries_covered", 2367),
        lambda p: p["cumulative_time_face_atlas"].__setitem__("occurrencewise_absolute_value_permitted", True),
        lambda p: p["remainder_interface"].__setitem__("pure_second_derivative_axes", 21),
        lambda p: p["release_test"].__setitem__("complete_order_ten_integral_emitted", True),
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
        raise AssertionError("K405 hostile mutation survived")
    print(f"K405 order-ten face-atlas probe passed ({sum(checks)}/{len(checks)} controls; {rejected}/{len(mutations)} hostile mutations rejected)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
