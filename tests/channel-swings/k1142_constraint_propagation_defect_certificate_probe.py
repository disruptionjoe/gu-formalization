#!/usr/bin/env python3
"""Hostile mutations for K1142."""
from copy import deepcopy
from k1142_constraint_propagation_defect_certificate import build, validate


def main():
    mutations = [
        ("theorem", "small leakage is exact propagation"),
        ("basis_invariance", "rank depends on basis"),
        ("norm_is_coordinate_dependent", False),
        ("zero_and_rank_are_basis_independent", False),
        ("action_ownership_supplied", True),
        ("target_claim", "SC-ACT-06-PASS"),
    ]
    caught = 0
    for key, value in mutations:
        d = deepcopy(build()); d[key] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    for key, value in [("E_pass", [[0, 1, 0]]), ("E_fail", [[0, 0, 0]]), ("fail_rank", 0), ("fail_frobenius_norm_squared", 0)]:
        d = deepcopy(build()); d["fixture"][key] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    assert caught == 10
    print("K1142 hostile probes: 10/10")


if __name__ == "__main__": main()
