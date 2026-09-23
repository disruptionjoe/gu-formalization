#!/usr/bin/env python3
"""Deterministic replay and hostile mutations for K382."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PRODUCER = Path(__file__).with_name("k382_order_nine_axis_jet_compiler.py")
STORED = ROOT / "lab/process/k382-order-nine-axis-jet-compiler.json"


def load():
    spec = importlib.util.spec_from_file_location("k382_probe_target", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K382 producer")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load()
    stored = json.loads(STORED.read_text())
    if stored != module.build():
        raise AssertionError("deterministic K382 replay differs")
    checks = [
        stored["fixed_control"]["paths"] == 256,
        stored["fixed_control"]["coherent_groups"] == 20,
        stored["fixed_control"]["upper_triangle_gram_entries_at_symmetric_node"] == 2368,
        stored["fixed_control"]["ordered_directional_entries"] == 4480,
        stored["fixed_control"]["maximum_species_determinant_rank"] == 5,
        len(stored["fixed_control"]["native_axes"]) == 20,
        len(stored["axis_incidence"]) == 20,
        all(row["entries_touched"] > 0 for row in stored["axis_incidence"]),
        stored["compiled_entry_interface"]["entry_count"] == 4480,
        stored["jet_algebra"]["off_diagonal_group_entries_kept_in_both_ordered_orientations"],
        stored["jet_algebra"]["maximum_zero_safe_scaled_primitive_order_available"] == 10,
        not stored["release_test"]["complete_order_nine_remainder_emitted"],
    ]
    if not all(checks):
        raise AssertionError("K382 control failed")
    mutations = [
        lambda p: p["fixed_control"].__setitem__("paths", 255),
        lambda p: p["fixed_control"].__setitem__("coherent_groups", 19),
        lambda p: p["fixed_control"].__setitem__("upper_triangle_gram_entries_at_symmetric_node", 2367),
        lambda p: p["fixed_control"].__setitem__("ordered_directional_entries", 4479),
        lambda p: p["fixed_control"].__setitem__("maximum_species_determinant_rank", 4),
        lambda p: p["fixed_control"].__setitem__("native_axes", p["fixed_control"]["native_axes"][:-1]),
        lambda p: p["jet_algebra"].__setitem__("off_diagonal_group_entries_kept_in_both_ordered_orientations", False),
        lambda p: p["jet_algebra"].__setitem__("occurrencewise_absolute_value_used", True),
        lambda p: p["jet_algebra"].__setitem__("maximum_zero_safe_scaled_primitive_order_available", 8),
        lambda p: p["release_test"].__setitem__("complete_order_nine_remainder_emitted", True),
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
        raise AssertionError("K382 hostile mutation survived")
    print(f"K382 order-nine axis-jet compiler probe passed ({sum(checks)}/{len(checks)} controls; {rejected}/{len(mutations)} hostile mutations rejected)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
