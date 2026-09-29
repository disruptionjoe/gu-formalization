#!/usr/bin/env sage-python
"""Independent controls and hostile mutations for K635."""

from __future__ import annotations

import copy

from k635_k77_full_commutant_source_stabilizer import build


def controls(p: dict) -> list[bool]:
    t = p["stabilizer_theorem"]
    o = p["ownership_reconciliation"]
    d = p["decision"]
    packets = p["cross_characteristic_packets"]
    return [
        p["classification"] == "BRIDGE_OR_SEMANTIC_BOUNDARY",
        p["direction"] == "observed_to_native",
        p["target_claim"] == "NONE-NOT-A-KILL",
        len(packets) == 2,
        all(x["slow_kernel_join_rank"] == 128 for x in packets),
        all(x["slow_kernel_intersection_rank"] == 0 for x in packets),
        all(x["induced_algebra_dimension"] == 8192 for x in packets),
        all(x["fixed_R_lift_dimension"] == 24576 for x in packets),
        all(x["full_stabilizer_dimension"] == 32768 for x in packets),
        all(x["nonscalar_involution_trace"] == 0 for x in packets),
        all(all(x["checks"].values()) for x in packets),
        t["fast_seed_blocks_are_injective"] is True,
        t["slow_seed_kernel_dimensions"] == [64, 64],
        t["slow_seed_kernels_are_complementary"] is True,
        t["induced_source_algebra_dimension"] == 8192,
        t["polynomial_induced_subalgebra_dimension"] == 1,
        t["fixed_R_lift_dimension"] == 24576,
        t["full_commutant_seed_stabilizer_dimension"] == 32768,
        t["explicit_nonscalar_involution_exists"] is True,
        t["every_induced_operator_is_selected_by_the_action"] is False,
        o["K621_fixed_domain_J0_to_X_obstruction_retracted"] is False,
        o["K633_polynomial_scalar_stabilizer_retracted"] is False,
        o["full_commutant_contains_nonscalar_seed_stabilizers"] is True,
        o["commutation_alone_selects_a_unique_nonscalar_operator"] is False,
        o["independently_action_owned_source_endomorphism_found"] is False,
        d["full_frozen_commutant_stabilizer_classified"] is True,
        d["algebraic_existence_releases_K596_K598"] is False,
        d["selected_source_action_rejected"] is False,
        p["source_and_ledger_effect"] == "none",
    ]


def mutations(payload: dict):
    specs = [
        (("classification",), "SOURCE_RESULT"),
        (("cross_characteristic_packets", 0, "slow_kernel_join_rank"), 64),
        (("cross_characteristic_packets", 0, "slow_kernel_intersection_rank"), 1),
        (("cross_characteristic_packets", 0, "induced_algebra_dimension"), 4096),
        (("cross_characteristic_packets", 0, "fixed_R_lift_dimension"), 0),
        (("cross_characteristic_packets", 0, "full_stabilizer_dimension"), 8192),
        (("stabilizer_theorem", "fast_seed_blocks_are_injective"), False),
        (("stabilizer_theorem", "slow_seed_kernel_dimensions"), [63, 65]),
        (("stabilizer_theorem", "slow_seed_kernels_are_complementary"), False),
        (("stabilizer_theorem", "induced_source_algebra_dimension"), 1),
        (("stabilizer_theorem", "polynomial_induced_subalgebra_dimension"), 2),
        (("stabilizer_theorem", "fixed_R_lift_dimension"), 1),
        (("stabilizer_theorem", "full_commutant_seed_stabilizer_dimension"), 8192),
        (("stabilizer_theorem", "explicit_nonscalar_involution_exists"), False),
        (("stabilizer_theorem", "every_induced_operator_is_selected_by_the_action"), True),
        (("ownership_reconciliation", "K621_fixed_domain_J0_to_X_obstruction_retracted"), True),
        (("ownership_reconciliation", "K633_polynomial_scalar_stabilizer_retracted"), True),
        (("ownership_reconciliation", "full_commutant_contains_nonscalar_seed_stabilizers"), False),
        (("ownership_reconciliation", "commutation_alone_selects_a_unique_nonscalar_operator"), True),
        (("ownership_reconciliation", "independently_action_owned_source_endomorphism_found"), True),
        (("decision", "full_frozen_commutant_stabilizer_classified"), False),
        (("decision", "algebraic_existence_releases_K596_K598"), True),
        (("decision", "selected_source_action_rejected"), True),
        (("source_and_ledger_effect",), "moved"),
    ]
    for path, value in specs:
        m = copy.deepcopy(payload)
        target = m
        for key in path[:-1]:
            target = target[key]
        target[path[-1]] = value
        yield m


def main() -> int:
    payload = build()
    base = controls(payload)
    assert len(base) == 29 and all(base)
    rejected = 0
    for mutant in mutations(payload):
        if not all(controls(mutant)):
            rejected += 1
    assert rejected == 24
    print("K635 independent controls: 29/29 passed")
    print("K635 hostile mutations: 24/24 rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
