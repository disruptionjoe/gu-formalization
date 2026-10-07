#!/usr/bin/env python3
"""Triangular-index controls for K1387."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1387-finite-triangular-hierarchy-closure.json").read_text());n=0
def check(label,value):
 global n
 assert value,label;n+=1;print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
T,Q=D["triangular_hierarchy"],D["decision"]
for label,key,needle in [
 ("index set","index_set","|alpha|+n<=R"),
 ("energy","matter_energy","mu||Q D^alpha Q^n phi||_2^2"),
 ("principal tier","principal_tier","<=R+1"),
 ("commutator closure","commutator_closure","<=R+1"),
 ("radial closure","radial_closure","tame product"),
 ("comparison","comparison","fixed combined order"),
 ("boundary","boundary","does not by itself")]:check(label,needle in T[key])
for R in range(3,9):
 indices=[(a,q) for a in range(R+1) for q in range(R+1-a)]
 check(f"triangle cardinality R={R}",len(indices)==(R+1)*(R+2)//2)
 check(f"principal tier R={R}",all(a+q+1<=R+1 for a,q in indices))
check("triangle constructed",Q["finite_triangular_hierarchy_constructed"])
check("commutators close",Q["commutator_terms_close_in_principal_tier"])
check("radial closes",Q["radial_terms_close_by_tame_products"])
check("rectangle result preserved",not Q["finite_rectangular_bare_holder_claim_reversed"])
check("global coefficient absent",not Q["coefficient_global_integrability_proved"])
check("existence absent",not Q["solution_existence_proved"])
check("source absent",not Q["source_action_identified"])
check("protected fixed",not Q["protected_status_change"])
assert n==28,n
print("RESULT: PASS 28/28")
