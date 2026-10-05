#!/usr/bin/env python3
"""Hostile mutations for K1158."""
from copy import deepcopy
from k1158_source_epsilon_k132_rank_budget import build, validate


def main():
    mutations=[
        ("inputs",None,[]),
        ("strongest_grant",None,"native bridge proved"),
        ("full_moment_map_91","timelike",0),
        ("full_moment_map_91","null",0),
        ("seven_invariant_lock","timelike",0),
        ("seven_invariant_lock","null",0),
        ("budget",None,True),
        ("direct_port_passes",None,True),
        ("decision",None,"passes"),
        ("scope_boundary",None,"global physical exclusion"),
        ("target_claim",None,"SC-ACT-06-KILLED"),
    ]
    caught=0
    for section,key,value in mutations:
        d=deepcopy(build())
        if section in d: d[section]=value
        elif section=="budget": d["targets"]["full_moment_map_91"]["spacelike"]["budget_passes"]=value
        else: d["targets"][section][key]["rank_shortfall"]=value
        try: validate(d)
        except (AssertionError,KeyError): caught+=1
    assert caught == 11
    print("K1158 hostile probes: 11/11")


if __name__ == "__main__": main()
