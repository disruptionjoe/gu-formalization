#!/usr/bin/env python3
"""Hostile mutations for K1106."""
from copy import deepcopy
from k1106_k1105_symmetric_loewner_factorization import build, validate


def main():
    mutations = [
        ("kernel", "ordinary covariance"), ("factorization", "indefinite"),
        ("theorem", "always full rank"), ("fixture_nodes", [0, 1]),
        ("fixture_matrix", []), ("leading_principal_minors", ["0"]),
        ("fixture_rank", 2), ("fixture_determinant", "0"),
        ("decision", "identifies GU"), ("scope_boundary", "physical apparatus"),
        ("target_claim", "FALSIFIED"),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1106 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
