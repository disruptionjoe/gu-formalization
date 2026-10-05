#!/usr/bin/env python3
"""Hostile mutations for K1084."""
from copy import deepcopy
from k1084_k1083_variable_mass_commutator_obstruction import build, validate


def main():
    mutations = [
        ("operators", "bounded matrices"), ("identity", "[H0,V]=0"),
        ("zero_criterion", "positivity is enough"), ("proof_route", "by inspection"),
        ("positive_counterexample", "constant scalar"), ("witness", "0"),
        ("witness_point", "none"), ("decision_rule", "rejects the action"),
        ("scope_boundary", "all curved manifolds"), ("target_claim", "FALSIFIED"),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1084 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
