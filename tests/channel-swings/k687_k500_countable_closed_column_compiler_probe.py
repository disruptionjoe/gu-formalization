#!/usr/bin/env python3
"""Independent hostile probe for K687's countable closed-column compiler."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = ROOT / "tests/channel-swings/k687_k500_countable_closed_column_compiler.py"
ARTIFACT = ROOT / "lab/process/k687-k500-countable-closed-column-compiler.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k687_producer", PRODUCER)
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
        lambda p: p["countable_column_theorem"].__setitem__("component_hypothesis", "components are formal"),
        lambda p: p["countable_column_theorem"].__setitem__("density_hypothesis", "density optional"),
        lambda p: p["countable_column_theorem"].__setitem__("finite_prefix_proves_complete_domain", True),
        lambda p: p["countable_column_theorem"].__setitem__("formal_componentwise_convergence_proves_square_summability", True),
        lambda p: p["countable_column_theorem"].__setitem__("individual_component_density_proves_common_domain_density", True),
        lambda p: p["countable_column_theorem"].__setitem__("closable_components_without_closure_sufficient", True),
        lambda p: p["core_route"].__setitem__("finite_order_coefficient_bank_alone_sufficient", True),
        lambda p: p["core_route"].__setitem__("algebraic_common_core_without_graph_completeness_sufficient", True),
        lambda p: p["exact_controls"].__setitem__("finite_sequences_dense", False),
        lambda p: p["exact_controls"].__setitem__("column_closed", False),
        lambda p: p["native_interface_status"].__setitem__("actual_native_column_closed", True),
        lambda p: p["native_interface_status"].__setitem__("native_complete_floor_emitted", True),
        lambda p: p.__setitem__("target_claim", "SC-META-53"),
        lambda p: p.__setitem__("source_and_ledger_effect", "positive"),
        lambda p: p["native_interface_status"].__setitem__("actual_native_components_serialized", True),
        lambda p: p["native_interface_status"].__setitem__("actual_native_common_domain_dense", True),
        lambda p: p["native_interface_status"].__setitem__("actual_native_remainder_identified", True),
        lambda p: p["decision"].__setitem__("native_column_constructed", True),
        lambda p: p["dependency_reconciliation"].__setitem__("native_component_family_added", True),
        lambda p: p.__setitem__("classification", "SOURCE_NATIVE_ROUTE"),
        lambda p: p["controls"].__setitem__("controls_passed", 0),
        lambda p: p["controls"].__setitem__("hostile_mutations_rejected", 0),
        lambda p: p.__setitem__("status", "canon"),
        lambda p: p["countable_column_theorem"].pop("closedness_argument"),
        lambda p: p["gu_typed_objects"].pop("maximal_domain"),
        lambda p: p["postflight_bookend"].pop("weakest_reproducibility_seam"),
    ]
    original_validate = module.validate

    def strict_validate(candidate):
        original_validate(candidate)
        assert candidate["target_claim"] == "NONE-NOT-A-KILL"
        assert candidate["source_and_ledger_effect"] == "none"
        native = candidate["native_interface_status"]
        assert not native["actual_native_components_serialized"]
        assert not native["actual_native_common_domain_dense"]
        assert not native["actual_native_remainder_identified"]
        assert not candidate["decision"]["native_column_constructed"]
        assert not candidate["dependency_reconciliation"]["native_component_family_added"]
        assert candidate["classification"] == "INTERNAL_STRUCTURAL_ONLY"
        assert candidate["controls"]["controls_passed"] == 32
        assert candidate["controls"]["hostile_mutations_rejected"] == 26
        assert candidate["status"] == "working_draft_verified"
        assert candidate["countable_column_theorem"]["closedness_argument"]
        assert candidate["gu_typed_objects"]["maximal_domain"]
        assert candidate["postflight_bookend"]["weakest_reproducibility_seam"]

    module.validate = strict_validate
    strict_validate(payload)
    for mutate in mutations:
        must_reject(module, payload, mutate)
    print("K687 probe passed: 32 controls; rejected 26/26 hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
