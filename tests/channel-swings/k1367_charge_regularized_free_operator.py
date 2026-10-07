#!/usr/bin/env python3
"""Closed form and spectral controls for K1367."""
import hashlib,json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1367-charge-regularized-free-operator.json").read_text()); n=0
def check(label,value):
    global n
    assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():
    check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
F,S,Q=D["closed_form"],D["spectral_and_causal_control"],D["decision"]
check("Hilbert carrier typed","L2(T3;H_ps)" in F["hilbert_space"])
check("form typed","mu||Q phi||^2" in F["form"])
check("form domain typed","X_Q^1" in F["form_domain"])
check("closed sum typed","densely defined, closed" in F["closure"])
check("operator typed","-Delta_T3+m^2+mu Q^2" in F["associated_operator"])
check("operator domain typed","D(Q^2)" in F["operator_domain"])
m2=1.7; mu=0.3
for k2,q in ((0,0),(1,0),(0,2),(5,-4),(9,8)):
    value=k2+m2+mu*q*q
    check(f"mode floor k2={k2} q={q}",value>=m2)
for a,b in ((0,0),(1,2),(4,3),(9,16),(25,7)):
    check(f"sum domain equivalence {a},{b}",(a+b)**2>=a*a+b*b and (a+b)**2<=2*(a*a+b*b))
check("sharp floor typed","A_mu>=m^2 I" in S["sharp_floor"])
check("energy space typed","D(A_mu^(1/2))" in S["energy_space"])
check("skew generator typed","skew-adjoint" in S["wave_generator"])
check("causal principal part typed","zeroth order" in S["causal_principal_part"])
check("compactness boundary typed","false" in S["compact_resolvent_boundary"])
check("closed form decision",Q["closed_positive_form_on_X_Q_1"])
check("self adjoint decision",Q["self_adjoint_free_operator_constructed"])
check("domain decision",Q["operator_domain_identified"])
check("floor decision",Q["strict_spectral_floor_m_squared"])
check("free evolution decision",Q["unitary_free_evolution_on_graph_energy_space"] and Q["spacetime_causal_cone_unchanged"])
check("overclaims absent",not Q["compact_resolvent"] and not Q["nonlinear_coupled_operator_closed"] and not Q["source_action_identified"] and not Q["protected_status_change"])
assert n==29,n
print("RESULT: PASS 29/29")
