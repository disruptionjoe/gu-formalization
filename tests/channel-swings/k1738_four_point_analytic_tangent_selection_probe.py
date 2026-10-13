#!/usr/bin/env python3
"""Hostile uniqueness-scope mutations for K1738."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];d=json.loads((ROOT/"lab/process/k1738-four-point-analytic-tangent-selection.json").read_text())
def accepts(x):
 s=x.get("selection",{});z=x.get("decision",{})
 return all([x.get("claim_id")=="K1738","kappa6_p P+kappa6_a A" in s.get("first_condition",""),
  "x_p P+x_a A=0" in s.get("second_condition",""),"nonzero" in s.get("jacobian",""),"xi^2/5040" in s.get("uniqueness",""),
  "remaining second-order freedom" in s.get("second_order_boundary",""),z.get("leading_analytic_tangent_unique"),
  not z.get("complete_local_analytic_branch_unique",True),"first chart velocity" in x.get("scope_guard","")])
mut=[]
for path,val in [(('claim_id',),'K1737'),(('selection','first_condition'),'none'),
 (('selection','second_condition'),'none'),(('selection','jacobian'),'zero'),
 (('selection','uniqueness'),'global uniqueness'),(('selection','second_order_boundary'),'all fixed'),
 (('decision','complete_local_analytic_branch_unique'),True),(('scope_guard',),'global optimizer')]:
 x=copy.deepcopy(d);cur=x
 for k in path[:-1]:cur=cur[k]
 cur[path[-1]]=val;mut.append(x)
assert accepts(d)
for i,x in enumerate(mut,1):assert not accepts(x),i;print(f"PASS {i:02d}: rejected hostile mutation")
print(f"RESULT: PASS {len(mut)}/{len(mut)}")
