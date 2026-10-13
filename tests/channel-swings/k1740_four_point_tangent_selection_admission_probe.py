#!/usr/bin/env python3
"""Hostile protected-state promotion mutations for K1740."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];d=json.loads((ROOT/"lab/process/k1740-four-point-tangent-selection-admission.json").read_text())
def accepts(x):
 c=x.get("bridge_census",{});p=x.get("protected_state",{});z=x.get("decision",{})
 return all([x.get("claim_id")=="K1740",c.get("row_count")==440,c.get("satisfied_count")==361,c.get("missing_count")==4,
  c.get("new_satisfied_rows")==["K1736","K1737","K1738","K1739","K1740"],"ASSERTS" in p.get("source_claims",""),
  "UNCERTAIN" in p.get("source_claims",""),not p.get("canon_change",True),not p.get("public_posture_change",True),
  not z.get("complete_local_branch_identified",True),not z.get("exact_finite_strength_optimizer_identified",True),
  "remaining second-order chart freedom" in x.get("next_condition","")])
mut=[]
for path,val in [(('claim_id',),'K1739'),(('bridge_census','row_count'),439),
 (('bridge_census','satisfied_count'),360),(('bridge_census','missing_count'),3),
 (('bridge_census','new_satisfied_rows'),['K1740']),(('protected_state','source_claims'),'proved'),
 (('protected_state','canon_change'),True),(('protected_state','public_posture_change'),True),
 (('decision','complete_local_branch_identified'),True),
 (('decision','exact_finite_strength_optimizer_identified'),True)]:
 x=copy.deepcopy(d);cur=x
 for k in path[:-1]:cur=cur[k]
 cur[path[-1]]=val;mut.append(x)
assert accepts(d)
for i,x in enumerate(mut,1):assert not accepts(x),i;print(f"PASS {i:02d}: rejected hostile mutation")
print(f"RESULT: PASS {len(mut)}/{len(mut)}")
