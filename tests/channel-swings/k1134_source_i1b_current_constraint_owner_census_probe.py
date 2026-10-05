#!/usr/bin/env python3
"""Hostile mutations for K1134."""
from copy import deepcopy
from k1134_source_i1b_current_constraint_owner_census import build, validate


def main():
    mutations = [
        ("negative_floor", [4, 4, 4]),
        ("action_owned_t0_gauge", "distortion gauge rank 8191"),
        ("rows", []),
        ("counts", {"candidate_classes": 4, "meets_floor_on_common_propagated_domain": 1}),
        ("conclusion", "constraint problem solved"),
        ("scope_boundary", "GU falsified"),
        ("target_claim", "SC-ACT-01-KILLED"),
    ]
    caught = 0
    for key, value in mutations:
        d = deepcopy(build()); d[key] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    for i in range(4):
        d = deepcopy(build()); d["rows"][i]["meets_non_gauge_floor"] = True
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    assert caught == len(mutations) + 4
    print(f"K1134 hostile probes: {caught}/{len(mutations)+4}")


if __name__ == "__main__": main()
