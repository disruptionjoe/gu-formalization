#!/usr/bin/env python3
"""Independent replay and hostile controls for K340."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = Path(__file__).with_name("k340_order_seven_barycentric_value_atlas.py")
STORED = ROOT / "lab/process/k340-order-seven-barycentric-value-atlas.json"


def load():
    spec = importlib.util.spec_from_file_location("k340_probe_producer", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K340 producer")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load()
    stored = json.loads(STORED.read_text())
    replay = module.build()
    module.validate_payload(replay)
    if replay != stored:
        raise AssertionError("deterministic K340 replay differs")
    checks = [
        stored["fixed_control"]["simplex_node"] == ["1/6"] * 6,
        stored["fixed_control"]["y_node"] == "1/2",
        stored["fixed_control"]["coherent_groups"] == 4,
        stored["value_mode_terminal_split_atlas"]["sector_count"] == 2,
        stored["value_mode_terminal_split_atlas"]["exact_sector_mass_sum"] == "1",
        stored["coverage"]["all_eight_split_variables_retained"],
        stored["coverage"]["left_right_sectors_related_by_exact_transpose"],
        not stored["value_mode_terminal_split_atlas"]["K318_Peano_kernel_used"],
        not stored["value_mode_terminal_split_atlas"]["raw_Bessel_zero_evaluation_used"],
        not stored["decision"]["full_radial_projective_value_integrated"],
    ]
    if not all(checks):
        raise AssertionError("K340 control failed")
    mutations = [
        lambda p: p["fixed_control"].__setitem__("y_node", "1/3"),
        lambda p: p["fixed_control"].__setitem__("simplex_weight", "1/24"),
        lambda p: p["value_mode_terminal_split_atlas"].__setitem__("sector_count", 1),
        lambda p: p["value_mode_terminal_split_atlas"].__setitem__("exact_sector_mass_sum", "1/2"),
        lambda p: p["value_mode_terminal_split_atlas"].__setitem__("K318_Peano_kernel_used", True),
        lambda p: p["value_mode_terminal_split_atlas"].__setitem__("K318_endpoint_Hepp_weight_used", True),
        lambda p: p["value_mode_terminal_split_atlas"].__setitem__("raw_Bessel_zero_evaluation_used", True),
        lambda p: p["value_mode_terminal_split_atlas"].__setitem__("detached_terminal_cofactor_used", True),
        lambda p: p["coverage"].__setitem__("all_eight_split_variables_retained", False),
        lambda p: p["decision"].__setitem__("full_radial_projective_value_integrated", True),
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
        raise AssertionError(f"K340 hostile rejection changed: {rejected}/{len(mutations)}")
    print(f"K340 probe passed {len(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
