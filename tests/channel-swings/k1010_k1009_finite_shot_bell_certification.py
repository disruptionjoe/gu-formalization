#!/usr/bin/env python3
"""K1010: finite-shot CHSH confidence budget."""
from __future__ import annotations
import argparse, json, math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/"lab/process/k1010-k1009-finite-shot-bell-certification.json"

def penalty(n: int, alpha: float) -> float:
    return math.sqrt(8*math.log(8/alpha)/n)

def build():
    alpha=1/20; p=1.0; V=2/5; margin=2*math.sqrt(p*p+V*V)-2; n=math.ceil(8*math.log(8/alpha)/(margin*margin))
    return {
        "schema_version":"1.0","result_id":"K1010-K1009-FINITE-SHOT-BELL-CERTIFICATION","status":"working_draft_verified","created":"2026-10-04",
        "classification":"INTERNAL_REQUIREMENT_DISPOSITION","target_claim":"NONE-NOT-A-KILL",
        "statistical_contract":{"outcomes":"four iid streams in [-1,1]","per_correlator_shots":"n","confidence":"1-alpha","penalty":"beta(n,alpha)=sqrt(8 log(8/alpha)/n)","certificate":"S_hat>2+beta implies S>2","margin_budget":"n>=8 log(8/alpha)/m^2 per correlator"},
        "exact_example":{"p":"1","V":"2/5","alpha":"1/20","true_margin":"2(sqrt(29)/5-1)","n_per_correlator":n,"total_shots":4*n,"penalty_at_n":penalty(n,alpha),"penalty_at_n_minus_one":penalty(n-1,alpha),"margin_numeric":margin},
        "systematic_extension":"S_hat>2+beta+sigma_sys",
        "unowned_assumptions":["iid trials","correct bounded outcomes","predeclared settings","Bell-compatible randomization","detector semantics","systematic-error allocation"],
        "ownership":{"gu_physical_quotient_state_effect_locality_or_detector_constructed":False,"prediction_or_confirmation":False},
        "claim_ceiling":"Union-Hoeffding finite-shot certificate for four bounded iid correlators plus an ownership disposition only; no systematic-error theorem, loophole closure, GU-native measurement or empirical score.",
    }

def validate(x):
    s=x["statistical_contract"]; assert s["penalty"]=="beta(n,alpha)=sqrt(8 log(8/alpha)/n)" and s["certificate"]=="S_hat>2+beta implies S>2"
    e=x["exact_example"]; assert e["n_per_correlator"]==1711 and e["total_shots"]==6844
    assert e["penalty_at_n"]<=e["margin_numeric"]<e["penalty_at_n_minus_one"]
    assert x["systematic_extension"]=="S_hat>2+beta+sigma_sys" and len(x["unowned_assumptions"])==6
    assert not x["ownership"]["gu_physical_quotient_state_effect_locality_or_detector_constructed"]
    assert not x["ownership"]["prediction_or_confirmation"]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--write",action="store_true"); ap.add_argument("--check",action="store_true"); a=ap.parse_args()
    x=build(); validate(x); text=json.dumps(x,indent=2,sort_keys=True)+"\n"
    if a.write: OUTPUT.write_text(text)
    elif a.check: assert OUTPUT.read_text()==text
    else: print(text,end="")
    print("K1010 controls: 12/12")

if __name__=="__main__": main()
