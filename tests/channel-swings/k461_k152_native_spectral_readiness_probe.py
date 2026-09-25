#!/usr/bin/env python3
"""Independent controls and hostile mutations for K461."""

from __future__ import annotations

import copy

from k461_k152_native_spectral_readiness import demo


def controls(packet):
    current = packet.get("current_native_readiness", {})
    positive = packet.get("exact_positive_control", {})
    decision = packet.get("decision", {})
    return [
        ("schema", packet.get("schema_version") == "1.0"),
        ("id", packet.get("result_id") == "K461-K152-NATIVE-SPECTRAL-READINESS"),
        ("classification", packet.get("classification") == "INTERNAL_STRUCTURAL_ONLY"),
        ("direction", packet.get("direction") == "observed_to_native"),
        ("three routes", len(packet.get("accepted_spectral_routes", [])) == 3),
        ("missing coercivity", current.get("missing_common_references") == ["center_zero_coercivity_ref"]),
        ("no current route", current.get("spectral_route") is None),
        ("current relative not ready", current.get("relative_coordinate_family_ready") is False),
        ("current absolute not ready", current.get("absolute_physical_axis_ready") is False),
        ("positive flux route", positive.get("spectral_route") == "native_flux_rank_one_count"),
        ("positive rank one", positive.get("rank_one_count_below_b") is True),
        ("positive floor released", positive.get("next_distinct_floor_b_released") is True),
        ("positive relative ready", positive.get("relative_coordinate_family_ready") is True),
        ("positive absolute not ready", positive.get("absolute_physical_axis_ready") is False),
        ("relative no center", positive.get("selected_extension_center_required_for_relative_family") is False),
        ("absolute center", positive.get("selected_extension_center_required_for_absolute_axis") is True),
        ("no native relative interval", current.get("native_K152_relative_interval_emitted") is False),
        ("no native absolute interval", current.get("native_K152_absolute_interval_emitted") is False),
        ("column released", decision.get("K456_column_released") is True),
        ("residual released", decision.get("K457_residual_released") is True),
        ("no HVZ substitution", decision.get("K169_HVZ_membership_released_as_complement_floor") is False),
        ("center correction", decision.get("selected_center_removed_from_relative_readiness") is True),
        ("next exact", "rank-one-below-b certificate" in decision.get("next_exact_input", "")),
    ]


def main() -> int:
    packet = demo()
    base = controls(packet)
    mutations = [
        lambda d: d.__setitem__("schema_version", "0"),
        lambda d: d.__setitem__("result_id", "K460"),
        lambda d: d.__setitem__("classification", "PHYSICAL"),
        lambda d: d.__setitem__("direction", "native_to_observed"),
        lambda d: d.__setitem__("accepted_spectral_routes", []),
        lambda d: d["current_native_readiness"].__setitem__("missing_common_references", []),
        lambda d: d["current_native_readiness"].__setitem__("spectral_route", "HVZ"),
        lambda d: d["current_native_readiness"].__setitem__("relative_coordinate_family_ready", True),
        lambda d: d["current_native_readiness"].__setitem__("absolute_physical_axis_ready", True),
        lambda d: d["exact_positive_control"].__setitem__("spectral_route", None),
        lambda d: d["exact_positive_control"].__setitem__("rank_one_count_below_b", False),
        lambda d: d["exact_positive_control"].__setitem__("next_distinct_floor_b_released", False),
        lambda d: d["exact_positive_control"].__setitem__("relative_coordinate_family_ready", False),
        lambda d: d["exact_positive_control"].__setitem__("absolute_physical_axis_ready", True),
        lambda d: d["exact_positive_control"].__setitem__("selected_extension_center_required_for_relative_family", True),
        lambda d: d["exact_positive_control"].__setitem__("selected_extension_center_required_for_absolute_axis", False),
        lambda d: d["current_native_readiness"].__setitem__("native_K152_relative_interval_emitted", True),
        lambda d: d["current_native_readiness"].__setitem__("native_K152_absolute_interval_emitted", True),
        lambda d: d["decision"].__setitem__("K456_column_released", False),
        lambda d: d["decision"].__setitem__("K457_residual_released", False),
        lambda d: d["decision"].__setitem__("K169_HVZ_membership_released_as_complement_floor", True),
        lambda d: d["decision"].__setitem__("selected_center_removed_from_relative_readiness", False),
        lambda d: d["decision"].__setitem__("next_exact_input", "repeat finite audit"),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(packet)
        mutate(candidate)
        if not all(ok for _, ok in controls(candidate)):
            rejected += 1
    print(f"K461 EXACT CONTROL: {sum(ok for _, ok in base)}/{len(base)} pass")
    print(f"K461 HOSTILE MUTATIONS: {rejected}/{len(mutations)} rejected")
    return 0 if all(ok for _, ok in base) and rejected == len(mutations) else 1


if __name__ == "__main__":
    raise SystemExit(main())
