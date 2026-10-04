#!/usr/bin/env python3
"""Hostile mutations for K1031."""
from copy import deepcopy
from k1031_k1030_positive_quotient_descent import build, validate


def main():
    mutations = [
        ("theorem.gauge_radical", "N arbitrary"),
        ("theorem.operator_descent_iff", "always"),
        ("theorem.self_adjointness", "A*=A"),
        ("theorem.effect_condition", "A>=0"),
        ("exact_control.M", [[1, 0], [0, -1]]),
        ("exact_control.kernel_basis", []),
        ("exact_control.quotient_effect_eigenvalues", [2, "1/2"]),
        ("exact_control.bad_representative_shift", "well-defined"),
        ("claim_ceiling", "GU quotient derived"),
        ("ownership.gu_quotient_selected", True),
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
    print(f"K1031 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__":
    main()
