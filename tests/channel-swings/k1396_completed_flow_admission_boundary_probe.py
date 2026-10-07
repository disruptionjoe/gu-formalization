#!/usr/bin/env python3
"""Data-mutation probe for K1396."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1396-completed-flow-admission-boundary.json").read_text())
def validate(x):
 b,q=x["bridge_census"],x["decision"];e=[]
 if b["row_count"]!=b["satisfied_count"]+b["conditional_count"]+b["excluded_count"]+b["missing_count"]:e.append("census")
 if (b["row_count"],b["satisfied_count"],b["conditional_count"],b["excluded_count"],b["missing_count"])!=(66,44,6,12,4):e.append("counts")
 if len(b["new_satisfied_rows"])!=4 or len(b["new_excluded_rows"])!=1:e.append("new rows")
 for key in ("completed_triangular_local_flow_constructed","completed_flow_unique_and_constraint_preserving","admissible_gauge_continuation_invariant","global_coefficient_integrability_target_excluded_on_T3"):
  if not q[key]:e.append(key)
 for key in ("global_large_data_propagation_constructed","fully_coupled_global_nonlinear_BV_BFV_domain_constructed","source_selected_reduction_constructed","positive_GU_physical_Hilbert_cohomology_constructed","protected_status_change"):
  if q[key]:e.append(key)
 return e
assert not validate(D),validate(D)
mutations=[("census",lambda x:x["bridge_census"].__setitem__("row_count",65)),("counts",lambda x:x["bridge_census"].__setitem__("satisfied_count",45)),("new rows",lambda x:x["bridge_census"].__setitem__("new_satisfied_rows",[])),("flow",lambda x:x["decision"].__setitem__("completed_triangular_local_flow_constructed",False)),("constraint",lambda x:x["decision"].__setitem__("completed_flow_unique_and_constraint_preserving",False)),("gauge",lambda x:x["decision"].__setitem__("admissible_gauge_continuation_invariant",False)),("obstruction",lambda x:x["decision"].__setitem__("global_coefficient_integrability_target_excluded_on_T3",False)),("global overclaim",lambda x:x["decision"].__setitem__("global_large_data_propagation_constructed",True)),("BV overclaim",lambda x:x["decision"].__setitem__("fully_coupled_global_nonlinear_BV_BFV_domain_constructed",True)),("source overclaim",lambda x:x["decision"].__setitem__("source_selected_reduction_constructed",True)),("cohomology overclaim",lambda x:x["decision"].__setitem__("positive_GU_physical_Hilbert_cohomology_constructed",True)),("protected overclaim",lambda x:x["decision"].__setitem__("protected_status_change",True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);errors=validate(x);assert errors,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 12/12")
