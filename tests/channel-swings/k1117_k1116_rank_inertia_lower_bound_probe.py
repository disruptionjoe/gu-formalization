#!/usr/bin/env python3
"""Hostile mutations for K1117."""
from copy import deepcopy
from k1117_k1116_rank_inertia_lower_bound import build, validate


def main():
    mutations = [
        ("theorem", "n_plus(H)>=0"), ("proof_route", "trace estimate"),
        ("sharp_fixture", {}), ("sharp_fixture_inertia", {"positive": 4}),
        ("nonzero_C_fixture", {"block_determinants": [4, 9]}),
        ("nonzero_C_fixture_inertia", {"positive": 4, "negative": 0, "zero": 0}),
        ("sharpness", "strict for every C"), ("scope_boundary", "physical Hilbert spectrum"),
        ("target_claim", "CONFIRMED"),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except (AssertionError, KeyError): caught += 1
    assert caught == len(mutations)
    print(f"K1117 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
