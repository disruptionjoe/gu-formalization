#!/usr/bin/env python3
"""Integrated bridge-admission census for K1355."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1355-principal-series-gauge-bridge-admission-boundary.json").read_text()); n=0
def check(label,value):
 global n; assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
C=D["bridge_census"]; Q=D["decision"]
check("row arithmetic",C["row_count"]==C["satisfied_count"]+C["conditional_count"]+C["excluded_count"]+C["missing_count"])
check("excluded length",len(C["excluded_rows"])==C["excluded_count"])
check("rows unique",len(set(C["satisfied_rows"]+C["conditional_rows"]+C["excluded_rows"]+C["missing_rows"]))==C["row_count"])
check("character excluded",any("character_to_U1" in row for row in C["excluded_rows"]))
check("uniform phase excluded",any("uniform_scalar_phase" in row for row in C["excluded_rows"]))
check("charged sector excluded",any("fixed_charge_sector" in row for row in C["excluded_rows"]))
check("finite map excluded",any("finite_source_fibre" in row for row in C["excluded_rows"]))
check("positive split kinetic excluded",any("positive_definite" in row for row in C["excluded_rows"]))
check("source reduction missing",any("source_owned_charge" in row for row in C["missing_rows"]))
check("global quotient missing",any("physical_Hilbert" in row for row in C["missing_rows"]))
check("character decision",Q["k1346_u1_direct_full_G_character_route_excluded"])
check("phase decision",Q["k1346_u1_internal_uniform_phase_route_excluded"])
check("sector decision",Q["full_G_invariant_nonzero_fixed_charge_route_excluded"])
check("finite map decision",Q["pointwise_finite_source_fibre_linear_bridge_excluded"])
check("kinetic decision",Q["positive_full_split_quadratic_gauge_kinetic_route_excluded"])
check("not all bridges excluded",not Q["all_source_to_control_bridges_excluded"])
check("compact route unbuilt",not Q["maximal_compact_or_stabilizer_route_constructed"])
check("nonlinear route unbuilt",not Q["nonlinear_or_nonlocal_source_bridge_constructed"])
check("source complex unbuilt",not Q["source_owned_interacting_gu_constraint_complex_constructed"])
check("global quotient unbuilt",not Q["closed_global_nonlinear_physical_hilbert_quotient_constructed"])
check("native counts fixed",not Q["k1145_k1150_candidate_counts_move"])
check("protected fixed",not Q["protected_status_change"])
check("surviving routes retained",len(D["surviving_bridge_routes"])==5)
assert n==28; print("RESULT: PASS 28/28")
