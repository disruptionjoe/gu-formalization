#!/usr/bin/env python3
"""Hostile mutations for K1059."""
from copy import deepcopy
from k1059_k1058_four_mode_quadratic_identifiability import build, validate


def main():
    mutations = [
        ("modes.3", 25), ("mass_one_frequencies.0", 1), ("transfer_space", "affine"),
        ("determinant", "zero"), ("determinant_numeric", 0.0),
        ("nonzero_proof", "assumed"), ("intersection", "all readouts"),
        ("identification", "both fit"), ("degenerate_boundary", "none"),
        ("scale_boundary", "absolute mass"), ("scope", "universal"),
        ("reopener", "none"), ("target_claim", "CONFIRMED"),
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
    print(f"K1059 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
