#!/usr/bin/env python3
"""Independent controls and hostile mutations for K458."""

from __future__ import annotations

import copy

from k458_k152_spectral_independence_boundary import demo


def controls(packet):
    independence = packet.get("independence", {})
    boundary = packet.get("native_boundary", {})
    ready = packet.get("K455_readiness_after_K456_K458", {})
    return [
        ("schema", packet.get("schema_version") == "1.0"),
        ("id", packet.get("result_id") == "K458-K152-SPECTRAL-INDEPENDENCE-BOUNDARY"),
        ("classification", packet.get("classification") == "INTERNAL_STRUCTURAL_ONLY"),
        ("direction", packet.get("direction") == "observed_to_native"),
        ("three controls", len(packet.get("exact_controls", [])) == 3),
        ("shared trial", independence.get("all_trial_data_identical") is True),
        ("complement independent", independence.get("orthogonal_compression_floor_not_determined") is True),
        ("next independent", independence.get("next_distinct_spectrum_not_determined") is True),
        ("coercivity independent", independence.get("shifted_coercivity_not_determined") is True),
        ("left independent", independence.get("native_left_floor_not_determined") is True),
        ("abstract only", boundary.get("abstract_controls_are_K162_values") is False),
        ("no floor implication", boundary.get("action_column_plus_residual_implies_exterior_floor") is False),
        ("no coercivity implication", boundary.get("action_column_plus_residual_implies_coercivity") is False),
        ("no next implication", boundary.get("action_column_plus_residual_implies_next_distinct_spectrum") is False),
        ("no left implication", boundary.get("action_column_plus_residual_implies_native_left_floor") is False),
        ("column serialized", ready.get("complete_continuum_action_column_serialized") is True),
        ("residual serialized", ready.get("complete_shifted_form_dual_residual_serialized") is True),
        ("coercivity pending", ready.get("coercivity_serialized") is False),
        ("next pending", ready.get("next_distinct_spectrum_serialized") is False),
        ("left pending", ready.get("native_left_floor_serialized") is False),
        ("no interval", ready.get("native_K152_interval_emitted") is False),
    ]


def main() -> int:
    packet = demo()
    base = controls(packet)
    mutations = [
        lambda d: d.__setitem__("schema_version", "0"),
        lambda d: d.__setitem__("result_id", "K457"),
        lambda d: d.__setitem__("classification", "PHYSICAL"),
        lambda d: d.__setitem__("direction", "native_to_observed"),
        lambda d: d.__setitem__("exact_controls", d["exact_controls"][:2]),
        lambda d: d["independence"].__setitem__("all_trial_data_identical", False),
        lambda d: d["independence"].__setitem__("orthogonal_compression_floor_not_determined", False),
        lambda d: d["independence"].__setitem__("next_distinct_spectrum_not_determined", False),
        lambda d: d["independence"].__setitem__("shifted_coercivity_not_determined", False),
        lambda d: d["independence"].__setitem__("native_left_floor_not_determined", False),
        lambda d: d["native_boundary"].__setitem__("abstract_controls_are_K162_values", True),
        lambda d: d["native_boundary"].__setitem__("action_column_plus_residual_implies_exterior_floor", True),
        lambda d: d["native_boundary"].__setitem__("action_column_plus_residual_implies_coercivity", True),
        lambda d: d["native_boundary"].__setitem__("action_column_plus_residual_implies_next_distinct_spectrum", True),
        lambda d: d["native_boundary"].__setitem__("action_column_plus_residual_implies_native_left_floor", True),
        lambda d: d["K455_readiness_after_K456_K458"].__setitem__("complete_continuum_action_column_serialized", False),
        lambda d: d["K455_readiness_after_K456_K458"].__setitem__("complete_shifted_form_dual_residual_serialized", False),
        lambda d: d["K455_readiness_after_K456_K458"].__setitem__("coercivity_serialized", True),
        lambda d: d["K455_readiness_after_K456_K458"].__setitem__("next_distinct_spectrum_serialized", True),
        lambda d: d["K455_readiness_after_K456_K458"].__setitem__("native_left_floor_serialized", True),
        lambda d: d["K455_readiness_after_K456_K458"].__setitem__("native_K152_interval_emitted", True),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(packet)
        mutate(candidate)
        if not all(ok for _, ok in controls(candidate)):
            rejected += 1
    print(f"K458 EXACT CONTROL: {sum(ok for _, ok in base)}/{len(base)} pass")
    print(f"K458 HOSTILE MUTATIONS: {rejected}/{len(mutations)} rejected")
    return 0 if all(ok for _, ok in base) and rejected == len(mutations) else 1


if __name__ == "__main__":
    raise SystemExit(main())
