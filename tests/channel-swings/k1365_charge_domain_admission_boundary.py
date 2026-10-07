#!/usr/bin/env python3
"""Integrated charge-domain admission census for K1365."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/"lab/process/k1365-charge-domain-admission-boundary.json").read_text());n=0
def check(label,value):
 global n;assert value,label;n+=1;print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
C,U,Q=D["bridge_census"],D["distance_update"],D["decision"]
check("row arithmetic",C["row_count"]==C["satisfied_count"]+C["conditional_count"]+C["excluded_count"]+C["missing_count"])
check("three new satisfied",len(C["new_satisfied_rows"])==3)
check("one new excluded",len(C["new_excluded_rows"])==1)
check("conditional length",len(C["conditional_rows"])==C["conditional_count"])
check("excluded length",len(C["excluded_rows"])==C["excluded_count"])
check("missing length",len(C["missing_rows"])==C["missing_count"])
check("graph domain row",any("graph_domain" in x for x in C["new_satisfied_rows"]))
check("radial row",any("radial" in x for x in C["new_satisfied_rows"]))
check("global flow row",any("global_defocusing" in x for x in C["new_satisfied_rows"]))
check("energy implication excluded",any("ordinary_positive" in x for x in C["new_excluded_rows"]))
check("source selection missing",any("source_owned_selection" in x for x in C["missing_rows"]))
check("coupled quotient missing",any("fully_coupled" in x for x in C["missing_rows"]))
check("three closed",len(U["closed"])==3)
check("one excluded distance",len(U["excluded"])==1)
check("two sharpened",len(U["opened_or_sharpened"])==2)
check("graph domain decision",Q["completed_local_gauge_graph_domain_constructed"])
check("radial decision",Q["radial_scalar_graph_domain_preserved"])
check("separate global flow",Q["separate_global_causal_charge_regular_flow_constructed"])
check("energy coercivity excluded",Q["ordinary_coupled_energy_graph_coercivity_excluded"])
check("source reduction absent",not Q["source_selected_reduction_constructed"])
check("coupled BV absent",not Q["fully_coupled_global_BV_BFV_domain_constructed"])
check("physical cohomology absent",not Q["positive_physical_Hilbert_cohomology_constructed"])
check("native counts fixed",not Q["k1145_k1150_candidate_counts_move"])
check("protected fixed",not Q["protected_status_change"])
assert n==29;print("RESULT: PASS 29/29")
