#!/usr/bin/env python3
"""Hostile mutations for K1066."""
from copy import deepcopy
from k1066_k1064_global_fourth_mode_monotonicity import build, validate


def main():
    mutations = [
        ("family", "all spectra"), ("normalizer_identity", "numerical fit"),
        ("limiting_direction", "directions equal"), ("derivative_reduction", "sampled derivative"),
        ("shifted_square_variable", "u=t"), ("shifted_square_coefficients.0", -1.0),
        ("radical_bounds.sqrt57_upper", 7.0), ("first_threshold", 0.02),
        ("asymptotic_ceiling", 0.1), ("global_result", "fixtures only"),
        ("scope", "physical detector theorem"), ("target_claim", "CONFIRMED"),
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
    print(f"K1066 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
