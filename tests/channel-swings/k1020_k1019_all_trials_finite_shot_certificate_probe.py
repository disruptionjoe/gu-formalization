#!/usr/bin/env python3
"""Hostile mutations for K1020."""
from copy import deepcopy
from k1020_k1019_all_trials_finite_shot_certificate import build, validate
def main():
    muts=[("protocol","postselect clicks"),("certificate","w>1/2"),("memory_scope","iid only"),("forecast_model","arbitrary loss"),("frozen_point.n_total",19809),("frozen_point.margin",0),("frozen_point.penalty_at_n",1),("frozen_point.penalty_at_n_minus_one",0),("frozen_point.eta","1"),("inference_boundary","fair sampling required for inference"),("unowned_assumptions",[]),("ownership.gu_protocol_constructed",True),("ownership.loophole_free_experiment_claimed",True),("target_claim","CONFIRMED")]
    caught=0
    for path,value in muts:
        d=deepcopy(build()); node=d; parts=path.split(".")
        for p in parts[:-1]: node=node[p]
        node[parts[-1]]=value
        try: validate(d)
        except AssertionError: caught+=1
    assert caught==len(muts); print(f"K1020 hostile probes: {caught}/{len(muts)}")
if __name__=="__main__": main()
