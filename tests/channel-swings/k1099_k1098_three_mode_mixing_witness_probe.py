#!/usr/bin/env python3
"""Hostile mutations for K1099."""
from copy import deepcopy
from k1099_k1098_three_mode_mixing_witness import build, validate


def main():
    mutations = [
        ("general_identity", "zero"), ("sign_rule", "positive"),
        ("fixture_modes", [0,1]), ("fixture_values", ["8/3","11/2","8"]),
        ("finite_second_difference", "0"), ("second_divided_difference", "-7/15"),
        ("single_auxiliary_alias", {}), ("decision", "identifies all auxiliaries"),
        ("zero_witness_boundary", "unconditional"),
        ("scope_boundary", "physical observation"), ("target_claim", "FALSIFIED"),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1099 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
