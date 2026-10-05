#!/usr/bin/env python3
"""Hostile mutations for K1086."""
from copy import deepcopy
from k1086_k1085_covariant_hessian_commutator import build, validate


def main():
    mutations = [
        ("operator", "bounded scalar"), ("identity", "[H0,C]=0"),
        ("zero_criterion", "positivity suffices"), ("proof_route", "by analogy"),
        ("positive_counterexample", "constant scalar"), ("witness", [0, 0]),
        ("witness_jet", "none"), ("decision_rule", "rejects the action"),
        ("scope_boundary", "source-selected GU theorem"), ("target_claim", "FALSIFIED"),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1086 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
