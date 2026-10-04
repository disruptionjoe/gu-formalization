#!/usr/bin/env python3
"""Hostile mutations for K1013."""
from copy import deepcopy
from k1013_k1012_memory_robust_chsh_game_certificate import build, validate


def main():
    mutations = [
        ("uniform_game.score_relation", "w=1/2+S/4"),
        ("local_conditional_ceiling", "E[W_i|F_(i-1)]<=1/2"),
        ("tail_bound", "P<=exp(-n*t^2/2)"),
        ("certificate", "w_hat>3/4+sqrt(log(1/alpha)/n)"),
        ("exact_point.n_total", 4038),
        ("exact_point.penalty_at_n", 1.0),
        ("exact_point.penalty_at_n_minus_one", 0.0),
        ("memory_scope", "iid devices required"),
        ("unowned_assumptions", ["measurement independence"]),
        ("ownership.gu_protocol_constructed", True),
        ("ownership.loophole_free_experiment_claimed", True),
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
    print(f"K1013 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__":
    main()
