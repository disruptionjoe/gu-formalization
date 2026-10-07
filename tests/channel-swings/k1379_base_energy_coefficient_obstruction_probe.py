#!/usr/bin/env python3
"""Data-mutation probe for K1379."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1379-base-energy-coefficient-obstruction.json").read_text())
def validate(x):
 c,q=x["concentration"],x["decision"];e=[]
 if "Dirichlet square" not in c["block"]:e.append("block")
 if "(2N+1)^(3/2)" not in c["linfinity"]:e.append("Linfinity")
 if "fixed L2" not in c["electric_data"]:e.append("electric")
 if "2lambda" not in c["radial_derivative"]:e.append("derivative")
 if "=0" not in c["neutrality"]:e.append("neutrality")
 if not q["base_energy_uniformly_bounded"]:e.append("energy")
 if not q["required_coefficient_norm_unbounded"]:e.append("unbounded")
 if q["k1378_gronwall_closed_by_base_energy"]:e.append("closure overclaim")
 if q["weaker_spacetime_estimate_excluded"]:e.append("weaker-route overclaim")
 if q["global_nonlinear_evolution_proved"]:e.append("global overclaim")
 return e
assert not validate(D),validate(D)
mutations=[("block",lambda x:x["concentration"].__setitem__("block","constant")),("Linfinity",lambda x:x["concentration"].__setitem__("linfinity","bounded")),("electric",lambda x:x["concentration"].__setitem__("electric_data","unbounded energy")),("derivative",lambda x:x["concentration"].__setitem__("radial_derivative","zero")),("neutrality",lambda x:x["concentration"].__setitem__("neutrality","unknown")),("energy",lambda x:x["decision"].__setitem__("base_energy_uniformly_bounded",False)),("unbounded",lambda x:x["decision"].__setitem__("required_coefficient_norm_unbounded",False)),("closure overclaim",lambda x:x["decision"].__setitem__("k1378_gronwall_closed_by_base_energy",True)),("weaker-route overclaim",lambda x:x["decision"].__setitem__("weaker_spacetime_estimate_excluded",True)),("global overclaim",lambda x:x["decision"].__setitem__("global_nonlinear_evolution_proved",True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);errors=validate(x);assert errors,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 10/10")
