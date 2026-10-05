#!/usr/bin/env python3
"""Hostile mutations for K1109."""
from copy import deepcopy
from k1109_k1108_noisy_loewner_gap_boundary import build, validate


def main():
    mutations = [
        ("perturbation_model", "unknown error"), ("weyl_bounds", []),
        ("robust_lower_bound_rule", "rank exact"), ("exact_order_rule", "automatic"),
        ("null_rule", "small means absent"), ("near_coalescent_family", "none"),
        ("determinant_formula", "constant"), ("fixture_t", ["1"]),
        ("fixture_determinants", ["0"]), ("stability_boundary", "uniform threshold"),
        ("decision", "exact implies stable"), ("scope_boundary", "measured apparatus"),
        ("target_claim", "FALSIFIED"),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1109 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
