#!/usr/bin/env python3
"""Independent hostile mutations for K1312."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1312-minimal-parabolic-polarized-sections.json").read_text())
def valid(x):
 c=x["construction"]; q=x["decision"]; return c["positive_root_count"]==42 and c["nilradical_dimension"]==42 and c["split_rank"]==7 and c["parabolic_dimension"]==49 and c["flag_dimension"]==42 and c["rho_vector_standard_chamber"]==[6,5,4,3,2,1,0] and c["half_density_correction_included"] and q["normalized_induced_control_constructed"] and not q["polarized_BFV_cohomology_constructed"] and not q["source_or_physical_status_moves"]
mut=[(("construction","positive_root_count"),49),(("construction","nilradical_dimension"),41),(("construction","split_rank"),6),(("construction","parabolic_dimension"),56),(("construction","flag_dimension"),35),(("construction","rho_vector_standard_chamber"),[7,6,5,4,3,2,1]),(("construction","half_density_correction_included"),False),(("decision","polarized_BFV_cohomology_constructed"),True),(("decision","source_or_physical_status_moves"),True)]
assert valid(D)
for i,(p,v) in enumerate(mut,1): x=copy.deepcopy(D); x[p[0]][p[1]]=v; assert not valid(x); print(f"REJECT {i:02d}: {'.'.join(p)}")
print("RESULT: PASS rejected 9/9 hostile mutations")
