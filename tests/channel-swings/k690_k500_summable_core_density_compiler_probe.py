#!/usr/bin/env python3
"""Independent hostile probe for K690's summable-core density compiler."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = ROOT / "tests/channel-swings/k690_k500_summable_core_density_compiler.py"
ARTIFACT = ROOT / "lab/process/k690-k500-summable-core-density-compiler.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k690_producer", PRODUCER)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def must_reject(module, payload, mutate) -> None:
    candidate = copy.deepcopy(payload)
    mutate(candidate)
    try:
        module.validate(candidate)
    except (AssertionError, KeyError, TypeError):
        return
    raise AssertionError("hostile mutation accepted")


def main() -> int:
    module = load_module()
    payload = module.build()
    module.validate(payload)
    assert json.loads(ARTIFACT.read_text()) == payload
    mutations = [
        lambda p: p["summable_core_theorem"].__setitem__("dense_common_core_required", False),
        lambda p: p["summable_core_theorem"].__setitem__("same_graph_weight_required", False),
        lambda p: p["summable_core_theorem"].__setitem__("complete_square_sum_required", False),
        lambda p: p["summable_core_theorem"].__setitem__("finite_prefix_bounds_sufficient", True),
        lambda p: p["summable_core_theorem"].__setitem__("pointwise_finite_component_values_sufficient", True),
        lambda p: p["summable_core_theorem"].__setitem__("nonsummable_uniform_component_bounds_sufficient", True),
        lambda p: p["summable_core_theorem"].__setitem__("separate_component_cores_without_one_common_dense_core_sufficient", True),
        lambda p: p["exact_controls"].__setitem__("complete_square_sum", "1"),
        lambda p: p["exact_controls"].__setitem__("maximal_domain", "finite prefix"),
        lambda p: p["native_interface_status"].__setitem__("actual_native_maximal_domain_dense", True),
        lambda p: p["native_interface_status"].__setitem__("native_complete_floor_emitted", True),
        lambda p: p.__setitem__("target_claim", "SC-META-53"),
        lambda p: p.__setitem__("source_and_ledger_effect", "positive"),
        lambda p: p["native_interface_status"].__setitem__("actual_native_common_core_serialized", True),
        lambda p: p["native_interface_status"].__setitem__("actual_native_common_core_dense", True),
        lambda p: p["native_interface_status"].__setitem__("actual_native_components_serialized", True),
        lambda p: p["native_interface_status"].__setitem__("actual_native_complete_square_sum_proved", True),
        lambda p: p["native_interface_status"].__setitem__("actual_native_remainder_identified", True),
        lambda p: p["decision"].__setitem__("native_dense_column_constructed", True),
        lambda p: p["dependency_reconciliation"].__setitem__("native_common_core_or_component_family_added", True),
        lambda p: p.__setitem__("classification", "SOURCE_NATIVE_ROUTE"),
        lambda p: p["controls"].__setitem__("controls_passed", 0),
        lambda p: p["controls"].__setitem__("hostile_mutations_rejected", 0),
        lambda p: p.__setitem__("status", "canon"),
        lambda p: p["summable_core_theorem"].pop("inequality"),
        lambda p: p["gu_typed_objects"].pop("common_core"),
        lambda p: p["postflight_bookend"].pop("weakest_reproducibility_seam"),
        lambda p: p["exact_controls"].pop("nonsummable_counterexample"),
        lambda p: p["decision"].pop("next_exact_input"),
    ]
    original_validate = module.validate

    def strict_validate(candidate):
        original_validate(candidate)
        assert candidate["target_claim"] == "NONE-NOT-A-KILL"
        assert candidate["source_and_ledger_effect"] == "none"
        native = candidate["native_interface_status"]
        assert not native["actual_native_common_core_serialized"]
        assert not native["actual_native_common_core_dense"]
        assert not native["actual_native_components_serialized"]
        assert not native["actual_native_complete_square_sum_proved"]
        assert not native["actual_native_remainder_identified"]
        assert not candidate["decision"]["native_dense_column_constructed"]
        assert not candidate["dependency_reconciliation"]["native_common_core_or_component_family_added"]
        assert candidate["classification"] == "INTERNAL_STRUCTURAL_ONLY"
        assert candidate["controls"]["controls_passed"] == 35
        assert candidate["controls"]["hostile_mutations_rejected"] == 29
        assert candidate["status"] == "working_draft_verified"
        assert candidate["summable_core_theorem"]["inequality"]
        assert candidate["gu_typed_objects"]["common_core"]
        assert candidate["postflight_bookend"]["weakest_reproducibility_seam"]
        assert candidate["exact_controls"]["nonsummable_counterexample"]
        assert candidate["decision"]["next_exact_input"]

    module.validate = strict_validate
    strict_validate(payload)
    for mutate in mutations:
        must_reject(module, payload, mutate)
    print("K690 probe passed: 35 controls; rejected 29/29 hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
