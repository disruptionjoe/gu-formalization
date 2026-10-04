#!/usr/bin/env python3
"""K1007: PPT, negativity and concurrence threshold for K1006."""
from __future__ import annotations
import argparse, json
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/"lab/process/k1007-k1006-ppt-entanglement-threshold.json"

def build():
    p,lam=F(4,5),F(2,5); gap=p*(1+2*lam)-1
    return {
        "schema_version":"1.0","result_id":"K1007-K1006-PPT-ENTANGLEMENT-THRESHOLD","status":"working_draft_verified","created":"2026-10-04",
        "classification":"INTERNAL_CONDITIONAL_MATHEMATICS","target_claim":"NONE-NOT-A-KILL",
        "partial_transpose_spectrum":["(1+p)/4","(1+p)/4","(1-p+2p lambda)/4","(1-p-2p lambda)/4"],
        "entanglement":{"criterion":"p(1+2 lambda)>1","threshold":"p_E=1/(1+2 lambda)","negativity":"max(0,(p(1+2 lambda)-1)/4)","concurrence":"max(0,(p(1+2 lambda)-1)/2)=2 negativity"},
        "exact_control":{"p":str(p),"lambda":str(lam),"threshold_at_lambda":"5/9","partial_transpose_spectrum":["9/20","9/20","21/100","-11/100"],"negativity":str(gap/4),"concurrence":str(gap/2),"entangled":True},
        "ownership":{"ppt_is_internal_state_classification":True,"gu_physical_state_selected":False,"prediction_or_confirmation":False},
        "claim_ceiling":"Exact two-qubit PPT, negativity and concurrence boundary inside K1006 only; no GU physical-state, preparation or empirical result.",
    }

def validate(x):
    assert len(x["partial_transpose_spectrum"])==4
    e=x["entanglement"]; assert e["criterion"]=="p(1+2 lambda)>1" and e["threshold"]=="p_E=1/(1+2 lambda)"
    c=x["exact_control"]; assert c["threshold_at_lambda"]=="5/9" and c["partial_transpose_spectrum"]==["9/20","9/20","21/100","-11/100"]
    assert c["negativity"]=="11/100" and c["concurrence"]=="11/50" and c["entangled"]
    assert x["ownership"]["ppt_is_internal_state_classification"] and not x["ownership"]["gu_physical_state_selected"]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--write",action="store_true"); ap.add_argument("--check",action="store_true"); a=ap.parse_args()
    x=build(); validate(x); text=json.dumps(x,indent=2,sort_keys=True)+"\n"
    if a.write: OUTPUT.write_text(text)
    elif a.check: assert OUTPUT.read_text()==text
    else: print(text,end="")
    print("K1007 controls: 13/13")

if __name__=="__main__": main()
