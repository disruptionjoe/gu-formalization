#!/usr/bin/env python3
"""Independent hostile mutations for K1301."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1301-nonzero-charge-shifting-parent.json").read_text())
def valid(x):
    c=x["construction"]; t=x["theorem"]; q=x["decision"]
    return (c["group_dimension"]==91 and c["charge_orbit_dimension"]==84 and c["parent_dimension"]==266 and
            t["vertical_cotangent_derivative_rank"]==91 and t["zero_is_regular_value"] and t["diagonal_action_free"] and
            t["constraint_surface_dimension"]==175 and t["expected_reduced_dimension"]==84 and
            not t["charge_parameter_selected_by_construction"] and not q["source_owned_boundary_law_constructed"])
mut=[(("construction","charge_orbit_dimension"),77),(("construction","parent_dimension"),182),
     (("theorem","vertical_cotangent_derivative_rank"),84),(("theorem","zero_is_regular_value"),False),
     (("theorem","diagonal_action_free"),False),(("theorem","constraint_surface_dimension"),266),
     (("theorem","expected_reduced_dimension"),0),(("theorem","charge_parameter_selected_by_construction"),True),
     (("decision","source_owned_boundary_law_constructed"),True)]
assert valid(D)
for i,(path,value) in enumerate(mut,1):
    x=copy.deepcopy(D); x[path[0]][path[1]]=value; assert not valid(x); print(f"REJECT {i:02d}: {'.'.join(path)}")
print("RESULT: PASS rejected 9/9 hostile mutations")
