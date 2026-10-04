#!/usr/bin/env python3
"""Hostile mutations for K1033."""
from copy import deepcopy
from k1033_k1032_quotient_local_nosignalling import build, validate


def main():
    mutations = [
        ("theorem.state", "rho arbitrary"),
        ("theorem.local_effects", "effects arbitrary"),
        ("theorem.joint_rule", "p assigned"),
        ("theorem.conclusions", []),
        ("exact_bell_control.joint", [["1", "0"], ["0", "1"]]),
        ("exact_bell_control.alice_marginal", ["1", "0"]),
        ("exact_bell_control.bob_marginal", ["1", "0"]),
        ("exact_bell_control.total", "2"),
        ("failure_controls", []),
        ("claim_ceiling", "GU no-signalling derived"),
        ("ownership.gu_state_selected", True),
        ("ownership.gu_locality_derived", True),
        ("target_claim", "CONFIRMED"),
    ]
    caught = 0
    for path, value in mutations:
        data = deepcopy(build())
        node = data
        parts = path.split(".")
        for part in parts[:-1]:
            node = node[part]
        node[parts[-1]] = value
        try:
            validate(data)
        except AssertionError:
            caught += 1
    assert caught == len(mutations)
    print(f"K1033 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__":
    main()
