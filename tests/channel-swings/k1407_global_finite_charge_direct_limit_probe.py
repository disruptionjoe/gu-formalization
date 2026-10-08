#!/usr/bin/env python3
"""Mutation probe for K1407."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1407-global-finite-charge-direct-limit.json").read_text())
def validate(x):
 f,q=x["direct_limit_flow"],x["decision"];e=[]
 for key,needle in (("core","union_"),("density","dense"),("global_existence","global"),("compatibility","S_N(t)x=S_M(t)x"),("flow_law","two-sided flow"),("conserved_data","Noether"),("completion_gap","cutoff-uniform"),("boundary","not a global flow on the completed")):
  if needle not in f[key]:e.append(key)
 if not q["global_direct_limit_flow_constructed"]:e.append("flow decision")
 if q["continuous_extension_to_completed_phase_space_constructed"]:e.append("completion overclaim")
 return e
assert not validate(D)
mutations=[("core",lambda x:x["direct_limit_flow"].__setitem__("core","none")),("density",lambda x:x["direct_limit_flow"].__setitem__("density","closed")),("global",lambda x:x["direct_limit_flow"].__setitem__("global_existence","local")),("compatibility",lambda x:x["direct_limit_flow"].__setitem__("compatibility","none")),("flow",lambda x:x["direct_limit_flow"].__setitem__("flow_law","family")),("data",lambda x:x["direct_limit_flow"].__setitem__("conserved_data","none")),("gap",lambda x:x["direct_limit_flow"].__setitem__("completion_gap","automatic")),("boundary",lambda x:x["direct_limit_flow"].__setitem__("boundary","completed global flow")),("decision",lambda x:x["decision"].__setitem__("global_direct_limit_flow_constructed",False)),("overclaim",lambda x:x["decision"].__setitem__("continuous_extension_to_completed_phase_space_constructed",True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);errors=validate(x);assert errors,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 10/10")
