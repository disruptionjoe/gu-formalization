#!/usr/bin/env python3
"""Independent replay and hostile controls for K336."""

from __future__ import annotations

import copy
import importlib.util
import json
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PRODUCER = HERE / "k336_order_seven_axis_native_map_bank.py"
MANIFEST = ROOT / "lab/process/k336-order-seven-axis-native-map-bank.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k336_probe_backend", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K336 producer")
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
        raise AssertionError("deterministic replay differs from stored K336 manifest")

    controls = 0
    classes = stored["axis_native_gap_classes"]
    if len(classes) != stored["fixed_control"]["unique_gap_box_class_count"]:
        raise AssertionError("gap class count mismatch")
    controls += 1
    for item in classes:
        for axis, row in enumerate(item["axes"]):
            bary = [Fraction(value) for value in row["barycentric_control"]]
            if sum(bary) != 0 or bary[axis] <= 0 or any(value for value in bary[:axis]) or any(value >= 0 for value in bary[axis + 1:]):
                raise AssertionError("barycentric Duffy direction malformed")
    controls += 1
    if stored["fixed_control"]["native_projective_linear_factor_count"] != 24:
        raise AssertionError("projective factor census mismatch")
    controls += 1
    if stored["map_release"]["K299_peano_masses"] != {"t0": "1/504", "t1": "1/300", "t2": "1/160", "t3": "1/72", "t4": "1/24"}:
        raise AssertionError("Peano mass bank changed")
    controls += 1
    if stored["face_tail_degree_ledger"]["s0_remaining_integrated_powers_value_first_second"] != [1, 1, 1]:
        raise AssertionError("s0 ledger changed")
    controls += 1
    if stored["face_tail_degree_ledger"]["s1_remaining_integrated_powers_value_first_second"] != [26, 25, 24]:
        raise AssertionError("s1 ledger changed")
    controls += 1
    if not stored["release_test"]["every_K334_finite_leaf_mapped_once"]:
        raise AssertionError("leaf release test failed")
    controls += 1
    if stored["release_test"]["native_K152_interval_emitted"]:
        raise AssertionError("K152 overclaim")
    controls += 1

    mutants = [
        lambda p: p["fixed_control"].__setitem__("accepted_subdivision_checksum", "sha256:bad"),
        lambda p: p["leaf_class_map"].pop(),
        lambda p: p["axis_native_gap_classes"].pop(),
        lambda p: p["axis_native_gap_classes"][0]["axes"][0].__setitem__("sum_dp_dt_exact", "1"),
        lambda p: p["axis_native_gap_classes"][0]["axes"][0].__setitem__("d2p_dt2_exact", ["1"] * 6),
        lambda p: p["axis_native_gap_classes"][0]["axes"][0].__setitem__("native_projective_polynomial_value_first_second_intervals", []),
        lambda p: p["axis_native_gap_classes"][0]["axes"][0]["shared_entry_normalized_argument_directions"].__setitem__("D4_normalized_argument_direction_matrix", []),
        lambda p: p["shared_entry_directional_jet_map"].__setitem__("D4_maximum_kernel_derivative_order", 7),
        lambda p: p["shared_entry_directional_jet_map"].__setitem__("bordered_B5_maximum_kernel_derivative_order", 5),
        lambda p: p["shared_entry_directional_jet_map"].__setitem__("literal_zero_slots", []),
        lambda p: p["face_tail_degree_ledger"].__setitem__("worst_gap_face_second_derivative_integrability_margin", 0),
        lambda p: p["face_tail_degree_ledger"].__setitem__("radial_tail_integrand_powers_value_first_second", [34, 35, 36]),
        lambda p: p["map_release"].__setitem__("all_K335_missing_map_classes_serialized", False),
        lambda p: p["decision"].__setitem__("complete_gap_axis_constants_emitted", True),
        lambda p: p["decision"].__setitem__("k294_gamma_join_released", True),
    ]
    for mutate in mutants:
        must_fail(module, stored, mutate)

    print(f"K336 axis-native map probe passed {controls}/{controls} controls and rejected {len(mutants)}/{len(mutants)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
