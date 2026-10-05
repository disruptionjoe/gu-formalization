#!/usr/bin/env python3
"""Hostile mutations for K1130."""
from copy import deepcopy
from k1130_k1129_corrected_action_boundary import build, validate


def main():
    mutations = [
        ("inputs", {}), ("exact_corrections", 0),
        ("first_order_principal_coefficient_status", "complete Hessian proved"),
        ("formal_projector_status", "action-owned physical projector"),
        ("action_owned_t0_gauge", "rank-16384 distortion gauge"),
        ("negative_sector_floor", [0, 0, 0]),
        ("action_owned_non_gauge_constraint_map_present", True),
        ("physical_quotient_present", True), ("scorable_rows_added", 1),
        ("retired_frontier", "current source-action gate"),
        ("next_condition", "score prediction"),
        ("protected_disposition", "promoted"),
        ("scope_boundary", "GU validated"),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1130 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
