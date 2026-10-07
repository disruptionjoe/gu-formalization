#!/usr/bin/env python3
"""Independent hostile mutations for K1324."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1324-canonical-d7-sign-normalization.json").read_text())
def valid(x):
 a=x["algorithm"]; k=x["k1319_replay"]; q=x["decision"]; return a["root"]==1 and a["root_sign"]==1 and len(a["edge_order"])==6 and a["deterministic"] and a["already_exact_input_is_fixed"] and k["defect"]==-1 and k["normalizing_signs"]==[1,1,1,1,1,-1,1] and k["all_normalized_edge_defects"]==[1]*6 and q["finite_sign_normalization_constructed"] and not q["analytic_operator_normalization_constructed"]
mut=[(("algorithm","root"),2),(("algorithm","root_sign"),-1),(("algorithm","edge_order"),[[1,2]]),(("algorithm","deterministic"),False),(("algorithm","already_exact_input_is_fixed"),False),(("k1319_replay","defect"),1),(("k1319_replay","normalizing_signs"),[1]*7),(("k1319_replay","all_normalized_edge_defects"),[-1]*6),(("decision","analytic_operator_normalization_constructed"),True)]
for i,(path,value) in enumerate(mut,1):
 x=copy.deepcopy(D); x[path[0]][path[1]]=value; assert not valid(x),path; print(f"REJECT {i:02d}: {path[1]}")
assert valid(D); print("RESULT: PASS 9/9 hostile mutations rejected")
