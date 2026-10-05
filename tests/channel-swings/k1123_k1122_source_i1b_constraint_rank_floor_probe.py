#!/usr/bin/env python3
"""Hostile mutations for K1123."""
from copy import deepcopy
from k1123_k1122_source_i1b_constraint_rank_floor import build, validate


def main():
    mutations = [
        ("source_input", "conventional GR"), ("rows", []),
        ("ordinary_radical_quotient_sufficient", True),
        ("reason", "quotient removes negative directions"),
        ("uniform_minimum_over_nonzero_causal_types", 0),
        ("stronger_typewise_floors", [4, 4, 2]),
        ("scope_boundary", "global physical theorem"),
        ("protected_effect", "ledger promoted"),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except (AssertionError, KeyError): caught += 1
    assert caught == len(mutations)
    print(f"K1123 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
