#!/usr/bin/env python3
"""K1018: compose K1011 noisy Bell coordinates with K1017 loss."""
import json, math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/"lab/process/k1018-k1017-noisy-lossy-bell-interface.json"

def factor(p,v,a,b): return a*b*math.sqrt(p*p+v*v)+(1-a)*(1-b)

def build():
    r=math.sqrt(29)/5; threshold=2/(1+r)
    return {"schema_version":"1.0","result_id":"K1018-K1017-NOISY-LOSSY-BELL-INTERFACE","status":"working_draft_verified","created":"2026-10-04",
      "domain":"0<=V<=p<=1 and 0<=eta_A,eta_B<=1",
      "observed_chsh":"S_loss=2[eta_A eta_B sqrt(p^2+V^2)+(1-eta_A)(1-eta_B)]",
      "violation_iff":"eta_A eta_B sqrt(p^2+V^2)+(1-eta_A)(1-eta_B)>1",
      "frozen_point":{"p":"1","V":"2/5","ideal_half_chsh":"sqrt(29)/5","equal_efficiency_threshold":"10/(5+sqrt(29))","threshold":threshold,"at_threshold_factor":factor(1,.4,threshold,threshold)},
      "interpretation":"small ideal Bell margins demand detector efficiencies much closer to one than the maximally entangled K1016 control",
      "claim_ceiling":"composition theorem inside the imported noisy-state and independent-loss models only",
      "ownership":{"gu_state_or_detector_constructed":False,"empirical_score":False},"target_claim":"NONE-NOT-A-KILL"}

def validate(d):
    assert d["domain"].startswith("0<=V<=p<=1")
    assert "sqrt(p^2+V^2)" in d["observed_chsh"]
    assert d["violation_iff"].endswith(">1")
    assert d["frozen_point"]["ideal_half_chsh"]=="sqrt(29)/5"
    assert d["frozen_point"]["equal_efficiency_threshold"]=="10/(5+sqrt(29))"
    assert abs(d["frozen_point"]["threshold"]-0.9629120178362601)<1e-15
    assert abs(d["frozen_point"]["at_threshold_factor"]-1)<1e-14
    assert "closer to one" in d["interpretation"]
    assert "imported noisy-state" in d["claim_ceiling"]
    assert d["ownership"]["gu_state_or_detector_constructed"] is False
    assert d["ownership"]["empirical_score"] is False
    assert d["target_claim"]=="NONE-NOT-A-KILL"

if __name__=="__main__":
    d=build(); validate(d); OUTPUT.write_text(json.dumps(d,indent=2,sort_keys=True)+"\n"); print("K1018 controls: 12/12")
