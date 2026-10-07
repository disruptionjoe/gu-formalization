#!/usr/bin/env python3
"""Independent hostile mutations for K1325."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1325-braid-normalization-admission-boundary.json").read_text())
def valid(x):
 c=x["certificate"]; q=x["decision"]; return c["row_count"]==19 and c["satisfied_count"]==8 and c["excluded_count"]==3 and c["conditional_count"]==2 and c["missing_count"]==6 and not q["K1319_minus_one_phase_is_intrinsic_obstruction"] and q["sign_only_D7_braid_normalization_constructed"] and not q["analytic_normalized_intertwiner_family_constructed"] and not q["G_equivariant_chamber_descent_constructed"] and not q["protected_status_change"]
mut=[(("certificate","row_count"),18),(("certificate","satisfied_count"),7),(("certificate","excluded_count"),4),(("certificate","conditional_count"),1),(("certificate","missing_count"),5),(("decision","K1319_minus_one_phase_is_intrinsic_obstruction"),True),(("decision","sign_only_D7_braid_normalization_constructed"),False),(("decision","analytic_normalized_intertwiner_family_constructed"),True),(("decision","G_equivariant_chamber_descent_constructed"),True),(("decision","protected_status_change"),True)]
for i,(path,value) in enumerate(mut,1):
 x=copy.deepcopy(D); x[path[0]][path[1]]=value; assert not valid(x),path; print(f"REJECT {i:02d}: {path[1]}")
assert valid(D); print("RESULT: PASS 10/10 hostile mutations rejected")
