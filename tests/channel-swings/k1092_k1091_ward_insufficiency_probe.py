#!/usr/bin/env python3
"""Hostile mutations for K1092."""
from copy import deepcopy
from k1092_k1091_ward_insufficiency import build, validate


def main():
    mutations = [
        ("hessian", [[0,0,0],[0,2,0],[0,0,2]]), ("eigenvalues", [0,2,2]),
        ("positive_semidefinite", False), ("ward_vector", [1,0,0]),
        ("harmonic_image", [0,2,0]), ("constraint_spill", 0),
        ("commutator_rank", 0), ("decision", "Ward implies descent"),
        ("scope_boundary", "source-owned physical spectrum"), ("target_claim", "FALSIFIED"),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1092 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
