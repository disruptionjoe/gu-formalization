#!/usr/bin/env python3
"""Hostile mutations for K1030."""
from copy import deepcopy
from k1030_k1029_composed_causal_loophole_budget import build, validate


def main():
    mutations = [
        ("certificate", "w_hat>3/4+epsilon+q+R/n"),
        ("forecast_model", "K1018 only"),
        ("frozen_point.n_total", 36042),
        ("frozen_point.locality_penalty", 0.001),
        ("frozen_point.penalty_at_n", 0.0),
        ("frozen_point.penalty_at_n_minus_one", 0.0),
        ("frozen_point.compromise_rate", "0"),
        ("feasibility_condition", "always"),
        ("inference_boundary", "empirical locality proved"),
        ("remaining_unowned_packet", []),
        ("ownership.loophole_free_experiment_claimed", True),
        ("target_claim", "CONFIRMED"),
    ]
    caught = 0
    for path, value in mutations:
        data = deepcopy(build())
        node = data
        parts = path.split(".")
        for part in parts[:-1]:
            node = node[int(part)] if part.isdigit() else node[part]
        key = parts[-1]
        if key.isdigit(): node[int(key)] = value
        else: node[key] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1030 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
