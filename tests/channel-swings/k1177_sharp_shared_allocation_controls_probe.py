#!/usr/bin/env python3
"""Hostile mutations for K1177."""
from copy import deepcopy
from k1177_sharp_shared_allocation_controls import build, validate


def main():
    mutations = [
        ("input", "K1175"), ("control_dimension", 8), ("allocation_count", 54),
        ("allocation_rule", "some triples"), ("extreme_controls", [[9, 0, 0]]),
        ("balanced_control", [4, 3, 3]), ("construction", "indefinite fitted model"),
        ("properties", []), ("decision", "constraint repair is preferred"),
        ("scope_boundary", "this is source-owned"), ("target_claim", "SC-ACT-06"),
    ]
    caught = 0
    for key, value in mutations:
        d = deepcopy(build()); d[key] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    assert caught == 11
    print("K1177 hostile probes: 11/11")


if __name__ == "__main__": main()
