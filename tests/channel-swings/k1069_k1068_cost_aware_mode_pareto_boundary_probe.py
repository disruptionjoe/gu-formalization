#!/usr/bin/env python3
"""Hostile mutations for K1069."""
from copy import deepcopy
from k1069_k1068_cost_aware_mode_pareto_boundary import build, validate


def main():
    mutations = [
        ("premises.0", "E is sampled"), ("premises.1", "cost is free"),
        ("pareto_theorem", "largest mode is best"), ("target_examples.0.pareto_n", 4),
        ("target_examples.4.pareto_n", 64), ("withheld_inputs.0", "none"),
        ("route_boundary", "n=4 is physically preferred"), ("scope", "empirical cost result"),
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
    print(f"K1069 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
