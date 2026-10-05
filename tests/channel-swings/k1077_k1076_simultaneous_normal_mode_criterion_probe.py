#!/usr/bin/env python3
"""Hostile mutations for K1077."""
from copy import deepcopy
from k1077_k1076_simultaneous_normal_mode_criterion import build, validate


def main():
    mutations = [
        ("normalized_operators", "X=B"), ("criterion", "always exists"),
        ("reason", "dimension count"), ("commuting_control", False),
        ("noncommuting_control", False), ("scope_boundary", "all operators"),
        ("source_boundary", "source supplies it"), ("claim_ceiling", "global QFT theorem"),
        ("target_claim", "CONFIRMED"),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1077 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
