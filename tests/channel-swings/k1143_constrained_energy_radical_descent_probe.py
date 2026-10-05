#!/usr/bin/env python3
"""Hostile mutations for K1143."""
from copy import deepcopy
from k1143_constrained_energy_radical_descent import build, validate


def main():
    mutations = [
        ("theorem", "nonnegative rank is enough"),
        ("functional_domain_supplied", True),
        ("source_action_constraint_supplied", True),
        ("target_claim", "GU-PHYSICAL-QUOTIENT"),
    ]
    caught = 0
    for key, value in mutations:
        d = deepcopy(build()); d[key] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    fixture_mutations = [
        ("QG_on_kernel_zero", False), ("H_skew_defect", [[1]]),
        ("restricted_inertia", [1, 1, 1]), ("radical_basis", []),
        ("radical_invariant", False), ("quotient_gram", [[2, 0], [0, -2]]),
        ("quotient_positive_definite", False),
    ]
    for key, value in fixture_mutations:
        d = deepcopy(build()); d["fixture"][key] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    assert caught == 11
    print("K1143 hostile probes: 11/11")


if __name__ == "__main__": main()
