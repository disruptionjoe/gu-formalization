#!/usr/bin/env python3
"""Independent controls and hostile mutations for K471."""

from __future__ import annotations

import copy

from k471_k77_effective_homology_transfer import demo, transfer


def controls(packet):
    theorem, exact, native = packet["theorem"], packet["exact_schur_control"], packet["native_status"]
    return [
        ("schema", packet["schema_version"] == "1.0"),
        ("id", packet["result_id"] == "K471-K77-EFFECTIVE-HOMOLOGY-TRANSFER"),
        ("classification", packet["classification"] == "INTERNAL_STRUCTURAL_ONLY"),
        ("direction", packet["direction"] == "observed_to_native"),
        ("retract", theorem["base_retract"] == "dh+hd=I-ip with ph=hi=h^2=0"),
        ("nilpotence", "D^2=0" in theorem["perturbed_differential"]),
        ("invertibility", "invertible" in theorem["invertibility"]),
        ("effective", theorem["effective_differential"] == "d_H'=p(1+delta h)^(-1)delta i"),
        ("adapted", "i'=" in theorem["adapted_data"] and "p'=" in theorem["adapted_data"] and "h'=" in theorem["adapted_data"]),
        ("conclusion", "deformation retracts" in theorem["conclusion"]),
        ("smallness", theorem["smallness_is_sufficient_not_necessary"] is True),
        ("domain", theorem["closed_domain_preservation_still_required"] is True),
        ("pivot", exact["pivot"] == "3/2"),
        ("effective control", exact["effective_differential"] == "17/18"),
        ("inclusion", exact["adapted_inclusion_h1"] == ["-2/9", "1"]),
        ("projection", exact["adapted_projection_h0"] == ["-1/6", "1"]),
        ("homotopy", exact["adapted_homotopy"] == [["2/3", "0"], ["0", "0"]]),
        ("identities", exact["both_retract_identities_exact"] is True),
        ("no coefficients", native["actual_action_coefficients_present"] is False),
        ("no selection", native["native_K77_packet_selected"] is False),
        ("no physics", native["physical_cohomology_claimed"] is False),
    ]


def main() -> int:
    packet = demo()
    base = controls(packet)
    mutations = [
        lambda d: d.__setitem__("classification", "PHYSICAL"),
        lambda d: d.__setitem__("direction", "native_to_observed"),
        lambda d: d["theorem"].__setitem__("base_retract", "dh=I"),
        lambda d: d["theorem"].__setitem__("perturbed_differential", "D=d+delta"),
        lambda d: d["theorem"].__setitem__("invertibility", "assumed"),
        lambda d: d["theorem"].__setitem__("effective_differential", "p delta i"),
        lambda d: d["theorem"].__setitem__("adapted_data", "unchanged"),
        lambda d: d["theorem"].__setitem__("conclusion", "physical cohomology"),
        lambda d: d["theorem"].__setitem__("smallness_is_sufficient_not_necessary", False),
        lambda d: d["theorem"].__setitem__("closed_domain_preservation_still_required", False),
        lambda d: d["exact_schur_control"].__setitem__("pivot", "1"),
        lambda d: d["exact_schur_control"].__setitem__("effective_differential", "1"),
        lambda d: d["exact_schur_control"].__setitem__("adapted_inclusion_h1", []),
        lambda d: d["exact_schur_control"].__setitem__("adapted_projection_h0", []),
        lambda d: d["exact_schur_control"].__setitem__("adapted_homotopy", []),
        lambda d: d["exact_schur_control"].__setitem__("both_retract_identities_exact", False),
        lambda d: d["native_status"].__setitem__("actual_action_coefficients_present", True),
        lambda d: d["native_status"].__setitem__("native_K77_packet_selected", True),
        lambda d: d["native_status"].__setitem__("physical_cohomology_claimed", True),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(packet)
        mutate(candidate)
        rejected += not all(ok for _, ok in controls(candidate))
    invalid = 0
    try:
        transfer(-1, 0, 0, 0)
    except ValueError:
        invalid += 1
    print(f"K471 EXACT CONTROL: {sum(ok for _, ok in base)}/{len(base)} pass")
    print(f"K471 HOSTILE MUTATIONS: {rejected}/{len(mutations)} rejected")
    print(f"K471 INVALID INPUTS: {invalid}/1 rejected")
    return 0 if all(ok for _, ok in base) and rejected == len(mutations) and invalid == 1 else 1


if __name__ == "__main__":
    raise SystemExit(main())
