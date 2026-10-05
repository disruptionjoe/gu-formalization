#!/usr/bin/env python3
"""Hostile mutations for K1162."""
from copy import deepcopy
from k1162_independent_symbol_family_control import build, validate


def main():
    mutations = [
        ("construction", None, "one derivative channel"),
        ("controls", None, []),
        ("row_rank", 0, 2),
        ("shared_rank", 1, 2),
        ("input_dimension", 2, 7),
        ("quotient_dimension", 3, 7),
        ("all_independent_stacks_gain_one_rank_per_symbol", None, False),
        ("all_shared_factor_stacks_remain_rank_one", None, False),
        ("decision", None, "derivatives suffice"),
        ("scope_boundary", None, "source owned"),
        ("target_claim", None, "SC-ACT-06-KILLED"),
    ]
    caught = 0
    for kind, index, value in mutations:
        d = deepcopy(build())
        if kind == "row_rank": d["controls"][index]["independent_stack_rank"] = value
        elif kind == "shared_rank": d["controls"][index]["shared_factor_descendant_rank"] = value
        elif kind == "input_dimension": d["controls"][index]["input_dimension"] = value
        elif kind == "quotient_dimension": d["controls"][index]["positive_quotient_dimension"] = value
        else: d[kind] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    assert caught == 11
    print("K1162 hostile probes: 11/11")


if __name__ == "__main__": main()
