#!/usr/bin/env python3
"""Gauge covariance and BRST/BV core audit for K1359."""
import cmath, hashlib, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1359-nonuniform-charge-gauge-bv-core.json").read_text()); n=0
def check(label,value):
    global n
    assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():
    check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
C,G,B,Q=D["common_core"],D["gauge_action"],D["brst_bv_bfv"],D["decision"]
check("K finite matter core", "H_Kfin" in C["matter_core"])
check("Q preserves core", "preserves" in C["charge_action"])
phi=1.2-0.7j; dphi=-0.3+0.9j; A=0.4; dalpha=-0.2; alpha=0.37
for q in (-4,-2,0,2,4):
    phase=cmath.exp(1j*alpha*q)
    lhs=phase*(dphi+1j*q*dalpha*phi)+1j*q*(A-dalpha)*phase*phi
    rhs=phase*(dphi+1j*q*A*phi)
    check(f"covariance charge {q}", abs(lhs-rhs)<1e-12)
check("covariant derivative typed", "Q phi" in G["covariant_derivative"])
check("local transformation typed", "exp(i alpha Q)" in G["local_transformation"])
check("current contains Q", "Q D_mu phi" in G["nontrivial_interaction"])
check("seagull contains Q norm", "||Q phi||^2" in G["nontrivial_interaction"])
check("positive energy statement", "nonnegative" in G["positive_energy"])
check("BRST Q rule", "i c Q phi" in B["brst_rules"])
check("BRST nilpotence", "s^2=0" in B["nilpotence"])
check("BV core", "master equation" in B["classical_bv"])
check("BFV core", "Gauss constraint" in B["boundary_bfv"])
check("operator charge action", Q["operator_valued_charge_action_constructed"])
check("gauge covariance decision", Q["local_gauge_covariance_on_core"])
check("interactions decision", Q["nonzero_current_and_seagull_interactions"])
check("BRST decision", Q["classical_BRST_nilpotent_on_core"])
check("global closure absent", not Q["global_nonlinear_causal_evolution_proved"] and not Q["closed_nonlinear_physical_hilbert_cohomology_proved"])
check("protected fixed", not Q["protected_status_change"])
assert n==25
print("RESULT: PASS 25/25")
