#!/usr/bin/env python3
"""Mutation probe for K1408."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1408-spectral-core-admission-boundary.json").read_text())
def validate(x):
 c,q=x["bridge_census"],x["decision"];e=[]
 if sum(c[k] for k in ("satisfied_count","conditional_count","excluded_count","missing_count"))!=c["row_count"]:e.append("census")
 if len(c["new_satisfied_rows"])!=4:e.append("satisfied rows")
 if len(c["new_excluded_rows"])!=1:e.append("excluded rows")
 if len(c["missing_rows"])!=4:e.append("missing rows")
 for key in ("charge_spectral_support_invariant","spectral_noether_measure_constructed","global_dense_finite_charge_core_constructed","nonconstant_quadratic_spectral_weight_conservation_route_excluded"):
  if not q[key]:e.append(key)
 for key in ("completed_unbounded_charge_global_flow_constructed","positive_gu_physical_hilbert_cohomology_constructed","source_selected_reduction_constructed","protected_status_change"):
  if q[key]:e.append(key)
 if "SOURCE_REGISTER_UNCHANGED" not in x["source_and_ledger_effect"]:e.append("source")
 return e
assert not validate(D)
mutations=[("census",lambda x:x["bridge_census"].__setitem__("row_count",77)),("satisfied rows",lambda x:x["bridge_census"]["new_satisfied_rows"].pop()),("excluded rows",lambda x:x["bridge_census"]["new_excluded_rows"].clear()),("missing rows",lambda x:x["bridge_census"]["missing_rows"].pop()),("support",lambda x:x["decision"].__setitem__("charge_spectral_support_invariant",False)),("measure",lambda x:x["decision"].__setitem__("spectral_noether_measure_constructed",False)),("core",lambda x:x["decision"].__setitem__("global_dense_finite_charge_core_constructed",False)),("global overclaim",lambda x:x["decision"].__setitem__("completed_unbounded_charge_global_flow_constructed",True)),("physical overclaim",lambda x:x["decision"].__setitem__("positive_gu_physical_hilbert_cohomology_constructed",True)),("source",lambda x:x.__setitem__("source_and_ledger_effect","changed"))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);errors=validate(x);assert errors,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 10/10")
