#!/usr/bin/env python3
"""Hostile uniqueness and promotion mutations for K1732."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def valid(d):
    t=d.get("tangent",{});z=d.get("decision",{});s=d.get("scope_guard","")
    return all([d.get("claim_id")=="K1732","kappa6_p" in t.get("constraint",""),
      "nonzero" in t.get("rank",""),"kappa6_a,-kappa6_p" in t.get("null_direction",""),
      z.get("k1728_attainment_preserved") is True,z.get("quartic_optimal_tangent_unique") is False,
      z.get("finite_strength_optimizer_identified") is False,"first-order" in s])
def main():
 d=json.loads((ROOT/"lab/process/k1732-quartic-optimal-tangent-family.json").read_text());assert valid(d);m=[]
 for path,val in [(('claim_id',),'bad'),(('tangent','constraint'),'none'),(('tangent','rank'),'zero'),
                  (('tangent','null_direction'),'none'),(('decision','k1728_attainment_preserved'),False),
                  (('decision','quartic_optimal_tangent_unique'),True),(('decision','finite_strength_optimizer_identified'),True),
                  (('scope_guard',),'global theorem')]:
  x=copy.deepcopy(d);c=x
  for k in path[:-1]:c=c[k]
  c[path[-1]]=val;m.append(x)
 for i,x in enumerate(m,1):assert not valid(x);print(f"REJECT {i:02d}")
 print(f"RESULT: PASS {len(m)}/{len(m)} hostile mutations rejected")
if __name__=="__main__":main()
