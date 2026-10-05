#!/usr/bin/env python3
"""Hostile mutations for K1079."""
from copy import deepcopy
from k1079_k1078_two_mode_commutator_witness import build, validate


def main():
    mutations = [
        ("identity", "zero"), ("recovery", "[X,Y]=0"), ("exact_control", False),
        ("counterexample", "commuting"), ("frequency_branches", "affine"),
        ("decision_rule", "rejects the action"), ("functional_boundary", "no domain needed"),
        ("source_boundary", "GU Hessian"), ("claim_ceiling", "all operators"),
        ("target_claim", "CONFIRMED"),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1079 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
