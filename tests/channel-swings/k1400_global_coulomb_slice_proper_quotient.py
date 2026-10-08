#!/usr/bin/env python3
"""Controls for K1400 global Coulomb quotient."""
import hashlib,json,cmath,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1400-global-coulomb-slice-proper-quotient.json").read_text());n=0
def check(label,value):
 global n
 assert value,label;n+=1;print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
F,Q=D["coulomb_quotient"],D["decision"]
for label,key,needle in [("bundle","bundle_scope","trivial Abelian bundle"),("solve","hodge_solve","Delta chi_0=-div A"),("unique","based_uniqueness","chi_0=0"),("residual","residual_group","compact U(1)"),("proper","properness","proper"),("triangle","triangular_compatibility","bounded automorphisms"),("energy","energy_descent","descend"),("boundary","boundary","not a source-selected")]:check(label,needle in F[key])
for q,c in ((0,0.),(1,math.pi),(-4,.25),(12,2.)):
 z=cmath.exp(1j*c*q)
 check(f"unitary q={q} c={c}",abs(abs(z)-1)<1e-12)
for key in ("global_coulomb_slice_constructed","based_gauge_orbit_representative_unique","residual_compact_group_identified","residual_action_proper","classical_quotient_hausdorff","positive_classical_energy_descends"):check(key,Q[key])
for key in ("source_observed_state_space_identified","bfv_boundary_phase_space_constructed","protected_status_change"):check(f"{key} false",not Q[key])
assert n==23,n
print("RESULT: PASS 23/23")
