#!/usr/bin/env python3
"""Hostile mutations for K1024."""
from copy import deepcopy
from k1024_k1023_record_corruption_certificate import build, validate


def main():
    muts=[("deterministic_budget","expected errors"),("pathwise_lipschitz_bound","sum recorded<=sum true"),
          ("certificate","w>3/4"),("combined_tv_form","w>3/4"),("example.R",0),("example.R_over_n",0),
          ("example.uniform_threshold",.75),("tightness","free correction"),("memory_scope","iid only"),
          ("unowned_assumptions",[]),("ownership.gu_record_system_constructed",True),
          ("ownership.record_budget_empirically_certified",True),("target_claim","CONFIRMED")]
    caught=0
    for path,value in muts:
        d=deepcopy(build()); node=d; parts=path.split(".")
        for p in parts[:-1]: node=node[p]
        node[parts[-1]]=value
        try: validate(d)
        except AssertionError: caught+=1
    assert caught==len(muts)
    print(f"K1024 hostile probes: {caught}/{len(muts)}")


if __name__=="__main__": main()
