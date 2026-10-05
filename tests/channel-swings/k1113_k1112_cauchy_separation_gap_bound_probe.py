#!/usr/bin/env python3
"""Hostile mutations for K1113."""
from copy import deepcopy
from k1113_k1112_cauchy_separation_gap_bound import build, validate


def main():
    mutations = [
        ("cauchy_determinant", "det V=1"), ("residual_determinant", "det R=0"),
        ("general_floor", "uniform without gaps"), ("norm_ceiling", "unbounded"),
        ("singular_floor", "determinant equals singular value"), ("fixture_det_vx", "0"),
        ("fixture_det_vy", "0"), ("fixture_det_r", "0"),
        ("fixture_conservative_det_floor", "1"), ("fixture_norm_ceiling", "1"),
        ("fixture_conservative_singular_floor", "1"), ("decision", "uniform class gap"),
        ("scope_boundary", "measured GU floor"), ("target_claim", "FALSIFIED"),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1113 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
