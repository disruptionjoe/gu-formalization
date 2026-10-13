#!/usr/bin/env python3
"""Hostile protected-state and grade mutations for K1745."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];d=json.loads((ROOT/"lab/process/k1745-four-point-branch-admission.json").read_text())
def accepts(x):
 c=x.get("bridge_census",{});p=x.get("protected_state",{});z=x.get("decision",{})
 return all([x.get("claim_id")=="K1745",c.get("row_count")==445,c.get("satisfied_count")==366,c.get("missing_count")==4,
  c.get("new_satisfied_rows")==["K1741","K1742","K1743","K1744","K1745"],"ASSERTS" in p.get("source_claims",""),
  "UNCERTAIN" in p.get("source_claims",""),not p.get("canon_change",True),not p.get("public_posture_change",True),
  z.get("unique_second_order_chart_jet_proved",False),not z.get("complete_local_branch_identified",True),
  not z.get("finite_strength_fisher_interval_proved",True),not z.get("global_two_radius_optimizer_identified",True),
  "third-order chart freedom" in x.get("next_condition","") and "Arb backend" in x.get("next_condition","")])
mut=[]
for path,val in [(('claim_id',),'K1744'),(('bridge_census','row_count'),444),(('bridge_census','satisfied_count'),365),
 (('bridge_census','missing_count'),3),(('bridge_census','new_satisfied_rows'),['K1745']),(('protected_state','source_claims'),'proved'),
 (('protected_state','canon_change'),True),(('protected_state','public_posture_change'),True),
 (('decision','unique_second_order_chart_jet_proved'),False),(('decision','complete_local_branch_identified'),True),
 (('decision','finite_strength_fisher_interval_proved'),True),(('decision','global_two_radius_optimizer_identified'),True)]:
 x=copy.deepcopy(d);cur=x
 for k in path[:-1]:cur=cur[k]
 cur[path[-1]]=val;mut.append(x)
assert accepts(d)
for i,x in enumerate(mut,1):assert not accepts(x),i;print(f"PASS {i:02d}: rejected hostile mutation")
print(f"RESULT: PASS {len(mut)}/{len(mut)}")
