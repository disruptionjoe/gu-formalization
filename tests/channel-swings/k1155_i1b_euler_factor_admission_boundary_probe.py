#!/usr/bin/env python3
"""Hostile mutations for K1155."""
from copy import deepcopy
from k1155_i1b_euler_factor_admission_boundary import build, validate


def main():
    mutations = [
        ("inputs", []),
        ("source_owned_class_tested", "one projector"),
        ("source_owned_class_passes", True),
        ("failure_gate", "none"),
        ("causal_radical_capture_floors", {"timelike": 6, "spacelike": 6, "null": 4}),
        ("current_candidates_meeting_full_packet", 1),
        ("admission_update", "reuse Euler rows"),
        ("protected_disposition", "SC-ACT-06 killed"),
        ("next_condition", "reuse current candidate"),
        ("scope_boundary", "global physical theorem"),
        ("scorable_rows_added", 1),
        ("target_claim", "SC-ACT-06-KILL"),
    ]
    caught = 0
    for key, value in mutations:
        d = deepcopy(build()); d[key] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    assert caught == 12
    print("K1155 hostile probes: 12/12")


if __name__ == "__main__": main()
