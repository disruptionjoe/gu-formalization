#!/usr/bin/env python3
"""Hostile mutations for K1133."""
from copy import deepcopy
from k1133_zero_kappa_symbol_null_propagation_audit import build, validate


def main():
    mutations = [
        ("normal_kernel_dimension", 11),
        ("normal_tangential_common_kernel_dimension", 24),
        ("normal_null_directions_lost_tangentially", 0),
        ("generic_weyl_distortion_complex", True),
        ("flat_selected_euler_square_zero", True),
        ("flat_symbol_cohomology_defined", True),
        ("square_zero_rank_ceiling", 200000),
        ("propagating_constraint_complex_owned", True),
        ("conclusion", "physical constraints proved"),
        ("scope_boundary", "all completions excluded"),
        ("target_claim", "GU-FALSIFIED"),
    ]
    caught = 0
    for key, value in mutations:
        d = deepcopy(build()); d[key] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    assert caught == len(mutations)
    print(f"K1133 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
