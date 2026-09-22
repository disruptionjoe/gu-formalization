#!/usr/bin/env python3
"""Independent replay and hostile controls for K339."""

from __future__ import annotations

import copy
import importlib.util
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = Path(__file__).with_name("k339_order_seven_normalized_residual_composition.py")
MANIFEST = ROOT / "lab/process/k339-order-seven-normalized-residual-composition.json"


def load_producer():
    spec = importlib.util.spec_from_file_location("k339_probe_producer", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K339 producer")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    producer = load_producer()
    stored = json.loads(MANIFEST.read_text())
    replay = producer.build()
    producer.validate_payload(replay)
    if json.dumps(replay, sort_keys=True) != json.dumps(stored, sort_keys=True):
        raise AssertionError("deterministic K339 replay differs from stored manifest")

    prefactor = (2 * math.pi) ** -9
    raw = float(stored["normalized_order_seven_peano_residual"]["prefactor_free_six_axis_radius_upper"])
    normalized = float(stored["normalized_order_seven_peano_residual"]["radius_upper"])
    prefactor_lower = float(stored["normalization_ledger"]["native_prefactor_interval"]["lower"])
    prefactor_upper = float(stored["normalization_ledger"]["native_prefactor_interval"]["upper"])
    checks = {
        "prefactor_interval_ordered_and_matches_binary64_control": prefactor_lower < prefactor_upper and math.isclose((prefactor_lower + prefactor_upper) / 2, prefactor, rel_tol=3e-15, abs_tol=0),
        "normalized_radius_matches_independent_control": math.isclose(normalized, prefactor * raw, rel_tol=3e-15, abs_tol=0),
        "normalized_radius_is_finite_positive": math.isfinite(normalized) and normalized > 0,
        "occurrence_census": stored["fixed_control"]["stored_occurrences"] == 24,
        "group_census": stored["fixed_control"]["coherent_groups"] == 4,
        "ordered_term_census": stored["fixed_control"]["ordered_terms_per_group"] == 9,
        "value_and_peano_weights_differ": stored["fixed_control"]["K299_simplex_weight"] != stored["fixed_control"]["K318_y_Peano_mass"],
        "base_value_withheld": not stored["value_residual_separation"]["base_action_value_evaluated"],
        "complete_residual_withheld": not stored["value_residual_separation"]["complete_action_residual_evaluated"],
        "K152_withheld": not stored["decision"]["native_K152_interval_emitted"],
    }
    if not all(checks.values()):
        raise AssertionError(checks)

    mutations = [
        lambda p: p["fixed_control"].__setitem__("stored_occurrences", 23),
        lambda p: p["fixed_control"].__setitem__("coherent_groups", 3),
        lambda p: p["fixed_control"].__setitem__("ordered_terms_per_group", 6),
        lambda p: p["fixed_control"].__setitem__("K299_simplex_weight", "1/24"),
        lambda p: p["normalization_ledger"].__setitem__("K294_radial_simplex_density_already_inside_K338", False),
        lambda p: p["normalization_ledger"].__setitem__("K299_one_node_weight_not_applied_to_the_residual", False),
        lambda p: p["normalization_ledger"].__setitem__("K294_complete_bare_mass_is_a_replay_control_not_an_extra_multiplier", False),
        lambda p: p["normalization_ledger"].__setitem__("K318_chart_mass_not_multiplied_twice", False),
        lambda p: p["normalization_ledger"].__setitem__("only_outstanding_scalar_applied_here", "1/120"),
        lambda p: p["normalized_order_seven_peano_residual"].__setitem__("native_prefactor_applied_once", False),
        lambda p: p["value_residual_separation"].__setitem__("K334_zero_order_coefficient_is_a_base_cubature_value", True),
        lambda p: p["value_residual_separation"].__setitem__("base_action_value_evaluated", True),
        lambda p: p["value_residual_separation"].__setitem__("complete_action_residual_evaluated", True),
        lambda p: p["decision"].__setitem__("K294_normalization_composed_into_order_seven_peano_residual", False),
        lambda p: p["decision"].__setitem__("complete_order_seven_action_value_emitted", True),
        lambda p: p["decision"].__setitem__("native_K152_interval_emitted", True),
    ]
    rejected = 0
    for mutate in mutations:
        payload = copy.deepcopy(stored)
        mutate(payload)
        try:
            producer.validate_payload(payload)
        except AssertionError:
            rejected += 1
    if rejected != len(mutations):
        raise AssertionError(f"K339 hostile rejection changed: {rejected}/{len(mutations)}")
    print(f"K339 probe passed {len(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
