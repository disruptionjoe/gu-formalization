#!/usr/bin/env python3
"""Hostile mutations for K1150."""
from copy import deepcopy
from k1150_i1b_functional_admission_compiler import build, validate


def main():
    caught = 0
    mutations = [
        ("current_candidates_meeting_functional_packet", 1),
        ("finite_algebraic_packet_executable", False),
        ("functional_gates_executable", False),
        ("source_action_map_supplied", True),
        ("common_closed_realization_supplied", True),
        ("current_source_and_ledger_effect", "positive"),
        ("protected_disposition", "SC-META-53 PROVED"),
        ("next_condition", "done"),
        ("scorable_rows_added", 1),
        ("target_claim", "SC-META-53"),
    ]
    for key, value in mutations:
        d = deepcopy(build()); d[key] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    assert caught == 10
    print("K1150 hostile probes: 10/10")


if __name__ == "__main__": main()
