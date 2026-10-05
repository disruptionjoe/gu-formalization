#!/usr/bin/env python3
"""Hostile mutations for K1124."""
from copy import deepcopy
from k1124_k590_acyclic_positivity_control import build, validate


def main():
    mutations = [
        ("control_input", "K128 I1B complex"),
        ("degree_dimensions", [21, 91, 70]),
        ("homology_dimensions", [0, 1, 0]), ("acyclic", False),
        ("positivity_on_zero_cohomology", "physical positivity"),
        ("supplies_nontrivial_physical_state_space", True),
        ("carrier_transfer_to_K128_K129", True),
        ("reason", "physical state supplied"),
        ("scope_boundary", "solves I1B"),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1124 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
