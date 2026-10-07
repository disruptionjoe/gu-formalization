#!/usr/bin/env python3
"""Independent hostile mutations for K1298."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1298-closed-range-gap-cohomology.json").read_text())
def valid(x):
    t=x["theorem"]; q=x["decision"]
    return ("delta=2 mu" in t["uniform_positive_gap"] and t["compact_resolvent"] and
            "D((1+L)^2)" in t["common_graph_domain"] and t["common_graph_domain_complete"] and
            t["differential_ranges_closed"] and t["cohomology_hausdorff"] and
            t["weyl_invariant_restriction_preserves_gap"] and t["weyl_invariant_cohomology_dimension"]==1 and
            not t["physical_pairing_supplied"] and q["k1145_positive_cohomology_gate_mathematically_satisfied"] and
            not q["native_i1b_candidate_admitted"])
mut=[(("theorem","uniform_positive_gap"),"delta=0"),(("theorem","compact_resolvent"),False),
     (("theorem","common_graph_domain"),"D(L)"),(("theorem","common_graph_domain_complete"),False),
     (("theorem","differential_ranges_closed"),False),(("theorem","cohomology_hausdorff"),False),
     (("theorem","weyl_invariant_cohomology_dimension"),0),(("theorem","physical_pairing_supplied"),True),
     (("decision","native_i1b_candidate_admitted"),True)]
assert valid(D)
for i,(path,value) in enumerate(mut,1):
    x=copy.deepcopy(D); x[path[0]][path[1]]=value; assert not valid(x); print(f"REJECT {i:02d}: {'.'.join(path)}")
print("RESULT: PASS rejected 9/9 hostile mutations")
