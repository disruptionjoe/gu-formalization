#!/usr/bin/env python3
"""Data-mutation probe for K1372."""
import copy, json
from pathlib import Path
D = json.loads((Path(__file__).resolve().parents[2] / "lab/process/k1372-covariant-charge-sobolev-repair.json").read_text())
def validate(x):
    r,c,q=x["repair"],x["current_control"],x["decision"]; e=[]
    if "D_A(Qphi)" not in r["space"]: e.append("domain")
    if "exp(i alpha Q)D_A(Qphi)" not in r["gauge_covariance"]: e.append("covariance")
    if "not added" not in r["not_an_action_term"]: e.append("owner")
    if "grad ||Qphi||" not in r["kato_bound"]: e.append("Kato")
    if "H^-1" not in c["hminus1_bound"]: e.append("bound")
    if not q["gauge_covariant_mixed_topology_constructed"]: e.append("construction")
    if not q["gauss_density_continuous_to_hminus1"]: e.append("continuity")
    if q["repair_selected_by_source"]: e.append("source overclaim")
    if q["mixed_topology_globally_propagated"]: e.append("propagation overclaim")
    if q["global_nonlinear_evolution_proved"]: e.append("evolution overclaim")
    return e
assert not validate(D), validate(D)
mutations=[
 ("domain",lambda x:x["repair"].__setitem__("space","ordinary H1")),
 ("covariance",lambda x:x["repair"].__setitem__("gauge_covariance","unknown")),
 ("owner",lambda x:x["repair"].__setitem__("not_an_action_term","source action term")),
 ("Kato",lambda x:x["repair"].__setitem__("kato_bound","none")),
 ("bound",lambda x:x["current_control"].__setitem__("hminus1_bound","L1 only")),
 ("construction",lambda x:x["decision"].__setitem__("gauge_covariant_mixed_topology_constructed",False)),
 ("continuity",lambda x:x["decision"].__setitem__("gauss_density_continuous_to_hminus1",False)),
 ("source overclaim",lambda x:x["decision"].__setitem__("repair_selected_by_source",True)),
 ("propagation overclaim",lambda x:x["decision"].__setitem__("mixed_topology_globally_propagated",True)),
 ("evolution overclaim",lambda x:x["decision"].__setitem__("global_nonlinear_evolution_proved",True))]
for i,(label,mutate) in enumerate(mutations,1):
    x=copy.deepcopy(D);mutate(x);errors=validate(x);assert errors,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 10/10")
