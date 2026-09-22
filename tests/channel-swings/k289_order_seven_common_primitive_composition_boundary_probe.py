#!/usr/bin/env python3
"""Independent replay and hostile controls for K289."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = Path(__file__).with_name("k289_order_seven_common_primitive_composition_boundary.py")
MANIFEST = ROOT / "lab/process/k289-order-seven-common-primitive-composition-boundary.json"


def load_producer():
    spec = importlib.util.spec_from_file_location("k289_for_probe", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K289 producer")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K289 = load_producer()


def validate(data: dict[str, Any]) -> None:
    fixed = data["fixed_control"]
    census = data["dependency_census"]
    decision = data["composition_decision"]
    release = data["release_test"]
    if fixed["size_four_occurrences"] != 24:
        raise AssertionError("occurrence count changed")
    if len(fixed["native_variables"]) != 16:
        raise AssertionError("native common chart lost variables")
    if not census["all_size_four_factors_pair_sum_only"]:
        raise AssertionError("size-four pair-sum identity lost")
    if not census["all_companion_size_three_factors_split_dependent"]:
        raise AssertionError("companion split dependency lost")
    if not census["all_old_position_kernel_pairs_split_dependent"]:
        raise AssertionError("old-position split dependency lost")
    if decision["k287_is_a_native_weighted_occurrence_remainder"]:
        raise AssertionError("K287 may not be promoted to native weight")
    if decision["signed_occurrence_weights_can_be_collapsed_before_integration"]:
        raise AssertionError("signed weights may not erase distinct rest factors")
    if release["native_weighted_jacobi_remainder_serialized"]:
        raise AssertionError("K289 does not serialize the weighted remainder")
    if "No native weighted remainder" not in data["claim_ceiling"]:
        raise AssertionError("claim ceiling lost native-weight boundary")


def mutate(data: dict[str, Any], name: str) -> dict[str, Any]:
    result = copy.deepcopy(data)
    if name == "occurrence_count":
        result["fixed_control"]["size_four_occurrences"] = 23
    elif name == "variable_count":
        result["fixed_control"]["native_variables"].pop()
    elif name == "pair_sum":
        result["dependency_census"]["all_size_four_factors_pair_sum_only"] = False
    elif name == "companion":
        result["dependency_census"]["all_companion_size_three_factors_split_dependent"] = False
    elif name == "old_position":
        result["dependency_census"]["all_old_position_kernel_pairs_split_dependent"] = False
    elif name == "native_promotion":
        result["composition_decision"]["k287_is_a_native_weighted_occurrence_remainder"] = True
    elif name == "collapse":
        result["composition_decision"]["signed_occurrence_weights_can_be_collapsed_before_integration"] = True
    elif name == "ceiling":
        result["claim_ceiling"] = "complete action column"
    else:
        raise KeyError(name)
    return result


def main() -> int:
    stored = json.loads(MANIFEST.read_text())
    replay = K289.certificate()
    checks = {
        "deterministic_manifest_replay": replay == stored,
        "complete_occurrence_audit": stored["release_test"]["all_24_occurrences_dependency_audited"],
        "pair_sum_identity": stored["dependency_census"]["all_size_four_factors_pair_sum_only"],
        "companion_dependency": stored["dependency_census"]["all_companion_size_three_factors_split_dependent"],
        "old_position_dependency": stored["dependency_census"]["all_old_position_kernel_pairs_split_dependent"],
        "native_ceiling": not stored["composition_decision"]["k287_is_a_native_weighted_occurrence_remainder"],
    }
    validate(stored)
    hostile = {}
    for name in (
        "occurrence_count",
        "variable_count",
        "pair_sum",
        "companion",
        "old_position",
        "native_promotion",
        "collapse",
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
