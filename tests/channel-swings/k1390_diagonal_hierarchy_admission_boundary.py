#!/usr/bin/env python3
"""Admission-census controls for K1390."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1390-diagonal-hierarchy-admission-boundary.json").read_text());n=0
def check(label,value):
 global n
 assert value,label;n+=1;print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
B,X,Q=D["bridge_census"],D["distance_update"],D["decision"]
check("census sum",B["row_count"]==B["satisfied_count"]+B["conditional_count"]+B["excluded_count"]+B["missing_count"])
check("row count",B["row_count"]==61)
check("satisfied count",B["satisfied_count"]==40)
check("conditional count",B["conditional_count"]==6)
check("excluded count",B["excluded_count"]==11)
check("missing count",B["missing_count"]==4)
check("four new satisfied",len(B["new_satisfied_rows"])==4)
check("four missing",len(B["missing_rows"])==4)
check("three closed effects",len(X["closed"])==3)
check("three sharpened effects",len(X["opened_or_sharpened"])==3)
check("three unchanged effects",len(X["unchanged"])==3)
check("hierarchy",Q["diagonal_covariant_hierarchy_constructed"])
check("top corner removed",Q["finite_high_regularity_top_corner_removed"])
check("Maxwell source",Q["differentiated_maxwell_source_closed"])
check("local bound",Q["local_apriori_continuation_bound_constructed"])
check("existence absent",not Q["smooth_solution_existence_constructed"])
check("global absent",not Q["global_large_data_propagation_constructed"])
check("BV-BFV absent",not Q["fully_coupled_global_nonlinear_BV_BFV_domain_constructed"])
check("source selection absent",not Q["source_selected_reduction_constructed"])
check("cohomology absent",not Q["positive_GU_physical_Hilbert_cohomology_constructed"])
check("native candidates fixed",not Q["k1145_k1150_candidate_counts_move"])
check("protected fixed",not Q["protected_status_change"])
check("ledger fixed","LEDGER_UNCHANGED" in D["source_and_ledger_effect"])
assert n==27,n
print("RESULT: PASS 27/27")
