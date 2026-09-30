#!/usr/bin/env python3
"""Independent hostile probe for K681's monotone-form compiler."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = ROOT / "tests/channel-swings/k681_k500_monotone_remainder_form_compiler.py"
ARTIFACT = ROOT / "lab/process/k681-k500-monotone-remainder-form-compiler.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k681_producer", PRODUCER)
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
        lambda p: p["monotone_form_theorem"].__setitem__("limit_density_required", False),
        lambda p: p["monotone_form_theorem"].__setitem__("finite_prefix_sufficient", True),
        lambda p: p["monotone_form_theorem"].__setitem__("pointwise_nonmonotone_family_sufficient", True),
        lambda p: p["monotone_form_theorem"].__setitem__("dense_limit_domain_may_be_assumed", True),
        lambda p: p["monotone_form_theorem"].__setitem__("native_identification_follows_from_abstract_convergence", True),
        lambda p: p["reduction_and_bound_inheritance"].__setitem__("stagewise_bath_labels_without_form_reduction_sufficient", True),
        lambda p: p["reduction_and_bound_inheritance"].__setitem__("nonuniform_constants_sufficient", True),
        lambda p: p["exact_controls"].__setitem__("limit_diagonal", ["1/16", "1/25", "1/25"]),
        lambda p: p["exact_controls"]["nonmonotone_counterexample"].__setitem__("pointwise_supremum_is_quadratic_form", True),
        lambda p: p["native_interface_status"].__setitem__("actual_native_r_free_identified", True),
        lambda p: p["native_interface_status"].__setitem__("native_complete_floor_emitted", True),
        lambda p: p.__setitem__("target_claim", "SC-META-53"),
        lambda p: p.__setitem__("source_and_ledger_effect", "positive"),
        lambda p: p["native_interface_status"].__setitem__("actual_native_T_constructed", True),
        lambda p: p["native_interface_status"].__setitem__("actual_native_closed_nonnegative_h_proved", True),
        lambda p: p["native_interface_status"].__setitem__("native_A_above_two_thirds_proved", True),
        lambda p: p["decision"].__setitem__("native_form_constructed", True),
        lambda p: p["dependency_reconciliation"].__setitem__("native_approximant_family_added", True),
        lambda p: p["exact_controls"].__setitem__("coordinate_projections_reduce_every_stage", False),
        lambda p: p["monotone_form_theorem"].__setitem__("strong_resolvent_consequence", "norm resolvent"),
        lambda p: p.__setitem__("classification", "SOURCE_NATIVE_ROUTE"),
        lambda p: p["controls"].__setitem__("hostile_mutations_rejected", 0),
        lambda p: p["controls"].__setitem__("controls_passed", 0),
        lambda p: p.__setitem__("status", "canon"),
        lambda p: p["monotone_form_theorem"].pop("limit_domain"),
        lambda p: p["reduction_and_bound_inheritance"].pop("uniform_graph_bound_hypothesis"),
    ]
    # Add invariant checks not already exercised by the producer's compact validator.
    original_validate = module.validate

    def strict_validate(candidate):
        original_validate(candidate)
        assert candidate["target_claim"] == "NONE-NOT-A-KILL"
        assert candidate["source_and_ledger_effect"] == "none"
        assert not candidate["native_interface_status"]["actual_native_T_constructed"]
        assert not candidate["native_interface_status"]["actual_native_closed_nonnegative_h_proved"]
        assert not candidate["native_interface_status"]["native_A_above_two_thirds_proved"]
        assert not candidate["decision"]["native_form_constructed"]
        assert not candidate["dependency_reconciliation"]["native_approximant_family_added"]
        assert candidate["exact_controls"]["coordinate_projections_reduce_every_stage"]
        assert candidate["monotone_form_theorem"]["strong_resolvent_consequence"].startswith("the associated H_N")
        assert candidate["classification"] == "INTERNAL_STRUCTURAL_ONLY"
        assert candidate["controls"]["hostile_mutations_rejected"] == 26
        assert candidate["controls"]["controls_passed"] == 32
        assert candidate["status"] == "working_draft_verified"
        assert candidate["monotone_form_theorem"]["limit_domain"]
        assert candidate["reduction_and_bound_inheritance"]["uniform_graph_bound_hypothesis"]

    module.validate = strict_validate
    strict_validate(payload)
    for mutate in mutations:
        must_reject(module, payload, mutate)
    print("K681 probe passed: 32 controls; rejected 26/26 hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
