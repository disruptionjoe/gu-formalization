#!/usr/bin/env python3
"""Hostile mutations for K1042."""
from copy import deepcopy
from k1042_k1041_two_mode_dispersion_holdout import build, validate


def main():
    mutations = [
        ("pre_registration.spatial_scale_squared", 4),
        ("pre_registration.mode_eigenvalues", [0, 1]),
        ("pre_registration.observable", "zero mode"),
        ("pre_registration.calibration_use", "fit on lambda 1 and 4"),
        ("horns.0.Q", "8/5"),
        ("horns.1.omega_squared", [2, 5]),
        ("ordering", "equal"),
        ("gap", "0"),
        ("midpoint", "2"),
        ("heldout_status", "scored"),
        ("credit_boundary", "GU confirmed"),
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
        except AssertionError:
            caught += 1
    assert caught == len(mutations)
    print(f"K1042 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__":
    main()
