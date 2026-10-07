#!/usr/bin/env python3
"""Independent hostile mutations for K1322."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1322-d7-tree-braid-sign-trivialization.json").read_text())
def valid(x):
 g=x["graph"]; t=x["theorem"]; q=x["decision"]; return g["type"]=="D7" and g["connected"] and g["acyclic"] and len(g["edges"])==6 and t["defect_assignment_count"]==64 and t["every_edge_sign_assignment_is_a_vertex_coboundary"] and t["solutions_per_assignment"]==2 and t["uniqueness_modulo_global_sign"] and not q["k1319_displayed_minus_one_is_intrinsic_D7_holonomy"] and not q["non_sign_or_analytic_obstruction_excluded"]
mut=[(("graph","type"),"A7"),(("graph","connected"),False),(("graph","acyclic"),False),(("graph","edges"),[[1,2]]),(("theorem","defect_assignment_count"),32),(("theorem","every_edge_sign_assignment_is_a_vertex_coboundary"),False),(("theorem","solutions_per_assignment"),1),(("decision","k1319_displayed_minus_one_is_intrinsic_D7_holonomy"),True),(("decision","non_sign_or_analytic_obstruction_excluded"),True)]
for i,(path,value) in enumerate(mut,1):
 x=copy.deepcopy(D); x[path[0]][path[1]]=value; assert not valid(x),path; print(f"REJECT {i:02d}: {path[1]}")
assert valid(D); print("RESULT: PASS 9/9 hostile mutations rejected")
