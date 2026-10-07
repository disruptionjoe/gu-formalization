#!/usr/bin/env python3
"""Data-mutation probe for K1362."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1362-radial-nonlinearity-charge-domain.json").read_text())
def validate(x):
 t,q=x["radial_domain_theorem"],x["decision"];e=[]
 if "D(Q)" not in t["domain_preservation"]:e.append("domain")
 if "Q N_f(v)" not in t["charge_identity"]:e.append("identity")
 if "N_f(Uv)=U N_f(v)" not in t["unitary_equivariance"]:e.append("equivariance")
 if not q["radial_nonlinearity_preserves_D_Q"]:e.append("preservation")
 if not q["exact_charge_identity_proved"]:e.append("identity decision")
 if not q["local_graph_lipschitz_control_proved"]:e.append("Lipschitz")
 if q["fully_coupled_gauge_flow_closed"]:e.append("coupled overclaim")
 if q["source_action_identified"]:e.append("source overclaim")
 if q["protected_status_change"]:e.append("protected movement")
 if "does not close" not in x["claim_ceiling"]:e.append("ceiling")
 return e
assert not validate(D)
mutations=[("domain",lambda x:x["radial_domain_theorem"].__setitem__("domain_preservation","unknown")),("identity",lambda x:x["radial_domain_theorem"].__setitem__("charge_identity","unknown")),("equivariance",lambda x:x["radial_domain_theorem"].__setitem__("unitary_equivariance","unknown")),("preservation",lambda x:x["decision"].__setitem__("radial_nonlinearity_preserves_D_Q",False)),("identity decision",lambda x:x["decision"].__setitem__("exact_charge_identity_proved",False)),("Lipschitz",lambda x:x["decision"].__setitem__("local_graph_lipschitz_control_proved",False)),("coupled overclaim",lambda x:x["decision"].__setitem__("fully_coupled_gauge_flow_closed",True)),("source overclaim",lambda x:x["decision"].__setitem__("source_action_identified",True)),("protected movement",lambda x:x["decision"].__setitem__("protected_status_change",True)),("ceiling",lambda x:x.__setitem__("claim_ceiling","complete physical theory"))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);e=validate(x);assert e,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {e[0]}")
print("RESULT: PASS 10/10")
