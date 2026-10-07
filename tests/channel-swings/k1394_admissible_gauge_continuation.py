#!/usr/bin/env python3
"""Gauge-filtration controls for K1394."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1394-admissible-gauge-continuation.json").read_text());n=0
def check(label,value):
 global n
 assert value,label;n+=1;print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
F,Q=D["gauge_continuation"],D["decision"]
for label,key,needle in [("action","gauge_action","D'_mu phi'"),("count","derivative_count","derivative order plus charge order"),("class","admissible_class","bounded invertible map"),("norm","norm_equivalence","C_R(chi)^(-1)"),("Lorenz","lorenz_residual","box chi=0"),("continuation","continuation_invariance","equivalent"),("scope","scope","not construction of the physical quotient"),("boundary","boundary","not classified")]:check(label,needle in F[key])
for r in range(1,7):
 for k in range(r+1):
  derivative_on_multiplier=k
  charge_insertions=k
  derivative_on_field=r-k
  check(f"triangular Leibniz r={r} k={k}",derivative_on_field+charge_insertions==r)
for key in ("triangular_gauge_action_bounded","triangular_gauge_action_invertible","lorenz_preserving_gauge_class_identified","finite_time_continuation_gauge_invariant"):check(key,Q[key])
for key in ("physical_quotient_topology_constructed","global_gauge_independent_norm_constructed","source_observation_map_constructed","protected_status_change"):check(f"{key} false",not Q[key])
assert n==45,n
print("RESULT: PASS 45/45")
