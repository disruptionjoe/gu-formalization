#!/usr/bin/env python3
"""Controls for K1408 spectral-core admission boundary."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1408-spectral-core-admission-boundary.json").read_text());n=0
def check(label,value):
 global n
 assert value,label;n+=1;print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
C,U,Q=D["bridge_census"],D["distance_update"],D["decision"]
for key,value in (("row_count",76),("satisfied_count",52),("conditional_count",6),("excluded_count",14),("missing_count",4)):check(key,C[key]==value)
check("census sum",sum(C[k] for k in ("satisfied_count","conditional_count","excluded_count","missing_count"))==C["row_count"])
check("four satisfied",len(C["new_satisfied_rows"])==4)
check("one excluded",len(C["new_excluded_rows"])==1)
check("four missing",len(C["missing_rows"])==4)
for needle in ("spectral", "Noether", "direct-limit", "quadratic spectral-weight"):check(f"distance {needle}",needle.lower() in json.dumps(U).lower())
for key in ("charge_spectral_support_invariant","spectral_noether_measure_constructed","global_dense_finite_charge_core_constructed","nonconstant_quadratic_spectral_weight_conservation_route_excluded"):check(key,Q[key])
for key in ("completed_unbounded_charge_global_flow_constructed","full_bv_bfv_boundary_theory_constructed","positive_gu_physical_hilbert_cohomology_constructed","source_selected_reduction_constructed","k1145_k1150_candidate_counts_move","protected_status_change"):check(f"{key} false",not Q[key])
check("source unchanged","SOURCE_REGISTER_UNCHANGED" in D["source_and_ledger_effect"])
check("ledger unchanged","LEDGER_UNCHANGED" in D["source_and_ledger_effect"])
check("K1145/K1150 unchanged","0/7" in D["source_and_ledger_effect"])
assert n==31,n
print("RESULT: PASS 31/31")
