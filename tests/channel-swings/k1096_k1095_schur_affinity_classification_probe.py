#!/usr/bin/env python3
"""Hostile mutations for K1096."""
from copy import deepcopy
from k1096_k1095_schur_affinity_classification import build, validate


def main():
    mutations = [
        ("pencil", "constant"), ("effective_branch", "S=A"),
        ("nonconstant_auxiliary", {"affine_iff": "always"}),
        ("constant_auxiliary", {"affine_iff": "b0=0"}),
        ("positive_repair_fixture", {"condition_value": "1"}),
        ("k1094_failure_fixture", {"condition_value": "0"}),
        ("constant_block_fixture", {"effective_branch": "3+2*lambda"}),
        ("scope_boundary", "GU branch theorem"), ("target_claim", "FALSIFIED"),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except (AssertionError, KeyError): caught += 1
    assert caught == len(mutations)
    print(f"K1096 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
