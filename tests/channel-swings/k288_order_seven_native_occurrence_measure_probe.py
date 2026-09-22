#!/usr/bin/env python3
"""Independent replay and hostile controls for K288."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = Path(__file__).with_name("k288_order_seven_native_occurrence_measure.py")
MANIFEST = ROOT / "lab/process/k288-order-seven-native-occurrence-measure.json"


def load_producer():
    spec = importlib.util.spec_from_file_location("k288_for_probe", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K288 producer")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K288 = load_producer()


def validate(data: dict[str, Any]) -> None:
    fixed = data["fixed_control"]
    coherent = data["coherent_gram_measure"]
    change = data["native_coordinate_change"]
    release = data["release_test"]
    if (fixed["paths"], fixed["groups"], fixed["gram_entries_upper_triangle"]) != (
        96,
        16,
        408,
    ):
        raise AssertionError("order-seven census changed")
    if fixed["size_four_occurrences"] != 24:
        raise AssertionError("size-four occurrence count changed")
    if coherent["signed_weight_histogram"] != {"-2": 8, "1": 12, "2": 4}:
        raise AssertionError("signed occurrence weights changed")
    if coherent["signed_weight_sum"] != 4 or coherent["absolute_weight_sum"] != 36:
        raise AssertionError("signed/L1 occurrence totals changed")
    if change["internal_splits"]["pair_jacobian"] != "product_i a_i*b_i":
        raise AssertionError("pair-split Jacobian changed")
    if change["radial_projective_variables"]["pair_sum_jacobian"] != "x^7":
        raise AssertionError("radial-projective Jacobian changed")
    if not change["mass_replay"]["exact_match"]:
        raise AssertionError("native bare measure mass no longer replays")
    if not release["native_bare_measure_mass_replays_exactly"]:
        raise AssertionError("release mass gate changed")
    if release["complete_base_action_column_evaluated"]:
        raise AssertionError("K288 may not emit an action-column value")
    if "No weighted regularizer remainder" not in data["claim_ceiling"]:
        raise AssertionError("claim ceiling lost weighted-remainder boundary")


def mutate(data: dict[str, Any], name: str) -> dict[str, Any]:
    result = copy.deepcopy(data)
    if name == "occurrence_count":
        result["fixed_control"]["size_four_occurrences"] = 23
    elif name == "weight_histogram":
        result["coherent_gram_measure"]["signed_weight_histogram"]["-2"] = 7
    elif name == "weight_sum":
        result["coherent_gram_measure"]["signed_weight_sum"] = 36
    elif name == "pair_jacobian":
        result["native_coordinate_change"]["internal_splits"]["pair_jacobian"] = "1"
    elif name == "radial_jacobian":
        result["native_coordinate_change"]["radial_projective_variables"]["pair_sum_jacobian"] = "x^6"
    elif name == "mass":
        result["native_coordinate_change"]["mass_replay"]["exact_match"] = False
    elif name == "action_column":
        result["release_test"]["complete_base_action_column_evaluated"] = True
    elif name == "ceiling":
        result["claim_ceiling"] = "complete action column"
    else:
        raise KeyError(name)
    return result


def main() -> int:
    stored = json.loads(MANIFEST.read_text())
    replay = K288.certificate()
    checks = {
        "deterministic_manifest_replay": replay == stored,
        "complete_census": stored["fixed_control"]["gram_entries_upper_triangle"] == 408,
        "occurrence_weights": stored["coherent_gram_measure"]["absolute_weight_sum"] == 36,
        "pair_split_jacobian": stored["native_coordinate_change"]["internal_splits"]["pair_jacobian"] == "product_i a_i*b_i",
        "radial_projective_jacobian": stored["native_coordinate_change"]["radial_projective_variables"]["pair_sum_jacobian"] == "x^7",
        "bare_mass": stored["native_coordinate_change"]["mass_replay"]["exact_match"],
        "claim_ceiling": not stored["release_test"]["complete_base_action_column_evaluated"],
    }
    validate(stored)
    hostile = {}
    for name in (
        "occurrence_count",
        "weight_histogram",
        "weight_sum",
        "pair_jacobian",
        "radial_jacobian",
        "mass",
        "action_column",
        "ceiling",
    ):
        try:
            validate(mutate(stored, name))
        except (AssertionError, KeyError, TypeError):
            hostile[name] = True
        else:
            hostile[name] = False
    if not all(checks.values()) or not all(hostile.values()):
        raise AssertionError({"checks": checks, "hostile": hostile})
    print(json.dumps({"checks": checks, "hostile_rejections": hostile}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
