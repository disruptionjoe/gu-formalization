#!/usr/bin/env python3
"""Hostile mutations for K1093."""
from copy import deepcopy
from k1093_k1092_schur_physical_hessian import build, validate


def main():
    mutations = [
        ("block_operator", "scalar"), ("auxiliary_solution", "y=0"),
        ("effective_hessian", "L_eff=A"), ("positivity_equivalence", "always positive"),
        ("fixture", {"A":2,"B":0,"D":2}), ("full_eigenvalues", [2,2]),
        ("effective_value", "2"), ("congruence", "none"),
        ("scope_boundary", "GU physical theorem"), ("target_claim", "FALSIFIED"),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except (AssertionError, ValueError, ZeroDivisionError): caught += 1
    assert caught == len(mutations)
    print(f"K1093 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
