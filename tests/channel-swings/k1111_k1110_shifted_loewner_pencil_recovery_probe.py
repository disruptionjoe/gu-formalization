#!/usr/bin/env python3
"""Hostile mutations for K1111."""
from copy import deepcopy
from k1111_k1110_shifted_loewner_pencil_recovery import build, validate


def main():
    mutations = [
        ("ordinary_centering", "uncentered"), ("shifted_centering", "ordinary"),
        ("recovery_theorem", "unbounded order automatic"), ("left_modes", [0]),
        ("right_modes", [0, 1]), ("sample_values", []),
        ("residual_loewner", []), ("pole_matrix", []),
        ("pencil_polynomial", ["0"]), ("normalized_pencil_polynomial", ["1"]),
        ("recovered_shifts", [1, 2]), ("scope_boundary", "physical GU spectrum"),
        ("target_claim", "FALSIFIED"),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1111 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
