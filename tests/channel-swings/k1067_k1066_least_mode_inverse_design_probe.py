#!/usr/bin/env python3
"""Hostile mutations for K1067."""
from copy import deepcopy
from k1067_k1066_least_mode_inverse_design import build, validate


def main():
    mutations = [
        ("target_table.0.least_n", 4), ("target_table.1.least_lambda_four", 64),
        ("target_table.2.previous", 0.008), ("target_table.3.achieved", 0.008),
        ("target_table.4.least_n", 64), ("ceiling", 0.02),
        ("leading_deficit_constant", 1.0), ("asymptotic_deficit", "exponential"),
        ("feasibility_rule", "every target is feasible"), ("cost_warning", "higher modes are free"),
        ("scope", "measured apparatus"), ("target_claim", "CONFIRMED"),
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
    print(f"K1067 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
