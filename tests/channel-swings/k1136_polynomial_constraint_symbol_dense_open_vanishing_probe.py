#!/usr/bin/env python3
"""Hostile mutations for K1136."""
from copy import deepcopy
from k1136_polynomial_constraint_symbol_dense_open_vanishing import build, validate


def main():
    mutations = [
        ("theorem", "a symbol can vanish on an open set and revive"),
        ("regularity_required", ["smooth"]),
        ("smooth_only_is_sufficient", True),
        ("shell_only_local_symbol_possible", True),
        ("distributional_or_nonlocal_shell_projector_excluded_by_theorem", True),
        ("scope_boundary", "all shell mechanisms excluded"),
        ("target_claim", "SC-ACT-06-KILLED"),
        ("status", "canon"),
    ]
    caught = 0
    for key, value in mutations:
        d = deepcopy(build()); d[key] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    d = deepcopy(build()); d["finite_degree_control"]["vandermonde_determinant"] = "0"
    try: validate(d)
    except (AssertionError, KeyError): caught += 1
    d = deepcopy(build()); d["finite_degree_control"]["zero_values_force_zero_coefficients"] = False
    try: validate(d)
    except (AssertionError, KeyError): caught += 1
    assert caught == len(mutations) + 2
    print(f"K1136 hostile probes: {caught}/{len(mutations)+2}")


if __name__ == "__main__": main()
