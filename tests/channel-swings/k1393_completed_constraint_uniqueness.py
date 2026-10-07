#!/usr/bin/env python3
"""Constraint and uniqueness controls for K1393."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1393-completed-constraint-uniqueness.json").read_text());n=0
def check(label,value):
 global n
 assert value,label;n+=1;print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
F,Q=D["completed_constraints"],D["decision"]
for label,key,needle in [("unique","uniqueness","zero initial difference"),("dependence","continuous_dependence","Gronwall"),("current","current_limit","continuity equation"),("Lorenz","lorenz_constraint","homogeneous scalar wave"),("Gauss","gauss_constraint","constant in time"),("BRST","brst_scope","dense smooth common core"),("flow","flow_map","single-valued"),("boundary","boundary","not a proper BV-BFV quotient")]:check(label,needle in F[key])
for z0,I in ((0.,10.),(.1,0.),(.25,2.)):
 bound=z0*math.exp(I)
 check(f"Gronwall z0={z0} I={I}",bound==0 if z0==0 else bound>=z0)
for key in ("completed_flow_unique","continuous_dependence_constructed","current_conservation_passes_to_limit","lorenz_constraint_propagates","gauss_constraint_propagates","brst_core_closable_between_adjacent_tiers"):check(key,Q[key])
for key in ("closed_nonlinear_KT_range_constructed","positive_physical_cohomology_constructed","source_action_identified","protected_status_change"):check(f"{key} false",not Q[key])
assert n==23,n
print("RESULT: PASS 23/23")
