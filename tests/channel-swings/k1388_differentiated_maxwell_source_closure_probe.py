#!/usr/bin/env python3
"""Data-mutation probe for K1388."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1388-differentiated-maxwell-source-closure.json").read_text())
def validate(x):
 m,q=x["maxwell_source"],x["decision"];e=[]
 if "partial_mu j^mu=0" not in m["current"]:e.append("continuity")
 if "|beta|+|gamma|<=|alpha|" not in m["differentiated_form"]:e.append("expansion")
 if "at most R+1" not in m["principal_count"]:e.append("count")
 if "||j||_(H^R)<=C_R Y_R^2" not in m["tame_bound"]:e.append("tame")
 if not q["differentiated_current_expanded"]:e.append("current decision")
 if not q["same_triangular_tier_controls_source"]:e.append("tier decision")
 if q["closed_nonlinear_KT_range_proved"]:e.append("KT overclaim")
 if q["physical_BFV_quotient_proved"]:e.append("BFV overclaim")
 if q["source_observation_map_constructed"]:e.append("observation overclaim")
 return e
assert not validate(D),validate(D)
mutations=[("continuity",lambda x:x["maxwell_source"].__setitem__("current","unconstrained")),("expansion",lambda x:x["maxwell_source"].__setitem__("differentiated_form","unknown")),("count",lambda x:x["maxwell_source"].__setitem__("principal_count","R+2")),("tame",lambda x:x["maxwell_source"].__setitem__("tame_bound","unbounded")),("current decision",lambda x:x["decision"].__setitem__("differentiated_current_expanded",False)),("tier decision",lambda x:x["decision"].__setitem__("same_triangular_tier_controls_source",False)),("KT overclaim",lambda x:x["decision"].__setitem__("closed_nonlinear_KT_range_proved",True)),("BFV overclaim",lambda x:x["decision"].__setitem__("physical_BFV_quotient_proved",True)),("observation overclaim",lambda x:x["decision"].__setitem__("source_observation_map_constructed",True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);errors=validate(x);assert errors,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 9/9")
