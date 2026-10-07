#!/usr/bin/env python3
"""Data-mutation probe for K1391."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1391-bounded-charge-local-evolution.json").read_text())
def validate(x):
 f,q=x["bounded_charge_flow"],x["decision"];e=[]
 if "P_N=1_{[-N,N]}(Q)" not in f["spectral_cutoff"]:e.append("projector")
 if "remain in ran(P_N)" not in f["invariant_sector"]:e.append("sector")
 if "||Q_N||<=N" not in f["bounded_generator"]:e.append("bound")
 if "Duhamel contraction" not in f["local_theorem"]:e.append("theorem")
 if not q["bounded_charge_local_solution_constructed"]:e.append("solution")
 if not q["bounded_charge_uniqueness_constructed"]:e.append("uniqueness")
 if q["cutoff_uniform_completed_flow_constructed"]:e.append("completion overclaim")
 if q["global_evolution_constructed"]:e.append("global overclaim")
 if q["source_action_identified"]:e.append("source overclaim")
 return e
assert not validate(D),validate(D)
mutations=[("projector",lambda x:x["bounded_charge_flow"].__setitem__("spectral_cutoff","none")),("sector",lambda x:x["bounded_charge_flow"].__setitem__("invariant_sector","escapes")),("bound",lambda x:x["bounded_charge_flow"].__setitem__("bounded_generator","unbounded")),("theorem",lambda x:x["bounded_charge_flow"].__setitem__("local_theorem","formal")),("solution",lambda x:x["decision"].__setitem__("bounded_charge_local_solution_constructed",False)),("uniqueness",lambda x:x["decision"].__setitem__("bounded_charge_uniqueness_constructed",False)),("completion overclaim",lambda x:x["decision"].__setitem__("cutoff_uniform_completed_flow_constructed",True)),("global overclaim",lambda x:x["decision"].__setitem__("global_evolution_constructed",True)),("source overclaim",lambda x:x["decision"].__setitem__("source_action_identified",True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);errors=validate(x);assert errors,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 9/9")
