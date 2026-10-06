#!/usr/bin/env python3
"""Hostile mutations for K1169."""
from copy import deepcopy
from k1169_mixed_channel_multiplicity_boundary import build, validate


def main():
    mutations=[("theorem",None,"names add rank"),("timelike","pure_moment_minimum",1082),
      ("null","pure_moment_minimum",1171),("timelike","pure_lock_minimum",14067),
      ("null","pure_lock_minimum",15233),("nonnull_fail_by_one","capacity",98470),
      ("nonnull_first_pass_nearby","surplus",7),("null_fail_by_three","deficit",2),
      ("null_first_pass_nearby","capacity",106637),("descendant_rule",None,"derivatives count"),
      ("ownership_boundary",None,"source-owned repair"),("target_claim",None,"SC-ACT-06-KILLED")]
    caught=0
    for a,b,v in mutations:
        d=deepcopy(build())
        if a in d["causal"]: d["causal"][a][b]=v
        elif a in d["mixed_controls"]: d["mixed_controls"][a][b]=v
        else: d[a]=v
        try: validate(d)
        except (AssertionError,KeyError): caught+=1
    assert caught==12
    print("K1169 hostile probes: 12/12")


if __name__=="__main__": main()
