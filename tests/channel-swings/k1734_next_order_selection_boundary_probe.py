#!/usr/bin/env python3
"""Hostile boundary-erasure mutations for K1734."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def valid(d):
 b=d.get("boundary",{});e=d.get("excluded_promotions",[]);s=d.get("scope_guard","")
 return all([d.get("claim_id")=="K1734","one affine constraint" in b.get("rank_defect",""),"beyond t^8" in b.get("required_next_calculation",""),
  "not the coefficient proof" in b.get("finite_grid_role",""),"all-seed infimum" in e,"source-owned physical state" in e,"not a no-go theorem" in s])
def main():
 d=json.loads((ROOT/"lab/process/k1734-next-order-selection-boundary.json").read_text());assert valid(d);m=[]
 for path,val in [(('claim_id',),'bad'),(('boundary','rank_defect'),'full rank'),(('boundary','required_next_calculation'),'done'),
                  (('boundary','finite_grid_role'),'proof'),(('excluded_promotions',),[]),(('scope_guard',),'global no-go')]:
  x=copy.deepcopy(d);c=x
  for k in path[:-1]:c=c[k]
  c[path[-1]]=val;m.append(x)
 for i,x in enumerate(m,1):assert not valid(x);print(f"REJECT {i:02d}")
 print(f"RESULT: PASS {len(m)}/{len(m)} hostile mutations rejected")
if __name__=="__main__":main()
