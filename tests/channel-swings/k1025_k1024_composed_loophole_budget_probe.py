#!/usr/bin/env python3
"""Hostile mutations for K1025."""
from copy import deepcopy
from k1025_k1024_composed_loophole_budget import build, validate


def main():
    muts=[("certificate","w>3/4"),("forecast_model","model free"),("frozen_point.n_total",33411),
          ("frozen_point.effective_margin",0),("frozen_point.penalty_at_n",1),
          ("frozen_point.penalty_at_n_minus_one",0),("frozen_point.epsilon","0"),
          ("feasibility_condition","none"),("inference_boundary","empirical GU prediction"),
          ("remaining_unowned_packet",[]),("ownership.gu_protocol_constructed",True),
          ("ownership.loophole_free_experiment_claimed",True),("target_claim","CONFIRMED")]
    caught=0
    for path,value in muts:
        d=deepcopy(build()); node=d; parts=path.split(".")
        for p in parts[:-1]: node=node[p]
        node[parts[-1]]=value
        try: validate(d)
        except AssertionError: caught+=1
    assert caught==len(muts)
    print(f"K1025 hostile probes: {caught}/{len(muts)}")


if __name__=="__main__": main()
