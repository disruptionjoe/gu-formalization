#!/usr/bin/env python3
"""Hostile mutations for K1061."""
from copy import deepcopy
from k1061_k1060_four_mode_residual_witness import build, validate


def main():
    mutations = [
        ("modes.3", 25), ("mass_one_exact_witness.0", "1/8"),
        ("mass_one_witness_l1.0", 0.0), ("mass_four_witness_l1.1", 0.0),
        ("directed_cross_contrast.true_mu_1_against_mu_4", 0.0),
        ("directed_cross_contrast.true_mu_4_against_mu_1", 0.0),
        ("annihilation_rule", "fits approximately"), ("linf_feasibility", "unknown"),
        ("scope", "universal detector theorem"), ("target_claim", "CONFIRMED"),
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
    print(f"K1061 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
