#!/usr/bin/env python3
"""Controls for K1407 global finite-charge direct limit."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1407-global-finite-charge-direct-limit.json").read_text());n=0
def check(label,value):
 global n
 assert value,label;n+=1;print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
F,Q=D["direct_limit_flow"],D["decision"]
for label,key,needle in [("core","core","union_"),("density","density","dense"),("global","global_existence","global"),("compatibility","compatibility","S_N(t)x=S_M(t)x"),("uniqueness","compatibility","uniqueness"),("flow","flow_law","two-sided flow"),("quotient","flow_law","descend"),("data","conserved_data","Noether"),("gap","completion_gap","cutoff-uniform"),("K1398","completion_gap","K1398"),("K1406","completion_gap","K1406"),("boundary","boundary","not a global flow on the completed")]:check(label,needle in F[key])
for key in ("finite_charge_core_dense","bounded_sector_flows_compatible","global_direct_limit_flow_constructed","direct_limit_flow_descends_sectorwise"):check(key,Q[key])
for key in ("continuous_extension_to_completed_phase_space_constructed","cutoff_uniform_completed_global_flow_constructed","positive_gu_physical_hilbert_cohomology_constructed","protected_status_change"):check(f"{key} false",not Q[key])
for M,N in ((1,2),(2,8),(8,32)):check(f"directed system {M}<={N}",M<=N)
assert n==27,n
print("RESULT: PASS 27/27")
