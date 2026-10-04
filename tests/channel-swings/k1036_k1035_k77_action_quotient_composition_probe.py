#!/usr/bin/env python3
"""Hostile mutations for K1036."""
from copy import deepcopy
from k1036_k1035_k77_action_quotient_composition import build, validate


def main():
    mutations = [
        ("predecessors", []),
        ("finite_control.M_equals_P_star_P", [[1]]),
        ("finite_control.ambient_rank", 5),
        ("finite_control.gauge_rank", 1),
        ("functional_composition.ambient", "finite toy"),
        ("functional_composition.closed_range", "assumed"),
        ("functional_composition.positive_pairing", "indefinite"),
        ("functional_composition.action_basicness", "not basic"),
        ("ownership.repository_owned_candidate_action", False),
        ("ownership.source_selected_GU_action", True),
        ("source_ledger_effect", "LT-SM8 SAME"),
        ("target_claim", "CONFIRMED"),
    ]
    caught = 0
    for path, value in mutations:
        data = deepcopy(build())
        node = data
        parts = path.split(".")
        for part in parts[:-1]:
            node = node[part]
        node[parts[-1]] = value
        try:
            validate(data)
        except AssertionError:
            caught += 1
    assert caught == len(mutations)
    print(f"K1036 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__":
    main()
