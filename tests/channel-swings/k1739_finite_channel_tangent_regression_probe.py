#!/usr/bin/env python3
"""Hostile numerical-promotion mutations for K1739."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];d=json.loads((ROOT/"lab/process/k1739-finite-channel-tangent-regression.json").read_text())
def accepts(x):
 r=x.get("regression",{});z=x.get("decision",{})
 return all([x.get("claim_id")=="K1739",x.get("grade")=="reproducible_numerical_regression_not_interval_certification",
  r.get("quadrature_orders")==[120,180],r.get("optimizer_starts")==4,"conditioning caveat" in r.get("controls",""),
  z.get("analytic_tangent_numerically_supported"),not z.get("analytic_tangent_proved_by_regression",True),
  not z.get("global_two_radius_optimizer_proved",True),"not an interval proof" in x.get("scope_guard","")])
mut=[]
for path,val in [(('claim_id',),'K1738'),(('grade',),'theorem'),
 (('regression','quadrature_orders'),[180]),(('regression','optimizer_starts'),1),
 (('regression','controls'),'perfect coordinates'),
 (('decision','analytic_tangent_proved_by_regression'),True),
 (('decision','global_two_radius_optimizer_proved'),True),(('scope_guard',),'global proof')]:
 x=copy.deepcopy(d);cur=x
 for k in path[:-1]:cur=cur[k]
 cur[path[-1]]=val;mut.append(x)
assert accepts(d)
for i,x in enumerate(mut,1):assert not accepts(x),i;print(f"PASS {i:02d}: rejected hostile mutation")
print(f"RESULT: PASS {len(mut)}/{len(mut)}")
