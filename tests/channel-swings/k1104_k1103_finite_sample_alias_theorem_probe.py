#!/usr/bin/env python3
"""Hostile mutations for K1104."""
from copy import deepcopy
from k1104_k1103_finite_sample_alias_theorem import build, validate


def main():
    mutations = [
        ("construction", "numerical fit"), ("general_decision", "four samples identify all"),
        ("fixture_modes", [0,1,2]), ("fixture_rational_difference", "F=0"),
        ("fixture_residues", []), ("left_branch", {"weights":[]}),
        ("right_branch", {"weights":[]}), ("common_values", []),
        ("all_samples_equal", False), ("branches_distinct", False),
        ("boundary", "unconditional identification"), ("scope_boundary", "GU sector"),
        ("target_claim", "FALSIFIED"),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except (AssertionError, KeyError): caught += 1
    assert caught == len(mutations)
    print(f"K1104 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
