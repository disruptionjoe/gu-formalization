#!/usr/bin/env python3
"""Hostile mutations for K1119."""
from copy import deepcopy
from k1119_k1118_definite_distortion_schur_sign import build, validate


def main():
    mutations = [
        ("congruence", "diag(A,C)"), ("positive_C_inertia", "positive"),
        ("negative_C_inertia", "negative"), ("fixture_A_diagonal", ["1"]),
        ("fixture_positive_C_schur_diagonal", ["4", "9/4"]),
        ("fixture_negative_C_schur_diagonal", ["-4", "-9/4"]),
        ("fixture_full_inertia_both_horns", {"positive": 4, "negative": 0, "zero": 0}),
        ("sign_boundary", "C>0 makes H positive"),
        ("scope_boundary", "global physical inverse"), ("target_claim", "CONFIRMED"),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1119 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
