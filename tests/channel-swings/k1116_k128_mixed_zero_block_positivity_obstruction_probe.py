#!/usr/bin/env python3
"""Hostile mutations for K1116."""
from copy import deepcopy
from k1116_k128_mixed_zero_block_positivity_obstruction import build, validate


def main():
    mutations = [
        ("block_form", "H=diag(0,C)"),
        ("positivity_theorem", "A may be nonzero"),
        ("negative_theorem", "A may be nonzero"),
        ("mixed_sign_witness_rule", "quadratic term dominates"),
        ("fixture", {}), ("fixture_q_plus", "1/2"),
        ("fixture_q_minus", "7/20"), ("fixture_signs", ["positive"]),
        ("scope_boundary", "physical GU positivity"),
        ("target_claim", "FALSIFIED"),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1116 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
