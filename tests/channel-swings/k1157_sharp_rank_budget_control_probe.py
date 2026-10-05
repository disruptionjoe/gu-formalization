#!/usr/bin/env python3
"""Hostile mutations for K1157."""
from copy import deepcopy
from k1157_sharp_rank_budget_control import build, validate


def main():
    mutations=[]
    for r in range(7): mutations.append((r, "constraint_target_dimension", 99))
    mutations += [
        (None, "all_splits_saturate_budget", False),
        (None, "all_splits_leave_positive_nonzero_quotient", False),
        (None, "conclusion", "not sharp"),
        (None, "scope_boundary", "source-owned functional theorem"),
        (None, "target_claim", "SC-ACT-06-KILLED"),
    ]
    caught=0
    for idx,key,value in mutations:
        d=deepcopy(build())
        if idx is None: d[key]=value
        else: d["splits"][idx][key]=value
        try: validate(d)
        except (AssertionError,KeyError): caught+=1
    assert caught == 12
    print("K1157 hostile probes: 12/12")


if __name__ == "__main__": main()
