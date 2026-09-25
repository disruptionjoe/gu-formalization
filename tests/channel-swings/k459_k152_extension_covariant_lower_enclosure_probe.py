#!/usr/bin/env python3
"""Independent controls and hostile mutations for K459."""

from __future__ import annotations

import copy

from k459_k152_extension_covariant_lower_enclosure import demo


def controls(packet):
    covariance = packet.get("covariance", {})
    boundary = packet.get("native_boundary", {})
    control = packet.get("exact_control", {})
    return [
        ("schema", packet.get("schema_version") == "1.0"),
        ("id", packet.get("result_id") == "K459-K152-EXTENSION-COVARIANT-LOWER-ENCLOSURE"),
        ("classification", packet.get("classification") == "INTERNAL_STRUCTURAL_ONLY"),
        ("direction", packet.get("direction") == "observed_to_native"),
        ("extension", control.get("extension") == "7"),
        ("base interval", control.get("base", {}).get("interval_lower") == "-3"),
        ("translated interval", control.get("translated", {}).get("interval_lower") == "4"),
        ("rayleigh covariance", covariance.get("rayleigh_translates_by_extension") is True),
        ("floor covariance", covariance.get("exterior_floor_translates_by_extension") is True),
        ("shift covariance", covariance.get("coercive_shift_translates_oppositely") is True),
        ("internal invariance", covariance.get("all_K152_internal_quantities_invariant") is True),
        ("interval covariance", covariance.get("interval_translates_by_extension") is True),
        ("relative no selection", boundary.get("selected_scalar_center_required_for_relative_coordinate_family") is False),
        ("absolute selection", boundary.get("selected_scalar_center_required_for_absolute_physical_placement") is True),
        ("base coercivity needed", boundary.get("center_zero_coercivity_or_left_floor_still_required") is True),
        ("count needed", boundary.get("complete_complement_or_count_certificate_still_required") is True),
        ("no native values", boundary.get("native_K162_values_emitted") is False),
    ]


def main() -> int:
    packet = demo()
    base = controls(packet)
    mutations = [
        lambda d: d.__setitem__("schema_version", "0"),
        lambda d: d.__setitem__("result_id", "K458"),
        lambda d: d.__setitem__("classification", "PHYSICAL"),
        lambda d: d.__setitem__("direction", "native_to_observed"),
        lambda d: d["exact_control"].__setitem__("extension", "6"),
        lambda d: d["exact_control"]["base"].__setitem__("interval_lower", "-2"),
        lambda d: d["exact_control"]["translated"].__setitem__("interval_lower", "5"),
        lambda d: d["covariance"].__setitem__("rayleigh_translates_by_extension", False),
        lambda d: d["covariance"].__setitem__("exterior_floor_translates_by_extension", False),
        lambda d: d["covariance"].__setitem__("coercive_shift_translates_oppositely", False),
        lambda d: d["covariance"].__setitem__("all_K152_internal_quantities_invariant", False),
        lambda d: d["covariance"].__setitem__("interval_translates_by_extension", False),
        lambda d: d["native_boundary"].__setitem__("selected_scalar_center_required_for_relative_coordinate_family", True),
        lambda d: d["native_boundary"].__setitem__("selected_scalar_center_required_for_absolute_physical_placement", False),
        lambda d: d["native_boundary"].__setitem__("center_zero_coercivity_or_left_floor_still_required", False),
        lambda d: d["native_boundary"].__setitem__("complete_complement_or_count_certificate_still_required", False),
        lambda d: d["native_boundary"].__setitem__("native_K162_values_emitted", True),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(packet)
        mutate(candidate)
        if not all(ok for _, ok in controls(candidate)):
            rejected += 1
    print(f"K459 EXACT CONTROL: {sum(ok for _, ok in base)}/{len(base)} pass")
    print(f"K459 HOSTILE MUTATIONS: {rejected}/{len(mutations)} rejected")
    return 0 if all(ok for _, ok in base) and rejected == len(mutations) else 1


if __name__ == "__main__":
    raise SystemExit(main())
