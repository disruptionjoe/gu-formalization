#!/usr/bin/env python3
"""Data-mutation probe for K1365."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1365-charge-domain-admission-boundary.json").read_text())
def validate(x):
 c,q=x["bridge_census"],x["decision"];e=[]
 if c["row_count"]!=c["satisfied_count"]+c["conditional_count"]+c["excluded_count"]+c["missing_count"]:e.append("arithmetic")
 if len(c["new_satisfied_rows"])!=3:e.append("new satisfied")
 if len(c["new_excluded_rows"])!=1:e.append("new excluded")
 if not q["completed_local_gauge_graph_domain_constructed"]:e.append("graph domain")
 if not q["separate_global_causal_charge_regular_flow_constructed"]:e.append("global flow")
 if not q["ordinary_coupled_energy_graph_coercivity_excluded"]:e.append("coercivity boundary")
 if q["source_selected_reduction_constructed"]:e.append("source overclaim")
 if q["fully_coupled_global_BV_BFV_domain_constructed"]:e.append("BV overclaim")
 if q["positive_physical_Hilbert_cohomology_constructed"]:e.append("cohomology overclaim")
 if q["protected_status_change"]:e.append("protected movement")
 return e
assert not validate(D)
mutations=[("arithmetic",lambda x:x["bridge_census"].__setitem__("row_count",42)),("new satisfied",lambda x:x["bridge_census"].__setitem__("new_satisfied_rows",[])),("new excluded",lambda x:x["bridge_census"].__setitem__("new_excluded_rows",[])),("graph domain",lambda x:x["decision"].__setitem__("completed_local_gauge_graph_domain_constructed",False)),("global flow",lambda x:x["decision"].__setitem__("separate_global_causal_charge_regular_flow_constructed",False)),("coercivity boundary",lambda x:x["decision"].__setitem__("ordinary_coupled_energy_graph_coercivity_excluded",False)),("source overclaim",lambda x:x["decision"].__setitem__("source_selected_reduction_constructed",True)),("BV overclaim",lambda x:x["decision"].__setitem__("fully_coupled_global_BV_BFV_domain_constructed",True)),("cohomology overclaim",lambda x:x["decision"].__setitem__("positive_physical_Hilbert_cohomology_constructed",True)),("protected movement",lambda x:x["decision"].__setitem__("protected_status_change",True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);e=validate(x);assert e,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {e[0]}")
print("RESULT: PASS 10/10")
