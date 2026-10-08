#!/usr/bin/env python3
"""Controls for K1406 conserved-weight rigidity."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1406-conserved-spectral-weight-rigidity.json").read_text());n=0
def check(label,value):
 global n
 assert value,label;n+=1;print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
F,Q=D["rigidity"],D["decision"]
for label,key,needle in [("class","claim_class","Time-independent"),("sufficiency","sufficiency","w=c"),("current test","current_test","q(w(q)-c)=0"),("arbitrary current","current_test","arbitrary"),("radial test","radial_test","w(q)=c"),("necessity","necessity","full active spectral support"),("coercivity","coercivity_consequence","unbounded"),("polynomial","coercivity_consequence","polynomials"),("reopeners","reopeners","additional structure"),("boundary","boundary","not for all")]:check(label,needle in F[key])
for key in ("constant_weight_sufficient","constant_weight_necessary_for_universal_conservation","finite_polynomial_spectral_reweighting_route_excluded"):check(key,Q[key])
for key in ("unbounded_charge_coercive_weight_in_declared_class_conserved","nonlinear_or_time_dependent_modified_energy_excluded","spacetime_or_infinite_hierarchy_route_excluded","completed_unbounded_charge_global_flow_constructed","protected_status_change"):check(f"{key} false",not Q[key])
assert n==20,n
print("RESULT: PASS 20/20")
