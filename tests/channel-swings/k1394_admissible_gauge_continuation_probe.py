#!/usr/bin/env python3
"""Data-mutation probe for K1394."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1394-admissible-gauge-continuation.json").read_text())
def validate(x):
 f,q=x["gauge_continuation"],x["decision"];e=[]
 for key,needle in (("gauge_action","D'_mu phi'"),("derivative_count","derivative order plus charge order"),("admissible_class","bounded invertible map"),("norm_equivalence","C_R(chi)^(-1)"),("lorenz_residual","box chi=0"),("continuation_invariance","equivalent")):
  if needle not in f[key]:e.append(key)
 for key in ("triangular_gauge_action_bounded","triangular_gauge_action_invertible","finite_time_continuation_gauge_invariant"):
  if not q[key]:e.append(key)
 for key in ("physical_quotient_topology_constructed","global_gauge_independent_norm_constructed","source_observation_map_constructed"):
  if q[key]:e.append(key)
 return e
assert not validate(D),validate(D)
mutations=[("action",lambda x:x["gauge_continuation"].__setitem__("gauge_action","uncovariant")),("count",lambda x:x["gauge_continuation"].__setitem__("derivative_count","loses order")),("class",lambda x:x["gauge_continuation"].__setitem__("admissible_class","unbounded")),("norm",lambda x:x["gauge_continuation"].__setitem__("norm_equivalence","one-sided")),("Lorenz",lambda x:x["gauge_continuation"].__setitem__("lorenz_residual","always")),("continuation",lambda x:x["gauge_continuation"].__setitem__("continuation_invariance","unknown")),("bounded decision",lambda x:x["decision"].__setitem__("triangular_gauge_action_bounded",False)),("invertible decision",lambda x:x["decision"].__setitem__("triangular_gauge_action_invertible",False)),("continuation decision",lambda x:x["decision"].__setitem__("finite_time_continuation_gauge_invariant",False)),("quotient overclaim",lambda x:x["decision"].__setitem__("physical_quotient_topology_constructed",True)),("global norm overclaim",lambda x:x["decision"].__setitem__("global_gauge_independent_norm_constructed",True)),("source overclaim",lambda x:x["decision"].__setitem__("source_observation_map_constructed",True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);errors=validate(x);assert errors,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 12/12")
