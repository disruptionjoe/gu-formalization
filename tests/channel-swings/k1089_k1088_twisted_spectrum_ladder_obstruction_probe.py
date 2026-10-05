#!/usr/bin/env python3
"""Hostile mutations for K1089."""
from copy import deepcopy
from k1089_k1088_twisted_spectrum_ladder_obstruction import build, validate


def main():
    mutations = [
        ("carrier", "one real scalar"), ("connections", "same connection"),
        ("holonomies", ["+1", "+1"]), ("kinetic_and_mass", "noncommuting"),
        ("branch_rule", "same ladder"), ("laplacian_fixtures", {}),
        ("spectral_obstruction", "none"), ("product_basis_obstruction", "tensor product exists"),
        ("decision_rule", "B,C suffice"), ("scope_boundary", "source GU spectrum"),
        ("target_claim", "FALSIFIED"),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except (AssertionError, KeyError): caught += 1
    assert caught == len(mutations)
    print(f"K1089 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
