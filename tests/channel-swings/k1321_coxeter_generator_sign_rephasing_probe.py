#!/usr/bin/env python3
"""Independent hostile mutations for K1321."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1321-coxeter-generator-sign-rephasing.json").read_text())
def valid(x):
 r=x["rephasing_law"]; q=x["decision"]; return r["defect_values"]==[-1,1] and r["involutions_preserved"] and r["unitarity_preserved"] and r["nonadjacent_commutation_preserved"] and "epsilon_i epsilon_j = beta_ij"==r["exact_braid_condition"] and q["k1319_minus_one_defect_is_normalization_dependent"] and not q["every_projective_unitary_representation_is_trivialized"] and not q["analytic_intertwiner_existence_proved"]
mut=[(("rephasing_law","defect_values"),[1]),(("rephasing_law","involutions_preserved"),False),(("rephasing_law","unitarity_preserved"),False),(("rephasing_law","nonadjacent_commutation_preserved"),False),(("rephasing_law","exact_braid_condition"),"none"),(("decision","k1319_minus_one_defect_is_normalization_dependent"),False),(("decision","every_projective_unitary_representation_is_trivialized"),True),(("decision","analytic_intertwiner_existence_proved"),True)]
for i,(path,value) in enumerate(mut,1):
 x=copy.deepcopy(D); x[path[0]][path[1]]=value; assert not valid(x),path; print(f"REJECT {i:02d}: {path[1]}")
assert valid(D); print("RESULT: PASS 8/8 hostile mutations rejected")
