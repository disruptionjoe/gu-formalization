#!/usr/bin/env python3
"""Independent hostile mutations for K1294."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1294-realized-selector-transfer.json").read_text())
def valid(x):
    t=x["theorem"]; q=x["decision"]
    return ("K1291 polynomial" in t["feasibility_condition"] and "discriminant" in t["feasibility_condition"] and t["proper_on_Cartan"] and t["cartan_hessian_rank"]==7 and
            t["cartan_hessian_inertia"]==[7,0,0] and t["infeasible_target_zero_set_empty"] and
            t["imports_one_scale_and_six_shapes"] and not t["source_owned"] and not t["functional_BV_BFV_properness"] and
            q["realized_orbit_gap_for_feasible_finite_targets_closed"] and not q["all_formal_targets_transfer"])
mut=[(("theorem","feasibility_condition"),"every formal point"),(("theorem","proper_on_Cartan"),False),(("theorem","cartan_hessian_rank"),6),(("theorem","cartan_hessian_inertia"),[6,1,0]),(("theorem","infeasible_target_zero_set_empty"),False),(("theorem","imports_one_scale_and_six_shapes"),False),(("theorem","source_owned"),True),(("theorem","functional_BV_BFV_properness"),True),(("decision","all_formal_targets_transfer"),True)]
assert valid(D)
for i,(path,value) in enumerate(mut,1):
    x=copy.deepcopy(D); x[path[0]][path[1]]=value; assert not valid(x); print(f"REJECT {i:02d}: {'.'.join(path)}")
print("RESULT: PASS rejected 9/9 hostile mutations")
