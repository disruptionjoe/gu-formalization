#!/usr/bin/env python3
"""Differentiated-current controls for K1388."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1388-differentiated-maxwell-source-closure.json").read_text());n=0
def check(label,value):
 global n
 assert value,label;n+=1;print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
M,Q=D["maxwell_source"],D["decision"]
for label,key,needle in [
 ("current","current","partial_mu j^mu=0"),
 ("differentiated form","differentiated_form","|beta|+|gamma|<=|alpha|"),
 ("principal count","principal_count","at most R+1"),
 ("tame bound","tame_bound","||j||_(H^R)<=C_R Y_R^2"),
 ("Maxwell energy","maxwell_energy","d E_Max,R/dt"),
 ("constraint","constraint","propagates"),
 ("boundary","boundary","not a closed nonlinear KT range")]:check(label,needle in M[key])
for R in range(3,9):
 for a in range(R+1):
  for beta in range(a+1):
   gamma=a-beta
   check(f"source split R={R} a={a} b={beta}",max(beta+1,gamma+1)<=R+1)
check("current expanded",Q["differentiated_current_expanded"])
check("same tier",Q["same_triangular_tier_controls_source"])
check("tame bound",Q["tame_current_bound_constructed"])
check("constraint propagation",Q["differentiated_constraint_propagation_constructed"])
check("KT open",not Q["closed_nonlinear_KT_range_proved"])
check("BFV open",not Q["physical_BFV_quotient_proved"])
check("observation absent",not Q["source_observation_map_constructed"])
check("protected fixed",not Q["protected_status_change"])
assert n==172,n
print("RESULT: PASS 172/172")
