#!/usr/bin/env python3
"""Hostile mutations for K1145."""
from copy import deepcopy
from k1145_i1b_dynamical_cohomology_admission_compiler import build, validate


def main():
    mutations = [
        ("inputs", []), ("executable_tests", []),
        ("current_candidates_meeting_composed_packet", 1),
        ("algebraic_controls_pass", False),
        ("source_action_map_supplied", True),
        ("common_closed_domain_supplied", True),
        ("current_source_and_ledger_effect", "confirmed"),
        ("protected_disposition", "SC-ACT-06 killed"),
        ("next_condition", "reuse finite fixture"),
        ("scope_boundary", "GU physical quotient complete"),
        ("scorable_rows_added", 1),
    ]
    caught = 0
    for key, value in mutations:
        d = deepcopy(build()); d[key] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    assert caught == 11
    print("K1145 hostile probes: 11/11")


if __name__ == "__main__": main()
