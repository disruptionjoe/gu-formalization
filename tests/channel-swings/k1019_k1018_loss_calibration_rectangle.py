#!/usr/bin/env python3
"""K1019: exact corner propagation for noisy-lossy calibration boxes."""
import json, math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/"lab/process/k1019-k1018-loss-calibration-rectangle.json"

def f(p,v,a,b): return a*b*math.sqrt(p*p+v*v)+(1-a)*(1-b)
def extrema(box, upper=False):
    p=box[1] if upper else box[0]; v=box[3] if upper else box[2]
    vals=[f(p,v,a,b) for a in box[4:6] for b in box[6:8]]
    return (max(vals) if upper else min(vals)), vals

def build():
    certify=[.99,1,.39,.41,.98,.99,.98,.99]
    exclude=[.79,.81,.31,.33,.90,.92,.90,.92]
    cmin,cc=extrema(certify); emax,ec=extrema(exclude,True)
    return {"schema_version":"1.0","result_id":"K1019-K1018-LOSS-CALIBRATION-RECTANGLE","status":"working_draft_verified","created":"2026-10-04",
      "rectangle_order":"[pL,pU,VL,VU,etaAL,etaAU,etaBL,etaBU]",
      "lower_rule":"min over four efficiency corners at (pL,VL); certify CHSH when min F>1",
      "upper_rule":"max over four efficiency corners at (pU,VU); exclude CHSH when max F<=1",
      "why_corners":"F is monotone in p,V but bilinear, not globally monotone, in eta_A,eta_B",
      "certifying_control":{"box":certify,"corner_values":cc,"minimum":cmin,"certified":cmin>1},
      "excluding_control":{"box":exclude,"corner_values":ec,"maximum":emax,"excluded":emax<=1},
      "nondecision":"all other rectangle outcomes are inconclusive",
      "claim_ceiling":"propagation of one supplied simultaneous confidence box; no calibration event or systematic budget constructed",
      "ownership":{"gu_calibration_constructed":False,"joint_confidence_event_owned":False},"target_claim":"NONE-NOT-A-KILL"}

def validate(d):
    assert d["rectangle_order"].startswith("[pL,pU")
    assert "four efficiency corners" in d["lower_rule"]
    assert "four efficiency corners" in d["upper_rule"]
    assert "not globally monotone" in d["why_corners"]
    assert len(d["certifying_control"]["corner_values"])==4
    assert d["certifying_control"]["certified"] is True and d["certifying_control"]["minimum"]>1
    assert len(d["excluding_control"]["corner_values"])==4
    assert d["excluding_control"]["excluded"] is True and d["excluding_control"]["maximum"]<=1
    assert d["nondecision"].endswith("inconclusive")
    assert "supplied simultaneous confidence box" in d["claim_ceiling"]
    assert d["ownership"]["gu_calibration_constructed"] is False
    assert d["ownership"]["joint_confidence_event_owned"] is False
    assert d["target_claim"]=="NONE-NOT-A-KILL"

if __name__=="__main__":
    d=build(); validate(d); OUTPUT.write_text(json.dumps(d,indent=2,sort_keys=True)+"\n"); print("K1019 controls: 13/13")
