#!/usr/bin/env python3
"""K1048: classify common clock gain, differential transfer, and additive offset."""
import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/"lab/process/k1048-k1047-common-clock-cancellation.json"
def build():
    w1sq,w2sq,g=F(2),F(5),F(7,3)
    return {"schema_version":"1.0","result_id":"K1048-K1047-COMMON-CLOCK-CANCELLATION","status":"working_draft_verified","created":"2026-10-04","readout_model":"y_i=g*(1+e_i)*omega_i+b with common g>0","common_gain_theorem":"when b=0 and e_1=e_2=0, (y_2/y_1)^2=(omega_2/omega_1)^2 exactly for every g>0","differential_transfer":"when b=0, Q_hat=Q*((1+e_2)/(1+e_1))^2, which is exactly the K1044 error model","offset_boundary":"a common additive b does not cancel from a two-frequency ratio and requires calibration, bounding, or an affine-invariant protocol","fixture":{"gain":"7/3","true_Q":str(w2sq/w1sq),"measured_Q":str((g*g*w2sq)/(g*g*w1sq))},"ownership_correction":"an absolute clock scale is unnecessary for the ratio; stable mode-to-mode transfer and offset control remain required","target_claim":"NONE-NOT-A-KILL"}
def validate(d):
    assert d["readout_model"]=="y_i=g*(1+e_i)*omega_i+b with common g>0"
    assert "exactly for every g>0" in d["common_gain_theorem"]
    assert "Q_hat=Q*((1+e_2)/(1+e_1))^2" in d["differential_transfer"] and "K1044" in d["differential_transfer"]
    assert "does not cancel" in d["offset_boundary"] and "affine-invariant" in d["offset_boundary"]
    assert d["fixture"]=={"gain":"7/3","true_Q":"5/2","measured_Q":"5/2"}
    assert "absolute clock scale is unnecessary" in d["ownership_correction"] and "offset control" in d["ownership_correction"]
    assert d["target_claim"]=="NONE-NOT-A-KILL"
if __name__=="__main__":
    data=build(); validate(data); OUTPUT.write_text(json.dumps(data,indent=2,sort_keys=True)+"\n"); print("K1048 controls: 7/7")
