#!/usr/bin/env python3
"""Hostile mutations for K1054."""
from copy import deepcopy
from k1054_k1053_sharp_component_readout_error_certificate import build, validate


def main():
    mutations = [
        ("readout_model", "exact"), ("offset_cancellation", "offset remains"),
        ("shared_middle_extrema.mass1_upper", "1"), ("shared_middle_extrema.mass4_lower", "1"),
        ("shared_middle_extrema.a4", "1"), ("shared_middle_extrema.b4", "1"),
        ("sharp_threshold", "eta<1"), ("sharp_threshold_decimal", "0.5"),
        ("touching_boundary", "never"), ("fixture.eta", "1/2"),
        ("fixture.mass1_upper", "2"), ("normalization_boundary", "calibrated detector"),
        ("target_claim", "CONFIRMED"),
    ]
    caught = 0
    for path, value in mutations:
        data = deepcopy(build()); node = data; parts = path.split(".")
        for part in parts[:-1]: node = node[part]
        node[parts[-1]] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1054 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
