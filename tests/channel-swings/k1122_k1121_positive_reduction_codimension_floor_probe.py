#!/usr/bin/env python3
"""Hostile mutations for K1122."""
from copy import deepcopy
from k1122_k1121_positive_reduction_codimension_floor import build, validate


def main():
    mutations = [
        ("theorem", "codim(W)>=0"), ("sharp", False),
        ("radical_quotient_is_separate_step", False),
        ("fixture_diagonal", [-4, 0, 2, 3, 5]),
        ("fixture_inertia", [4, 1, 1]),
        ("fixture_nonnegative_indices", [3, 4, 5]),
        ("fixture_codimension", 1),
        ("constraint_interpretation", "gauge quotient is sufficient"),
        ("scope_boundary", "constraints constructed"),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1122 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
