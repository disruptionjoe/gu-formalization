#!/usr/bin/env python3
"""Charge-regularity propagation controls for K1363."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1363-defocusing-charge-regularity-propagation.json").read_text());n=0
def check(label,value):
 global n;assert value,label;n+=1;print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
T,Q=D["propagation_theorem"],D["decision"]
check("equation inherited","lambda ||u||_Hps^2 u" in T["equation"])
check("global base","global finite-energy" in T["base_result"])
check("all powers","every integer r>=1" in T["charge_commutation"])
check("differentiated equation","w_r=Q^r u" in T["differentiated_equation"])
charges=(-4,-2,0,2,4);u=(1.,-2.,3.,.5,-.25);lam=2.0
norm=sum(x*x for x in u)
for r in (1,2,3,4):
 lhs=tuple((q**r)*(lam*norm*x) for q,x in zip(charges,u));rhs=tuple(lam*norm*((q**r)*x) for q,x in zip(charges,u))
 check(f"Q^{r} radial identity",lhs==rhs)
check("graph data typed","Q^r u(0)" in T["graph_initial_data"])
check("global propagation typed","all real times" in T["global_propagation"])
check("causal cone typed","same wave principal part" in T["causal_support"])
check("nonconservation explicit","not claimed conserved" in T["energy_limit"])
check("one order decision",Q["one_charge_graph_order_propagated_globally"])
check("all finite orders decision",Q["every_finite_charge_graph_order_propagated_for_smooth_data"])
check("causal decision",Q["same_causal_cone_preserved"])
check("energy ceiling",not Q["higher_charge_energy_conserved"])
check("coupled ceiling",not Q["coupled_gauge_matter_global_evolution_proved"])
check("BV ceiling",not Q["closed_KT_BV_BFV_quotient_proved"])
check("source ceiling",not Q["source_action_identified"])
check("protected fixed",not Q["protected_status_change"])
check("claim ceiling honest","does not include" in D["claim_ceiling"])
assert n==23;print("RESULT: PASS 23/23")
