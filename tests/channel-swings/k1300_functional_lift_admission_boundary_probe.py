#!/usr/bin/env python3
"""Independent hostile mutations for K1300."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1300-functional-lift-admission-boundary.json").read_text())
def valid(x):
    a=x["k1145_control_replay"]; b=x["k1150_control_replay"]; i=x["integrated_k1295_boundary"]; q=x["decision"]
    return (a["mathematical_rows_satisfied"]==3 and a["native_candidate_pass_count"]==0 and
            b["mathematical_rows_satisfied"]==4 and b["mathematical_rows_conditional"]==1 and b["native_candidate_pass_count"]==0 and
            (i["satisfied_count"],i["excluded_count"],i["conditional_count"],i["missing_count"])==(19,6,7,3) and
            q["functional_gate_joint_feasibility_demonstrated"] and not q["source_selected_functional_packet_constructed"] and
            not q["physical_bv_bfv_cohomology_constructed"] and not q["hyperbolic_causal_green_constructed"] and
            not q["protected_status_change"])
mut=[(("k1145_control_replay","native_candidate_pass_count"),1),(("k1150_control_replay","mathematical_rows_satisfied"),7),
     (("k1150_control_replay","native_candidate_pass_count"),1),(("integrated_k1295_boundary","conditional_count"),4),
     (("integrated_k1295_boundary","missing_count"),0),(("decision","source_selected_functional_packet_constructed"),True),
     (("decision","physical_bv_bfv_cohomology_constructed"),True),(("decision","hyperbolic_causal_green_constructed"),True),
     (("decision","protected_status_change"),True)]
assert valid(D)
for i,(path,value) in enumerate(mut,1):
    x=copy.deepcopy(D); x[path[0]][path[1]]=value; assert not valid(x); print(f"REJECT {i:02d}: {'.'.join(path)}")
print("RESULT: PASS rejected 9/9 hostile mutations")
