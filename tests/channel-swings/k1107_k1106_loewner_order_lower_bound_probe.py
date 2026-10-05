#!/usr/bin/env python3
"""Hostile mutations for K1107."""
from copy import deepcopy
from k1107_k1106_loewner_order_lower_bound import build, validate


def main():
    mutations = [
        ("data_type", "values only"), ("rank_identity", "rank=m"),
        ("lower_bound_rule", "exact order"), ("upper_bound_composition", "automatic"),
        ("fixture_nodes", [0, 1]), ("fixture_positive_minor", "0"),
        ("fixture_conclusion", "one pole matches"), ("finite_value_boundary", "K1104 is false"),
        ("decision", "upper bound"), ("scope_boundary", "measured GU sector"),
        ("target_claim", "FALSIFIED"),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1107 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
