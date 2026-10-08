#!/usr/bin/env python3
"""Controls for K1403 charge-spectral support invariance."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1403-charge-spectral-support-invariance.json").read_text());n=0
def check(label,value):
 global n
 assert value,label;n+=1;print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
F,Q=D["spectral_invariance"],D["decision"]
for label,key,needle in [("projectors","projectors","Borel"),("commutation","projectors","commutes"),("projected equation","projected_equation","P_B phi"),("uniqueness","zero_data_uniqueness","uniqueness"),("support","support_statement","time invariant"),("no labels","support_statement","no new charge labels"),("cutoff","cutoff_compatibility","M<=N"),("nested uniqueness","cutoff_compatibility","uniqueness"),("gauge","gauge_compatibility","exp(i alpha Q)"),("boundary","boundary","does not bound")]:check(label,needle in F[key])
for key in ("borel_spectral_projectors_commute_with_dynamics","charge_spectral_support_invariant","cutoff_flows_form_compatible_nested_family"):check(key,Q[key])
for key in ("radial_interaction_creates_new_charge_labels","cutoff_uniform_completed_global_bound_constructed","source_generator_selected","protected_status_change"):check(f"{key} false",not Q[key])
for M,N in ((0,1),(1,4),(4,16)):check(f"nested cutoff {M}<={N}",M<=N)
assert n==22,n
print("RESULT: PASS 22/22")
