#!/usr/bin/env python3
"""Hostile mutations for K1172."""
from copy import deepcopy
from k1172_sharp_repair_allocation_controls import build, validate


def main():
    mutations = [
        ("construction", None, "no coordinate construction"), ("allocation_count", None, 77),
        ("allocation_invariants", None, "unchecked"),
        ("constraint_heavy", "constraint_rank_on_kernel", 9),
        ("balanced", "gauge_rank", 4), ("balanced", "constraint_rank_on_kernel", 4),
        ("gauge_heavy", "gauge_rank", 9), ("sharpness", None, "only one split"),
        ("scope_boundary", None, "source construction"), ("target_claim", None, "SC-ACT-06-KILLED"),
        ("allocation_count", None, 76), ("sharpness", None, "not sharp"),
    ]
    caught = 0
    for a, b, v in mutations:
        d = deepcopy(build())
        if a in d["extreme_controls"]: d["extreme_controls"][a][b] = v
        else: d[a] = v
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    assert caught == 12
    print("K1172 hostile probes: 12/12")


if __name__ == "__main__": main()
