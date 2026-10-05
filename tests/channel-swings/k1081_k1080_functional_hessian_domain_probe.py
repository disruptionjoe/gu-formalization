#!/usr/bin/env python3
"""Hostile mutations for K1081."""
from copy import deepcopy
from k1081_k1080_functional_hessian_domain import build, validate


def main():
    mutations = [
        ("carrier", "R2"), ("form_domain", "L2"), ("operator_domain", "H1"),
        ("hessian", "variable coefficients"), ("fourier_rule", "unknown"),
        ("fibres.1.lambda", 2), ("fibres.3.eigenvalues", [0, 0]),
        ("domain_result", "formal only"), ("compactness", "continuous spectrum"),
        ("ownership", "source-selected GU Hessian"), ("claim_ceiling", "all manifolds"),
        ("target_claim", "CONFIRMED"),
    ]
    caught = 0
    for path, value in mutations:
        data = deepcopy(build()); node = data; parts = path.split(".")
        for part in parts[:-1]: node = node[int(part)] if part.isdigit() else node[part]
        node[parts[-1]] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1081 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
