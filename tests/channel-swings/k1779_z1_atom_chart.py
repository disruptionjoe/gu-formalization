#!/usr/bin/env python3
"""Exact replay of K1779's regular z=1 atom chart."""
import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];ARTIFACT=ROOT/"lab/process/k1779-z1-atom-chart.json"
def compute():
 slab=json.loads((ROOT/"lab/process/k1771-interior-survivor-topology.json").read_text())["topology"]["slabs"][0]
 q=F(1,1024);ta,tb=map(F,slab["t"]);ca=F(2)-q/ta**2;cb=F(2)-q/tb**2
 return ca,cb,ca/(1+ca)
def validate(d):
 ca,cb,p=compute();x=d["chart"];z=d["decision"]
 return [("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1779"),("q",x["q"]=="1/1024"),
  ("law","P(X=0)=c/(1+c)" in x["law"]),("variance",x["variance"]=="E[X^2]=1"),("c interval",list(map(F,x["first_slab_c_interval"]))==[ca,cb]),
  ("p lower",F(x["first_slab_p_lower"])==p),("positive denominator",">=p" in x["positive_denominator"]),
  ("regular",z["z1_chart_regularized"]),("no raw division",not z["raw_b_or_c_over_z_required"]),("edge open",not z["z1_edge_excluded"]),("not optimizer",not z["global_optimizer_proved"])]
def main():
 d=json.loads(ARTIFACT.read_text());checks=validate(d)
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
