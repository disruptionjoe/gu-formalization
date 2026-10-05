#!/usr/bin/env python3
"""Hostile mutations for K1112."""
from copy import deepcopy
from k1112_k1111_positive_stieltjes_reconstruction_test import build, validate


def main():
    mutations = [
        ("reconstruction_rule", "guess residues"), ("membership_rule", "roots suffice"),
        ("rejection_rule", "falsifies GU"), ("cauchy_matrix", []),
        ("cauchy_determinant", "0"), ("correction_values", []),
        ("recovered_weights", ["-1", "4"]), ("fixture_membership", "fail"),
        ("scope_boundary", "premise free"), ("target_claim", "FALSIFIED"),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1112 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
