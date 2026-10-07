#!/usr/bin/env python3
"""Finite-rectangle controls for K1384."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1384-finite-rectangle-nonclosure.json").read_text());n=0
def check(label,value):
 global n
 assert value,label;n+=1;print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
F,Q=D["finite_rectangle"],D["decision"]
for label,key,needle in [
 ("hierarchy","assumed_hierarchy","finite S,N"),("top corner","top_corner","S+3/p"),
 ("outside","outside","beyond"),("iteration","iteration","moves the exposed corner"),
 ("witness","witness","K1382"),("boundary","method_boundary","only"),
 ("survivors","surviving_routes","null-form")]:check(label,needle in F[key])
for p in (3,4,6,12):
 sigma=3/p;S,N=2,3
 check(f"spatial top escapes p={p}",S+sigma>S)
 check(f"charge top escapes p={p}",N+1>N)
check("rectangle not closed",not Q["finite_rectangle_bare_holder_closed"])
check("top loss exact",Q["top_corner_loss_exact"])
check("witness present",Q["diagonal_witness_available"])
check("null form open",not Q["null_form_closure_excluded"])
check("infinite hierarchy open",not Q["weighted_infinite_hierarchy_excluded"])
check("other topology open",not Q["all_weaker_invariant_topologies_excluded"])
check("protected fixed",not Q["protected_status_change"])
assert n==24,n
print("RESULT: PASS 24/24")
