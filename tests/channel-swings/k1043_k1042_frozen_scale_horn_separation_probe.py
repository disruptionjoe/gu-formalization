#!/usr/bin/env python3
"""Hostile mutations for K1043."""
from copy import deepcopy
from k1043_k1042_frozen_scale_horn_separation import build, validate


def main():
    mutations = [
        ("true_values.mass1", "8/5"),
        ("gap", "1"),
        ("midpoint_classifier.threshold", "2"),
        ("midpoint_classifier.above", "mass_squared_4"),
        ("sharp_additive_radius", "9/10"),
        ("strict_intervals.mass1.0", "1"),
        ("touching_intervals.mass1.0", "2"),
        ("theorem", "all radii separate"),
        ("scope", "unconditional empirical score"),
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
    print(f"K1043 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__":
    main()
