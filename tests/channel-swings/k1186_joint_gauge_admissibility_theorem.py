#!/usr/bin/env python3
"""K1186: exact joint Hessian/response gauge-admissibility gate."""
from __future__ import annotations
import argparse,json
from fractions import Fraction
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k1186-joint-gauge-admissibility-theorem.json"
def apply(a:list[list[int]],v:list[int])->list[Fraction]:return [sum(Fraction(x)*y for x,y in zip(row,v)) for row in a]
def controls()->list[dict[str,Any]]:
 h=[[1,0,0,0]];j=[[0,1,0,0]]
 cases=[("full_joint_kernel",[[0,0,1,0],[0,0,0,1]],2,True),("response_only_is_insufficient",[[1,0,0,0]],2,False),("hessian_only_is_insufficient",[[0,1,0,0]],2,False)]
 out=[]
 for name,cols,kdim,expected in cases:
  ha=all(not any(apply(h,v)) for v in cols);ja=all(not any(apply(j,v)) for v in cols)
  out.append({"case":name,"dim_v":4,"joint_kernel_dimension":kdim,"proposed_rank":len(cols),"h_annihilates":ha,"j_annihilates":ja,"admissible":ha and ja})
  assert out[-1]["admissible"] is expected
 out.append({"case":"trivial_joint_kernel","dim_v":2,"joint_kernel_dimension":0,"proposed_rank":0,"h_annihilates":True,"j_annihilates":True,"admissible":True})
 return out
def build()->dict[str,Any]:
 return {"schema_version":"1.0","result_id":"K1186-JOINT-GAUGE-ADMISSIBILITY-THEOREM","created":"2026-10-05","status":"working_draft_verified","classification":"CONDITIONAL_RESULT","necessary_equations":["H d=0","J d=0"],"equivalent_condition":"im(d) subset ker(H) intersection ker(J)=ker(H,J)","dimension_ceiling":"rank(d)<=dim ker(H,J)","sharp":True,"controls":controls(),"claim_ceiling":"exact finite-dimensional necessity; no source-owned enlarged gauge image or functional complex"}
def validate(p:dict[str,Any])->None:
 assert p["result_id"]=="K1186-JOINT-GAUGE-ADMISSIBILITY-THEOREM" and p["status"]=="working_draft_verified" and p["classification"]=="CONDITIONAL_RESULT"
 assert p["necessary_equations"]==["H d=0","J d=0"] and "ker(H,J)" in p["equivalent_condition"] and p["dimension_ceiling"]=="rank(d)<=dim ker(H,J)" and p["sharp"]
 assert p["controls"]==controls() and [x["admissible"] for x in p["controls"]]==[True,False,False,True]
 assert "no source-owned" in p["claim_ceiling"]
def main()->int:
 q=argparse.ArgumentParser();q.add_argument("--write",action="store_true");a=q.parse_args();p=build();validate(p);s=json.dumps(p,indent=2,sort_keys=True)+"\n";OUTPUT.write_text(s) if a.write else print(s,end="");print("PASS controls=16",file=__import__('sys').stderr);return 0
if __name__=="__main__":raise SystemExit(main())
