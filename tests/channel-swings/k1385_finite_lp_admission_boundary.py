#!/usr/bin/env python3
"""Admission-census controls for K1385."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1385-finite-lp-admission-boundary.json").read_text());n=0
def check(label,value):
 global n
 assert value,label;n+=1;print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
B,X,Q=D["bridge_census"],D["distance_update"],D["decision"]
check("census sum",B["row_count"]==B["satisfied_count"]+B["conditional_count"]+B["excluded_count"]+B["missing_count"])
check("row count",B["row_count"]==57)
check("satisfied count",B["satisfied_count"]==36)
check("conditional count",B["conditional_count"]==6)
check("excluded count",B["excluded_count"]==11)
check("missing count",B["missing_count"]==4)
check("two new satisfied",len(B["new_satisfied_rows"])==2)
check("one new conditional",len(B["new_conditional_rows"])==1)
check("one new excluded",len(B["new_excluded_rows"])==1)
check("four missing",len(B["missing_rows"])==4)
check("two closed effects",len(X["closed"])==2)
check("one conditional effect",len(X["conditional"])==1)
check("one excluded effect",len(X["excluded"])==1)
check("two sharpened effects",len(X["opened_or_sharpened"])==2)
check("finite-p boundary",Q["sharp_finite_p_boundary_constructed"])
check("diagonal obstruction",Q["diagonal_obstruction_constructed"])
check("conditional staircase",Q["conditional_mixed_staircase_estimate_constructed"])
check("rectangle closure absent",not Q["finite_rectangle_bare_holder_closure_constructed"])
check("global alternative absent",not Q["global_null_form_or_weighted_hierarchy_constructed"])
check("BV-BFV absent",not Q["fully_coupled_global_nonlinear_BV_BFV_domain_constructed"])
check("source selection absent",not Q["source_selected_reduction_constructed"])
check("cohomology absent",not Q["positive_GU_physical_Hilbert_cohomology_constructed"])
check("native candidates fixed",not Q["k1145_k1150_candidate_counts_move"])
check("protected fixed",not Q["protected_status_change"])
check("ledger fixed","LEDGER_UNCHANGED" in D["source_and_ledger_effect"])
assert n==27,n
print("RESULT: PASS 27/27")
