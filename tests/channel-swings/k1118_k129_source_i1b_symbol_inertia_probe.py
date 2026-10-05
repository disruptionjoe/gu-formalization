#!/usr/bin/env python3
"""Hostile mutations for K1118."""
from copy import deepcopy
from k1118_k129_source_i1b_symbol_inertia import build, validate


def main():
    mutations = [
        ("source_block", "toy block"), ("source_rank_input", "ranks unknown"),
        ("strata", {}),
        ("strata", {"timelike": {}, "spacelike": {}, "null": {}}),
        ("ordinary_quotient_result", "quotient makes H positive"),
        ("strongest_conclusion", "physical positivity proved"),
        ("scope_boundary", "global closed domain"), ("target_claim", "CONFIRMED"),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except (AssertionError, KeyError): caught += 1
    assert caught == len(mutations)
    print(f"K1118 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
