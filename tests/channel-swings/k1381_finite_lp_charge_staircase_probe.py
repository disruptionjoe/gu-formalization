#!/usr/bin/env python3
"""Data-mutation probe for K1381."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1381-finite-lp-charge-staircase.json").read_text())
def validate(x):
 h,q=x["holder_sobolev_trade"],x["decision"];e=[]
 if "Q^(n+1)phi" not in h["lift"]:e.append("lift")
 if "sigma_p=3/p" not in h["range"]:e.append("exponent")
 if "||E||_p" not in h["holder"]:e.append("Holder")
 if "finite p requires" not in h["mixed_cost"]:e.append("cost")
 if "2p/(p-1)" not in h["radial_term"]:e.append("radial")
 if not q["finite_p_trade_derived"]:e.append("trade")
 if not q["endpoint_same_energy_closure"]:e.append("endpoint")
 if q["finite_p_same_energy_closure"]:e.append("finite-p overclaim")
 if q["null_form_or_strichartz_route_excluded"]:e.append("route overclaim")
 if q["source_action_identified"]:e.append("source overclaim")
 return e
assert not validate(D),validate(D)
mutations=[("lift",lambda x:x["holder_sobolev_trade"].__setitem__("lift","psi")),("exponent",lambda x:x["holder_sobolev_trade"].__setitem__("range","unknown")),("Holder",lambda x:x["holder_sobolev_trade"].__setitem__("holder","L2")),("cost",lambda x:x["holder_sobolev_trade"].__setitem__("mixed_cost","none")),("radial",lambda x:x["holder_sobolev_trade"].__setitem__("radial_term","unknown")),("trade",lambda x:x["decision"].__setitem__("finite_p_trade_derived",False)),("endpoint",lambda x:x["decision"].__setitem__("endpoint_same_energy_closure",False)),("finite-p overclaim",lambda x:x["decision"].__setitem__("finite_p_same_energy_closure",True)),("route overclaim",lambda x:x["decision"].__setitem__("null_form_or_strichartz_route_excluded",True)),("source overclaim",lambda x:x["decision"].__setitem__("source_action_identified",True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);errors=validate(x);assert errors,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 10/10")
