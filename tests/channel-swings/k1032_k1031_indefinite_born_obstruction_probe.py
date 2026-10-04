#!/usr/bin/env python3
"""Hostile mutations for K1032."""
from copy import deepcopy
from k1032_k1031_indefinite_born_obstruction import build, validate


def main():
    mutations = [
        ("theorem", "indefinite is positive"),
        ("inertia_is_congruence_invariant", False),
        ("exact_control.J", [[1, 0], [0, 1]]),
        ("exact_control.positive_norm", -1),
        ("exact_control.negative_norm", 1),
        ("exact_control.full_space_radical_dimension", 1),
        ("repair_boundary", []),
        ("source_scope.SC-META-53", "ASSERTS positivity"),
        ("source_scope.SC-ACT-01", "DERIVES Born pairing"),
        ("claim_ceiling", "global GU no-go"),
        ("ownership.positive_sector_selected", True),
        ("target_claim", "REFUTED"),
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
    print(f"K1032 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__":
    main()
