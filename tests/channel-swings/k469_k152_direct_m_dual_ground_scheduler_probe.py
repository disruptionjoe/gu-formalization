#!/usr/bin/env python3
"""Independent controls and hostile mutations for K469."""

from __future__ import annotations

import copy
from fractions import Fraction

from k469_k152_direct_m_dual_ground_scheduler import deficit_upper, demo, residual_budget


def controls(packet):
    theorem, exact, release = packet["theorem"], packet["exact_two_block_control"], packet["release_rule"]
    return [
        ("schema", packet["schema_version"] == "1.0"),
        ("id", packet["result_id"] == "K469-K152-DIRECT-M-DUAL-GROUND-SCHEDULER"),
        ("classification", packet["classification"] == "INTERNAL_STRUCTURAL_ONLY"),
        ("direction", packet["direction"] == "observed_to_native"),
        ("premise", "complete M-orthogonal complement" in theorem["premise"]),
        ("cross norm", "M-dual" in theorem["cross_norm"]),
        ("interval", "sqrt" in theorem["ground_interval"]),
        ("budget", theorem["target_budget"] == "eta^2<=d(beta-rho+d)"),
        ("shift free", theorem["shift_required"] is False),
        ("bridge free", theorem["K466_bridge_required_on_this_route"] is False),
        ("floor required", theorem["complete_complement_floor_still_required"] is True),
        ("deficit", exact["ground_deficit"] == "1/2"),
        ("budget equality", exact["M_dual_square_budget"] == "9/4" and exact["equality"] is True),
        ("payload", release["finite_Gram_entries"] == 59586),
        ("no beta", release["native_beta_present"] is False),
        ("no target", release["native_target_deficit_present"] is False),
        ("no release", release["native_accuracy_released"] is False),
    ]


def main() -> int:
    packet = demo()
    base = controls(packet)
    mutations = [
        lambda d: d.__setitem__("classification", "PHYSICAL"),
        lambda d: d.__setitem__("direction", "native_to_observed"),
        lambda d: d["theorem"].__setitem__("premise", "finite Ritz floor"),
        lambda d: d["theorem"].__setitem__("cross_norm", "Hilbert norm"),
        lambda d: d["theorem"].__setitem__("ground_interval", "[rho,rho]"),
        lambda d: d["theorem"].__setitem__("target_budget", "eta^2<=d(beta-rho-d)"),
        lambda d: d["theorem"].__setitem__("shift_required", True),
        lambda d: d["theorem"].__setitem__("K466_bridge_required_on_this_route", True),
        lambda d: d["theorem"].__setitem__("complete_complement_floor_still_required", False),
        lambda d: d["exact_two_block_control"].__setitem__("ground_deficit", "0"),
        lambda d: d["exact_two_block_control"].__setitem__("equality", False),
        lambda d: d["release_rule"].__setitem__("finite_Gram_entries", 0),
        lambda d: d["release_rule"].__setitem__("native_beta_present", True),
        lambda d: d["release_rule"].__setitem__("native_target_deficit_present", True),
        lambda d: d["release_rule"].__setitem__("native_accuracy_released", True),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(packet)
        mutate(candidate)
        rejected += not all(ok for _, ok in controls(candidate))
    invalid = 0
    for args in ((0, 0, 0), (0, 1, -1)):
        try:
            deficit_upper(*args)
        except ValueError:
            invalid += 1
    try:
        residual_budget(0, 1, 0)
    except ValueError:
        invalid += 1
    assert deficit_upper(-2, 2, Fraction(9, 4)) == Fraction(1, 2)
    print(f"K469 EXACT CONTROL: {sum(ok for _, ok in base)}/{len(base)} pass")
    print(f"K469 HOSTILE MUTATIONS: {rejected}/{len(mutations)} rejected")
    print(f"K469 INVALID INPUTS: {invalid}/3 rejected")
    return 0 if all(ok for _, ok in base) and rejected == len(mutations) and invalid == 3 else 1


if __name__ == "__main__":
    raise SystemExit(main())
