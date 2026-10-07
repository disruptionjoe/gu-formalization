#!/usr/bin/env python3
"""Independent hostile mutations for K1296."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1296-weyl-covariant-quadratic-model.json").read_text())
def valid(x):
    t=x["theorem"]; q=x["decision"]
    return (t["regular_orbit_size"]==322560 and t["base_hessian_positive_definite"] and
            "w B_o w^T" in t["transport_law"] and t["quadratic_hessian_equals_selector_hessian"] and
            t["all_orbit_models_isospectral"] and not t["finite_selector_equal_to_quadratic_model_globally"] and
            not t["source_owned"] and q["weyl_covariant_normal_family_exists"] and
            not q["physical_phase_space_identified"])
mut=[(("theorem","regular_orbit_size"),1),(("theorem","base_hessian_positive_definite"),False),
     (("theorem","transport_law"),"none"),(("theorem","quadratic_hessian_equals_selector_hessian"),False),
     (("theorem","all_orbit_models_isospectral"),False),(("theorem","finite_selector_equal_to_quadratic_model_globally"),True),
     (("theorem","source_owned"),True),(("decision","physical_phase_space_identified"),True)]
assert valid(D)
for i,(path,value) in enumerate(mut,1):
    x=copy.deepcopy(D); x[path[0]][path[1]]=value; assert not valid(x); print(f"REJECT {i:02d}: {'.'.join(path)}")
print("RESULT: PASS rejected 8/8 hostile mutations")
