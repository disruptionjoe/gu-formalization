#!/usr/bin/env python3
"""Hostile mutations for K1655."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def valid(d):
 q,z=d.get("admission",{}),d.get("decision",{})
 return all([d.get("claim_id")=="K1655","O_(g,eta)(N^3)" in q.get("quantum_result",""),"larger admissible amplitudes" in q.get("remaining_quantum_gate",""),"0/7" in q.get("physical_admission",""),"370 rows" in q.get("bridge_census",""),"SC-ACT-01/02/06 remain ASSERTS" in q.get("protected_state",""),"Do not promote" in q.get("scope_guard",""),z.get("larger_amplitude_family_open") is True,z.get("unrestricted_coefficient_open") is True,z.get("source_status_changed") is False,z.get("physics_ledger_changed") is False,z.get("canon_or_public_status_changed") is False])
def main():
 s=json.loads((ROOT/"lab/process/k1655-score-saturation-admission.json").read_text());assert valid(s)
 changes=[(("claim_id",),"K1654"),(("admission","quantum_result"),"exact zero"),(("admission","remaining_quantum_gate"),"closed"),(("admission","physical_admission"),"7/7"),(("admission","bridge_census"),"365 rows"),(("admission","protected_state"),"resolved"),(("admission","scope_guard"),"promote"),(("decision","larger_amplitude_family_open"),False),(("decision","unrestricted_coefficient_open"),False),(("decision","source_status_changed"),True),(("decision","physics_ledger_changed"),True),(("decision","canon_or_public_status_changed"),True)]
 for i,(path,value) in enumerate(changes,1):
  m=copy.deepcopy(s);cur=m
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(m),i;print(f"REJECT {i:02d}: hostile mutation")
 print(f"RESULT: REJECTED {len(changes)}/{len(changes)}")
if __name__=="__main__":main()
