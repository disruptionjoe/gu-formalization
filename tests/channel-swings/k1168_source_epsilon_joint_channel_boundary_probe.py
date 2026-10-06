#!/usr/bin/env python3
"""Hostile mutations for K1168."""
from copy import deepcopy
from k1168_source_epsilon_joint_channel_boundary import build, validate


def main():
    mutations=[("inputs",None,[]),("favorable_grant",None,"source coupling proved"),
      ("timelike","best_case_shortfall",0),("spacelike","joint_target_ceiling",99),
      ("null","best_case_shortfall",106535),("null","gauge_rank",5),
      ("overlap_rule",None,"overlap helps"),("decision",None,"packet passes"),
      ("necessity_not_sufficiency",None,"physical quotient complete"),
      ("protected_disposition",None,"SC-ACT-06 refuted"),("target_claim",None,"SC-ACT-06-KILLED")]
    caught=0
    for a,b,v in mutations:
        d=deepcopy(build())
        if a in d["causal"]: d["causal"][a][b]=v
        else: d[a]=v
        try: validate(d)
        except (AssertionError,KeyError): caught+=1
    assert caught==11
    print("K1168 hostile probes: 11/11")


if __name__=="__main__": main()
