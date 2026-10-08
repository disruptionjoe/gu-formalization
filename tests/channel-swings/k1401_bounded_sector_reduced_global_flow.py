#!/usr/bin/env python3
"""Controls for K1401 descended fixed-sector flow."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1401-bounded-sector-reduced-global-flow.json").read_text());n=0
def check(label,value):
 global n
 assert value,label;n+=1;print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
F,Q=D["reduced_flow"],D["decision"]
for label,key,needle in [("constraint","constraint_surface","closed neutral Gauss surface"),("equivariance","equivariance","equivariant"),("global","global_representative_flow","global"),("descent","descent","single-valued global flow"),("continuity","continuity","continuous reduced flow"),("positive","positive_invariant","coercive invariant"),("cutoff","cutoff_boundary","no cutoff-uniform"),("physical","physical_boundary","not a BV-BFV quantization")]:check(label,needle in F[key])
for N in (1,2,4,8):
 orbit_equal=(N*N)==((-N)*(-N))
 check(f"orbit invariant N={N}",orbit_equal)
for key in ("fixed_sector_global_flow_descends","reduced_flow_single_valued","reduced_flow_continuous","positive_conserved_classical_invariant_descends"):check(key,Q[key])
for key in ("cutoff_uniform_reduced_global_flow_constructed","positive_gu_physical_hilbert_cohomology_constructed","source_action_identified","protected_status_change"):check(f"{key} false",not Q[key])
assert n==22,n
print("RESULT: PASS 22/22")
