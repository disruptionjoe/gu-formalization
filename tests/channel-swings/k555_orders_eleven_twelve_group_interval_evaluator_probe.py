#!/usr/bin/env python3
"""Deterministic replay and hostile mutations for K555."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PRODUCER = HERE / "k555_orders_eleven_twelve_group_interval_evaluator.py"
MANIFEST = ROOT / "lab/process/k555-orders-eleven-twelve-group-interval-evaluator.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k555_probe_target", PRODUCER)
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
        stored["fixed_control"]["combined_upper_triangle_entries"] == 48272,
        stored["fixed_control"]["combined_ordered_terms"] == 94752,
        [row["fixed_control"]["positive_time_variables"] for row in stored["order_evaluations"]] == [24, 26],
        [row["fixed_control"]["native_prefactor"] for row in stored["order_evaluations"]] == ["(2*pi)^-13", "(2*pi)^-14"],
        all(row["complete_node_evaluation"]["signed_rule_value_is_strictly_positive"] for row in stored["order_evaluations"]),
        all(stored["release_test"].values()),
    ]
    mutations = []
    for mutate in (
        lambda p: p["fixed_control"].__setitem__("combined_paths", 1791),
        lambda p: p["fixed_control"].__setitem__("combined_groups", 56),
        lambda p: p["fixed_control"].__setitem__("combined_upper_triangle_entries", 48271),
        lambda p: p["fixed_control"].__setitem__("combined_ordered_terms", 94751),
        lambda p: p["order_evaluations"][0]["fixed_control"].__setitem__("maximum_species_determinant_rank", 5),
        lambda p: p["order_evaluations"][1]["fixed_control"].__setitem__("native_prefactor", "(2*pi)^-13"),
        lambda p: p["order_evaluations"][0]["assembly_contract"].__setitem__("occurrencewise_absolute_value_used", True),
        lambda p: p["order_evaluations"][1]["assembly_contract"].__setitem__("order_ten_weight_or_prefactor_reused", True),
        lambda p: p["decision"].__setitem__("complete_order_eleven_integral_emitted", True),
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
        raise AssertionError(f"K555 probe failed: controls={controls}, mutations={mutations}")
    print(f"K555 probe: {sum(controls)}/{len(controls)} controls; {sum(mutations)}/{len(mutations)} hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
