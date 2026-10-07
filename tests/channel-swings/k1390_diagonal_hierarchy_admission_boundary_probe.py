#!/usr/bin/env python3
"""Data-mutation probe for K1390."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1390-diagonal-hierarchy-admission-boundary.json").read_text())
def validate(x):
 b,q=x["bridge_census"],x["decision"];e=[]
 if b["row_count"]!=b["satisfied_count"]+b["conditional_count"]+b["excluded_count"]+b["missing_count"]:e.append("sum")
 if b["row_count"]!=61:e.append("rows")
 if len(b["new_satisfied_rows"])!=4:e.append("satisfied delta")
 if b["missing_count"]!=4:e.append("missing")
 if not q["diagonal_covariant_hierarchy_constructed"]:e.append("hierarchy")
 if not q["differentiated_maxwell_source_closed"]:e.append("Maxwell")
 if not q["local_apriori_continuation_bound_constructed"]:e.append("local")
 if q["smooth_solution_existence_constructed"]:e.append("existence overclaim")
 if q["global_large_data_propagation_constructed"]:e.append("global overclaim")
 if q["source_selected_reduction_constructed"]:e.append("source overclaim")
 return e
assert not validate(D),validate(D)
mutations=[("sum",lambda x:x["bridge_census"].__setitem__("satisfied_count",41)),("rows",lambda x:x["bridge_census"].__setitem__("row_count",62)),("satisfied delta",lambda x:x["bridge_census"].__setitem__("new_satisfied_rows",[])),("missing",lambda x:x["bridge_census"].__setitem__("missing_count",3)),("hierarchy",lambda x:x["decision"].__setitem__("diagonal_covariant_hierarchy_constructed",False)),("Maxwell",lambda x:x["decision"].__setitem__("differentiated_maxwell_source_closed",False)),("local",lambda x:x["decision"].__setitem__("local_apriori_continuation_bound_constructed",False)),("existence overclaim",lambda x:x["decision"].__setitem__("smooth_solution_existence_constructed",True)),("global overclaim",lambda x:x["decision"].__setitem__("global_large_data_propagation_constructed",True)),("source overclaim",lambda x:x["decision"].__setitem__("source_selected_reduction_constructed",True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);errors=validate(x);assert errors,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 10/10")
