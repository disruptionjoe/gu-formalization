#!/usr/bin/env python3
"""Hostile half-order and promotion mutations for K1737."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];d=json.loads((ROOT/"lab/process/k1737-matched-half-order-cancellation.json").read_text())
def accepts(x):
 m=x.get("matched_path",{});z=x.get("decision",{})
 return all([x.get("claim_id")=="K1737","alpha=35/3" in m.get("quartic_equality",""),"0*q^(9/2)" in m.get("law",""),
  "beta^2/120" in m.get("law",""),"xi^2/5040" in m.get("law",""),not z.get("q_nine_halves_selects_tangent",True),
  z.get("q_five_is_first_tangent_varying_order"),"q^5" in m.get("first_tangent_varying_term",""),
  "local regular" in x.get("scope_guard","")])
mut=[]
for path,val in [(('claim_id',),'K1736'),(('matched_path','quartic_equality'),'none'),
 (('matched_path','law'),'nonzero q^(9/2)'),(('matched_path','law'),'beta only'),
 (('decision','q_nine_halves_selects_tangent'),True),
 (('decision','q_five_is_first_tangent_varying_order'),False),
 (('scope_guard',),'global branch'),(('matched_path','first_tangent_varying_term'),'q^(9/2)')]:
 x=copy.deepcopy(d);cur=x
 for k in path[:-1]:cur=cur[k]
 cur[path[-1]]=val;mut.append(x)
assert accepts(d)
for i,x in enumerate(mut,1):assert not accepts(x),i;print(f"PASS {i:02d}: rejected hostile mutation")
print(f"RESULT: PASS {len(mut)}/{len(mut)}")
