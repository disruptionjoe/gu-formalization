#!/usr/bin/env python3
"""Mutation probe for K1397."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1397-bounded-charge-global-evolution.json").read_text())
def validate(x):
 f,q=x["bounded_sector_globalization"],x["decision"];e=[]
 for key,needle in (("sector","fixed finite N"),("gauge","Coulomb"),("conserved_energy","E_mu controls"),("connection_control","Hodge and Poincare"),("matter_control","diamagnetic"),("continuation","energy subcritical"),("recurrent_compatibility","does not require any global L1_t"),("boundary","depend on N")):
  if needle not in f[key]:e.append(key)
 for key in ("fixed_bounded_charge_global_large_data_evolution_constructed","finite_interval_low_norm_control_constructed","smooth_higher_regular_persistence_constructed"):
  if not q[key]:e.append(key)
 for key in ("cutoff_uniform_global_bound_constructed","completed_unbounded_charge_global_flow_constructed","source_action_identified"):
  if q[key]:e.append(key)
 return e
assert not validate(D),validate(D)
mutations=[("sector",lambda x:x["bounded_sector_globalization"].__setitem__("sector","unbounded")),("gauge",lambda x:x["bounded_sector_globalization"].__setitem__("gauge","none")),("energy",lambda x:x["bounded_sector_globalization"].__setitem__("conserved_energy","absent")),("Hodge",lambda x:x["bounded_sector_globalization"].__setitem__("connection_control","none")),("matter",lambda x:x["bounded_sector_globalization"].__setitem__("matter_control","none")),("continuation",lambda x:x["bounded_sector_globalization"].__setitem__("continuation","critical")),("recurrence",lambda x:x["bounded_sector_globalization"].__setitem__("recurrent_compatibility","L1 only")),("boundary",lambda x:x["bounded_sector_globalization"].__setitem__("boundary","uniform")),("global",lambda x:x["decision"].__setitem__("fixed_bounded_charge_global_large_data_evolution_constructed",False)),("uniform overclaim",lambda x:x["decision"].__setitem__("cutoff_uniform_global_bound_constructed",True)),("completion overclaim",lambda x:x["decision"].__setitem__("completed_unbounded_charge_global_flow_constructed",True)),("source overclaim",lambda x:x["decision"].__setitem__("source_action_identified",True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);errors=validate(x);assert errors,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 12/12")
