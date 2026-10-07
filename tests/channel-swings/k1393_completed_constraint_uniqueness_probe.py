#!/usr/bin/env python3
"""Data-mutation probe for K1393."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1393-completed-constraint-uniqueness.json").read_text())
def validate(x):
 f,q=x["completed_constraints"],x["decision"];e=[]
 for key,needle in (("uniqueness","zero initial difference"),("continuous_dependence","Gronwall"),("current_limit","continuity equation"),("lorenz_constraint","homogeneous scalar wave"),("gauss_constraint","constant in time")):
  if needle not in f[key]:e.append(key)
 for key in ("completed_flow_unique","current_conservation_passes_to_limit","lorenz_constraint_propagates","gauss_constraint_propagates"):
  if not q[key]:e.append(key)
 for key in ("closed_nonlinear_KT_range_constructed","positive_physical_cohomology_constructed","source_action_identified"):
  if q[key]:e.append(key)
 return e
assert not validate(D),validate(D)
mutations=[("unique",lambda x:x["completed_constraints"].__setitem__("uniqueness","unknown")),("dependence",lambda x:x["completed_constraints"].__setitem__("continuous_dependence","none")),("current",lambda x:x["completed_constraints"].__setitem__("current_limit","lost")),("Lorenz",lambda x:x["completed_constraints"].__setitem__("lorenz_constraint","forced")),("Gauss",lambda x:x["completed_constraints"].__setitem__("gauss_constraint","drifts")),("unique decision",lambda x:x["decision"].__setitem__("completed_flow_unique",False)),("current decision",lambda x:x["decision"].__setitem__("current_conservation_passes_to_limit",False)),("Lorenz decision",lambda x:x["decision"].__setitem__("lorenz_constraint_propagates",False)),("Gauss decision",lambda x:x["decision"].__setitem__("gauss_constraint_propagates",False)),("KT overclaim",lambda x:x["decision"].__setitem__("closed_nonlinear_KT_range_constructed",True)),("cohomology overclaim",lambda x:x["decision"].__setitem__("positive_physical_cohomology_constructed",True)),("source overclaim",lambda x:x["decision"].__setitem__("source_action_identified",True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);errors=validate(x);assert errors,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 12/12")
