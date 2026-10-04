#!/usr/bin/env python3
"""K1009: visibility/contrast identifiability for K1006."""
from __future__ import annotations
import argparse, json
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/"lab/process/k1009-k1008-visibility-noise-identifiability.json"

def build():
    V=F(2,5)
    controls=[]
    for p,lam in ((F(1),F(2,5)),(F(1,2),F(4,5))):
        controls.append({"p":str(p),"lambda":str(lam),"V":str(p*lam),"S_max_squared_over_4":str(p*p+V*V),"violates_CHSH":p*p+V*V>1})
    return {
        "schema_version":"1.0","result_id":"K1009-K1008-VISIBILITY-NOISE-IDENTIFIABILITY","status":"working_draft_verified","created":"2026-10-04",
        "classification":"INTERNAL_CONDITIONAL_MATHEMATICS","target_claim":"NONE-NOT-A-KILL",
        "shared_noise_model":{"visibility":"V=p lambda","longitudinal_correlation":"<ZZ>=p","optimized_relation":"S_max^2/4=p^2+V^2","violation_iff":"p^2+V^2>1"},
        "identifiability":{"visibility_alone_sufficient":False,"for_p_positive":"lambda=V/p","additional_calibration":"<ZZ>=p"},
        "same_visibility_controls":controls,
        "ownership":{"shared_p_across_anchors_is_imported":True,"gu_cross_anchor_law_constructed":False,"prediction_or_confirmation":False},
        "claim_ceiling":"Exact two-parameter cross-anchor relation and visibility-only nonidentifiability inside the imported shared-noise model; no GU-owned noise law or empirical result.",
    }

def validate(x):
    m=x["shared_noise_model"]; assert m["visibility"]=="V=p lambda" and m["optimized_relation"]=="S_max^2/4=p^2+V^2"
    assert not x["identifiability"]["visibility_alone_sufficient"] and x["identifiability"]["additional_calibration"]=="<ZZ>=p"
    a,b=x["same_visibility_controls"]; assert a["V"]==b["V"]=="2/5"
    assert a["S_max_squared_over_4"]=="29/25" and a["violates_CHSH"]
    assert b["S_max_squared_over_4"]=="41/100" and not b["violates_CHSH"]
    assert x["ownership"]["shared_p_across_anchors_is_imported"] and not x["ownership"]["gu_cross_anchor_law_constructed"]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--write",action="store_true"); ap.add_argument("--check",action="store_true"); a=ap.parse_args()
    x=build(); validate(x); text=json.dumps(x,indent=2,sort_keys=True)+"\n"
    if a.write: OUTPUT.write_text(text)
    elif a.check: assert OUTPUT.read_text()==text
    else: print(text,end="")
    print("K1009 controls: 13/13")

if __name__=="__main__": main()
