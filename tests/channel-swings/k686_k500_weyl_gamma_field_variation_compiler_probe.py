#!/usr/bin/env python3
"""Independent hostile probe for K686's Weyl gamma-field compiler."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = ROOT / "tests/channel-swings/k686_k500_weyl_gamma_field_variation_compiler.py"
ARTIFACT = ROOT / "lab/process/k686-k500-weyl-gamma-field-variation-compiler.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k686_producer", PRODUCER)
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
        lambda p: p["gamma_field_identity"].__setitem__("connected_reference_resolvent_interval_required", False),
        lambda p: p["gamma_field_identity"].__setitem__("same_boundary_coordinate_required", False),
        lambda p: p["gamma_field_identity"].__setitem__("complete_boundary_space_required", False),
        lambda p: p["gamma_field_identity"].__setitem__("finite_sector_gamma_bounds_sufficient", True),
        lambda p: p["gamma_field_identity"].__setitem__("nonreal_contour_bound_substitutable_without_real_interval_proof", True),
        lambda p: p["target_composition"].__setitem__("level_distance", "1/10"),
        lambda p: p["target_composition"].__setitem__("complete_weyl_variation_omega", "1/100"),
        lambda p: p["target_composition"].__setitem__("transferred_target_margin", "0"),
        lambda p: p["target_composition"].__setitem__("accepted", False),
        lambda p: p["failing_control"].__setitem__("transferred_target_margin", "1/100"),
        lambda p: p["failing_control"].__setitem__("accepted", True),
        lambda p: p["native_interface_status"].__setitem__("actual_native_complete_gamma_norms_proved", True),
        lambda p: p["native_interface_status"].__setitem__("native_complete_floor_emitted", True),
        lambda p: p.__setitem__("target_claim", "SC-META-53"),
        lambda p: p.__setitem__("source_and_ledger_effect", "positive"),
        lambda p: p["native_interface_status"].__setitem__("actual_native_boundary_triple_authenticated", True),
        lambda p: p["native_interface_status"].__setitem__("actual_native_Friedrichs_reference_proved", True),
        lambda p: p["native_interface_status"].__setitem__("actual_native_real_interval_authenticated", True),
        lambda p: p["native_interface_status"].__setitem__("actual_native_weyl_variation_bound_proved", True),
        lambda p: p["native_interface_status"].__setitem__("actual_native_target_denominator_nonnegative", True),
        lambda p: p["decision"].__setitem__("native_target_denominator_proved", True),
        lambda p: p["dependency_reconciliation"].__setitem__("native_gamma_bound_added", True),
        lambda p: p.__setitem__("classification", "SOURCE_NATIVE_ROUTE"),
        lambda p: p["controls"].__setitem__("controls_passed", 0),
        lambda p: p["controls"].__setitem__("hostile_mutations_rejected", 0),
        lambda p: p.__setitem__("status", "canon"),
        lambda p: p["gamma_field_identity"].pop("two_point_identity"),
        lambda p: p["gu_typed_objects"].pop("gamma_field"),
        lambda p: p["postflight_bookend"].pop("weakest_reproducibility_seam"),
    ]
    original_validate = module.validate

    def strict_validate(candidate):
        original_validate(candidate)
        assert candidate["target_claim"] == "NONE-NOT-A-KILL"
        assert candidate["source_and_ledger_effect"] == "none"
        native = candidate["native_interface_status"]
        assert not native["actual_native_boundary_triple_authenticated"]
        assert not native["actual_native_Friedrichs_reference_proved"]
        assert not native["actual_native_real_interval_authenticated"]
        assert not native["actual_native_weyl_variation_bound_proved"]
        assert not native["actual_native_target_denominator_nonnegative"]
        assert not candidate["decision"]["native_target_denominator_proved"]
        assert not candidate["dependency_reconciliation"]["native_gamma_bound_added"]
        assert candidate["classification"] == "INTERNAL_STRUCTURAL_ONLY"
        assert candidate["controls"]["controls_passed"] == 35
        assert candidate["controls"]["hostile_mutations_rejected"] == 29
        assert candidate["status"] == "working_draft_verified"
        assert candidate["gamma_field_identity"]["two_point_identity"]
        assert candidate["gu_typed_objects"]["gamma_field"]
        assert candidate["postflight_bookend"]["weakest_reproducibility_seam"]

    module.validate = strict_validate
    strict_validate(payload)
    for mutate in mutations:
        must_reject(module, payload, mutate)
    print("K686 probe passed: 35 controls; rejected 29/29 hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
