#!/usr/bin/env python3
"""Data-mutation probe for K1385."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1385-finite-lp-admission-boundary.json").read_text())
def validate(x):
 b,q=x["bridge_census"],x["decision"];e=[]
 if b["row_count"]!=b["satisfied_count"]+b["conditional_count"]+b["excluded_count"]+b["missing_count"]:e.append("sum")
 if b["row_count"]!=57:e.append("rows")
 if len(b["new_satisfied_rows"])!=2:e.append("satisfied delta")
 if len(b["new_conditional_rows"])!=1:e.append("conditional delta")
 if len(b["new_excluded_rows"])!=1:e.append("excluded delta")
 if b["missing_count"]!=4:e.append("missing")
 if not q["sharp_finite_p_boundary_constructed"]:e.append("boundary")
 if not q["diagonal_obstruction_constructed"]:e.append("obstruction")
 if q["global_null_form_or_weighted_hierarchy_constructed"]:e.append("global overclaim")
 if q["source_selected_reduction_constructed"]:e.append("source overclaim")
 return e
assert not validate(D),validate(D)
mutations=[("sum",lambda x:x["bridge_census"].__setitem__("satisfied_count",37)),("rows",lambda x:x["bridge_census"].__setitem__("row_count",58)),("satisfied delta",lambda x:x["bridge_census"].__setitem__("new_satisfied_rows",[])),("conditional delta",lambda x:x["bridge_census"].__setitem__("new_conditional_rows",[])),("excluded delta",lambda x:x["bridge_census"].__setitem__("new_excluded_rows",[])),("missing",lambda x:x["bridge_census"].__setitem__("missing_count",3)),("boundary",lambda x:x["decision"].__setitem__("sharp_finite_p_boundary_constructed",False)),("obstruction",lambda x:x["decision"].__setitem__("diagonal_obstruction_constructed",False)),("global overclaim",lambda x:x["decision"].__setitem__("global_null_form_or_weighted_hierarchy_constructed",True)),("source overclaim",lambda x:x["decision"].__setitem__("source_selected_reduction_constructed",True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);errors=validate(x);assert errors,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 10/10")
