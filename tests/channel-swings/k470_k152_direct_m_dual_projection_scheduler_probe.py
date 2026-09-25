#!/usr/bin/env python3
"""Independent controls and hostile mutations for K470."""

from __future__ import annotations

import copy

from k470_k152_direct_m_dual_projection_scheduler import demo, projection_residual_budget, projection_sq_upper


def controls(packet):
    theorem, exact, native = packet["theorem"], packet["exact_two_block_control"], packet["native_status"]
    return [
        ("schema", packet["schema_version"] == "1.0"),
        ("id", packet["result_id"] == "K470-K152-DIRECT-M-DUAL-PROJECTION-SCHEDULER"),
        ("classification", packet["classification"] == "INTERNAL_STRUCTURAL_ONLY"),
        ("direction", packet["direction"] == "observed_to_native"),
        ("premise", "complete-complement" in theorem["premise"]),
        ("bound", theorem["projection_bound"] == "sin_M^2(u,E0)<=delta/(beta-rho+delta)"),
        ("delta", "sqrt" in theorem["delta"]),
        ("budget", theorem["target_budget"] == "eta^2<=p^2(beta-rho)^2/(1-p^2)^2"),
        ("complete projection", theorem["complete_ground_eigenspace_projection"] is True),
        ("no Ritz substitute", theorem["finite_Ritz_projection_substitutable"] is False),
        ("projection", exact["projection_square"] == "1/9"),
        ("budget equality", exact["M_dual_square_budget"] == "9/4" and exact["equality"] is True),
        ("no floor", native["native_complete_complement_floor_present"] is False),
        ("no tolerance", native["native_projection_tolerance_selected"] is False),
        ("no claim", native["native_projection_claim_emitted"] is False),
    ]


def main() -> int:
    packet = demo()
    base = controls(packet)
    mutations = [
        lambda d: d.__setitem__("classification", "PHYSICAL"),
        lambda d: d.__setitem__("direction", "native_to_observed"),
        lambda d: d["theorem"].__setitem__("premise", "finite control"),
        lambda d: d["theorem"].__setitem__("projection_bound", "sin=0"),
        lambda d: d["theorem"].__setitem__("delta", "0"),
        lambda d: d["theorem"].__setitem__("target_budget", "eta^2<=p^2"),
        lambda d: d["theorem"].__setitem__("complete_ground_eigenspace_projection", False),
        lambda d: d["theorem"].__setitem__("finite_Ritz_projection_substitutable", True),
        lambda d: d["exact_two_block_control"].__setitem__("projection_square", "0"),
        lambda d: d["exact_two_block_control"].__setitem__("equality", False),
        lambda d: d["native_status"].__setitem__("native_complete_complement_floor_present", True),
        lambda d: d["native_status"].__setitem__("native_projection_tolerance_selected", True),
        lambda d: d["native_status"].__setitem__("native_projection_claim_emitted", True),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(packet)
        mutate(candidate)
        rejected += not all(ok for _, ok in controls(candidate))
    invalid = 0
    for args in ((0, 0, 0), (0, 1, -1)):
        try:
            projection_sq_upper(*args)
        except ValueError:
            invalid += 1
    for p in (0, 1):
        try:
            projection_residual_budget(0, 1, p)
        except ValueError:
            invalid += 1
    print(f"K470 EXACT CONTROL: {sum(ok for _, ok in base)}/{len(base)} pass")
    print(f"K470 HOSTILE MUTATIONS: {rejected}/{len(mutations)} rejected")
    print(f"K470 INVALID INPUTS: {invalid}/4 rejected")
    return 0 if all(ok for _, ok in base) and rejected == len(mutations) and invalid == 4 else 1


if __name__ == "__main__":
    raise SystemExit(main())
