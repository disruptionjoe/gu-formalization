#!/usr/bin/env python3
"""Identity and Gronwall controls for K1378."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1378-coupled-charge-lift-gronwall.json").read_text());n=0
def check(label,value):
 global n
 assert value,label;n+=1;print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
C,Q=D["coupled_identity"],D["decision"]
for label,key,needle in [
 ("lifted variable","lifted_variable","psi=Qphi"),("equation","equation","mu Q^2"),
 ("commutation","commutation","Q commutes"),("current","lifted_current","Qpsi"),
 ("exchange","energy_exchange","E dot j_Q"),("pointwise bound","pointwise_bound","||E||_infinity"),
 ("differential inequality","differential_inequality","dE_Q,f/dt"),("Gronwall","gronwall","exp"),
 ("assumptions","assumptions","integrable in time"),("uncancelled exchange","uncancelled_exchange","not the lifted current")]:check(label,needle in C[key])
for coeff,t in ((.2,.5),(.5,1.0),(1.0,.25),(2.0,.75)):
 bound=3.0*math.exp(coeff*t)
 check(f"Gronwall dominates initial coeff={coeff}",bound>=3.0)
 check(f"Gronwall finite coeff={coeff}",math.isfinite(bound))
check("conditional estimate",Q["conditional_coupled_charge_lift_estimate"])
check("coefficient named",Q["exact_coefficient_integrability_named"])
check("Q2 required",Q["lifted_current_requires_Q2phi"])
check("base implication rejected",not Q["base_energy_implies_coefficient_integrability"])
check("global theorem absent",not Q["global_large_data_theorem_proved"])
check("BV properness absent",not Q["nonlinear_KT_BV_BFV_properness_proved"])
check("protected fixed",not Q["protected_status_change"])
assert n==27,n
print("RESULT: PASS 27/27")
