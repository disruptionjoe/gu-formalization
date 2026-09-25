#!/usr/bin/env python3
"""Independent controls and hostile mutations for K443."""

from __future__ import annotations

import copy
import json

from k443_k77_boundary_kt_coupling_obstruction import demo


def controls(result: dict) -> list[bool]:
    theorem = result["general_theorem"]
    counts = result["actual_rank_count"]
    exact = result["exact_controls"]
    decision = result["decision"]
    return [
        result["classification"] == "BRIDGE_OR_SEMANTIC_BOUNDARY",
        result["direction"] == "observed_to_native",
        theorem["criterion_necessary_and_sufficient"] is True,
        theorem["nilpotence_and_properness_separate_obligations"] is True,
        counts["corrected_carrier_rank"] == 512,
        counts["incoming_rank"] == 256,
        counts["outgoing_rank"] == 256,
        counts["all_endomorphisms_dimension"] == 262144,
        counts["boundary_compatible_endomorphisms_dimension"] == 131072,
        counts["off_diagonal_obstruction_space_dimension"] == 131072,
        exact["compatible_diagonal_commutator_rank"] == 0,
        exact["slow_swap_representative_commutator_rank"] == 2,
        exact["slow_swap_actual_commutator_rank"] == 128,
        exact["incoming_to_outgoing_leak_rank"] == 64,
        exact["outgoing_to_incoming_leak_rank"] == 64,
        exact["slow_swap_exchanges_equal_rank_blocks"] is True,
        decision["decoupled_k442_product_passes"] is True,
        decision["arbitrary_lower_order_coupling_passes"] is False,
        decision["slow_sector_exchange_rejected"] is True,
        decision["actual_action_coupling_tested"] is False,
        decision["full_bv_kt_properness_proved"] is False,
        decision["physical_cohomology_constructed"] is False,
    ]


def valid(result: dict) -> bool:
    return all(controls(result))


def main() -> int:
    result = demo()
    assert valid(result)
    specs = [
        (("classification",), "SUPPORTED"),
        (("direction",), "native_to_observed"),
        (("general_theorem", "criterion_necessary_and_sufficient"), False),
        (("general_theorem", "nilpotence_and_properness_separate_obligations"), False),
        (("actual_rank_count", "corrected_carrier_rank"), 640),
        (("actual_rank_count", "incoming_rank"), 192),
        (("actual_rank_count", "outgoing_rank"), 320),
        (("actual_rank_count", "all_endomorphisms_dimension"), 512),
        (("actual_rank_count", "boundary_compatible_endomorphisms_dimension"), 262144),
        (("actual_rank_count", "off_diagonal_obstruction_space_dimension"), 0),
        (("exact_controls", "compatible_diagonal_commutator_rank"), 1),
        (("exact_controls", "slow_swap_representative_commutator_rank"), 0),
        (("exact_controls", "slow_swap_actual_commutator_rank"), 64),
        (("exact_controls", "incoming_to_outgoing_leak_rank"), 0),
        (("exact_controls", "outgoing_to_incoming_leak_rank"), 0),
        (("exact_controls", "slow_swap_exchanges_equal_rank_blocks"), False),
        (("decision", "decoupled_k442_product_passes"), False),
        (("decision", "arbitrary_lower_order_coupling_passes"), True),
        (("decision", "slow_sector_exchange_rejected"), False),
        (("decision", "actual_action_coupling_tested"), True),
        (("decision", "full_bv_kt_properness_proved"), True),
        (("decision", "physical_cohomology_constructed"), True),
    ]
    mutations = []
    for path, value in specs:
        candidate = copy.deepcopy(result)
        target = candidate
        for key in path[:-1]:
            target = target[key]
        target[path[-1]] = value
        mutations.append(candidate)
    rejected = sum(not valid(candidate) for candidate in mutations)
    assert rejected == len(mutations)
    print(json.dumps({"controls_passed": len(controls(result)), "hostile_mutations_rejected": rejected}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
