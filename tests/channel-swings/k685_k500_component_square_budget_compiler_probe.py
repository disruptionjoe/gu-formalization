#!/usr/bin/env python3
"""Independent hostile probe for K685's component-square compiler."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = ROOT / "tests/channel-swings/k685_k500_component_square_budget_compiler.py"
ARTIFACT = ROOT / "lab/process/k685-k500-component-square-budget-compiler.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k685_producer", PRODUCER)
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
        lambda p: p["component_square_theorem"].__setitem__("finite_prefix_without_tail_sufficient", True),
        lambda p: p["component_square_theorem"].__setitem__("scalar_coefficient_bounds_without_operator_norms_sufficient", True),
        lambda p: p["component_square_theorem"].__setitem__("same_codomain_sum_without_cross_Gram_control_sufficient", True),
        lambda p: p["seed_composition"].__setitem__("three_untyped_scalar_values_sufficient", True),
        lambda p: p["seed_composition"].__setitem__("complement_budget_alone_proves_seed_identity", True),
        lambda p: p["exact_controls"].__setitem__("total_complement_square_budget", "1/50"),
        lambda p: p["exact_controls"].__setitem__("slack", "-1/100"),
        lambda p: p["exact_controls"].__setitem__("accepted", False),
        lambda p: p["exact_controls"]["nonorthogonal_counterexample"].__setitem__("squared_norm_of_component_sum", "2"),
        lambda p: p["native_interface_status"].__setitem__("actual_native_complete_square_tail_proved", True),
        lambda p: p["native_interface_status"].__setitem__("native_complete_floor_emitted", True),
        lambda p: p.__setitem__("target_claim", "SC-META-53"),
        lambda p: p.__setitem__("source_and_ledger_effect", "positive"),
        lambda p: p["native_interface_status"].__setitem__("actual_native_component_column_serialized", True),
        lambda p: p["native_interface_status"].__setitem__("actual_native_component_operator_bounds_proved", True),
        lambda p: p["native_interface_status"].__setitem__("actual_native_seed_actions_identified", True),
        lambda p: p["native_interface_status"].__setitem__("actual_native_complement_below_one_over_one_hundred", True),
        lambda p: p["native_interface_status"].__setitem__("native_A_above_two_thirds_proved", True),
        lambda p: p["decision"].__setitem__("native_complement_budget_proved", True),
        lambda p: p["dependency_reconciliation"].__setitem__("native_component_bounds_added", True),
        lambda p: p.__setitem__("classification", "SOURCE_NATIVE_ROUTE"),
        lambda p: p["controls"].__setitem__("controls_passed", 0),
        lambda p: p["controls"].__setitem__("hostile_mutations_rejected", 0),
        lambda p: p.__setitem__("status", "canon"),
        lambda p: p["component_square_theorem"].pop("tail_hypothesis"),
        lambda p: p["seed_composition"].pop("charge_orthogonality_requirement"),
        lambda p: p["gu_typed_objects"].pop("tail"),
        lambda p: p["postflight_bookend"].pop("weakest_reproducibility_seam"),
    ]
    original_validate = module.validate

    def strict_validate(candidate):
        original_validate(candidate)
        assert candidate["target_claim"] == "NONE-NOT-A-KILL"
        assert candidate["source_and_ledger_effect"] == "none"
        native = candidate["native_interface_status"]
        assert not native["actual_native_component_column_serialized"]
        assert not native["actual_native_component_operator_bounds_proved"]
        assert not native["actual_native_seed_actions_identified"]
        assert not native["actual_native_complement_below_one_over_one_hundred"]
        assert not native["native_A_above_two_thirds_proved"]
        assert not candidate["decision"]["native_complement_budget_proved"]
        assert not candidate["dependency_reconciliation"]["native_component_bounds_added"]
        assert candidate["classification"] == "INTERNAL_STRUCTURAL_ONLY"
        assert candidate["controls"]["controls_passed"] == 34
        assert candidate["controls"]["hostile_mutations_rejected"] == 28
        assert candidate["status"] == "working_draft_verified"
        assert candidate["component_square_theorem"]["tail_hypothesis"]
        assert candidate["seed_composition"]["charge_orthogonality_requirement"]
        assert candidate["gu_typed_objects"]["tail"]
        assert candidate["postflight_bookend"]["weakest_reproducibility_seam"]

    module.validate = strict_validate
    strict_validate(payload)
    for mutate in mutations:
        must_reject(module, payload, mutate)
    print("K685 probe passed: 34 controls; rejected 28/28 hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
