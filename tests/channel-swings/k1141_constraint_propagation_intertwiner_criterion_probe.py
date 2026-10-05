#!/usr/bin/env python3
"""Hostile mutations for K1141."""
from copy import deepcopy
from k1141_constraint_propagation_intertwiner_criterion import build, validate


def main():
    mutations = [
        ("theorem", "rank alone propagates"),
        ("induced_row_generator", "R is arbitrary"),
        ("action_ownership_supplied", True),
        ("scope_boundary", "physical complex complete"),
        ("target_claim", "GU-CONFIRMED"),
    ]
    caught = 0
    for key, value in mutations:
        d = deepcopy(build()); d[key] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    fixture_mutations = [
        ("R", [[3]]), ("QG_pass", [[2, 1, 0]]), ("propagates", False),
        ("failing_kernel_witness", [1, 0, 0]), ("failing_constraint_derivative", 0),
    ]
    for key, value in fixture_mutations:
        d = deepcopy(build()); d["fixture"][key] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    assert caught == 10
    print("K1141 hostile probes: 10/10")


if __name__ == "__main__": main()
