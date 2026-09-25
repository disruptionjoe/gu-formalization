#!/usr/bin/env python3
"""Independent controls and hostile mutations for K460."""

from __future__ import annotations

import copy

from k460_k152_hvz_membership_complement_boundary import demo


def controls(packet):
    replay = packet.get("K169_replay", {})
    independence = packet.get("independence", {})
    boundary = packet.get("native_boundary", {})
    rows = packet.get("exact_controls", [])
    return [
        ("schema", packet.get("schema_version") == "1.0"),
        ("id", packet.get("result_id") == "K460-K152-HVZ-MEMBERSHIP-COMPLEMENT-BOUNDARY"),
        ("classification", packet.get("classification") == "INTERNAL_STRUCTURAL_ONLY"),
        ("direction", packet.get("direction") == "observed_to_native"),
        ("cluster cost", replay.get("neutral_cluster_cost") == "5/2"),
        ("not first", replay.get("membership_proves_first_threshold") is False),
        ("not floor", replay.get("membership_proves_complete_complement_floor") is False),
        ("three controls", len(rows) == 3),
        ("same trial", independence.get("same_trial_data") is True),
        ("same threshold", independence.get("same_named_HVZ_threshold") is True),
        ("same essential edge", independence.get("same_essential_edge") is True),
        ("floor differs", independence.get("different_complete_complement_floors") is True),
        ("count differs", independence.get("different_counts_below_threshold") is True),
        ("abstract only", boundary.get("abstract_controls_are_K162_values") is False),
        ("no K169 substitution", boundary.get("K169_membership_may_be_used_as_K162_complement_floor") is False),
        ("three native routes", len(boundary.get("valid_native_routes", [])) == 3),
        ("hidden floor", rows[1].get("complete_complement_floor") == "-1"),
        ("hidden count", rows[1].get("spectral_count_strictly_below_named_threshold") == 2),
    ]


def main() -> int:
    packet = demo()
    base = controls(packet)
    mutations = [
        lambda d: d.__setitem__("schema_version", "0"),
        lambda d: d.__setitem__("result_id", "K459"),
        lambda d: d.__setitem__("classification", "PHYSICAL"),
        lambda d: d.__setitem__("direction", "native_to_observed"),
        lambda d: d["K169_replay"].__setitem__("neutral_cluster_cost", "3"),
        lambda d: d["K169_replay"].__setitem__("membership_proves_first_threshold", True),
        lambda d: d["K169_replay"].__setitem__("membership_proves_complete_complement_floor", True),
        lambda d: d.__setitem__("exact_controls", d["exact_controls"][:2]),
        lambda d: d["independence"].__setitem__("same_trial_data", False),
        lambda d: d["independence"].__setitem__("same_named_HVZ_threshold", False),
        lambda d: d["independence"].__setitem__("same_essential_edge", False),
        lambda d: d["independence"].__setitem__("different_complete_complement_floors", False),
        lambda d: d["independence"].__setitem__("different_counts_below_threshold", False),
        lambda d: d["native_boundary"].__setitem__("abstract_controls_are_K162_values", True),
        lambda d: d["native_boundary"].__setitem__("K169_membership_may_be_used_as_K162_complement_floor", True),
        lambda d: d["native_boundary"].__setitem__("valid_native_routes", []),
        lambda d: d["exact_controls"][1].__setitem__("complete_complement_floor", "1/2"),
        lambda d: d["exact_controls"][1].__setitem__("spectral_count_strictly_below_named_threshold", 1),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(packet)
        mutate(candidate)
        if not all(ok for _, ok in controls(candidate)):
            rejected += 1
    print(f"K460 EXACT CONTROL: {sum(ok for _, ok in base)}/{len(base)} pass")
    print(f"K460 HOSTILE MUTATIONS: {rejected}/{len(mutations)} rejected")
    return 0 if all(ok for _, ok in base) and rejected == len(mutations) else 1


if __name__ == "__main__":
    raise SystemExit(main())
