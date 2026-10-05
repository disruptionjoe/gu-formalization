#!/usr/bin/env python3
"""Hostile mutations for K1121."""
from copy import deepcopy
from k1121_k1118_radical_quotient_inertia_preservation import build, validate


def main():
    mutations = [
        ("theorem", "arbitrary quotient preserves inertia"),
        ("nonzero_inertia_preserved", False),
        ("gauge_only_can_remove_negative_directions", True),
        ("fixture_diagonal", [-3, 2, 5]),
        ("fixture_gauge_index", 0),
        ("fixture_inertia_before", [3, 0, 1]),
        ("fixture_inertia_after", [2, 0, 1]),
        ("scope_boundary", "global physical quotient"),
        ("target_claim", "FALSIFIED"),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1121 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
