#!/usr/bin/env python3
"""Hostile protected-state promotion mutations for K1735."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def valid(d):
 c=d.get("bridge_census",{});p=d.get("protected_state",{});z=d.get("decision",{})
 return all([d.get("claim_id")=="K1735",c.get("row_count")==435,c.get("satisfied_count")==356,
  "ASSERTS" in p.get("source_claims",""),"UNCERTAIN" in p.get("source_claims",""),p.get("canon_change") is False,
  p.get("public_posture_change") is False,z.get("exact_finite_strength_optimizer_identified") is False,
  z.get("unrestricted_stationary_lower_bound_proved") is False,z.get("source_owned_physical_theory") is False,z.get("protected_status_change") is False])
def main():
 d=json.loads((ROOT/"lab/process/k1735-four-point-finite-strength-admission.json").read_text());assert valid(d);m=[]
 for path,val in [(('claim_id',),'bad'),(('bridge_census','row_count'),434),(('bridge_census','satisfied_count'),355),
                  (('protected_state','source_claims'),'proved'),(('protected_state','canon_change'),True),
                  (('protected_state','public_posture_change'),True),(('decision','exact_finite_strength_optimizer_identified'),True),
                  (('decision','unrestricted_stationary_lower_bound_proved'),True),(('decision','source_owned_physical_theory'),True),
                  (('decision','protected_status_change'),True)]:
  x=copy.deepcopy(d);c=x
  for k in path[:-1]:c=c[k]
  c[path[-1]]=val;m.append(x)
 for i,x in enumerate(m,1):assert not valid(x);print(f"REJECT {i:02d}")
 print(f"RESULT: PASS {len(m)}/{len(m)} hostile mutations rejected")
if __name__=="__main__":main()
