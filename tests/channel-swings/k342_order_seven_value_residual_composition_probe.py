#!/usr/bin/env python3
"""Independent replay and hostile controls for K342."""

from __future__ import annotations

import copy
import importlib.util
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = Path(__file__).with_name("k342_order_seven_value_residual_composition.py")
STORED = ROOT / "lab/process/k342-order-seven-value-residual-composition.json"


def load():
    spec = importlib.util.spec_from_file_location("k342_probe_producer", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K342 producer")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load()
    stored = json.loads(STORED.read_text())
    replay = module.build()
    module.validate_payload(replay)
    if replay != stored:
        raise AssertionError("deterministic K342 replay differs")
    base = float(stored["normalized_base_value"]["radius_upper"])
    residual = float(stored["normalized_peano_residual"]["radius_upper"])
    complete = float(stored["complete_order_seven_cubature_enclosure"]["radius_upper"])
    checks = [
        stored["fixed_control"]["coherent_groups"] == 4,
        stored["fixed_control"]["ordered_terms_per_group"] == 9,
        math.isfinite(base) and base > 0,
        stored["normalized_base_value"]["radius_upper"] == module.EXPECTED_NORMALIZED_BASE_UPPER,
        residual == 0.004477466184517202,
        complete >= base + residual,
        stored["complete_order_seven_cubature_enclosure"]["radius_upper"] == module.EXPECTED_COMPLETE_UPPER,
        stored["normalization_ledger"]["native_prefactor_applied_to_base_value_once"],
        not stored["normalization_ledger"]["K294_bare_mass_applied_again"],
        not stored["normalization_ledger"]["K318_y_Peano_mass_applied_to_value"],
        not stored["normalized_base_value"]["signed_center_determined"],
        not stored["normalized_peano_residual"]["recomputed_or_rescaled"],
        stored["complete_order_seven_cubature_enclosure"]["base_and_residual_kept_distinct"],
        not stored["decision"]["native_K152_interval_emitted"],
    ]
    if not all(checks):
        raise AssertionError("K342 control failed")
    mutations = [
        lambda p: p["fixed_control"].__setitem__("simplex_weight", "1/24"),
        lambda p: p["normalization_ledger"].__setitem__("native_prefactor_applied_to_base_value_once", False),
        lambda p: p["normalization_ledger"].__setitem__("K294_bare_mass_applied_again", True),
        lambda p: p["normalization_ledger"].__setitem__("K318_y_Peano_mass_applied_to_value", True),
        lambda p: p["normalized_base_value"].__setitem__("radius_upper", "inf"),
        lambda p: p["normalized_base_value"].__setitem__("radius_upper", "1e-13"),
        lambda p: p["normalized_peano_residual"].__setitem__("radius_upper", "0.004"),
        lambda p: p["normalized_peano_residual"].__setitem__("recomputed_or_rescaled", True),
        lambda p: p["complete_order_seven_cubature_enclosure"].__setitem__("base_and_residual_kept_distinct", False),
        lambda p: p["complete_order_seven_cubature_enclosure"].__setitem__("radius_upper", "1e-15"),
        lambda p: p["complete_order_seven_cubature_enclosure"].__setitem__("radius_upper", "0.005"),
        lambda p: p["decision"].__setitem__("order_seven_signed_center_determined", True),
        lambda p: p["decision"].__setitem__("complete_R_ref_residual_evaluated", True),
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
        raise AssertionError(f"K342 hostile rejection changed: {rejected}/{len(mutations)}")
    print(f"K342 probe passed {len(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
