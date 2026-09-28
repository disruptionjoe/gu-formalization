#!/usr/bin/env python3
"""Deterministic replay and hostile mutations for K556."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PRODUCER = HERE / "k556_orders_eleven_twelve_axis_jet_compiler.py"
MANIFEST = ROOT / "lab/process/k556-orders-eleven-twelve-axis-jet-compiler.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k556_probe_target", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {PRODUCER}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load_module()
    stored = json.loads(MANIFEST.read_text())
    rebuilt = module.build()
    module.validate_payload(rebuilt)
    controls = [
        stored == rebuilt,
        stored["fixed_control"]["combined_paths"] == 1792,
        stored["fixed_control"]["combined_groups"] == 57,
        stored["fixed_control"]["combined_symmetric_node_entries"] == 48272,
        stored["fixed_control"]["combined_ordered_directional_entries"] == 94752,
        stored["fixed_control"]["combined_native_axes"] == 50,
        [len(row["fixed_control"]["native_axes"]) for row in stored["order_interfaces"]] == [24, 26],
        all(row["release_test"]["every_axis_touches_an_entry"] for row in stored["order_interfaces"]),
        stored["jet_algebra"]["off_diagonal_group_entries_kept_in_both_ordered_orientations"],
        stored["jet_algebra"]["maximum_zero_safe_scaled_primitive_order_available"] == 12,
        all(stored["release_test"].values()),
    ]
    mutations = []
    for mutate in (
        lambda p: p["fixed_control"].__setitem__("combined_paths", 1791),
        lambda p: p["fixed_control"].__setitem__("combined_groups", 56),
        lambda p: p["fixed_control"].__setitem__("combined_symmetric_node_entries", 48271),
        lambda p: p["fixed_control"].__setitem__("combined_ordered_directional_entries", 94751),
        lambda p: p["fixed_control"].__setitem__("combined_native_axes", 49),
        lambda p: p["order_interfaces"][0]["fixed_control"].__setitem__("maximum_species_determinant_rank", 5),
        lambda p: p["order_interfaces"][1]["fixed_control"].__setitem__("native_axes", p["order_interfaces"][1]["fixed_control"]["native_axes"][:-1]),
        lambda p: p["jet_algebra"].__setitem__("off_diagonal_group_entries_kept_in_both_ordered_orientations", False),
        lambda p: p["jet_algebra"].__setitem__("maximum_zero_safe_scaled_primitive_order_available", 10),
        lambda p: p["decision"].__setitem__("complete_order_twelve_integral_emitted", True),
        lambda p: p["release_test"].__setitem__("native_K152_interval_not_emitted", False),
    ):
        candidate = copy.deepcopy(stored)
        mutate(candidate)
        try:
            module.validate_payload(candidate)
        except AssertionError:
            mutations.append(True)
        else:
            mutations.append(False)
    if not all(controls) or not all(mutations):
        raise AssertionError(f"K556 probe failed: controls={controls}, mutations={mutations}")
    print(f"K556 probe: {sum(controls)}/{len(controls)} controls; {sum(mutations)}/{len(mutations)} hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
