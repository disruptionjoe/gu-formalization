#!/usr/bin/env python3
"""Hostile mutations for K1180."""
from copy import deepcopy
from k1180_i1b_native_candidate_admission_boundary import build, validate


def main():
    mutations = [
        ("inputs", []), ("uniform_shared_floor", 98372),
        ("strongest_single_optimistic_residual", {}), ("all_four_optimistic_residual", {}),
        ("current_typed_k132_couplings", 1), ("current_measured_complement_stacks", 1),
        ("current_candidates_meeting_full_packet", 1), ("next_condition", "repeat a named map"),
        ("protected_disposition", "SC-ACT-06 rejected"), ("scope_boundary", "owned additive stack"),
        ("scorable_rows_added", 1), ("target_claim", "SC-ACT-01"),
    ]
    caught = 0
    for key, value in mutations:
        d = deepcopy(build()); d[key] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    assert caught == 12
    print("K1180 hostile probes: 12/12")


if __name__ == "__main__": main()
