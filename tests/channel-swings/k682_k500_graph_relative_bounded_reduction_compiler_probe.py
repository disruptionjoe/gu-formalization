#!/usr/bin/env python3
"""Independent hostile probe for K682's graph-relative boundedness compiler."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = ROOT / "tests/channel-swings/k682_k500_graph_relative_bounded_reduction_compiler.py"
ARTIFACT = ROOT / "lab/process/k682-k500-graph-relative-bounded-reduction-compiler.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k682_producer", PRODUCER)
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
        lambda p: p["boundedness_theorem"].__setitem__("complete_domain_required", False),
        lambda p: p["boundedness_theorem"].__setitem__("factorization_alone_sufficient", True),
        lambda p: p["boundedness_theorem"].__setitem__("finite_seed_rows_sufficient", True),
        lambda p: p["boundedness_theorem"].__setitem__("sampled_bath_rows_sufficient", True),
        lambda p: p["projection_reduction_theorem"].__setitem__("K643_monomial_preservation_substitutable", True),
        lambda p: p["projection_reduction_theorem"].__setitem__("reduction_of_h_without_reduction_of_a_sufficient", True),
        lambda p: p["exact_controls"].__setitem__("R_diagonal", ["1/4", "1/25", "1/18"]),
        lambda p: p["exact_controls"].__setitem__("sharp_global_c_squared", "1/32"),
        lambda p: p["exact_controls"]["seed_only_counterexample"].__setitem__("seed_bound_proves_complete_boundedness_at_one", True),
        lambda p: p["native_interface_status"].__setitem__("actual_native_R_bounded", True),
        lambda p: p["native_interface_status"].__setitem__("native_complete_floor_emitted", True),
        lambda p: p.__setitem__("target_claim", "SC-META-53"),
        lambda p: p.__setitem__("source_and_ledger_effect", "positive"),
        lambda p: p["native_interface_status"].__setitem__("actual_native_uniform_relative_bound_proved", True),
        lambda p: p["native_interface_status"].__setitem__("actual_native_charge_reduction_proved", True),
        lambda p: p["native_interface_status"].__setitem__("actual_native_bath_reduction_proved", True),
        lambda p: p["native_interface_status"].__setitem__("actual_K609_map_identity_proved", True),
        lambda p: p["decision"].__setitem__("native_bounded_R_constructed", True),
        lambda p: p["dependency_reconciliation"].__setitem__("native_relative_form_row_added", True),
        lambda p: p["exact_controls"].__setitem__("coordinate_projections_reduce_h_a_R_and_R_star_R", False),
        lambda p: p["localized_bounds"].__setitem__("one_over_one_hundred_target", "finite row suffices"),
        lambda p: p.__setitem__("classification", "SOURCE_NATIVE_ROUTE"),
        lambda p: p["controls"].__setitem__("hostile_mutations_rejected", 0),
        lambda p: p["controls"].__setitem__("controls_passed", 0),
        lambda p: p.__setitem__("status", "canon"),
        lambda p: p["boundedness_theorem"].pop("domain_hypothesis"),
        lambda p: p["projection_reduction_theorem"].pop("hypothesis"),
        lambda p: p["localized_bounds"].pop("projection_test"),
    ]
    original_validate = module.validate

    def strict_validate(candidate):
        original_validate(candidate)
        assert candidate["target_claim"] == "NONE-NOT-A-KILL"
        assert candidate["source_and_ledger_effect"] == "none"
        native = candidate["native_interface_status"]
        assert not native["actual_native_uniform_relative_bound_proved"]
        assert not native["actual_native_charge_reduction_proved"]
        assert not native["actual_native_bath_reduction_proved"]
        assert not native["actual_K609_map_identity_proved"]
        assert not candidate["decision"]["native_bounded_R_constructed"]
        assert not candidate["dependency_reconciliation"]["native_relative_form_row_added"]
        assert candidate["exact_controls"]["coordinate_projections_reduce_h_a_R_and_R_star_R"]
        assert candidate["localized_bounds"]["one_over_one_hundred_target"].startswith("h[a^-1 x]")
        assert candidate["classification"] == "INTERNAL_STRUCTURAL_ONLY"
        assert candidate["controls"]["hostile_mutations_rejected"] == 28
        assert candidate["controls"]["controls_passed"] == 34
        assert candidate["status"] == "working_draft_verified"
        assert candidate["boundedness_theorem"]["domain_hypothesis"]
        assert candidate["projection_reduction_theorem"]["hypothesis"]
        assert candidate["localized_bounds"]["projection_test"]

    module.validate = strict_validate
    strict_validate(payload)
    for mutate in mutations:
        must_reject(module, payload, mutate)
    print("K682 probe passed: 34 controls; rejected 28/28 hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
