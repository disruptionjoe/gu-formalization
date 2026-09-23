#!/usr/bin/env python3
"""Deterministic replay and hostile controls for K346."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = Path(__file__).with_name("k346_order_eight_axis_jet_compiler.py")
STORED = ROOT / "lab/process/k346-order-eight-axis-jet-compiler.json"


def load():
    spec = importlib.util.spec_from_file_location("k346_probe_target", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K346 producer")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load()
    stored = json.loads(STORED.read_text())
    if stored != module.build():
        raise AssertionError("deterministic K346 replay differs")
    checks = [
        stored["fixed_control"]["paths"] == 192,
        stored["fixed_control"]["coherent_groups"] == 23,
        stored["fixed_control"]["upper_triangle_gram_entries_at_symmetric_node"] == 1296,
        stored["fixed_control"]["ordered_directional_entries"] == 2400,
        len(stored["axis_incidence"]) == 18,
        all(row["entries_touched"] > 0 for row in stored["axis_incidence"]),
        max(row["maximum_species_determinant_rank_touched"] for row in stored["axis_incidence"]) == 4,
        stored["jet_algebra"]["maximum_bessel_order_required"] == 3,
        stored["jet_algebra"]["determinants_differentiated_before_group_enclosure"],
        stored["jet_algebra"]["complete_group_quadratic_forms_differentiated_before_enclosure"],
        not stored["release_test"]["global_second_derivative_integrals_computed"],
        not stored["release_test"]["complete_order_eight_remainder_emitted"],
    ]
    if not all(checks):
        raise AssertionError("K346 control failed")
    mutations = [
        lambda p: p["fixed_control"].__setitem__("paths", 191),
        lambda p: p["fixed_control"].__setitem__("coherent_groups", 22),
        lambda p: p["fixed_control"].__setitem__("upper_triangle_gram_entries_at_symmetric_node", 1295),
        lambda p: p["fixed_control"].__setitem__("ordered_directional_entries", 2399),
        lambda p: p["fixed_control"].__setitem__("native_axes", p["fixed_control"]["native_axes"][:-1]),
        lambda p: p["fixed_control"].__setitem__("maximum_species_determinant_rank", 5),
        lambda p: p["axis_incidence"][0].__setitem__("entries_touched", 0),
        lambda p: p["jet_algebra"].__setitem__("maximum_bessel_order_required", 2),
        lambda p: p["jet_algebra"].__setitem__("determinants_differentiated_before_group_enclosure", False),
        lambda p: p["jet_algebra"].__setitem__("complete_group_quadratic_forms_differentiated_before_enclosure", False),
        lambda p: p["jet_algebra"].__setitem__("occurrencewise_absolute_value_used", True),
        lambda p: p["jet_algebra"].__setitem__("raw_zero_bessel_evaluation_used", True),
        lambda p: p["release_test"].__setitem__("all_18_native_axes_compiled", False),
        lambda p: p["release_test"].__setitem__("global_second_derivative_integrals_computed", True),
        lambda p: p["release_test"].__setitem__("complete_order_eight_remainder_emitted", True),
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
        raise AssertionError(f"K346 hostile rejection changed: {rejected}/{len(mutations)}")
    print(f"K346 probe passed {len(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
