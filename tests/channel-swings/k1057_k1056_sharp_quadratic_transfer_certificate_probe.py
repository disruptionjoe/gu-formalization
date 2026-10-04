#!/usr/bin/env python3
"""Hostile mutations for K1057."""
from copy import deepcopy
from k1057_k1056_sharp_quadratic_transfer_certificate import build, validate


def main():
    mutations = [
        ("model", "affine"), ("horn_ratio", "constant"), ("monotonicity", "decreasing"),
        ("separation", "overlap"), ("threshold_equation", "numerical fit"),
        ("threshold", "0.2"), ("threshold_percent_in_inverse_normalized_frequency", "20"),
        ("touching_residual", "1"), ("safe_fixture.gap", "-1"),
        ("scope", "universal detector"), ("reopener", "none"), ("target_claim", "CONFIRMED"),
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
    print(f"K1057 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
