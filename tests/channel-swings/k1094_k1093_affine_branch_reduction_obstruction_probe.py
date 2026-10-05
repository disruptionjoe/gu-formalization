#!/usr/bin/env python3
"""Hostile mutations for K1094."""
from copy import deepcopy
from k1094_k1093_affine_branch_reduction_obstruction import build, validate


def main():
    mutations = [
        ("pencil", "constant"), ("unreduced_eigenvalues", ["lambda+2"]),
        ("positive_domain", "all real"), ("effective_branch", "lambda+2"),
        ("sample_values", ["2","3","4"]), ("second_finite_difference", "0"),
        ("second_derivative", "0"), ("affine_repairs", []),
        ("scope_boundary", "GU branch theorem"), ("target_claim", "FALSIFIED"),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1094 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
