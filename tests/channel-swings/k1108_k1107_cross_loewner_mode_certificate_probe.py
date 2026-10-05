#!/usr/bin/env python3
"""Hostile mutations for K1108."""
from copy import deepcopy
from k1108_k1107_cross_loewner_mode_certificate import build, validate


def main():
    mutations = [
        ("cross_kernel", "ordinary covariance"), ("data_type", "requires derivatives"),
        ("rank_theorem", "always singular"), ("left_modes", [0, 1]),
        ("right_modes", [0, 1, 2]), ("fixture_matrix", []),
        ("fixture_determinant", "0"), ("fixture_rank", 2),
        ("fixture_conclusion", "exact unbounded order"), ("relation_to_k1103", "fewer samples"),
        ("scope_boundary", "physical score"), ("target_claim", "FALSIFIED"),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1108 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
