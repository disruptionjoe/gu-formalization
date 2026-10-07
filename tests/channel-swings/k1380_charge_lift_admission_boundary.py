#!/usr/bin/env python3
"""Admission-census controls for K1380."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1380-charge-lift-admission-boundary.json").read_text());n=0
def check(label,value):
 global n
 assert value,label;n+=1;print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
B,X,Q=D["bridge_census"],D["distance_update"],D["decision"]
check("census sum",B["row_count"]==B["satisfied_count"]+B["conditional_count"]+B["excluded_count"]+B["missing_count"])
check("row count",B["row_count"]==53)
check("satisfied count",B["satisfied_count"]==34)
check("conditional count",B["conditional_count"]==5)
check("excluded count",B["excluded_count"]==10)
check("missing count",B["missing_count"]==4)
check("one new satisfied",len(B["new_satisfied_rows"])==1)
check("one new conditional",len(B["new_conditional_rows"])==1)
check("two new excluded",len(B["new_excluded_rows"])==2)
check("four missing",len(B["missing_rows"])==4)
check("one closed effect",len(X["closed"])==1)
check("one conditional effect",len(X["conditional"])==1)
check("two excluded effects",len(X["excluded"])==2)
check("two sharpened effects",len(X["opened_or_sharpened"])==2)
check("free lift constructed",Q["free_invariant_charge_lift_constructed"])
check("one-sided rejected",Q["one_sided_k1372_phase_space_rejected"])
check("conditional estimate",Q["conditional_coupled_estimate_constructed"])
check("base closure absent",not Q["base_energy_global_closure_constructed"])
check("BV-BFV absent",not Q["fully_coupled_global_nonlinear_BV_BFV_domain_constructed"])
check("source selection absent",not Q["source_selected_reduction_constructed"])
check("cohomology absent",not Q["positive_GU_physical_Hilbert_cohomology_constructed"])
check("native candidates fixed",not Q["k1145_k1150_candidate_counts_move"])
check("protected fixed",not Q["protected_status_change"])
check("ledger fixed","LEDGER_UNCHANGED" in D["source_and_ledger_effect"])
assert n==26,n
print("RESULT: PASS 26/26")
