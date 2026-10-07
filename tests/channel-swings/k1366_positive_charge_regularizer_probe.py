#!/usr/bin/env python3
"""Data-mutation probe for K1366."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1366-positive-charge-regularizer.json").read_text())
def validate(x):
 r,c,q=x["regularized_action"],x["coercivity"],x["decision"]; e=[]
 if "mu>0" not in r["coefficient"]:e.append("coefficient")
 if "mu||Q phi||^2" not in r["added_potential"]:e.append("term")
 if "Q exp(i alpha Q)" not in r["local_gauge_identity"]:e.append("gauge identity")
 if "Q^2 phi" not in r["euler_contribution"]:e.append("Euler term")
 if "E_mu/mu" not in c["sharp_bound"]:e.append("coercivity")
 if not q["positive_charge_regularizer_constructed"]:e.append("construction")
 if not q["local_circle_gauge_invariant"]:e.append("invariance")
 if not q["charge_graph_coercive"]:e.append("graph control")
 if q["source_action_identified"]:e.append("source overclaim")
 if q["global_nonlinear_coupled_evolution_proved"]:e.append("nonlinear overclaim")
 return e
assert not validate(D),validate(D)
mutations=[
 ("coefficient",lambda x:x["regularized_action"].__setitem__("coefficient","mu arbitrary")),
 ("term",lambda x:x["regularized_action"].__setitem__("added_potential","ordinary mass")),
 ("gauge identity",lambda x:x["regularized_action"].__setitem__("local_gauge_identity","unknown")),
 ("Euler term",lambda x:x["regularized_action"].__setitem__("euler_contribution","bounded scalar")),
 ("coercivity",lambda x:x["coercivity"].__setitem__("sharp_bound","none")),
 ("construction",lambda x:x["decision"].__setitem__("positive_charge_regularizer_constructed",False)),
 ("invariance",lambda x:x["decision"].__setitem__("local_circle_gauge_invariant",False)),
 ("graph control",lambda x:x["decision"].__setitem__("charge_graph_coercive",False)),
 ("source overclaim",lambda x:x["decision"].__setitem__("source_action_identified",True)),
 ("nonlinear overclaim",lambda x:x["decision"].__setitem__("global_nonlinear_coupled_evolution_proved",True)),
]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);errors=validate(x);assert errors,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 10/10")
