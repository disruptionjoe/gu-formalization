#!/usr/bin/env python3
"""Hostile mutations for K1053."""
from copy import deepcopy
from k1053_k1052_sharp_relative_gap_resolution_certificate import build, validate


def main():
    mutations = [
        ("error_model", "exact"), ("interval_rule", "D unchanged"), ("mass4_D", "1"),
        ("separation_condition", "rho<1"), ("sharp_threshold", "rho<1"),
        ("sharp_threshold_decimal", "0.5"), ("touching_boundary", "never"),
        ("fixture.rho", "1/2"), ("fixture.mass1_upper", "2"),
        ("systematics_boundary", "measured detector"), ("target_claim", "CONFIRMED"),
    ]
    caught = 0
    for path, value in mutations:
        data = deepcopy(build()); node = data; parts = path.split(".")
        for part in parts[:-1]: node = node[part]
        node[parts[-1]] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1053 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
