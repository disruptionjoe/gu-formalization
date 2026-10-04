#!/usr/bin/env python3
"""K1074: a common-normalization pairing selects an affine stiffness law."""
import json
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/"lab/process/k1074-k1073-multimode-affine-stiffness-law.json"


def recover(l1,a1,l2,a2):
    c=(a2-a1)/(l2-l1); u=a1/c-l1; return c,u


def build():
    rows=[]
    for u,c in ((F(1),F(1)),(F(4),F(3)),(F(5,2),F(7,3))):
        l1,l2=F(3),F(15); a1,a2=c*(l1+u),c*(l2+u); cr,ur=recover(l1,a1,l2,a2)
        rows.append({"mass_squared":str(u),"kinetic_scale":str(c),"lambda_pair":[str(l1),str(l2)],"stiffness_pair":[str(a1),str(a2)],"recovered_scale":str(cr),"recovered_mass_squared":str(ur)})
    return {
        "schema_version":"1.0","result_id":"K1074-K1073-MULTIMODE-AFFINE-STIFFNESS-LAW","status":"working_draft_verified","created":"2026-10-04",
        "law":"S_qq(lambda)=c(lambda+u), S_pp(lambda)=c with common c>0",
        "affine_characterization":"the stiffness slope is c and the intercept is c u",
        "two_mode_recovery":"c=(A2-A1)/(lambda2-lambda1), u=A1/c-lambda1",
        "controls":rows,
        "normalization_boundary":"if each mode has an unrelated kinetic scale c_lambda, invariance alone selects only the per-mode ratio and does not identify one common u",
        "source_boundary":"the affine law is a candidate action requirement; no source-owned functional Hessian/pairing supplies its slope or intercept",
        "claim_ceiling":"exact multimode compatibility and recovery theorem for the supplied quadratic wave family",
        "target_claim":"NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["law"]=="S_qq(lambda)=c(lambda+u), S_pp(lambda)=c with common c>0"
    assert d["affine_characterization"]=="the stiffness slope is c and the intercept is c u"
    assert d["two_mode_recovery"]=="c=(A2-A1)/(lambda2-lambda1), u=A1/c-lambda1"
    assert len(d["controls"])==3 and all(x["kinetic_scale"]==x["recovered_scale"] and x["mass_squared"]==x["recovered_mass_squared"] for x in d["controls"])
    assert "unrelated kinetic scale" in d["normalization_boundary"] and "does not identify" in d["normalization_boundary"]
    assert "no source-owned functional" in d["source_boundary"]
    assert "supplied quadratic wave family" in d["claim_ceiling"]
    assert d["target_claim"]=="NONE-NOT-A-KILL"


if __name__=="__main__":
    data=build(); validate(data); OUTPUT.write_text(json.dumps(data,indent=2,sort_keys=True)+"\n"); print("K1074 controls: 8/8")
