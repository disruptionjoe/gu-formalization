#!/usr/bin/env python3
"""Hostile mutations for K1160."""
from copy import deepcopy
from k1160_i1b_source_epsilon_admission_boundary import build,validate


def main():
    mutations=[
        ("inputs",[]),
        ("classes_now_excluded_for_current_k132_parent",[]),
        ("classes_now_excluded_for_current_k132_parent",["Q=L H","small","seven-invariant"]),
        ("classes_now_excluded_for_current_k132_parent",["Q=L H","91-component","small"]),
        ("current_candidates_meeting_full_packet",1),
        ("protected_disposition","SC-ACT-06 refuted"),
        ("next_condition","stop"),
        ("scope_boundary","global GU no-go"),
        ("scorable_rows_added",1),
        ("target_claim","SC-ACT-06-KILLED"),
    ]
    caught=0
    for key,value in mutations:
        d=deepcopy(build());d[key]=value
        try:validate(d)
        except (AssertionError,KeyError,IndexError):caught+=1
    assert caught==10
    print("K1160 hostile probes: 10/10")


if __name__=="__main__":main()
