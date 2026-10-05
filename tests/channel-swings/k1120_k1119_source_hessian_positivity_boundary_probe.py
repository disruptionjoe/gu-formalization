#!/usr/bin/env python3
"""Hostile mutations for K1120."""
from copy import deepcopy
from k1120_k1119_source_hessian_positivity_boundary import build, validate


def main():
    mutations = [
        ("requirements", []),
        ("requirements", [{"state": "open"}] * 7),
        ("counts", {"global_physical_owned": 4}),
        ("protected_disposition", "SC-ACT-01 confirmed"),
        ("protected_disposition", "SC-META-53 certain"),
        ("next_condition", "more conditional inverse work"),
        ("do_not_continue", "continue inverse refinement"),
        ("scope_boundary", "GU confirmed"), ("target_claim", "CONFIRMED"),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except (AssertionError, KeyError): caught += 1
    assert caught == len(mutations)
    print(f"K1120 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
