#!/usr/bin/env python3
"""Data-mutation probe for K1369."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1369-charge-regularized-linearized-brst-cohomology.json").read_text())
def validate(x):
 l,b,q=x["linearized_complex"],x["completion_boundary"],x["decision"]; e=[]
 if "s_lin A=d c" not in l["brst_differential"]:e.append("BRST differential")
 if "X_Q^1" not in l["matter_energy_space"]:e.append("graph energy")
 if "H_Maxwell_transverse direct_sum E_matter" not in l["cohomology"]:e.append("cohomology")
 if "Closed nonlinear range" not in b["nonlinear_missing"]:e.append("nonlinear boundary")
 if not q["closed_linearized_brst_complex_on_graph_domain"]:e.append("linear complex")
 if not q["positive_nonzero_linearized_cohomology"]:e.append("positivity")
 if q["nonlinear_KT_BV_BFV_properness"]:e.append("properness overclaim")
 if q["global_nonlinear_evolution"]:e.append("evolution overclaim")
 if q["gu_physical_hilbert_cohomology"]:e.append("physical overclaim")
 if q["source_observation_map_constructed"]:e.append("observation overclaim")
 return e
assert not validate(D),validate(D)
mutations=[
 ("BRST differential",lambda x:x["linearized_complex"].__setitem__("brst_differential","unknown")),
 ("graph energy",lambda x:x["linearized_complex"].__setitem__("matter_energy_space","ordinary H1")),
 ("cohomology",lambda x:x["linearized_complex"].__setitem__("cohomology","zero")),
 ("nonlinear boundary",lambda x:x["completion_boundary"].__setitem__("nonlinear_missing","none")),
 ("linear complex",lambda x:x["decision"].__setitem__("closed_linearized_brst_complex_on_graph_domain",False)),
 ("positivity",lambda x:x["decision"].__setitem__("positive_nonzero_linearized_cohomology",False)),
 ("properness overclaim",lambda x:x["decision"].__setitem__("nonlinear_KT_BV_BFV_properness",True)),
 ("evolution overclaim",lambda x:x["decision"].__setitem__("global_nonlinear_evolution",True)),
 ("physical overclaim",lambda x:x["decision"].__setitem__("gu_physical_hilbert_cohomology",True)),
 ("observation overclaim",lambda x:x["decision"].__setitem__("source_observation_map_constructed",True)),
]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);errors=validate(x);assert errors,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 10/10")
