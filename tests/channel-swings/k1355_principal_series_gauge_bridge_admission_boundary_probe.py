#!/usr/bin/env python3
"""Data-mutation probe for K1355."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1355-principal-series-gauge-bridge-admission-boundary.json").read_text())
def validate(x):
 c,q=x["bridge_census"],x["decision"]; e=[]
 if c["row_count"]!=c["satisfied_count"]+c["conditional_count"]+c["excluded_count"]+c["missing_count"]: e.append("arithmetic")
 if len(c["excluded_rows"])!=c["excluded_count"]: e.append("excluded length")
 if not any("character_to_U1" in r for r in c["excluded_rows"]): e.append("character row")
 if not q["k1346_u1_internal_uniform_phase_route_excluded"]: e.append("phase result")
 if not q["pointwise_finite_source_fibre_linear_bridge_excluded"]: e.append("finite map result")
 if not q["positive_full_split_quadratic_gauge_kinetic_route_excluded"]: e.append("kinetic result")
 if q["all_source_to_control_bridges_excluded"]: e.append("global overreach")
 if q["maximal_compact_or_stabilizer_route_constructed"]: e.append("compact overclaim")
 if q["closed_global_nonlinear_physical_hilbert_quotient_constructed"]: e.append("quotient overclaim")
 if q["protected_status_change"]: e.append("protected movement")
 return e
assert not validate(D),validate(D)
mutations=[
 ("arithmetic",lambda x:x["bridge_census"].__setitem__("row_count",30)),
 ("excluded length",lambda x:x["bridge_census"]["excluded_rows"].pop()),
 ("character row",lambda x:x["bridge_census"]["excluded_rows"].__setitem__(0,"missing_character_row")),
 ("phase result",lambda x:x["decision"].__setitem__("k1346_u1_internal_uniform_phase_route_excluded",False)),
 ("finite map result",lambda x:x["decision"].__setitem__("pointwise_finite_source_fibre_linear_bridge_excluded",False)),
 ("kinetic result",lambda x:x["decision"].__setitem__("positive_full_split_quadratic_gauge_kinetic_route_excluded",False)),
 ("global overreach",lambda x:x["decision"].__setitem__("all_source_to_control_bridges_excluded",True)),
 ("compact overclaim",lambda x:x["decision"].__setitem__("maximal_compact_or_stabilizer_route_constructed",True)),
 ("quotient overclaim",lambda x:x["decision"].__setitem__("closed_global_nonlinear_physical_hilbert_quotient_constructed",True)),
 ("protected movement",lambda x:x["decision"].__setitem__("protected_status_change",True)),
]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D); mutate(x); errors=validate(x); assert errors,label; print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 10/10")
