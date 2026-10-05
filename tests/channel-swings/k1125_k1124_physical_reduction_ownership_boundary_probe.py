#!/usr/bin/env python3
"""Hostile mutations for K1125."""
from copy import deepcopy
from k1125_k1124_physical_reduction_ownership_boundary import build, validate


def main():
    mutations = [
        ("requirements", []), ("counts", {}),
        ("protected_disposition", "promoted"),
        ("next_condition", "ordinary gauge quotient"),
        ("alternate_source_advances", []),
        ("scope_boundary", "physical positivity proved"),
        ("target_claim", "GU-CONFIRMED"),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1125 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
