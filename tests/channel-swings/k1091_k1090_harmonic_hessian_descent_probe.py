#!/usr/bin/env python3
"""Hostile mutations for K1091."""
from copy import deepcopy
from k1091_k1090_harmonic_hessian_descent import build, validate


def main():
    mutations = [
        ("complex", "arbitrary maps"), ("harmonic_space", "ker d0"),
        ("hodge_splitting", "no splitting"), ("criterion", "positivity suffices"),
        ("proof", "by analogy"), ("fixture_d0", [0, 0, 0]),
        ("fixture_projector", [[1,0,0],[0,1,0],[0,0,1]]),
        ("good_commutator_rank", 1), ("scope_boundary", "GU physical theorem"),
        ("target_claim", "FALSIFIED"),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1091 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
