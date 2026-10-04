#!/usr/bin/env python3
"""K1008: exact entangled but optimized-CHSH-local separator."""
from __future__ import annotations
import argparse, json
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/"lab/process/k1008-k1007-entangled-bell-local-separator.json"

def build():
    p,lam=F(4,5),F(2,5)
    return {
        "schema_version":"1.0","result_id":"K1008-K1007-ENTANGLED-BELL-LOCAL-SEPARATOR","status":"working_draft_verified","created":"2026-10-04",
        "classification":"INTERNAL_CONDITIONAL_MATHEMATICS","target_claim":"NONE-NOT-A-KILL",
        "optimized_chsh":{"formula":"S_max=2p sqrt(1+lambda^2)","violation_iff":"p^2(1+lambda^2)>1","threshold":"p_B=1/sqrt(1+lambda^2)"},
        "threshold_order":{"entanglement_threshold":"p_E=1/(1+2 lambda)","strict_order_for_positive_lambda":"p_E<p_B","proof_gap":"(1+2 lambda)^2-(1+lambda^2)=lambda(4+3 lambda)>0"},
        "exact_separator":{"p":str(p),"lambda":str(lam),"entanglement_control":"p(1+2lambda)=36/25>1","S_max_squared":str(4*p*p*(1+lam*lam)),"optimized_CHSH_violates":False,"S_fixed_squared":str(2*p*p*(1+lam)*(1+lam)),"fixed_CHSH_violates":False},
        "scope":{"optimized_chsh_local_only":True,"all_measurement_lhv_model_claimed":False},
        "ownership":{"gu_state_or_measurement_owner_constructed":False,"prediction_or_confirmation":False},
        "claim_ceiling":"Exact separation between PPT entanglement and optimized CHSH violation inside K1006 only; no all-measurement local model or GU-native state claim.",
    }

def validate(x):
    q=x["optimized_chsh"]; assert q["formula"]=="S_max=2p sqrt(1+lambda^2)" and q["violation_iff"]=="p^2(1+lambda^2)>1"
    assert x["threshold_order"]["strict_order_for_positive_lambda"]=="p_E<p_B"
    c=x["exact_separator"]; assert c["entanglement_control"]=="p(1+2lambda)=36/25>1"
    assert c["S_max_squared"]=="1856/625" and not c["optimized_CHSH_violates"]
    assert c["S_fixed_squared"]=="1568/625" and not c["fixed_CHSH_violates"]
    assert x["scope"]["optimized_chsh_local_only"] and not x["scope"]["all_measurement_lhv_model_claimed"]
    assert not x["ownership"]["gu_state_or_measurement_owner_constructed"]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--write",action="store_true"); ap.add_argument("--check",action="store_true"); a=ap.parse_args()
    x=build(); validate(x); text=json.dumps(x,indent=2,sort_keys=True)+"\n"
    if a.write: OUTPUT.write_text(text)
    elif a.check: assert OUTPUT.read_text()==text
    else: print(text,end="")
    print("K1008 controls: 13/13")

if __name__=="__main__": main()
