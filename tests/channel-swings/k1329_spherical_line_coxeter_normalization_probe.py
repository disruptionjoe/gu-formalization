#!/usr/bin/env python3
"""Independent hostile mutations for K1329."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1329-spherical-line-coxeter-normalization.json").read_text())
def valid(x):
 t=x["normalized_transport"]; c=x["coxeter_relations"]; k=x["comparison_with_k1325"]; q=x["decision"]; return t["fiber_count"]==322560 and t["fiber_dimension"]==1 and t["basis_action"]=="R_i(lambda)v_lambda=v_s_i_lambda" and c["scalar_relator_defect"]==1 and c["adjacent_braid"].startswith("R_i R_j R_i=R_j R_i R_j") and k["arbitrary_nonzero_meromorphic_scalar_defects_on_spherical_line_normalized"] and not k["nonspherical_k_type_defects_classified"] and q["spherical_line_coxeter_flat"] and not q["full_principal_series_G_intertwiner_family_constructed"]
mut=[(("normalized_transport","fiber_count"),1),(("normalized_transport","fiber_dimension"),2),(("normalized_transport","basis_action"),"0"),(("coxeter_relations","scalar_relator_defect"),-1),(("coxeter_relations","adjacent_braid"),"projective"),(("comparison_with_k1325","arbitrary_nonzero_meromorphic_scalar_defects_on_spherical_line_normalized"),False),(("comparison_with_k1325","nonspherical_k_type_defects_classified"),True),(("decision","full_principal_series_G_intertwiner_family_constructed"),True)]
for i,(path,value) in enumerate(mut,1):
 x=copy.deepcopy(D); x[path[0]][path[1]]=value; assert not valid(x),path; print(f"REJECT {i:02d}: {path[1]}")
assert valid(D); print("RESULT: PASS 8/8 hostile mutations rejected")
