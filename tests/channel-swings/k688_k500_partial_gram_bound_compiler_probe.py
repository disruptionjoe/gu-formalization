#!/usr/bin/env python3
"""Independent hostile probe for K688's partial-Gram compiler."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = ROOT / "tests/channel-swings/k688_k500_partial_gram_bound_compiler.py"
ARTIFACT = ROOT / "lab/process/k688-k500-partial-gram-bound-compiler.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k688_producer", PRODUCER)
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
        lambda p: p["partial_gram_theorem"].__setitem__("identity", "finite only"),
        lambda p: p["partial_gram_theorem"].__setitem__("finite_partial_gram_without_tail_sufficient", True),
        lambda p: p["partial_gram_theorem"].__setitem__("diagonal_matrix_elements_on_sampled_vectors_sufficient", True),
        lambda p: p["partial_gram_theorem"].__setitem__("component_scalar_coefficients_without_operator_domains_sufficient", True),
        lambda p: p["partial_gram_theorem"].__setitem__("weak_or_uncontrolled_tail_sufficient", True),
        lambda p: p["exact_controls"].__setitem__("complete_column_square_upper", "1/100"),
        lambda p: p["exact_controls"].__setitem__("slack", "0"),
        lambda p: p["exact_controls"].__setitem__("accepted", False),
        lambda p: p["seed_composition"].__setitem__("partial_gram_bound_proves_seed_identity", True),
        lambda p: p["seed_composition"].__setitem__("partial_gram_bound_proves_native_remainder_identification", True),
        lambda p: p["native_interface_status"].__setitem__("actual_native_seed_complement_below_one_over_one_hundred", True),
        lambda p: p["native_interface_status"].__setitem__("native_complete_floor_emitted", True),
        lambda p: p.__setitem__("target_claim", "SC-META-53"),
        lambda p: p.__setitem__("source_and_ledger_effect", "positive"),
        lambda p: p["native_interface_status"].__setitem__("actual_native_bounded_components_serialized", True),
        lambda p: p["native_interface_status"].__setitem__("actual_native_partial_gram_order_proved", True),
        lambda p: p["native_interface_status"].__setitem__("actual_native_complete_tail_gram_proved", True),
        lambda p: p["native_interface_status"].__setitem__("actual_native_global_graph_bound_proved", True),
        lambda p: p["decision"].__setitem__("native_graph_or_complement_bound_proved", True),
        lambda p: p["dependency_reconciliation"].__setitem__("native_partial_gram_added", True),
        lambda p: p.__setitem__("classification", "SOURCE_NATIVE_ROUTE"),
        lambda p: p["controls"].__setitem__("controls_passed", 0),
        lambda p: p["controls"].__setitem__("hostile_mutations_rejected", 0),
        lambda p: p.__setitem__("status", "canon"),
        lambda p: p["partial_gram_theorem"].pop("finite_plus_tail_bound"),
        lambda p: p["gu_typed_objects"].pop("partial_gram"),
        lambda p: p["postflight_bookend"].pop("weakest_reproducibility_seam"),
    ]
    original_validate = module.validate

    def strict_validate(candidate):
        original_validate(candidate)
        assert candidate["target_claim"] == "NONE-NOT-A-KILL"
        assert candidate["source_and_ledger_effect"] == "none"
        native = candidate["native_interface_status"]
        assert not native["actual_native_bounded_components_serialized"]
        assert not native["actual_native_partial_gram_order_proved"]
        assert not native["actual_native_complete_tail_gram_proved"]
        assert not native["actual_native_global_graph_bound_proved"]
        assert not candidate["decision"]["native_graph_or_complement_bound_proved"]
        assert not candidate["dependency_reconciliation"]["native_partial_gram_added"]
        assert candidate["classification"] == "INTERNAL_STRUCTURAL_ONLY"
        assert candidate["controls"]["controls_passed"] == 33
        assert candidate["controls"]["hostile_mutations_rejected"] == 27
        assert candidate["status"] == "working_draft_verified"
        assert candidate["partial_gram_theorem"]["finite_plus_tail_bound"]
        assert candidate["gu_typed_objects"]["partial_gram"]
        assert candidate["postflight_bookend"]["weakest_reproducibility_seam"]

    module.validate = strict_validate
    strict_validate(payload)
    for mutate in mutations:
        must_reject(module, payload, mutate)
    print("K688 probe passed: 33 controls; rejected 27/27 hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
