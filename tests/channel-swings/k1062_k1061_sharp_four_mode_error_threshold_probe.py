#!/usr/bin/env python3
"""Hostile mutations for K1062."""
from copy import deepcopy
from k1062_k1061_sharp_four_mode_error_threshold import build, validate


def main():
    mutations = [
        ("limiting_contrast", 0.1), ("sharp_symmetric_eta_over_gamma", 0.02),
        ("model", "unbounded error"), ("decision_rule", "guess"),
        ("sharpness", "nonsharp"), ("scale_boundary", "absolute mass accuracy"),
        ("scope", "all transfers and modes"), ("target_claim", "CONFIRMED"),
    ]
    caught = 0
    for path, value in mutations:
        data = deepcopy(build()); data[path] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1062 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
