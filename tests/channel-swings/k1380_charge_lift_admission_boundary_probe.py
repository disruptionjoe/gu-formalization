#!/usr/bin/env python3
"""Data-mutation probe for K1380."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1380-charge-lift-admission-boundary.json").read_text())
def validate(x):
 b,q=x["bridge_census"],x["decision"];e=[]
 if b["row_count"]!=b["satisfied_count"]+b["conditional_count"]+b["excluded_count"]+b["missing_count"]:e.append("sum")
 if b["row_count"]!=53:e.append("rows")
 if len(b["new_satisfied_rows"])!=1:e.append("satisfied delta")
 if len(b["new_conditional_rows"])!=1:e.append("conditional delta")
 if len(b["new_excluded_rows"])!=2:e.append("excluded delta")
 if b["missing_count"]!=4:e.append("missing")
 if not q["free_invariant_charge_lift_constructed"]:e.append("free lift")
 if not q["one_sided_k1372_phase_space_rejected"]:e.append("one-sided")
 if q["base_energy_global_closure_constructed"]:e.append("global overclaim")
 if q["source_selected_reduction_constructed"]:e.append("source overclaim")
 return e
assert not validate(D),validate(D)
mutations=[("sum",lambda x:x["bridge_census"].__setitem__("satisfied_count",35)),("rows",lambda x:x["bridge_census"].__setitem__("row_count",54)),("satisfied delta",lambda x:x["bridge_census"].__setitem__("new_satisfied_rows",[])),("conditional delta",lambda x:x["bridge_census"].__setitem__("new_conditional_rows",[])),("excluded delta",lambda x:x["bridge_census"].__setitem__("new_excluded_rows",[])),("missing",lambda x:x["bridge_census"].__setitem__("missing_count",3)),("free lift",lambda x:x["decision"].__setitem__("free_invariant_charge_lift_constructed",False)),("one-sided",lambda x:x["decision"].__setitem__("one_sided_k1372_phase_space_rejected",False)),("global overclaim",lambda x:x["decision"].__setitem__("base_energy_global_closure_constructed",True)),("source overclaim",lambda x:x["decision"].__setitem__("source_selected_reduction_constructed",True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);errors=validate(x);assert errors,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 10/10")
