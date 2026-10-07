#!/usr/bin/env python3
"""Data-mutation probe for K1375."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1375-nonlinear-gauss-admission-boundary.json").read_text())
def validate(x):
 b,q=x["bridge_census"],x["decision"];e=[]
 if b["row_count"]!=b["satisfied_count"]+b["conditional_count"]+b["excluded_count"]+b["missing_count"]:e.append("sum")
 if b["row_count"]!=49:e.append("rows")
 if len(b["new_satisfied_rows"])!=3:e.append("satisfied delta")
 if len(b["new_excluded_rows"])!=1:e.append("excluded delta")
 if b["missing_count"]!=4:e.append("missing")
 if not q["gauss_functional_layer_closed"]:e.append("Gauss layer")
 if q["original_energy_sufficient"]:e.append("energy overclaim")
 if q["global_mixed_graph_estimate_constructed"]:e.append("global overclaim")
 if q["fully_coupled_global_nonlinear_BV_BFV_domain_constructed"]:e.append("BV overclaim")
 if q["source_selected_reduction_constructed"]:e.append("source overclaim")
 return e
assert not validate(D),validate(D)
mutations=[
 ("sum",lambda x:x["bridge_census"].__setitem__("satisfied_count",34)),
 ("rows",lambda x:x["bridge_census"].__setitem__("row_count",50)),
 ("satisfied delta",lambda x:x["bridge_census"].__setitem__("new_satisfied_rows",[])),
 ("excluded delta",lambda x:x["bridge_census"].__setitem__("new_excluded_rows",[])),
 ("missing",lambda x:x["bridge_census"].__setitem__("missing_count",3)),
 ("Gauss layer",lambda x:x["decision"].__setitem__("gauss_functional_layer_closed",False)),
 ("energy overclaim",lambda x:x["decision"].__setitem__("original_energy_sufficient",True)),
 ("global overclaim",lambda x:x["decision"].__setitem__("global_mixed_graph_estimate_constructed",True)),
 ("BV overclaim",lambda x:x["decision"].__setitem__("fully_coupled_global_nonlinear_BV_BFV_domain_constructed",True)),
 ("source overclaim",lambda x:x["decision"].__setitem__("source_selected_reduction_constructed",True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);errors=validate(x);assert errors,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 10/10")
