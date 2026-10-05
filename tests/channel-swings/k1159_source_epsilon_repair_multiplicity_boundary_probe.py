#!/usr/bin/env python3
"""Hostile mutations for K1159."""
from copy import deepcopy
from k1159_source_epsilon_repair_multiplicity_boundary import build,validate


def main():
    mutations=[
        ("full_moment_map_91","timelike","minimum_copies_with_rank4_gauge",1),
        ("full_moment_map_91","null","minimum_copies_with_rank4_gauge",1),
        ("full_moment_map_91","timelike","minimum_gauge_rank_with_one_copy",4),
        ("full_moment_map_91","null","minimum_gauge_rank_with_one_copy",4),
        ("seven_invariant_lock","timelike","minimum_copies_with_rank4_gauge",1),
        ("seven_invariant_lock","null","minimum_copies_with_rank4_gauge",1),
        ("seven_invariant_lock","timelike","minimum_gauge_rank_with_one_copy",4),
        ("seven_invariant_lock","null","minimum_gauge_rank_with_one_copy",4),
        (None,None,"ownership_status","source owns copies"),
        (None,None,"necessity_not_sufficiency","rank is sufficient"),
        (None,None,"target_claim","SC-ACT-06-PROVED"),
    ]
    caught=0
    for group,case,key,value in mutations:
        d=deepcopy(build())
        if group is None:d[key]=value
        else:d[group][case][key]=value
        try:validate(d)
        except (AssertionError,KeyError):caught+=1
    assert caught==11
    print("K1159 hostile probes: 11/11")


if __name__=="__main__":main()
