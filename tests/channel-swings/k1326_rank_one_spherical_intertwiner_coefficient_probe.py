#!/usr/bin/env python3
"""Independent hostile mutations for K1326."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1326-rank-one-spherical-intertwiner-coefficient.json").read_text())
def valid(x):
 r=x["rank_one_model"]; n=x["normalization"]; q=x["decision"]; return r["split_root_multiplicity"]==1 and r["double_root_multiplicity"]==0 and r["absolute_convergence_half_plane"]=="Re(z)>0" and r["beta_value"]=="B(1/2,z/2)" and r["coefficient"]=="m(z)=sqrt(pi)*Gamma(z/2)/Gamma((z+1)/2)" and n["normalized_spherical_action"]=="R_alpha(z)v_z=v_s_alpha_z" and q["rank_one_spherical_coefficient_constructed"] and not q["full_knapp_stein_operator_constructed"] and not q["physical_intertwiner_constructed"]
mut=[(("rank_one_model","split_root_multiplicity"),2),(("rank_one_model","double_root_multiplicity"),1),(("rank_one_model","absolute_convergence_half_plane"),"Re(z)>-1"),(("rank_one_model","beta_value"),"B(1,z)"),(("rank_one_model","coefficient"),"Gamma(z)"),(("normalization","normalized_spherical_action"),"0"),(("decision","full_knapp_stein_operator_constructed"),True),(("decision","physical_intertwiner_constructed"),True)]
for i,(path,value) in enumerate(mut,1):
 x=copy.deepcopy(D); x[path[0]][path[1]]=value; assert not valid(x),path; print(f"REJECT {i:02d}: {path[1]}")
assert valid(D); print("RESULT: PASS 8/8 hostile mutations rejected")
