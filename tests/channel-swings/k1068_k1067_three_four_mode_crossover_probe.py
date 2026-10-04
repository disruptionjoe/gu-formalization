#!/usr/bin/env python3
"""Hostile mutations for K1068."""
from copy import deepcopy
from k1068_k1067_three_four_mode_crossover import build, validate


def main():
    mutations = [
        ("three_mode_budget", "constant"), ("four_mode_assumption", "arbitrary transfer"),
        ("normalization_assumption", "unrelated units"),
        ("crossover_table.0.crossover_tau", 0.001), ("crossover_table.1.n", 9),
        ("crossover_table.2.crossover_tau", 0.02), ("crossover_table.3.crossover_tau", 0.02),
        ("asymptotic_crossover_tau", 0.02), ("decision_rule", "four modes always win"),
        ("non_dominance", "four modes are physically superior"), ("scope", "measured route score"),
        ("target_claim", "CONFIRMED"),
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
    print(f"K1068 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
