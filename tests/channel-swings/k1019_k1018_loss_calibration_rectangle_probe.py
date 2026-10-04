#!/usr/bin/env python3
"""Hostile mutations for K1019."""
from copy import deepcopy
from k1019_k1018_loss_calibration_rectangle import build, validate
def main():
    muts=[("rectangle_order","wrong"),("lower_rule","center only"),("upper_rule","center only"),("why_corners","globally monotone"),("certifying_control.corner_values",[]),("certifying_control.certified",False),("certifying_control.minimum",.9),("excluding_control.corner_values",[]),("excluding_control.excluded",False),("excluding_control.maximum",1.1),("nondecision","decide"),("claim_ceiling","empirical result"),("ownership.gu_calibration_constructed",True),("ownership.joint_confidence_event_owned",True),("target_claim","CONFIRMED")]
    caught=0
    for path,value in muts:
        d=deepcopy(build()); node=d; parts=path.split(".")
        for p in parts[:-1]: node=node[p]
        node[parts[-1]]=value
        try: validate(d)
        except AssertionError: caught+=1
    assert caught==len(muts); print(f"K1019 hostile probes: {caught}/{len(muts)}")
if __name__=="__main__": main()
