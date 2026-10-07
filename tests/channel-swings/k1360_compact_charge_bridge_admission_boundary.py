#!/usr/bin/env python3
"""Integrated compact-charge bridge census for K1360."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/"lab/process/k1360-compact-charge-bridge-admission-boundary.json").read_text());n=0
def check(label,value):
 global n;assert value,label;n+=1;print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
C,U,Q=D["bridge_census"],D["distance_update"],D["decision"]
check("row arithmetic",C["row_count"]==C["satisfied_count"]+C["conditional_count"]+C["excluded_count"]+C["missing_count"])
check("six new satisfied",len(C["new_satisfied_rows"])==6)
check("conditional length",len(C["conditional_rows"])==C["conditional_count"])
check("excluded length",len(C["excluded_rows"])==C["excluded_count"])
check("missing length",len(C["missing_rows"])==C["missing_count"])
check("compact circle row",any("maximal_compact_circle" in r for r in C["new_satisfied_rows"]))
check("positive kinetic row",any("positive_quadratic" in r for r in C["new_satisfied_rows"]))
check("nonuniform charge row",any("nonuniform" in r for r in C["new_satisfied_rows"]))
check("unbounded generator row",any("unbounded_self_adjoint" in r for r in C["new_satisfied_rows"]))
check("common core row",any("common_charge_core" in r for r in C["new_satisfied_rows"]))
check("BV core row",any("BRST_BV_BFV" in r for r in C["new_satisfied_rows"]))
check("source selection missing",any("source_owned_selection" in r for r in C["missing_rows"]))
check("global quotient missing",any("physical_Hilbert" in r for r in C["missing_rows"]))
check("four closed distances",len(U["closed"])==4)
check("three sharpened debts",len(U["opened_or_sharpened"])==3)
check("compact route built",Q["maximal_compact_route_mathematically_constructed"])
check("nonuniform route built",Q["nonuniform_charge_route_mathematically_constructed"])
check("operator core built",Q["operator_charge_interacting_core_constructed"])
check("source reduction absent",not Q["source_selected_reduction_constructed"])
check("observed map absent",not Q["actual_observed_carrier_charge_map_constructed"])
check("global domain absent",not Q["completed_global_nonlinear_domain_constructed"])
check("physical cohomology absent",not Q["positive_physical_Hilbert_cohomology_constructed"])
check("native counts fixed",not Q["k1145_k1150_candidate_counts_move"])
check("protected fixed",not Q["protected_status_change"])
assert n==29
print("RESULT: PASS 29/29")
