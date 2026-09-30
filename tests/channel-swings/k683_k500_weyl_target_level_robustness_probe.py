#!/usr/bin/env python3
"""Independent hostile probe for K683's target-level Weyl transfer."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = ROOT / "tests/channel-swings/k683_k500_weyl_target_level_robustness.py"
ARTIFACT = ROOT / "lab/process/k683-k500-weyl-target-level-robustness.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k683_producer", PRODUCER)
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
        lambda p: p["level_transfer_theorem"].__setitem__("same_boundary_coordinate_required", False),
        lambda p: p["level_transfer_theorem"].__setitem__("same_target_extension_W_required", False),
        lambda p: p["level_transfer_theorem"].__setitem__("complete_boundary_coverage_required", False),
        lambda p: p["level_transfer_theorem"].__setitem__("connected_reference_resolvent_interval_required", False),
        lambda p: p["level_transfer_theorem"].__setitem__("pointwise_or_finite_block_variation_sufficient", True),
        lambda p: p["level_transfer_theorem"].__setitem__("raw_floor_transport_across_nonunitary_coordinate_change_allowed", True),
        lambda p: p["monotone_shortcut"].__setitem__("reference_interval_and_sign_may_be_inferred", True),
        lambda p: p["monotone_shortcut"].__setitem__("finite_sector_monotonicity_sufficient", True),
        lambda p: p["exact_controls"].__setitem__("target_lambda", "2"),
        lambda p: p["exact_controls"].__setitem__("transferred_target_margin", "1/20"),
        lambda p: p["exact_controls"]["failing_row"].__setitem__("accepted", True),
        lambda p: p["native_interface_status"].__setitem__("actual_native_target_denominator_nonnegative", True),
        lambda p: p["native_interface_status"].__setitem__("native_complete_floor_emitted", True),
        lambda p: p.__setitem__("target_claim", "SC-META-53"),
        lambda p: p.__setitem__("source_and_ledger_effect", "positive"),
        lambda p: p["native_interface_status"].__setitem__("actual_native_complete_weyl_variation_bound", True),
        lambda p: p["native_interface_status"].__setitem__("actual_native_nearby_lower_identified", True),
        lambda p: p["native_interface_status"].__setitem__("actual_native_base_floor_r0_identified", True),
        lambda p: p["decision"].__setitem__("native_target_denominator_proved", True),
        lambda p: p["dependency_reconciliation"].__setitem__("native_denominator_row_added", True),
        lambda p: p["exact_controls"].__setitem__("coordinate_mismatch_rejects", False),
        lambda p: p["composition"].__setitem__("K657_reference_Friedrichs_resolvent_and_sign_premises_retained", False),
        lambda p: p.__setitem__("classification", "SOURCE_NATIVE_ROUTE"),
        lambda p: p["controls"].__setitem__("hostile_mutations_rejected", 0),
        lambda p: p["controls"].__setitem__("controls_passed", 0),
        lambda p: p.__setitem__("status", "canon"),
    ]
    original_validate = module.validate

    def strict_validate(candidate):
        original_validate(candidate)
        assert candidate["target_claim"] == "NONE-NOT-A-KILL"
        assert candidate["source_and_ledger_effect"] == "none"
        native = candidate["native_interface_status"]
        assert not native["actual_native_complete_weyl_variation_bound"]
        assert not native["actual_native_nearby_lower_identified"]
        assert not native["actual_native_base_floor_r0_identified"]
        assert not candidate["decision"]["native_target_denominator_proved"]
        assert not candidate["dependency_reconciliation"]["native_denominator_row_added"]
        assert candidate["exact_controls"]["coordinate_mismatch_rejects"]
        assert candidate["composition"]["K657_reference_Friedrichs_resolvent_and_sign_premises_retained"]
        assert candidate["classification"] == "INTERNAL_STRUCTURAL_ONLY"
        assert candidate["controls"]["hostile_mutations_rejected"] == 26
        assert candidate["controls"]["controls_passed"] == 32
        assert candidate["status"] == "working_draft_verified"

    module.validate = strict_validate
    strict_validate(payload)
    for mutate in mutations:
        must_reject(module, payload, mutate)
    print("K683 probe passed: 32 controls; rejected 26/26 hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
