#!/usr/bin/env python3
"""Independent hostile probe for K689's gamma-anchor compiler."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = ROOT / "tests/channel-swings/k689_k500_gamma_anchor_propagation_compiler.py"
ARTIFACT = ROOT / "lab/process/k689-k500-gamma-anchor-propagation-compiler.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k689_producer", PRODUCER)
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
        lambda p: p["gamma_resolvent_theorem"].__setitem__("same_reference_required", False),
        lambda p: p["gamma_resolvent_theorem"].__setitem__("same_boundary_coordinate_required", False),
        lambda p: p["gamma_resolvent_theorem"].__setitem__("complete_boundary_space_required", False),
        lambda p: p["gamma_resolvent_theorem"].__setitem__("real_interval_inside_reference_resolvent_required", False),
        lambda p: p["gamma_resolvent_theorem"].__setitem__("finite_sector_gap_sufficient", True),
        lambda p: p["gamma_resolvent_theorem"].__setitem__("endpoint_membership_without_quantitative_gap_sufficient", True),
        lambda p: p["gamma_resolvent_theorem"].__setitem__("anchor_from_different_boundary_triple_substitutable", True),
        lambda p: p["target_composition"].__setitem__("propagation_factor", "1"),
        lambda p: p["target_composition"].__setitem__("target_gamma_norm_upper", "1/5"),
        lambda p: p["target_composition"].__setitem__("K686_weyl_variation_upper", "1/100"),
        lambda p: p["target_composition"].__setitem__("transferred_target_margin", "0"),
        lambda p: p["target_composition"].__setitem__("accepted", False),
        lambda p: p["native_interface_status"].__setitem__("actual_native_target_gamma_norm_proved", True),
        lambda p: p["native_interface_status"].__setitem__("native_complete_floor_emitted", True),
        lambda p: p.__setitem__("target_claim", "SC-META-53"),
        lambda p: p.__setitem__("source_and_ledger_effect", "positive"),
        lambda p: p["native_interface_status"].__setitem__("actual_native_boundary_triple_authenticated", True),
        lambda p: p["native_interface_status"].__setitem__("actual_native_Friedrichs_reference_proved", True),
        lambda p: p["native_interface_status"].__setitem__("actual_native_reference_spectral_distance_proved", True),
        lambda p: p["native_interface_status"].__setitem__("actual_native_anchor_gamma_norm_proved", True),
        lambda p: p["native_interface_status"].__setitem__("actual_native_denominator_margin_proved", True),
        lambda p: p["decision"].__setitem__("native_target_denominator_proved", True),
        lambda p: p["dependency_reconciliation"].__setitem__("native_gamma_anchor_or_gap_added", True),
        lambda p: p.__setitem__("classification", "SOURCE_NATIVE_ROUTE"),
        lambda p: p["controls"].__setitem__("controls_passed", 0),
        lambda p: p["controls"].__setitem__("hostile_mutations_rejected", 0),
        lambda p: p["gamma_resolvent_theorem"].pop("identity"),
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
        assert not native["actual_native_reference_spectral_distance_proved"]
        assert not native["actual_native_anchor_gamma_norm_proved"]
        assert not native["actual_native_denominator_margin_proved"]
        assert not candidate["decision"]["native_target_denominator_proved"]
        assert not candidate["dependency_reconciliation"]["native_gamma_anchor_or_gap_added"]
        assert candidate["classification"] == "INTERNAL_STRUCTURAL_ONLY"
        assert candidate["controls"]["controls_passed"] == 34
        assert candidate["controls"]["hostile_mutations_rejected"] == 28
        assert candidate["gamma_resolvent_theorem"]["identity"]
        assert candidate["postflight_bookend"]["weakest_reproducibility_seam"]

    module.validate = strict_validate
    strict_validate(payload)
    for mutate in mutations:
        must_reject(module, payload, mutate)
    print("K689 probe passed: 34 controls; rejected 28/28 hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
