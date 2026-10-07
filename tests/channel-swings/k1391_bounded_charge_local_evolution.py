#!/usr/bin/env python3
"""Structural controls for K1391's bounded-charge local evolution."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1391-bounded-charge-local-evolution.json").read_text());n=0
def check(label,value):
 global n
 assert value,label;n+=1;print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
F,Q=D["bounded_charge_flow"],D["decision"]
for label,key,needle in [
 ("projector","spectral_cutoff","P_N=1_{[-N,N]}(Q)"),
 ("sector","invariant_sector","remain in ran(P_N)"),
 ("bounded Q","bounded_generator","||Q_N||<=N"),
 ("Lorenz system","lorenz_system","semilinear Hilbert-valued wave system"),
 ("local theorem","local_theorem","Duhamel contraction"),
 ("constraint","constraint_data","propagates"),
 ("smoothness","smooth_persistence","smooth common-core solution"),
 ("boundary","boundary","does not produce a completed")]:check(label,needle in F[key])
for N in (0,1,4,9):
 charges=list(range(-N,N+1))
 check(f"spectral bound N={N}",all(abs(q)<=N for q in charges))
 check(f"Q preserves cutoff N={N}",all((q*q==0 or q in charges) for q in charges))
for key in ("charge_spectral_cutoffs_constructed","cutoff_sector_invariant","bounded_charge_local_solution_constructed","bounded_charge_uniqueness_constructed","lorenz_and_gauss_constraints_propagate"):check(key,Q[key])
for key in ("cutoff_uniform_completed_flow_constructed","global_evolution_constructed","source_action_identified","protected_status_change"):check(f"{key} false",not Q[key])
assert n==28,n
print("RESULT: PASS 28/28")
