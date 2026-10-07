#!/usr/bin/env python3
"""Data-mutation probe for K1353."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1353-finite-source-fibre-principal-series-map-obstruction.json").read_text())
def validate(x):
 t,q=x["finite_fibre_theorem"],x["decision"]; e=[]
 if "finite-dimensional" not in t["domain"]: e.append("domain")
 if "infinite-dimensional irreducible" not in t["codomain"]: e.append("codomain")
 if "either zero or all" not in t["irreducibility_step"]: e.append("irreducibility")
 if "T=0" not in t["conclusion"]: e.append("conclusion")
 if q["nonzero_pointwise_finite_fibre_linear_equivariant_map_exists"]: e.append("map overclaim")
 if q["section_space_or_nonlocal_bridge_excluded"]: e.append("section overreach")
 if q["nonlinear_bridge_excluded"]: e.append("nonlinear overreach")
 if q["symmetry_reduced_bridge_excluded"]: e.append("reduction overreach")
 if q["source_action_bridge_constructed"]: e.append("source overclaim")
 return e
assert not validate(D),validate(D)
mutations=[
 ("domain",lambda x:x["finite_fibre_theorem"].__setitem__("domain","arbitrary domain")),
 ("codomain",lambda x:x["finite_fibre_theorem"].__setitem__("codomain","finite reducible codomain")),
 ("irreducibility",lambda x:x["finite_fibre_theorem"].__setitem__("irreducibility_step","unknown")),
 ("conclusion",lambda x:x["finite_fibre_theorem"].__setitem__("conclusion","T may be nonzero")),
 ("map overclaim",lambda x:x["decision"].__setitem__("nonzero_pointwise_finite_fibre_linear_equivariant_map_exists",True)),
 ("section overreach",lambda x:x["decision"].__setitem__("section_space_or_nonlocal_bridge_excluded",True)),
 ("nonlinear overreach",lambda x:x["decision"].__setitem__("nonlinear_bridge_excluded",True)),
 ("reduction overreach",lambda x:x["decision"].__setitem__("symmetry_reduced_bridge_excluded",True)),
 ("source overclaim",lambda x:x["decision"].__setitem__("source_action_bridge_constructed",True)),
]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D); mutate(x); errors=validate(x); assert errors,label; print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 9/9")
