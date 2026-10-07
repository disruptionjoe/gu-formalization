#!/usr/bin/env python3
"""Independent hostile mutations for K1330."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1330-spherical-intertwiner-admission-boundary.json").read_text())
def valid(x):
 c=x["certificate"]; q=x["decision"]; return c["row_count"]==20 and sum(c[k] for k in ("satisfied_count","excluded_count","conditional_count","missing_count"))==20 and c["satisfied_count"]==9 and c["conditional_count"]==2 and c["missing_count"]==6 and q["spherical_line_D7_coxeter_flat"] and not q["full_analytic_normalized_intertwiner_family_constructed"] and not q["G_equivariant_full_chamber_descent_constructed"] and not q["canonical_or_source_selected_chamber_constructed"] and not q["positive_physical_pairing_constructed"] and not q["protected_status_change"]
mut=[(("certificate","row_count"),19),(("certificate","satisfied_count"),8),(("certificate","conditional_count"),1),(("certificate","missing_count"),5),(("decision","spherical_line_D7_coxeter_flat"),False),(("decision","full_analytic_normalized_intertwiner_family_constructed"),True),(("decision","G_equivariant_full_chamber_descent_constructed"),True),(("decision","canonical_or_source_selected_chamber_constructed"),True),(("decision","protected_status_change"),True)]
for i,(path,value) in enumerate(mut,1):
 x=copy.deepcopy(D); x[path[0]][path[1]]=value; assert not valid(x),path; print(f"REJECT {i:02d}: {path[1]}")
assert valid(D); print("RESULT: PASS 9/9 hostile mutations rejected")
