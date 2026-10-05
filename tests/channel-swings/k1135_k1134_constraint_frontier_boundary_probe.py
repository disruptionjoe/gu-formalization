#!/usr/bin/env python3
"""Hostile mutations for K1135."""
from copy import deepcopy
from k1135_k1134_constraint_frontier_boundary import build, validate


def main():
    mutations = [
        ("current_candidates_meeting_complete_gate", 1),
        ("requirements", []),
        ("reopeners", []),
        ("protected_disposition", "promoted"),
        ("scorable_rows_added", 1),
        ("next_condition", "ordinary gauge quotient"),
        ("scope_boundary", "GU confirmed"),
        ("target_claim", "GU-CONFIRMED"),
    ]
    caught = 0
    for key, value in mutations:
        d = deepcopy(build()); d[key] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    d = deepcopy(build()); d["requirements"][0]["state"] = "closed"
    try: validate(d)
    except (AssertionError, KeyError): caught += 1
    assert caught == len(mutations) + 1
    print(f"K1135 hostile probes: {caught}/{len(mutations)+1}")


if __name__ == "__main__": main()
