#!/usr/bin/env python3
"""K1049: any two ordered frequency pairs are equivalent under positive affine readout."""
import json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/"lab/process/k1049-k1048-affine-readout-nonidentifiability.json"
def build():
    u1,u2=math.sqrt(2),math.sqrt(5); v1,v2=math.sqrt(5),math.sqrt(8)
    g=(v2-v1)/(u2-u1); b=v1-g*u1
    return {"schema_version":"1.0","result_id":"K1049-K1048-AFFINE-READOUT-NONIDENTIFIABILITY","status":"working_draft_verified","created":"2026-10-04","general_theorem":"for ordered pairs u1<u2 and v1<v2, g=(v2-v1)/(u2-u1)>0 and b=v1-g*u1 give g*u_i+b=v_i for i=1,2","horn_map":{"source":"mass1 frequencies (sqrt(2),sqrt(5))","target":"mass4 frequencies (sqrt(5),sqrt(8))","gain_exact":"(sqrt(8)-sqrt(5))/(sqrt(5)-sqrt(2))","offset_exact":"sqrt(5)-gain*sqrt(2)","gain_decimal":f"{g:.15f}","offset_decimal":f"{b:.15f}","residuals":[f"{g*u1+b-v1:.3e}",f"{g*u2+b-v2:.3e}"]},"consequence":"two prepared modes cannot discriminate the horns when common gain and additive offset are both free","reopener":"calibrate or bound the offset, or add a third mode and use an affine-invariant statistic","scope":"candidate apparatus countermodel only; the common ruler and both mass horns remain imported","target_claim":"NONE-NOT-A-KILL"}
def validate(d):
    assert "g=(v2-v1)/(u2-u1)>0" in d["general_theorem"] and "i=1,2" in d["general_theorem"]
    assert d["horn_map"]["source"].startswith("mass1") and d["horn_map"]["target"].startswith("mass4")
    assert d["horn_map"]["gain_exact"].startswith("(sqrt(8)-sqrt(5))")
    assert d["horn_map"]["offset_exact"].startswith("sqrt(5)-gain")
    assert float(d["horn_map"]["gain_decimal"])>0 and abs(float(d["horn_map"]["offset_decimal"]))<10
    assert all(abs(float(x))<1e-12 for x in d["horn_map"]["residuals"])
    assert "cannot discriminate" in d["consequence"] and "both free" in d["consequence"]
    assert "third mode" in d["reopener"] and "affine-invariant" in d["reopener"]
    assert "candidate apparatus countermodel only" in d["scope"] and "imported" in d["scope"]
    assert d["target_claim"]=="NONE-NOT-A-KILL"
if __name__=="__main__":
    data=build(); validate(data); OUTPUT.write_text(json.dumps(data,indent=2,sort_keys=True)+"\n"); print("K1049 controls: 10/10")
