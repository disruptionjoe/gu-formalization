#!/usr/bin/env python3
"""Hostile mutations for K1044."""
from copy import deepcopy
from k1044_k1043_frequency_resolution_certificate import build, validate


def main():
    mutations = [
        ("measurement_model", "exact detector"),
        ("ratio_inflation", "beta=1"),
        ("separation_condition", "beta<2"),
        ("sharp_epsilon.exact", "1/2"),
        ("sharp_epsilon.minimal_polynomial", "epsilon=0"),
        ("sharp_epsilon.decimal", "0.5"),
        ("theorem", "always disjoint"),
        ("safe_fixture.epsilon", "1/2"),
        ("safe_fixture.gap", "-1"),
        ("systematics_boundary", "detector certified"),
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
    print(f"K1044 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__":
    main()
