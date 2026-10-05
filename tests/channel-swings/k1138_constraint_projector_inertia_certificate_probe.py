#!/usr/bin/env python3
"""Hostile mutations for K1138."""
from copy import deepcopy
from k1138_constraint_projector_inertia_certificate import build, validate


def main():
    mutations = [
        ("theorem", "rank Q is sufficient"),
        ("basis_invariance", "basis changes alter inertia"),
        ("radical_quotient_effect", "removes negative inertia"),
        ("rank_alone_decides_nonnegativity", True),
        ("action_ownership_supplied", True),
        ("scope_boundary", "physical quotient complete"),
        ("target_claim", "GU-CONFIRMED"),
        ("status", "canon"),
    ]
    caught = 0
    for key, value in mutations:
        d = deepcopy(build()); d[key] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    for key, value in [("P_idempotent", False), ("QP_zero", False), ("kernel_inertia", [1, 1, 0])]:
        d = deepcopy(build()); d["fixture"][key] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    assert caught == len(mutations) + 3
    print(f"K1138 hostile probes: {caught}/{len(mutations)+3}")


if __name__ == "__main__": main()
