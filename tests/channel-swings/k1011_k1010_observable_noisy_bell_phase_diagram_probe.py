#!/usr/bin/env python3
"""Hostile mutations for K1011."""
from copy import deepcopy
from k1011_k1010_observable_noisy_bell_phase_diagram import build, validate


def main():
    mutations = [
        ("observable_domain", "0<=p<=V<=1"),
        ("entanglement_region", "p+V>1"),
        ("optimized_chsh_region", "p^2+2V^2>1"),
        ("separator.p", "3/5"),
        ("separator.lambda", "1/5"),
        ("separator.V", "2/5"),
        ("separator.entanglement_lhs", "24/25"),
        ("separator.chsh_lhs", "700/625"),
        ("ownership.gu_state_or_observable_constructed", True),
        ("ownership.prediction_or_confirmation", True),
        ("target_claim", "SC-ACT-06"),
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
        except (AssertionError, ValueError, ZeroDivisionError):
            caught += 1
    assert caught == len(mutations)
    print(f"K1011 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__":
    main()
