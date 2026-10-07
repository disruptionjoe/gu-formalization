#!/usr/bin/env python3
"""Admission-census controls for K1375."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1375-nonlinear-gauss-admission-boundary.json").read_text());n=0
def check(label,value):
 global n
 assert value,label;n+=1;print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
B,X,Q=D["bridge_census"],D["distance_update"],D["decision"]
check("census sum",B["row_count"]==B["satisfied_count"]+B["conditional_count"]+B["excluded_count"]+B["missing_count"])
check("row count",B["row_count"]==49)
check("satisfied count",B["satisfied_count"]==33)
check("conditional count",B["conditional_count"]==4)
check("excluded count",B["excluded_count"]==8)
check("missing count",B["missing_count"]==4)
check("three new satisfied",len(B["new_satisfied_rows"])==3)
check("one new excluded",len(B["new_excluded_rows"])==1)
for row in ("source_owned_selection_and_normalization_of_the_compact_charge_reduction_on_the_observed_carrier","identification_with_one_source_action_derived_interacting_constraint_complex","closed_fully_coupled_global_nonlinear_BV_BFV_quotient_with_positive_physical_Hilbert_cohomology","source_owned_observed_state_and_export_map"):
 check(f"missing row {row[:20]}",row in B["missing_rows"])
check("closed effects",len(X["closed"])==3)
check("excluded effect",len(X["excluded"])==1)
check("sharpened effects",len(X["opened_or_sharpened"])==2)
check("Gauss layer closed",Q["gauss_functional_layer_closed"])
check("original energy rejected",not Q["original_energy_sufficient"])
check("global estimate absent",not Q["global_mixed_graph_estimate_constructed"])
check("BV-BFV absent",not Q["fully_coupled_global_nonlinear_BV_BFV_domain_constructed"])
check("source selection absent",not Q["source_selected_reduction_constructed"])
check("GU cohomology absent",not Q["positive_GU_physical_Hilbert_cohomology_constructed"])
check("native candidates fixed",not Q["k1145_k1150_candidate_counts_move"])
check("protected fixed",not Q["protected_status_change"])
check("ledger fixed","LEDGER_UNCHANGED" in D["source_and_ledger_effect"])
assert n==26,n
print("RESULT: PASS 26/26")
