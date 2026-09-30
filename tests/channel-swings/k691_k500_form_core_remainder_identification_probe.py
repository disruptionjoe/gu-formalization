#!/usr/bin/env python3
"""Independent hostile probe for K691's form-core identification."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = ROOT / "tests/channel-swings/k691_k500_form_core_remainder_identification.py"
ARTIFACT = ROOT / "lab/process/k691-k500-form-core-remainder-identification.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k691_producer", PRODUCER)
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
        lambda p: p["form_core_theorem"].__setitem__("closed_dense_column_required", False),
        lambda p: p["form_core_theorem"].__setitem__("closed_nonnegative_native_form_required", False),
        lambda p: p["form_core_theorem"].__setitem__("one_common_form_core_for_both_required", False),
        lambda p: p["form_core_theorem"].__setitem__("algebraically_dense_test_space_sufficient", True),
        lambda p: p["form_core_theorem"].__setitem__("core_for_only_column_form_sufficient", True),
        lambda p: p["form_core_theorem"].__setitem__("core_for_only_native_form_sufficient", True),
        lambda p: p["form_core_theorem"].__setitem__("finite_component_identity_sufficient", True),
        lambda p: p["form_core_theorem"].__setitem__("pointwise_quadratic_values_without_domain_identity_sufficient", True),
        lambda p: p["exact_controls"].__setitem__("column_square", "1"),
        lambda p: p["exact_controls"].__setitem__("native_form_value", "1"),
        lambda p: p["exact_controls"].__setitem__("operators_identical", False),
        lambda p: p["native_interface_status"].__setitem__("actual_native_CstarC_equals_H", True),
        lambda p: p["native_interface_status"].__setitem__("native_complete_floor_emitted", True),
        lambda p: p.__setitem__("target_claim", "SC-META-53"),
        lambda p: p.__setitem__("source_and_ledger_effect", "positive"),
        lambda p: p["native_interface_status"].__setitem__("actual_native_column_serialized", True),
        lambda p: p["native_interface_status"].__setitem__("actual_native_remainder_form_serialized", True),
        lambda p: p["native_interface_status"].__setitem__("actual_native_common_form_core_proved", True),
        lambda p: p["native_interface_status"].__setitem__("actual_native_same_form_identity_proved", True),
        lambda p: p["native_interface_status"].__setitem__("actual_native_T_identified", True),
        lambda p: p["decision"].__setitem__("native_remainder_identified", True),
        lambda p: p["dependency_reconciliation"].__setitem__("native_remainder_identity_added", True),
        lambda p: p.__setitem__("classification", "SOURCE_NATIVE_ROUTE"),
        lambda p: p["controls"].__setitem__("controls_passed", 0),
        lambda p: p["controls"].__setitem__("hostile_mutations_rejected", 0),
        lambda p: p.__setitem__("status", "canon"),
        lambda p: p["form_core_theorem"].pop("same_form_identity"),
        lambda p: p["form_core_theorem"].pop("operator_consequence"),
        lambda p: p["postflight_bookend"].pop("weakest_reproducibility_seam"),
        lambda p: p["exact_controls"].pop("extension_counterexample"),
    ]
    original_validate = module.validate

    def strict_validate(candidate):
        original_validate(candidate)
        assert candidate["target_claim"] == "NONE-NOT-A-KILL"
        assert candidate["source_and_ledger_effect"] == "none"
        native = candidate["native_interface_status"]
        assert not native["actual_native_column_serialized"]
        assert not native["actual_native_remainder_form_serialized"]
        assert not native["actual_native_common_form_core_proved"]
        assert not native["actual_native_same_form_identity_proved"]
        assert not native["actual_native_T_identified"]
        assert not candidate["decision"]["native_remainder_identified"]
        assert not candidate["dependency_reconciliation"]["native_remainder_identity_added"]
        assert candidate["classification"] == "INTERNAL_STRUCTURAL_ONLY"
        assert candidate["controls"]["controls_passed"] == 36
        assert candidate["controls"]["hostile_mutations_rejected"] == 30
        assert candidate["status"] == "working_draft_verified"
        assert candidate["form_core_theorem"]["same_form_identity"]
        assert candidate["form_core_theorem"]["operator_consequence"]
        assert candidate["postflight_bookend"]["weakest_reproducibility_seam"]
        assert candidate["exact_controls"]["extension_counterexample"]

    module.validate = strict_validate
    strict_validate(payload)
    for mutate in mutations:
        must_reject(module, payload, mutate)
    print("K691 probe passed: 36 controls; rejected 30/30 hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
