#!/usr/bin/env python3
"""Hostile mutations for K1052."""
from copy import deepcopy
from k1052_k1051_affine_spectrum_shape_identifiability import build, validate


def main():
    mutations = [
        ("parameter", "mu=m"), ("statistic", "Q"), ("rationalized", "none"),
        ("log_derivative", "0"), ("theorem", "not injective"), ("range", "unbounded"),
        ("frozen_modes.0", 1), ("frozen_controls.D_at_mu_1", "2"),
        ("frozen_controls.D_at_mu_4", "1"), ("frozen_controls.D_at_mu_0", "2"),
        ("frozen_controls.large_mu_control", "1"), ("frozen_controls.upper_limit", "2"),
        ("identifiability_boundary", "absolute m"), ("target_claim", "CONFIRMED"),
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
    print(f"K1052 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
