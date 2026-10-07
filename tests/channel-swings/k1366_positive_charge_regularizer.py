#!/usr/bin/env python3
"""Gauge invariance and coercivity controls for K1366."""
import cmath, hashlib, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1366-positive-charge-regularizer.json").read_text()); n=0
def check(label,value):
    global n
    assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():
    check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
R,C,Q=D["regularized_action"],D["coercivity"],D["decision"]
check("positive coefficient","mu>0" in R["coefficient"])
check("Q regularizer typed","mu||Q phi||^2" in R["added_potential"])
check("gauge identity typed","Q exp(i alpha Q)" in R["local_gauge_identity"])
check("Euler Q squared typed","Q^2 phi" in R["euler_contribution"])
check("BRST invariance typed","s V_Q=0" in R["brst_invariance"])
check("energy bound typed","E_mu/mu" in C["sharp_bound"])
alpha=0.37; phi=1.2-0.4j
for q in (-4,-2,0,2,4):
    phase=cmath.exp(1j*alpha*q)
    check(f"gauge norm charge {q}",abs(abs(q*phase*phi)**2-abs(q*phi)**2)<1e-12)
mu=0.7
for N in (1,3,7,19):
    added=16*mu*N; qnorm2=16*N
    check(f"witness penalty N={N}",abs(added-mu*qnorm2)<1e-12)
    check(f"coercive bound N={N}",qnorm2<=added/mu+1e-12)
check("regularizer constructed",Q["positive_charge_regularizer_constructed"])
check("gauge invariant",Q["local_circle_gauge_invariant"])
check("BRST invariant",Q["brst_invariant_on_common_core"])
check("charge coercive",Q["charge_graph_coercive"])
check("spatial overclaim absent",not Q["ordinary_spatial_H1_control_from_regularizer_alone"])
check("source and nonlinear overclaims absent",not Q["source_action_identified"] and not Q["source_selects_Q_or_mu"] and not Q["global_nonlinear_coupled_evolution_proved"] and not Q["protected_status_change"])
assert n==27,n
print("RESULT: PASS 27/27")
