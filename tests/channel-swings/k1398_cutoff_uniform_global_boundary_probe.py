#!/usr/bin/env python3
"""Mutation probe for K1398."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1398-cutoff-uniform-global-boundary.json").read_text())
def validate(x):
 f,q=x["uniformity_audit"],x["decision"];e=[]
 for key,needle in (("bounded_generator_step","||Q_N||<=N"),("energy_sequence","Gauss density unbounded"),("local_completion","one additional completed triangular tier"),("iteration_gap","No conserved or uniformly bounded"),("logical_effect","route boundary"),("boundary","do not commute automatically")):
  if needle not in f[key]:e.append(key)
 for key in ("fixed_sector_global_theorem_preserved","current_restart_constant_cutoff_dependent","base_energy_uniform_completion_route_excluded"):
  if not q[key]:e.append(key)
 for key in ("all_global_completed_flow_mechanisms_excluded","completed_unbounded_charge_global_flow_constructed"):
  if q[key]:e.append(key)
 return e
assert not validate(D),validate(D)
mutations=[("bounded",lambda x:x["uniformity_audit"].__setitem__("bounded_generator_step","uniform")),("sequence",lambda x:x["uniformity_audit"].__setitem__("energy_sequence","bounded")),("local",lambda x:x["uniformity_audit"].__setitem__("local_completion","none")),("gap",lambda x:x["uniformity_audit"].__setitem__("iteration_gap","closed")),("logic",lambda x:x["uniformity_audit"].__setitem__("logical_effect","universal no-go")),("limits",lambda x:x["uniformity_audit"].__setitem__("boundary","commute")),("fixed lost",lambda x:x["decision"].__setitem__("fixed_sector_global_theorem_preserved",False)),("dependence lost",lambda x:x["decision"].__setitem__("current_restart_constant_cutoff_dependent",False)),("route lost",lambda x:x["decision"].__setitem__("base_energy_uniform_completion_route_excluded",False)),("all mechanisms overclaim",lambda x:x["decision"].__setitem__("all_global_completed_flow_mechanisms_excluded",True)),("completion overclaim",lambda x:x["decision"].__setitem__("completed_unbounded_charge_global_flow_constructed",True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);errors=validate(x);assert errors,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 11/11")
