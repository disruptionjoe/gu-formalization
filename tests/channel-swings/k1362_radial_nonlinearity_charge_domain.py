#!/usr/bin/env python3
"""Radial nonlinearity charge-domain controls for K1362."""
import cmath,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1362-radial-nonlinearity-charge-domain.json").read_text());n=0
def check(label,value):
 global n;assert value,label;n+=1;print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
T,Q=D["radial_domain_theorem"],D["decision"]
check("radial form","N_f(v)=f(||v||^2)v" in T["nonlinearity"])
check("domain statement","D(Q)" in T["domain_preservation"])
check("charge identity","Q N_f(v)" in T["charge_identity"])
check("unitary equivariance","N_f(Uv)=U N_f(v)" in T["unitary_equivariance"])
charges=(-4,-2,0,2,4);v=(1+2j,-2+.5j,.7j,3-1j,-.2+.1j);lam=1.7
norm=sum(abs(z)**2 for z in v);Nv=tuple(lam*norm*z for z in v)
Qv=tuple(q*z for q,z in zip(charges,v));QN=tuple(q*z for q,z in zip(charges,Nv));NQ=tuple(lam*norm*z for z in Qv)
check("finite charge identity",max(abs(a-b) for a,b in zip(QN,NQ))<1e-12)
for alpha in (.1,.7,1.3):
 Uv=tuple(cmath.exp(1j*alpha*q)*z for q,z in zip(charges,v));Unorm=sum(abs(z)**2 for z in Uv)
 lhs=tuple(lam*Unorm*z for z in Uv);rhs=tuple(cmath.exp(1j*alpha*q)*z for q,z in zip(charges,Nv))
 check(f"gauge equivariance alpha={alpha}",max(abs(a-b) for a,b in zip(lhs,rhs))<1e-11)
check("graph estimate stated","locally Lipschitz" in T["graph_lipschitz"])
check("cubic instance","f(r)=lambda r" in T["defocusing_instance"])
check("domain decision",Q["radial_nonlinearity_preserves_D_Q"])
check("identity decision",Q["exact_charge_identity_proved"])
check("Lipschitz decision",Q["local_graph_lipschitz_control_proved"])
check("unitary decision",Q["all_internal_unitaries_preserve_nonlinearity"])
check("local gauge decision",Q["local_circle_gauge_equivariance_proved"])
check("coupled ceiling",not Q["fully_coupled_gauge_flow_closed"])
check("source ceiling",not Q["source_action_identified"])
check("protected fixed",not Q["protected_status_change"])
check("claim ceiling honest","does not close" in D["claim_ceiling"])
assert n==21;print("RESULT: PASS 21/21")
