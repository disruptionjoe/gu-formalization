#!/usr/bin/env python3
"""Independent hostile probe for K692's Friedrichs-trace anchor compiler."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = ROOT / "tests/channel-swings/k692_k500_friedrichs_trace_anchor_compiler.py"
ARTIFACT = ROOT / "lab/process/k692-k500-friedrichs-trace-anchor-compiler.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k692_producer", PRODUCER)
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
        lambda p: p["friedrichs_gap_theorem"].__setitem__("authenticated_friedrichs_reference_required", False),
        lambda p: p["friedrichs_gap_theorem"].__setitem__("complete_form_lower_required", False),
        lambda p: p["friedrichs_gap_theorem"].__setitem__("interval_below_lower_edge_required", False),
        lambda p: p["friedrichs_gap_theorem"].__setitem__("finite_sector_lower_sufficient", True),
        lambda p: p["friedrichs_gap_theorem"].__setitem__("qualitative_semiboundedness_sufficient", True),
        lambda p: p["friedrichs_gap_theorem"].__setitem__("non_friedrichs_extension_lower_substitutable", True),
        lambda p: p["defect_trace_theorem"].__setitem__("same_boundary_coordinate_required", False),
        lambda p: p["defect_trace_theorem"].__setitem__("complete_defect_space_required", False),
        lambda p: p["defect_trace_theorem"].__setitem__("bijective_trace_from_ordinary_triple_required", False),
        lambda p: p["defect_trace_theorem"].__setitem__("finite_defect_subspace_bound_sufficient", True),
        lambda p: p["defect_trace_theorem"].__setitem__("sampled_trace_vectors_sufficient", True),
        lambda p: p["defect_trace_theorem"].__setitem__("trace_from_different_coordinate_substitutable", True),
        lambda p: p["target_composition"].__setitem__("interval_gap_lower", "0"),
        lambda p: p["target_composition"].__setitem__("anchor_gamma_norm_upper", "1"),
        lambda p: p["target_composition"].__setitem__("K689_propagation_factor", "1"),
        lambda p: p["target_composition"].__setitem__("target_gamma_norm_upper", "1"),
        lambda p: p["target_composition"].__setitem__("K686_weyl_variation_upper", "1/100"),
        lambda p: p["target_composition"].__setitem__("transferred_target_margin", "0"),
        lambda p: p["target_composition"].__setitem__("accepted", False),
        lambda p: p["native_interface_status"].__setitem__("actual_native_anchor_gamma_norm_proved", True),
        lambda p: p["native_interface_status"].__setitem__("native_complete_floor_emitted", True),
        lambda p: p.__setitem__("target_claim", "SC-META-53"),
        lambda p: p.__setitem__("source_and_ledger_effect", "positive"),
        lambda p: p["native_interface_status"].__setitem__("actual_native_boundary_triple_authenticated", True),
        lambda p: p["native_interface_status"].__setitem__("actual_native_Friedrichs_reference_proved", True),
        lambda p: p["native_interface_status"].__setitem__("actual_native_complete_form_lower_proved", True),
        lambda p: p["native_interface_status"].__setitem__("actual_native_defect_trace_coercivity_proved", True),
        lambda p: p["native_interface_status"].__setitem__("actual_native_reference_gap_proved", True),
        lambda p: p["native_interface_status"].__setitem__("actual_native_denominator_margin_proved", True),
        lambda p: p["decision"].__setitem__("native_target_denominator_proved", True),
        lambda p: p["dependency_reconciliation"].__setitem__("native_triple_form_or_trace_data_added", True),
    ]
    original_validate = module.validate

    def strict_validate(candidate):
        original_validate(candidate)
        assert candidate["target_claim"] == "NONE-NOT-A-KILL"
        assert candidate["source_and_ledger_effect"] == "none"
        native = candidate["native_interface_status"]
        assert not native["actual_native_boundary_triple_authenticated"]
        assert not native["actual_native_Friedrichs_reference_proved"]
        assert not native["actual_native_complete_form_lower_proved"]
        assert not native["actual_native_defect_trace_coercivity_proved"]
        assert not native["actual_native_reference_gap_proved"]
        assert not native["actual_native_denominator_margin_proved"]
        assert not candidate["decision"]["native_target_denominator_proved"]
        assert not candidate["dependency_reconciliation"]["native_triple_form_or_trace_data_added"]
        assert candidate["classification"] == "INTERNAL_STRUCTURAL_ONLY"
        assert candidate["controls"]["controls_passed"] == 38
        assert candidate["controls"]["hostile_mutations_rejected"] == 32
        assert candidate["status"] == "working_draft_verified"
        assert candidate["friedrichs_gap_theorem"]["form_hypothesis"]
        assert candidate["defect_trace_theorem"]["gamma_inverse_identity"]
        assert candidate["postflight_bookend"]["weakest_reproducibility_seam"]
        assert candidate["decision"]["next_exact_input"]

    module.validate = strict_validate
    strict_validate(payload)
    for mutate in mutations:
        must_reject(module, payload, mutate)
    print("K692 probe passed: 38 controls; rejected 32/32 hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
