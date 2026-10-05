#!/usr/bin/env python3
"""Hostile mutations for K1083."""
from copy import deepcopy
from k1083_k1082_functional_branch_selector import build, validate


def main():
    mutations = [
        ("criterion", "positivity suffices"), ("branch_law", "omega is affine"),
        ("branches.0.values", [6, 9, 10]), ("branches.1.recovered_b", 4),
        ("branches.0.u", "6"), ("k1036_specialization", "u selected by GU"),
        ("selector_boundary", "no ruler needed"), ("degeneracy_boundary", "preferred basis"),
        ("source_boundary", "source-selected GU coefficient"), ("target_claim", "CONFIRMED"),
    ]
    caught = 0
    for path, value in mutations:
        data = deepcopy(build()); node = data; parts = path.split(".")
        for part in parts[:-1]: node = node[int(part)] if part.isdigit() else node[part]
        node[parts[-1]] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1083 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
