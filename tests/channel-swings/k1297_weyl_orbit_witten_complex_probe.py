#!/usr/bin/env python3
"""Independent hostile mutations for K1297."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1297-weyl-orbit-witten-complex.json").read_text())
def valid(x):
    c=x["construction"]; t=x["theorem"]; q=x["decision"]
    return (c["nilpotent"] and c["closed_extension"] and c["equivariant"] and
            t["full_degree_zero_cohomology_dimension"]==322560 and t["full_positive_degree_cohomology_dimension"]==0 and
            t["weyl_invariant_degree_zero_cohomology_dimension"]==1 and not t["source_bv_bfv_complex"] and
            q["positive_nonzero_invariant_cohomology_constructed_conditionally"] and not q["physical_cohomology_identified"])
mut=[(("construction","nilpotent"),False),(("construction","closed_extension"),False),
     (("construction","equivariant"),False),(("theorem","full_degree_zero_cohomology_dimension"),1),
     (("theorem","full_positive_degree_cohomology_dimension"),1),(("theorem","weyl_invariant_degree_zero_cohomology_dimension"),0),
     (("theorem","source_bv_bfv_complex"),True),(("decision","physical_cohomology_identified"),True)]
assert valid(D)
for i,(path,value) in enumerate(mut,1):
    x=copy.deepcopy(D); x[path[0]][path[1]]=value; assert not valid(x); print(f"REJECT {i:02d}: {'.'.join(path)}")
print("RESULT: PASS rejected 8/8 hostile mutations")
