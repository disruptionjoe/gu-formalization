#!/usr/bin/env python3
"""Independent hostile mutations for K1302."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1302-regular-shifted-reduction.json").read_text())
def valid(x):
    t=x["theorem"]; q=x["decision"]
    return (t["constraint_surface_dimension"]==175 and t["reduced_dimension"]==84 and
            t["quotient_is_diffeomorphic_to"]=="O_mu" and t["quotient_map_well_defined"] and
            t["quotient_map_bijective"] and t["quotient_smooth"] and t["reduced_form_nondegenerate"] and
            not t["seven_invariant_values_derived"] and q["shifting_changes_presentation_not_physical_selection"] and
            not q["regular_charge_orbit_selected_by_source"])
mut=[(("theorem","constraint_surface_dimension"),84),(("theorem","reduced_dimension"),0),
     (("theorem","quotient_is_diffeomorphic_to"),"point"),(("theorem","quotient_map_well_defined"),False),
     (("theorem","quotient_map_bijective"),False),(("theorem","quotient_smooth"),False),
     (("theorem","seven_invariant_values_derived"),True),(("decision","regular_charge_orbit_selected_by_source"),True)]
assert valid(D)
for i,(path,value) in enumerate(mut,1):
    x=copy.deepcopy(D); x[path[0]][path[1]]=value; assert not valid(x); print(f"REJECT {i:02d}: {'.'.join(path)}")
print("RESULT: PASS rejected 8/8 hostile mutations")
