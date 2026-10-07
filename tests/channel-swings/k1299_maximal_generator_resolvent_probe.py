#!/usr/bin/env python3
"""Independent hostile mutations for K1299."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1299-maximal-generator-resolvent.json").read_text())
def valid(x):
    t=x["theorem"]; q=x["decision"]
    return (t["skew_adjoint"] and t["maximal"] and "exp(-i t L)" in t["unitary_group"] and
            t["preserves_common_spectral_domains"] and t["commutes_with_differential"] and
            "1/|Re z|" in t["resolvent_bound"] and t["boundaryless_trace_compatibility"] and
            not t["hyperbolic_causal_green_operator"] and q["k1149_maximal_generator_gate_mathematically_satisfied"] and
            not q["source_boundary_law_supplied"])
mut=[(("theorem","skew_adjoint"),False),(("theorem","maximal"),False),
     (("theorem","unitary_group"),"none"),(("theorem","preserves_common_spectral_domains"),False),
     (("theorem","commutes_with_differential"),False),(("theorem","resolvent_bound"),"unbounded"),
     (("theorem","hyperbolic_causal_green_operator"),True),(("decision","source_boundary_law_supplied"),True)]
assert valid(D)
for i,(path,value) in enumerate(mut,1):
    x=copy.deepcopy(D); x[path[0]][path[1]]=value; assert not valid(x); print(f"REJECT {i:02d}: {'.'.join(path)}")
print("RESULT: PASS rejected 8/8 hostile mutations")
