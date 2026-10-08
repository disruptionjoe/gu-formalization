#!/usr/bin/env python3
"""Mutation probe for K1402."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1402-global-reduction-admission-boundary.json").read_text())
def validate(x):
 b,q=x["bridge_census"],x["decision"];e=[]
 if b["row_count"]!=b["satisfied_count"]+b["conditional_count"]+b["excluded_count"]+b["missing_count"]:e.append("census")
 if (b["row_count"],b["satisfied_count"],b["conditional_count"],b["excluded_count"],b["missing_count"])!=(71,48,6,13,4):e.append("counts")
 if len(b["new_satisfied_rows"])!=4 or len(b["new_excluded_rows"])!=1:e.append("new rows")
 for key in ("fixed_sector_global_large_data_evolution_constructed","closed_nonlinear_gauge_range_constructed","proper_classical_coulomb_quotient_constructed","fixed_sector_global_reduced_flow_constructed"):
  if not q[key]:e.append(key)
 for key in ("completed_unbounded_charge_global_flow_constructed","full_bv_bfv_boundary_theory_constructed","positive_gu_physical_hilbert_cohomology_constructed","source_selected_reduction_constructed","protected_status_change"):
  if q[key]:e.append(key)
 return e
assert not validate(D),validate(D)
mutations=[("census",lambda x:x["bridge_census"].__setitem__("row_count",70)),("counts",lambda x:x["bridge_census"].__setitem__("satisfied_count",49)),("new rows",lambda x:x["bridge_census"].__setitem__("new_satisfied_rows",[])),("global",lambda x:x["decision"].__setitem__("fixed_sector_global_large_data_evolution_constructed",False)),("range",lambda x:x["decision"].__setitem__("closed_nonlinear_gauge_range_constructed",False)),("quotient",lambda x:x["decision"].__setitem__("proper_classical_coulomb_quotient_constructed",False)),("flow",lambda x:x["decision"].__setitem__("fixed_sector_global_reduced_flow_constructed",False)),("completion overclaim",lambda x:x["decision"].__setitem__("completed_unbounded_charge_global_flow_constructed",True)),("BV overclaim",lambda x:x["decision"].__setitem__("full_bv_bfv_boundary_theory_constructed",True)),("Hilbert overclaim",lambda x:x["decision"].__setitem__("positive_gu_physical_hilbert_cohomology_constructed",True)),("source overclaim",lambda x:x["decision"].__setitem__("source_selected_reduction_constructed",True)),("protected overclaim",lambda x:x["decision"].__setitem__("protected_status_change",True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);errors=validate(x);assert errors,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 12/12")
