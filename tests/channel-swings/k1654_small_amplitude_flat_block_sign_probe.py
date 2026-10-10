#!/usr/bin/env python3
"""Hostile mutations for K1654."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def valid(d):
 q,z=d.get("sign_classification",{}),d.get("decision",{})
 return all([d.get("claim_id")=="K1654","eta N^4" in q.get("positive_lower",""),"eta^2 N^4" in q.get("negative_upper",""),"a_0^2c_0/(6gc_1^2)" in q.get("threshold",""),"sufficiently small fixed amplitudes" in q.get("scope_guard",""),z.get("small_amplitude_leading_gap_positive") is True,z.get("all_admissible_amplitudes_classified") is False,z.get("unrestricted_coefficient_identified") is False,z.get("protected_status_change") is False])
def main():
 s=json.loads((ROOT/"lab/process/k1654-small-amplitude-flat-block-sign.json").read_text());assert valid(s)
 changes=[(("claim_id",),"K1648"),(("sign_classification","positive_lower"),"eta^2"),(("sign_classification","negative_upper"),"eta"),(("sign_classification","threshold"),"all eta"),(("sign_classification","scope_guard"),"unrestricted"),(("decision","small_amplitude_leading_gap_positive"),False),(("decision","all_admissible_amplitudes_classified"),True),(("decision","unrestricted_coefficient_identified"),True),(("decision","protected_status_change"),True)]
 for i,(path,value) in enumerate(changes,1):
  m=copy.deepcopy(s);cur=m
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(m),i;print(f"REJECT {i:02d}: hostile mutation")
 print(f"RESULT: REJECTED {len(changes)}/{len(changes)}")
if __name__=="__main__":main()
