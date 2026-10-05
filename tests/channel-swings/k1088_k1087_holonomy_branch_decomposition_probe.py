#!/usr/bin/env python3
"""Hostile mutations for K1088."""
from copy import deepcopy
from k1088_k1087_holonomy_branch_decomposition import build, validate


def main():
    mutations = [
        ("hypotheses", "positive matrices"), ("decomposition", "coordinate axes"),
        ("branch_rule", "omega is arbitrary"), ("holonomy_rule", "holonomy irrelevant"),
        ("common_ladder_condition", "automatic"), ("tensor_product_sufficient_case", "none"),
        ("fixture", []), ("decision_rule", "universal Fourier ladder"),
        ("scope_boundary", "source-selected physical modes"), ("target_claim", "CONFIRMED"),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except (AssertionError, IndexError): caught += 1
    assert caught == len(mutations)
    print(f"K1088 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
