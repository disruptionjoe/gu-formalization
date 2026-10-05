#!/usr/bin/env python3
"""Hostile mutations for K1140."""
from copy import deepcopy
from k1140_i1b_constraint_admission_compiler import build, validate


def main():
    mutations = [
        ("inputs", []),
        ("admission_gates", []),
        ("current_candidates_meeting_all_gates", 1),
        ("rank_floor_retyped", "sufficient"),
        ("exceptional_shell_retyped", "physical_constraint"),
        ("current_source_and_ledger_effect", "confirmed"),
        ("protected_disposition", "SC-ACT-06 killed"),
        ("next_condition", "reuse inverse graph"),
        ("scope_boundary", "GU falsified"),
        ("scorable_rows_added", 1),
        ("target_claim", "SC-ACT-06-KILLED"),
    ]
    caught = 0
    for key, value in mutations:
        d = deepcopy(build()); d[key] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    assert caught == len(mutations)
    print(f"K1140 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
