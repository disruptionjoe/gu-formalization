#!/usr/bin/env python3
"""Hostile mutations for K1041."""
from copy import deepcopy
from k1041_k1040_mass_scale_nonidentifiability import build, validate


def main():
    mutations = [
        ("mode_family", "omega=mass"),
        ("observable", "Q=mass"),
        ("scaling_theorem", "scale selects mass"),
        ("scaling_checks.0.after", "9/4"),
        ("degenerate_horns.0.Q", "2"),
        ("degenerate_horns.1.scale_squared", 1),
        ("degenerate_value", "2"),
        ("consequence", "mass one selected"),
        ("scope", "global GU no-go"),
        ("ownership.spatial_scale_owned_by_GU", True),
        ("ownership.scorable", True),
        ("target_claim", "FALSIFIED"),
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
    print(f"K1041 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__":
    main()
