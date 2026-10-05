#!/usr/bin/env python3
"""Hostile mutations for K1165."""
from copy import deepcopy
from k1165_i1b_prolongation_admission_boundary import build, validate


def main():
    mutations = [
        ("inputs", None, []),
        ("classes", 0, "Euler factors pass"),
        ("classes", 1, "no finite target"),
        ("classes", 2, "independent symbols excluded"),
        ("current_candidates_meeting_full_packet", None, 1),
        ("protected_disposition", None, "SC-ACT-06 refuted"),
        ("next_condition", None, "take more derivatives"),
        ("scope_boundary", None, "global no-go"),
        ("scorable_rows_added", None, 1),
        ("target_claim", None, "SC-ACT-06-KILLED"),
    ]
    caught = 0
    for kind, index, value in mutations:
        d = deepcopy(build())
        if kind == "classes": d["classes_now_excluded_for_current_k132_parent"][index] = value
        else: d[kind] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    assert caught == 10
    print("K1165 hostile probes: 10/10")


if __name__ == "__main__": main()
