#!/usr/bin/env python3
"""Independent hostile probe for K684's closed-column compiler."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = ROOT / "tests/channel-swings/k684_k500_closed_column_remainder_compiler.py"
ARTIFACT = ROOT / "lab/process/k684-k500-closed-column-remainder-compiler.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k684_producer", PRODUCER)
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
        lambda p: p["closed_column_theorem"].__setitem__("native_identification_required", False),
        lambda p: p["closed_column_theorem"].__setitem__("finite_or_formal_component_list_sufficient", True),
        lambda p: p["closed_column_theorem"].__setitem__("unclosed_column_sufficient", True),
        lambda p: p["bounded_realization"].__setitem__("norm_identity", "||R||<=||B||"),
        lambda p: p["bounded_realization"].__setitem__("factorization_without_bounded_column_sufficient", True),
        lambda p: p["bounded_realization"].__setitem__("seed_only_column_sufficient", True),
        lambda p: p["reduction_theorem"].__setitem__("component_labels_without_intertwining_sufficient", True),
        lambda p: p["exact_controls"].__setitem__("R_norm_square", "1/36"),
        lambda p: p["exact_controls"]["nonclosed_counterexample"].__setitem__("square_form_closed_on_that_uncompleted_domain", True),
        lambda p: p["native_interface_status"].__setitem__("actual_native_complete_column_serialized", True),
        lambda p: p["native_interface_status"].__setitem__("native_complete_floor_emitted", True),
        lambda p: p.__setitem__("target_claim", "SC-META-53"),
        lambda p: p.__setitem__("source_and_ledger_effect", "positive"),
        lambda p: p["native_interface_status"].__setitem__("actual_native_column_closed", True),
        lambda p: p["native_interface_status"].__setitem__("actual_native_r_free_identified", True),
        lambda p: p["native_interface_status"].__setitem__("actual_native_C_a_inverse_bounded", True),
        lambda p: p["native_interface_status"].__setitem__("native_A_above_two_thirds_proved", True),
        lambda p: p["decision"].__setitem__("native_column_constructed", True),
        lambda p: p["dependency_reconciliation"].__setitem__("native_closed_column_added", True),
        lambda p: p["exact_controls"].__setitem__("coordinate_projections_intertwine_column_and_reduce_weight", False),
        lambda p: p.__setitem__("classification", "SOURCE_NATIVE_ROUTE"),
        lambda p: p["controls"].__setitem__("controls_passed", 0),
        lambda p: p["controls"].__setitem__("hostile_mutations_rejected", 0),
        lambda p: p.__setitem__("status", "canon"),
        lambda p: p["closed_column_theorem"].pop("domain_identity"),
        lambda p: p["bounded_realization"].pop("relative_form_identity"),
        lambda p: p["reduction_theorem"].pop("graph_consequence"),
        lambda p: p["gu_typed_objects"].pop("coefficient_column"),
        lambda p: p["postflight_bookend"].pop("weakest_reproducibility_seam"),
    ]
    original_validate = module.validate

    def strict_validate(candidate):
        original_validate(candidate)
        assert candidate["target_claim"] == "NONE-NOT-A-KILL"
        assert candidate["source_and_ledger_effect"] == "none"
        native = candidate["native_interface_status"]
        assert not native["actual_native_column_closed"]
        assert not native["actual_native_r_free_identified"]
        assert not native["actual_native_C_a_inverse_bounded"]
        assert not native["native_A_above_two_thirds_proved"]
        assert not candidate["decision"]["native_column_constructed"]
        assert not candidate["dependency_reconciliation"]["native_closed_column_added"]
        assert candidate["exact_controls"]["coordinate_projections_intertwine_column_and_reduce_weight"]
        assert candidate["classification"] == "INTERNAL_STRUCTURAL_ONLY"
        assert candidate["controls"]["controls_passed"] == 35
        assert candidate["controls"]["hostile_mutations_rejected"] == 29
        assert candidate["status"] == "working_draft_verified"
        assert candidate["closed_column_theorem"]["domain_identity"]
        assert candidate["bounded_realization"]["relative_form_identity"]
        assert candidate["reduction_theorem"]["graph_consequence"]
        assert candidate["gu_typed_objects"]["coefficient_column"]
        assert candidate["postflight_bookend"]["weakest_reproducibility_seam"]

    module.validate = strict_validate
    strict_validate(payload)
    for mutate in mutations:
        must_reject(module, payload, mutate)
    print("K684 probe passed: 35 controls; rejected 29/29 hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
