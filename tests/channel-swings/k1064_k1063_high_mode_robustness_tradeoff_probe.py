#!/usr/bin/env python3
"""Hostile mutations for K1064."""
from copy import deepcopy
from k1064_k1063_high_mode_robustness_tradeoff import build, validate


def main():
    mutations = [
        ("fixed_modes.0", 4), ("prepared_fourth_mode_family", "all modes"),
        ("fixture_table.0.eta_over_gamma", 0.02), ("fixture_table.1.n", 7),
        ("asymptotic_symmetric_eta_over_gamma", 0.1), ("limit_proof", "numerical guess"),
        ("monotonicity_ceiling", "globally monotone"), ("apparatus_tradeoff", "owns detector and ruler"),
        ("scope", "universal spectrum theorem"), ("target_claim", "CONFIRMED"),
    ]
    caught = 0
    for path, value in mutations:
        data = deepcopy(build()); node = data; parts = path.split(".")
        for part in parts[:-1]: node = node[int(part)] if isinstance(node, list) else node[part]
        if isinstance(node, list): node[int(parts[-1])] = value
        else: node[parts[-1]] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1064 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
