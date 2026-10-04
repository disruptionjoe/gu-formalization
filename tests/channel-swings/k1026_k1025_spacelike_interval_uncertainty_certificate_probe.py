#!/usr/bin/env python3
"""Hostile mutations for K1026."""
from copy import deepcopy
from k1026_k1025_spacelike_interval_uncertainty_certificate import build, validate


def main():
    mutations = [
        ("metric_convention", "timelike when equal"),
        ("robust_condition", "L_nom>c|Delta t_nom|"),
        ("margin", "m=L_nom-c|Delta t_nom|"),
        ("sharpness", "not sharp"),
        ("controls.0.margin", 7.8),
        ("controls.0.certified", False),
        ("controls.1.margin", 0.1),
        ("controls.1.certified", True),
        ("controls.2.margin", 1.0),
        ("audit_boundary", "nonpositive proves influence"),
        ("ownership.measured_coordinates_supplied", True),
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
    print(f"K1026 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__":
    main()
