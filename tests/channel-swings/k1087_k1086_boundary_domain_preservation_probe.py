#!/usr/bin/env python3
"""Hostile mutations for K1087."""
from copy import deepcopy
from k1087_k1086_boundary_domain_preservation import build, validate


def main():
    mutations = [
        ("dirichlet", "requires C=0"), ("neumann", "automatic"),
        ("robin", "automatic"), ("identity", "no boundary term"),
        ("parallel_reduction", "all domains automatic"),
        ("positive_robin_counterexample", "commuting scalars"), ("witness", [0, 0]),
        ("witness_vector", "none"), ("decision_rule", "bulk is enough"),
        ("scope_boundary", "physical GU boundary"), ("target_claim", "FALSIFIED"),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1087 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
