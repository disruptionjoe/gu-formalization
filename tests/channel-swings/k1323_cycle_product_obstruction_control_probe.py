#!/usr/bin/env python3
"""Independent hostile mutations for K1323."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1323-cycle-product-obstruction-control.json").read_text())
def valid(x):
 t=x["triangle_control"]; q=x["decision"]; return t["assignment_count"]==8 and t["solvable_count"]==4 and t["one_negative_edge_product"]==-1 and not t["one_negative_edge_solvable"] and t["two_negative_edges_product"]==1 and t["two_negative_edges_solvable"] and q["cycle_sign_can_be_intrinsic_to_edge_rephasing_problem"] and not q["D7_simple_graph_has_cycle_obstruction"] and not q["arbitrary_projective_Coxeter_cocycle_classified"]
mut=[(("triangle_control","assignment_count"),4),(("triangle_control","solvable_count"),8),(("triangle_control","one_negative_edge_product"),1),(("triangle_control","one_negative_edge_solvable"),True),(("triangle_control","two_negative_edges_product"),-1),(("triangle_control","two_negative_edges_solvable"),False),(("decision","cycle_sign_can_be_intrinsic_to_edge_rephasing_problem"),False),(("decision","D7_simple_graph_has_cycle_obstruction"),True),(("decision","arbitrary_projective_Coxeter_cocycle_classified"),True)]
for i,(path,value) in enumerate(mut,1):
 x=copy.deepcopy(D); x[path[0]][path[1]]=value; assert not valid(x),path; print(f"REJECT {i:02d}: {path[1]}")
assert valid(D); print("RESULT: PASS 9/9 hostile mutations rejected")
