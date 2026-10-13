#!/usr/bin/env python3
"""Hostile theorem-promotion mutations for K1733."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def valid(d):
 b=d.get("benchmark",{});z=d.get("decision",{});s=d.get("scope_guard","")
 return all([d.get("claim_id")=="K1733",d.get("grade")=="reproducible_numerical_evidence_not_interval_certification",
  b.get("q_grid")==[.003,.01,.03],"120 and 180" in b.get("quadrature",""),"Nelder-Mead" in b.get("optimization",""),
  z.get("two_radius_global_optimizer_proved") is False,z.get("all_seed_optimizer_proved") is False,"intervals" in s,"remote" in s])
def main():
 d=json.loads((ROOT/"lab/process/k1733-finite-strength-four-point-benchmark.json").read_text());assert valid(d);m=[]
 for path,val in [(('claim_id',),'bad'),(('grade',),'theorem'),(('benchmark','q_grid'),[.01]),
                  (('benchmark','quadrature'),'one order'),(('benchmark','optimization'),'one start'),
                  (('decision','two_radius_global_optimizer_proved'),True),(('decision','all_seed_optimizer_proved'),True),
                  (('scope_guard',),'proved global')]:
  x=copy.deepcopy(d);c=x
  for k in path[:-1]:c=c[k]
  c[path[-1]]=val;m.append(x)
 for i,x in enumerate(m,1):assert not valid(x);print(f"REJECT {i:02d}")
 print(f"RESULT: PASS {len(m)}/{len(m)} hostile mutations rejected")
if __name__=="__main__":main()
