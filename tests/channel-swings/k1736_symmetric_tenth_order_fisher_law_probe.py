#!/usr/bin/env python3
"""Hostile coefficient and scope mutations for K1736."""
import copy, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
d=json.loads((ROOT/"lab/process/k1736-symmetric-tenth-order-fisher-law.json").read_text())
def accepts(x):
 h=x.get("hermite_law",{});z=x.get("decision",{})
 return all([x.get("claim_id")=="K1736","bounded symmetric" in h.get("scope",""),
  "kappa_6(" in h.get("ninth_coefficient",""),"855kappa_4^3" in h.get("ninth_coefficient",""),
  "h_10^2" in h.get("tenth_coefficient",""),"/362880" in h.get("tenth_coefficient",""),
  "(r_t')^2/r_t" in h.get("derivation",""),
  z.get("new_moment_first_enters_at_tenth_order")=="h_10",not z.get("all_seed_finite_strength_optimizer_identified",True),
  "growing support" in x.get("scope_guard","")])
mutations=[]
for path,val in [(('claim_id',),'K1735'),(('hermite_law','scope'),'arbitrary law'),
 (('hermite_law','ninth_coefficient'),'0'),(('hermite_law','tenth_coefficient'),'h_10'),
 (('decision','new_moment_first_enters_at_tenth_order'),'h_8'),
 (('decision','all_seed_finite_strength_optimizer_identified'),True),
 (('scope_guard',),'finite strength solved'),(('hermite_law','derivation'),'numerical fit')]:
 x=copy.deepcopy(d);cur=x
 for k in path[:-1]:cur=cur[k]
 cur[path[-1]]=val;mutations.append(x)
assert accepts(d)
for i,x in enumerate(mutations,1):assert not accepts(x),i;print(f"PASS {i:02d}: rejected hostile mutation")
print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")
