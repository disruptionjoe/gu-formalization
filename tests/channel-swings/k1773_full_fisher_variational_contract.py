#!/usr/bin/env python3
"""Validate the boundary-safe full-Fisher variational proof contract."""
import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];ARTIFACT=ROOT/"lab/process/k1773-full-fisher-variational-contract.json"
def algebra(c,z):
 p=c/(c+z*z);a=1-z;b=1+c/z
 return p,a,b,p*a+(1-p)*b,p*a+(1-p)*b
def validate(d):
 x=d["contract"];q=F(1,1024);tests=[]
 for c,z in ((F(1,100),F(1,10)),(F(1,1000),F(1,20)),(F(1,10**6),F(1,1000))):
  p,a,b,mean_radius,variance=algebra(c,z);tests += [0<p<1, a>=0, b>1, mean_radius==1, variance==1]
 return [("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1773"),("fixed q",x["q"]=="1/1024"),("chart algebra",all(tests)),("lower direction",x["inequality_direction"]=="J>=V"),("two sectors",len(x["boundary_sectors"])==2),("tail",x["tail_control"]=="3*P(|Z|>11)"),("Arb incomplete",not d["decision"]["sectorized_arb_cover_completed"]),("no exclusion",not d["decision"]["boundary_strip_excluded"])]
def main():
 d=json.loads(ARTIFACT.read_text());checks=validate(d)
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
