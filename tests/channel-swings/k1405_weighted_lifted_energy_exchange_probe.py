#!/usr/bin/env python3
"""Mutation probe for K1405."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1405-weighted-lifted-energy-exchange.json").read_text())
def validate(x):
 f,q=x["weighted_exchange"],x["decision"];e=[]
 for key,needle in (("weight","w(Q)>=0"),("functional","H_(w,c)"),("weighted_current","j_w"),("exact_identity","dH_(w,c)/dt"),("exact_identity","j_w-c j_1"),("exact_identity","w(Q)-c I"),("constant_control","w=c I"),("polynomial_lifts","q^(2n)"),("boundary","does not cover")):
  if needle not in f[key]:e.append(f"{key}:{needle}")
 if not q["exact_weighted_energy_exchange_derived"]:e.append("identity decision")
 if q["all_modified_energy_routes_excluded"]:e.append("scope overclaim")
 return e
assert not validate(D)
mutations=[("weight",lambda x:x["weighted_exchange"].__setitem__("weight","none")),("functional",lambda x:x["weighted_exchange"].__setitem__("functional","none")),("current",lambda x:x["weighted_exchange"].__setitem__("weighted_current","none")),("identity",lambda x:x["weighted_exchange"].__setitem__("exact_identity","none")),("Maxwell defect",lambda x:x["weighted_exchange"].__setitem__("exact_identity","dH_(w,c)/dt and w(Q)-c I")),("radial defect",lambda x:x["weighted_exchange"].__setitem__("exact_identity","dH_(w,c)/dt and j_w-c j_1")),("constant",lambda x:x["weighted_exchange"].__setitem__("constant_control","none")),("polynomial",lambda x:x["weighted_exchange"].__setitem__("polynomial_lifts","none")),("decision",lambda x:x["decision"].__setitem__("exact_weighted_energy_exchange_derived",False)),("scope",lambda x:x["decision"].__setitem__("all_modified_energy_routes_excluded",True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);errors=validate(x);assert errors,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 10/10")
