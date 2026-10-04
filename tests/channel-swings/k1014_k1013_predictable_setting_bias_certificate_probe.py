#!/usr/bin/env python3
"""Hostile mutations for K1014."""
from copy import deepcopy
from k1014_k1013_predictable_setting_bias_certificate import build, validate


def main():
    mutations = [
        ("per_trial_local_ceiling", "b_i=3/4"),
        ("variable_bias_certificate", "sum_i(W_i-3/4)>0"),
        ("q_floor_certificate", "w_hat>q"),
        ("tightness", "the local ceiling is never attained"),
        ("example.q", 0.25),
        ("example.local_ceiling", 0.75),
        ("example.n_total", 4039),
        ("example.penalty_at_n", 1.0),
        ("unowned_assumptions", ["known law"]),
        ("ownership.gu_randomness_source_constructed", True),
        ("ownership.measurement_independence_proved", True),
        ("target_claim", "CONFIRMED"),
    ]
    caught = 0
    for path, value in mutations:
        data = deepcopy(build())
        node = data
        parts = path.split(".")
        for part in parts[:-1]:
            node = node[part]
        node[parts[-1]] = value
        try:
            validate(data)
        except AssertionError:
            caught += 1
    assert caught == len(mutations)
    print(f"K1014 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__":
    main()
