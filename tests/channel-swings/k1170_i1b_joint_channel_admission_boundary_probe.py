#!/usr/bin/env python3
"""Hostile mutations for K1170."""
from copy import deepcopy
from k1170_i1b_joint_channel_admission_boundary import build, validate


def main():
    mutations=[("inputs",None,[]),("class",0,"Euler factors pass"),("class",1,"single target passes"),
      ("class",2,"direct sum passes"),("class",3,"independent maps excluded"),
      ("short","timelike",98371),("short","null",106535),("current",None,1),
      ("next_condition",None,"take more derivatives"),("protected_disposition",None,"SC-ACT-06 refuted"),
      ("scope_boundary",None,"global no-go"),("scorable_rows_added",None,1),("target_claim",None,"SC-ACT-06-KILLED")]
    caught=0
    for a,b,v in mutations:
        d=deepcopy(build())
        if a=="class": d["classes_now_excluded_for_current_k132_parent"][b]=v
        elif a=="short": d["best_case_joint_shortfalls"][b]=v
        elif a=="current": d["current_candidates_meeting_full_packet"]=v
        else: d[a]=v
        try: validate(d)
        except (AssertionError,KeyError): caught+=1
    assert caught==13
    print("K1170 hostile probes: 13/13")


if __name__=="__main__": main()
