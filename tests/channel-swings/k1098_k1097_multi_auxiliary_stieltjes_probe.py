#!/usr/bin/env python3
"""Hostile mutations for K1098."""
from copy import deepcopy
from k1098_k1097_multi_auxiliary_stieltjes import build, validate


def main():
    mutations = [
        ("operator_class", "arbitrary"), ("effective_branch", "affine"),
        ("domain", "all real"), ("first_derivative", "alpha"),
        ("second_derivative", "0"), ("strict_concavity_iff", "never"),
        ("affine_iff", "always"), ("stieltjes_correction", "oscillatory"),
        ("fixture", {}), ("sample_values", ["5","7","9"]),
        ("scope_boundary", "GU theorem"), ("target_claim", "FALSIFIED"),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1098 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
