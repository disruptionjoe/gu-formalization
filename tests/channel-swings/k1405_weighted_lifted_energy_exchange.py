#!/usr/bin/env python3
"""Controls for K1405 weighted energy exchange."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1405-weighted-lifted-energy-exchange.json").read_text());n=0
def check(label,value):
 global n
 assert value,label;n+=1;print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
F,Q=D["weighted_exchange"],D["decision"]
for label,key,needle in [("weight","weight","w(Q)>=0"),("functional","functional","H_(w,c)"),("quadratic","functional","mu||"),("quartic","functional","lambda/4"),("current","weighted_current","j_w"),("physical current","weighted_current","j_1"),("identity","exact_identity","dH_(w,c)/dt"),("Maxwell defect","exact_identity","j_w-c j_1"),("radial defect","exact_identity","w(Q)-c I"),("constant","constant_control","w=c I"),("polynomial","polynomial_lifts","q^(2n)"),("one Maxwell","polynomial_lifts","one Maxwell"),("support","spectral_support","finite collections"),("boundary","boundary","does not cover")]:check(label,needle in F[key])
for key in ("exact_weighted_energy_exchange_derived","maxwell_current_defect_identified","radial_weight_defect_identified","constant_weight_recovers_conserved_energy"):check(key,Q[key])
for key in ("nonconstant_polynomial_weight_automatically_conserved","all_modified_energy_routes_excluded","source_action_identified","protected_status_change"):check(f"{key} false",not Q[key])
assert n==24,n
print("RESULT: PASS 24/24")
