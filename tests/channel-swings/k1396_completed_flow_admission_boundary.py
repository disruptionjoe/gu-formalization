#!/usr/bin/env python3
"""Admission controls for K1396."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1396-completed-flow-admission-boundary.json").read_text());n=0
def check(label,value):
 global n
 assert value,label;n+=1;print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
B,X,Q=D["bridge_census"],D["distance_update"],D["decision"]
check("census sum",B["row_count"]==B["satisfied_count"]+B["conditional_count"]+B["excluded_count"]+B["missing_count"])
for label,key,value in (("rows","row_count",66),("satisfied","satisfied_count",44),("conditional","conditional_count",6),("excluded","excluded_count",12),("missing","missing_count",4)):check(label,B[key]==value)
check("four satisfied rows",len(B["new_satisfied_rows"])==4)
check("one excluded row",len(B["new_excluded_rows"])==1)
check("four missing rows",len(B["missing_rows"])==4)
check("three closed",len(X["closed"])==3)
check("one excluded",len(X["excluded"])==1)
check("three opened",len(X["opened_or_sharpened"])==3)
check("three unchanged",len(X["unchanged"])==3)
for key in ("bounded_charge_local_flow_constructed","completed_triangular_local_flow_constructed","completed_flow_unique_and_constraint_preserving","admissible_gauge_continuation_invariant","global_coefficient_integrability_target_excluded_on_T3"):check(key,Q[key])
for key in ("global_large_data_propagation_constructed","fully_coupled_global_nonlinear_BV_BFV_domain_constructed","source_selected_reduction_constructed","positive_GU_physical_Hilbert_cohomology_constructed","k1145_k1150_candidate_counts_move","protected_status_change"):check(f"{key} false",not Q[key])
check("ledger fixed","LEDGER_UNCHANGED" in D["source_and_ledger_effect"])
assert n==30,n
print("RESULT: PASS 30/30")
