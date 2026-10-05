#!/usr/bin/env python3
"""Hostile mutations for K1078."""
from copy import deepcopy
from k1078_k1077_matrix_branch_selector import build, validate


def main():
    mutations = [
        ("branch_law", "quadratic"), ("selector", "u_j=c_j"),
        ("controls.0.recovered_intercept", "7"), ("controls.1.mass_to_speed_ratio", "4"),
        ("field_normalization", "changes spectrum"), ("ruler_boundary", "no ruler needed"),
        ("degeneracy_boundary", "unique basis"), ("source_boundary", "source selected"),
        ("claim_ceiling", "functional theorem"), ("target_claim", "CONFIRMED"),
    ]
    caught = 0
    for path, value in mutations:
        data = deepcopy(build()); node = data; parts = path.split(".")
        for part in parts[:-1]: node = node[int(part)] if part.isdigit() else node[part]
        node[parts[-1]] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1078 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
