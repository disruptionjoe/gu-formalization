#!/usr/bin/env python3
"""Hostile mutations for K1097."""
from copy import deepcopy
from k1097_k1096_one_auxiliary_curvature import build, validate


def main():
    mutations = [
        ("branch_family", "affine"), ("domain", "all real"),
        ("first_derivative", "0"), ("second_derivative", "> 0"),
        ("fixture", {}), ("fixture_roots", ["-1"]),
        ("unique_domain_root", "-5/2"), ("sample_values", ["3","5","7"]),
        ("second_finite_difference", "0"), ("decision", "affine"),
        ("scope_boundary", "source-selected"), ("target_claim", "FALSIFIED"),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1097 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
