#!/usr/bin/env python3
"""Hostile mutations for K1012."""
from copy import deepcopy
from k1012_k1011_calibration_rectangle_certificates import build, validate


def main():
    mutations = [
        ("rules.entanglement_certify", "pU+2VU>1"),
        ("rules.entanglement_exclude", "pL+2VL<=1"),
        ("rules.chsh_certify", "pU^2+VU^2>1"),
        ("rules.chsh_exclude", "pL^2+VL^2<=1"),
        ("separator_rectangle.entanglement_certified", False),
        ("separator_rectangle.chsh_excluded", False),
        ("separator_rectangle.chsh_certified", True),
        ("violator_rectangle.entanglement_certified", False),
        ("violator_rectangle.chsh_certified", False),
        ("nondecision", "failure disproves the claim"),
        ("ownership.gu_calibration_constructed", True),
        ("ownership.empirical_score", True),
        ("target_claim", "CONFIRMED"),
    ]
    caught = 0
    for path, value in mutations:
        data = deepcopy(build())
        node = data
        parts = path.split(".")
        for part in parts[:-1]:
            node = node[part]
        node[parts[-1]] = value
        try:
            validate(data)
        except AssertionError:
            caught += 1
    assert caught == len(mutations)
    print(f"K1012 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__":
    main()
