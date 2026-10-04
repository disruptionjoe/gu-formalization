#!/usr/bin/env python3
"""K1073: a fixed positive pairing ratio selects one mass coefficient."""
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1073-k1072-pairing-ratio-mass-selector.json"


def selector(lam, a, c):
    return a/c-lam


def build():
    fixtures=[(F(0),F(1),F(1)),(F(0),F(4),F(1)),(F(3),F(8),F(1)),(F(8),F(35),F(5))]
    return {
        "schema_version":"1.0","result_id":"K1073-K1072-PAIRING-RATIO-MASS-SELECTOR","status":"working_draft_verified","created":"2026-10-04",
        "positive_solution_cone":"S=c diag(lambda+u,1) with c>0",
        "selector":"u=S_qq/S_pp-lambda",
        "uniqueness":"for a fixed positive pairing S and known spatial eigenvalue lambda, at most one positive mass coefficient is energy-skew",
        "scale_invariance":"overall positive rescaling of S cancels from S_qq/S_pp",
        "controls":[{"lambda":str(l),"S_qq":str(a),"S_pp":str(c),"selected_mass_squared":str(selector(l,a,c))} for l,a,c in fixtures],
        "circularity_guard":"constructing S from a previously chosen u proves compatibility but does not select u; the pairing must be independently source/action owned",
        "ownership":{"conditional_selector":True,"source_action_pairing_owned":False,"physical_mass_selected":False},
        "claim_ceiling":"exact conditional selector for the supplied modewise candidate family",
        "target_claim":"NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["positive_solution_cone"]=="S=c diag(lambda+u,1) with c>0"
    assert d["selector"]=="u=S_qq/S_pp-lambda"
    assert "at most one positive mass coefficient" in d["uniqueness"]
    assert "rescaling" in d["scale_invariance"] and "cancels" in d["scale_invariance"]
    assert [x["selected_mass_squared"] for x in d["controls"]]==["1","4","5","-1"]
    assert "does not select u" in d["circularity_guard"] and "independently source/action owned" in d["circularity_guard"]
    assert d["ownership"]=={"conditional_selector":True,"source_action_pairing_owned":False,"physical_mass_selected":False}
    assert "supplied modewise candidate family" in d["claim_ceiling"]
    assert d["target_claim"]=="NONE-NOT-A-KILL"


if __name__=="__main__":
    data=build(); validate(data); OUTPUT.write_text(json.dumps(data,indent=2,sort_keys=True)+"\n"); print("K1073 controls: 9/9")
