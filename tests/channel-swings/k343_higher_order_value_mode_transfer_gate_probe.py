#!/usr/bin/env python3
"""Independent replay and hostile controls for K343."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = Path(__file__).with_name("k343_higher_order_value_mode_transfer_gate.py")
STORED = ROOT / "lab/process/k343-higher-order-value-mode-transfer-gate.json"


def load():
    spec = importlib.util.spec_from_file_location("k343_probe_producer", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K343 producer")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load()
    stored = json.loads(STORED.read_text())
    replay = module.build()
    module.validate_payload(replay)
    if replay != stored:
        raise AssertionError("deterministic K343 replay differs")
    rows = {int(row["order"]): row for row in stored["orders"]}
    groups = stored["exact_generic_coherence_interface"]["group_records"]
    checks = [
        stored["fixed_control"]["higher_order_paths"] == 2720,
        stored["fixed_control"]["higher_order_groups"] == 128,
        stored["fixed_control"]["higher_order_upper_triangle_gram_entries"] == 58826,
        stored["fixed_control"]["higher_order_ordered_quadratic_terms"] == 114932,
        len(groups) == 128,
        sum(row["path_count"] for row in groups) == 2720,
        sum(row["upper_triangle_gram_entries"] for row in groups) == 58826,
        sum(row["ordered_quadratic_terms"] for row in groups) == 114932,
        rows[8]["maximum_species_determinant_rank"] == 4,
        rows[9]["maximum_species_determinant_rank"] == 5,
        rows[11]["maximum_species_determinant_rank"] == 6,
        rows[12]["native_prefactor"] == "(2*pi)^-14",
        all(row["crude_origin_power_after_bessel_factors"] == row["order"] - 1 for row in rows.values()),
        stored["exact_generic_coherence_interface"]["all_coherent_cross_terms_retained"],
        not stored["exact_generic_coherence_interface"]["occurrencewise_absolute_value_permitted"],
        not stored["transfer_audit"]["K341_is_dimension_free_integrator"],
        not stored["decision"]["numerical_order_eight_value_emitted"],
        not stored["decision"]["native_K152_interval_emitted"],
    ]
    if not all(checks):
        raise AssertionError("K343 control failed")
    mutations = [
        lambda p: p["fixed_control"].__setitem__("higher_order_paths", 2719),
        lambda p: p["fixed_control"].__setitem__("higher_order_groups", 127),
        lambda p: p["fixed_control"].__setitem__("higher_order_upper_triangle_gram_entries", 58825),
        lambda p: p["orders"][0].__setitem__("old_position_support", [1, 3, 5]),
        lambda p: p["orders"][0].__setitem__("maximum_species_determinant_rank", 5),
        lambda p: p["orders"][1].__setitem__("maximum_species_determinant_rank", 4),
        lambda p: p["orders"][3].__setitem__("new_rank_calculus_required", [5]),
        lambda p: p["exact_generic_coherence_interface"].__setitem__("all_K179_coefficients_retained", False),
        lambda p: p["exact_generic_coherence_interface"].__setitem__("all_contracted_positions_retained", False),
        lambda p: p["exact_generic_coherence_interface"].__setitem__("all_coherent_cross_terms_retained", False),
        lambda p: p["exact_generic_coherence_interface"].__setitem__("occurrencewise_absolute_value_permitted", True),
        lambda p: p["transfer_audit"].__setitem__("K341_is_dimension_free_integrator", True),
        lambda p: p["decision"].__setitem__("direct_reuse_route_rejected", False),
        lambda p: p["decision"].__setitem__("numerical_order_eight_value_emitted", True),
        lambda p: p["decision"].__setitem__("orders_eight_through_twelve_action_column_emitted", True),
        lambda p: p["decision"].__setitem__("complete_R_ref_residual_emitted", True),
        lambda p: p["decision"].__setitem__("native_K152_interval_emitted", True),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(stored)
        mutate(candidate)
        try:
            module.validate_payload(candidate)
        except (AssertionError, ValueError):
            rejected += 1
    if rejected != len(mutations):
        raise AssertionError(f"K343 hostile rejection changed: {rejected}/{len(mutations)}")
    print(f"K343 probe passed {len(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
