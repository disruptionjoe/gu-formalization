#!/usr/bin/env python3
"""Hostile mutations for K1154."""
from copy import deepcopy
from k1154_source_i1b_constraint_repair_trilemma import build, validate


def main():
    mutations = [
        ("rejected_class", "all constraints"),
        ("branches", []),
        ("branches_currently_supplied", 1),
        ("prior_negative_capture_floor_retained", {}),
        ("stronger_radical_capture_floor", {"null": 4}),
        ("functional_gates_retained", []),
        ("claim_ceiling", "SC-ACT-06 refuted"),
        ("target_claim", "SC-ACT-06-KILL"),
    ]
    caught = 0
    for key, value in mutations:
        d = deepcopy(build()); d[key] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    assert caught == 8
    print("K1154 hostile probes: 8/8")


if __name__ == "__main__": main()
