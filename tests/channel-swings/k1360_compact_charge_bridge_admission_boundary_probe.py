#!/usr/bin/env python3
"""Data-mutation probe for K1360."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1360-compact-charge-bridge-admission-boundary.json").read_text())
def validate(x):
 c,q=x["bridge_census"],x["decision"];e=[]
 if c["row_count"]!=c["satisfied_count"]+c["conditional_count"]+c["excluded_count"]+c["missing_count"]:e.append("arithmetic")
 if len(c["new_satisfied_rows"])!=6:e.append("new rows")
 if len(c["missing_rows"])!=c["missing_count"]:e.append("missing length")
 if not any("source_owned_selection" in r for r in c["missing_rows"]):e.append("source missing")
 if not q["maximal_compact_route_mathematically_constructed"]:e.append("compact result")
 if not q["operator_charge_interacting_core_constructed"]:e.append("core result")
 if q["source_selected_reduction_constructed"]:e.append("source overclaim")
 if q["completed_global_nonlinear_domain_constructed"]:e.append("domain overclaim")
 if q["positive_physical_Hilbert_cohomology_constructed"]:e.append("cohomology overclaim")
 if q["protected_status_change"]:e.append("protected movement")
 return e
assert not validate(D),validate(D)
mutations=[
 ("arithmetic",lambda x:x["bridge_census"].__setitem__("row_count",36)),
 ("new rows",lambda x:x["bridge_census"]["new_satisfied_rows"].pop()),
 ("missing length",lambda x:x["bridge_census"]["missing_rows"].pop()),
 ("source missing",lambda x:x["bridge_census"]["missing_rows"].__setitem__(0,"resolved_source_selection")),
 ("compact result",lambda x:x["decision"].__setitem__("maximal_compact_route_mathematically_constructed",False)),
 ("core result",lambda x:x["decision"].__setitem__("operator_charge_interacting_core_constructed",False)),
 ("source overclaim",lambda x:x["decision"].__setitem__("source_selected_reduction_constructed",True)),
 ("domain overclaim",lambda x:x["decision"].__setitem__("completed_global_nonlinear_domain_constructed",True)),
 ("cohomology overclaim",lambda x:x["decision"].__setitem__("positive_physical_Hilbert_cohomology_constructed",True)),
 ("protected movement",lambda x:x["decision"].__setitem__("protected_status_change",True)),
]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);errors=validate(x);assert errors,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 10/10")
