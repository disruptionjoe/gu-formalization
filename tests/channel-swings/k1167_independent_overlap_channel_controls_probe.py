#!/usr/bin/env python3
"""Hostile mutations for K1167."""
from copy import deepcopy
from k1167_independent_overlap_channel_controls import build, validate


def main():
    mutations = [
        ("independent","stacked_rank",4), ("independent","overlap_defect",1),
        ("one_overlap","stacked_rank",5), ("one_overlap","overlap_defect",0),
        ("duplicate","stacked_rank",4), ("duplicate","overlap_defect",0),
        ("sharpness",None,"all additive"), ("interpretation",None,"names prove independence"),
        ("scope_boundary",None,"source channels classified"), ("target_claim",None,"SC-ACT-06-KILLED"),
    ]
    caught=0
    for a,b,v in mutations:
        d=deepcopy(build())
        if a in d["controls"]: d["controls"][a][b]=v
        else: d[a]=v
        try: validate(d)
        except (AssertionError,KeyError): caught+=1
    assert caught==10
    print("K1167 hostile probes: 10/10")


if __name__ == "__main__": main()
