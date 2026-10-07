#!/usr/bin/env python3
"""Data-mutation probe for K1367."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1367-charge-regularized-free-operator.json").read_text())
def validate(x):
 f,s,q=x["closed_form"],x["spectral_and_causal_control"],x["decision"]; e=[]
 if "X_Q^1" not in f["form_domain"]:e.append("form domain")
 if "D(Q^2)" not in f["operator_domain"]:e.append("operator domain")
 if "-Delta_T3+m^2+mu Q^2" not in f["associated_operator"]:e.append("operator")
 if "A_mu>=m^2 I" not in s["sharp_floor"]:e.append("floor")
 if "skew-adjoint" not in s["wave_generator"]:e.append("generator")
 if not q["closed_positive_form_on_X_Q_1"]:e.append("closure")
 if not q["self_adjoint_free_operator_constructed"]:e.append("self adjointness")
 if q["compact_resolvent"]:e.append("compactness overclaim")
 if q["nonlinear_coupled_operator_closed"]:e.append("nonlinear overclaim")
 if q["source_action_identified"]:e.append("source overclaim")
 return e
assert not validate(D),validate(D)
mutations=[
 ("form domain",lambda x:x["closed_form"].__setitem__("form_domain","ordinary H1")),
 ("operator domain",lambda x:x["closed_form"].__setitem__("operator_domain","all H")),
 ("operator",lambda x:x["closed_form"].__setitem__("associated_operator","bounded mass")),
 ("floor",lambda x:x["spectral_and_causal_control"].__setitem__("sharp_floor","unknown")),
 ("generator",lambda x:x["spectral_and_causal_control"].__setitem__("wave_generator","formal")),
 ("closure",lambda x:x["decision"].__setitem__("closed_positive_form_on_X_Q_1",False)),
 ("self adjointness",lambda x:x["decision"].__setitem__("self_adjoint_free_operator_constructed",False)),
 ("compactness overclaim",lambda x:x["decision"].__setitem__("compact_resolvent",True)),
 ("nonlinear overclaim",lambda x:x["decision"].__setitem__("nonlinear_coupled_operator_closed",True)),
 ("source overclaim",lambda x:x["decision"].__setitem__("source_action_identified",True)),
]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);errors=validate(x);assert errors,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 10/10")
