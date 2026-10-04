#!/usr/bin/env python3
"""Hostile mutations for K1037."""
from copy import deepcopy
from k1037_k1036_stationary_wave_generator import build, validate


def main():
    mutations = [
        ("background", "nonstationary"),
        ("phase_space", "configuration only"),
        ("mode_rule", "omega_squared=mass_squared only"),
        ("horns.0.mass_squared", 2),
        ("horns.0.defect", [[1]]),
        ("horns.0.energy_derivative", 1),
        ("horns.0.M", [[1]]),
        ("horns.1.K", [[1]]),
        ("theorem.radical", "not invariant"),
        ("theorem.compatibility", "K^T M-M K=0"),
        ("theorem.consequence", "ambient probability"),
        ("analytic_scope", "full nonlinear BV"),
        ("ownership.source_GU_generator_owned", True),
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
        if key.isdigit():
            node[int(key)] = value
        else:
            node[key] = value
        try:
            validate(data)
        except (AssertionError, IndexError):
            caught += 1
    assert caught == len(mutations)
    print(f"K1037 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__":
    main()
