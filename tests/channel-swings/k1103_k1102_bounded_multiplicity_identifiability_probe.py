#!/usr/bin/env python3
"""Hostile mutations for K1103."""
from copy import deepcopy
from k1103_k1102_bounded_multiplicity_identifiability import build, validate


def main():
    mutations = [
        ("theorem", "m modes suffice"), ("degree_argument", "degree 2m+2"),
        ("parameter_recovery", "ordered labels fixed"), ("cases", []),
        ("one_pole_consistency", "three modes"), ("boundary", "necessary and noise stable"),
        ("scope_boundary", "source owned"), ("target_claim", "CONFIRMED"),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1103 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
