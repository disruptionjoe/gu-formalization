#!/usr/bin/env python3
"""Hostile mutations for K1132."""
from copy import deepcopy
from k1132_nonzero_kappa_elimination_not_constraint import build, validate


def main():
    mutations = [
        ("inputs", []), ("rows", []), ("negative_floor", [4, 4, 4]),
        ("conclusion", "nonzero kappa provides six constraints"),
        ("scope_boundary", "all GU completions excluded"),
        ("target_claim", "SC-ACT-01-KILLED"),
    ]
    caught = 0
    for key, value in mutations:
        d = deepcopy(build()); d[key] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    for i, value in [(0, 1), (1, 6), (2, 4)]:
        d = deepcopy(build()); d["rows"][i]["constraint_rank"] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    assert caught == len(mutations) + 3
    print(f"K1132 hostile probes: {caught}/{len(mutations)+3}")


if __name__ == "__main__": main()
