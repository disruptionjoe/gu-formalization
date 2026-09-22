#!/usr/bin/env python3
"""Deterministic replay and hostile controls for K337."""

from __future__ import annotations

import copy
import importlib.util
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PRODUCER = HERE / "k337_order_seven_gap_axis_leaf_evaluator.py"
MANIFEST = ROOT / "lab/process/k337-order-seven-gap-axis-leaf-evaluator.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k337_probe_backend", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K337 producer")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def must_fail(module, payload, mutate) -> None:
    candidate = copy.deepcopy(payload)
    mutate(candidate)
    try:
        module.validate_payload(candidate)
    except AssertionError:
        return
    raise AssertionError("hostile mutation escaped")


def main() -> int:
    module = load_module()
    stored = json.loads(MANIFEST.read_text())
    replay = module.build()
    module.validate_payload(stored)
    if replay != stored:
        raise AssertionError("deterministic replay differs from stored K337 manifest")

    bank = stored["reference_positive_slab_bank"]
    controls = 0
    if bank["D4_complete_permutation_count"] != 24 or bank["bordered_B5_complete_permutation_count"] != 120:
        raise AssertionError("complete permutation census changed")
    controls += 1
    if len(bank["summed_value_first_second_abs_uppers"]) != 3 or any(not math.isfinite(float(value)) or float(value) <= 0 for value in bank["summed_value_first_second_abs_uppers"]):
        raise AssertionError("summed reference bank invalid")
    controls += 1
    if not stored["release_test"]["K334_checksum_replayed"] or not stored["release_test"]["all_class_axis_bounds_finite_positive"]:
        raise AssertionError("release replay failed")
    controls += 1
    if not bank["right_endpoint_bank_obtained_by_exact_transpose"]:
        raise AssertionError("endpoint transpose control failed")
    controls += 1
    if stored["release_test"]["native_K152_interval_emitted"]:
        raise AssertionError("K152 overclaim")
    controls += 1

    mutants = [
        lambda p: p["fixed_control"].__setitem__("accepted_subdivision_checksum", "sha256:bad"),
        lambda p: p["reference_positive_slab_bank"]["rows"].pop(),
        lambda p: p["reference_positive_slab_bank"].__setitem__("class_axis_evaluation_count", 1),
        lambda p: p["reference_positive_slab_bank"]["rows"][0].__setitem__("axes", []),
        lambda p: p["reference_positive_slab_bank"]["rows"][0]["axes"][0].__setitem__("complete_value_first_second_abs_uppers", []),
        lambda p: p["reference_positive_slab_bank"].__setitem__("shared_entry_interval_substitution_precedes_complete_determinant_coefficient_enclosure", False),
        lambda p: p["reference_positive_slab_bank"].__setitem__("literal_border_zeros_retained", False),
        lambda p: p["reference_positive_slab_bank"].__setitem__("terminal_gap_direction_exactly_zero_on_reference_map", False),
        lambda p: p["scope_boundary"].__setitem__("reference_bank_is_not_a_gap_axis_constant", False),
        lambda p: p["decision"].__setitem__("complete_gap_axis_constants_emitted", True),
        lambda p: p["decision"].__setitem__("complete_six_axis_peano_norm_emitted", True),
        lambda p: p["decision"].__setitem__("k294_gamma_join_released", True),
    ]
    for mutate in mutants:
        must_fail(module, stored, mutate)

    print(f"K337 gap-axis evaluator probe passed {controls}/{controls} controls and rejected {len(mutants)}/{len(mutants)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
