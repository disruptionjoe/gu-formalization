#!/usr/bin/env python3
"""Hostile mutations for K1101."""
from copy import deepcopy
from k1101_k1100_higher_divided_difference_sign_law import build, validate


def main():
    mutations = [
        ("general_identity", "zero"), ("strict_sign_rule", "nonnegative"),
        ("fixture_modes", [0, 1]), ("fixture_values", []),
        ("fixture_witnesses", {"2": "7/30"}), ("orders_checked", [2]),
        ("decision", "identifies all poles"), ("scope_boundary", "physical spectrum"),
        ("target_claim", "FALSIFIED"),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1101 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
