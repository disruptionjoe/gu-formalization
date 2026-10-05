#!/usr/bin/env python3
"""Hostile mutations for K1114."""
from copy import deepcopy
from k1114_k1113_loewner_data_error_propagation import build, validate


def main():
    mutations = [
        ("sample_model", "no gap needed"), ("affine_model", "exact automatically"),
        ("ordinary_entry_bound", "eta"), ("ordinary_norm_bound", "eta"),
        ("shifted_entry_bound", "eta"), ("shifted_norm_bound", "eta"),
        ("fixture", {}), ("fixture_ordinary_entry_bound", "0"),
        ("fixture_ordinary_norm_bound", "0"), ("fixture_shifted_entry_bound", "0"),
        ("fixture_shifted_norm_bound", "0"), ("decision", "spacing irrelevant"),
        ("scope_boundary", "measured apparatus"), ("target_claim", "FALSIFIED"),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1114 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
