#!/usr/bin/env python3
"""Data-mutation probe for K1389."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1389-local-high-regularity-continuation.json").read_text())
def validate(x):
 l,q=x["local_continuation"],x["decision"];e=[]
 if "Lorenz gauge" not in l["gauge_and_model"]:e.append("gauge")
 if "triangular matter energy" not in l["control_norm"]:e.append("norm")
 if "B_R<=C_R(1+Y_R)^2" not in l["tame_inequality"]:e.append("tame")
 if "log(2)/(C_R(1+2Y_0)^2)" not in l["local_bound"]:e.append("lifespan")
 if "does not prove global" not in l["global_boundary"]:e.append("boundary")
 if not q["closed_local_apriori_inequality_constructed"]:e.append("local decision")
 if not q["finite_triangular_phase_topology_locally_controlled"]:e.append("topology decision")
 if q["smooth_solution_existence_constructed"]:e.append("existence overclaim")
 if q["global_large_data_bound_constructed"]:e.append("global overclaim")
 if q["closed_nonlinear_BV_BFV_quotient_constructed"]:e.append("BV overclaim")
 if q["source_action_identified"]:e.append("source overclaim")
 return e
assert not validate(D),validate(D)
mutations=[("gauge",lambda x:x["local_continuation"].__setitem__("gauge_and_model","gauge free")),("norm",lambda x:x["local_continuation"].__setitem__("control_norm","base energy")),("tame",lambda x:x["local_continuation"].__setitem__("tame_inequality","unclosed")),("lifespan",lambda x:x["local_continuation"].__setitem__("local_bound","global")),("boundary",lambda x:x["local_continuation"].__setitem__("global_boundary","global theorem")),("local decision",lambda x:x["decision"].__setitem__("closed_local_apriori_inequality_constructed",False)),("topology decision",lambda x:x["decision"].__setitem__("finite_triangular_phase_topology_locally_controlled",False)),("existence overclaim",lambda x:x["decision"].__setitem__("smooth_solution_existence_constructed",True)),("global overclaim",lambda x:x["decision"].__setitem__("global_large_data_bound_constructed",True)),("BV overclaim",lambda x:x["decision"].__setitem__("closed_nonlinear_BV_BFV_quotient_constructed",True)),("source overclaim",lambda x:x["decision"].__setitem__("source_action_identified",True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);errors=validate(x);assert errors,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 11/11")
