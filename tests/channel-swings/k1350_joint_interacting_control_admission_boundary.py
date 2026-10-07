#!/usr/bin/env python3
"""Integrated admission census for K1350."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1350-joint-interacting-control-admission-boundary.json").read_text()); n=0
def check(label,value):
 global n; assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
C=D["joint_control_census"]; Q=D["decision"]
check("row arithmetic",C["row_count"]==C["satisfied_count"]+C["conditional_count"]+C["missing_count"])
check("satisfied length",len(C["satisfied_rows"])==C["satisfied_count"])
check("conditional length",len(C["conditional_rows"])==C["conditional_count"])
check("missing length",len(C["missing_rows"])==C["missing_count"])
check("rows unique",len(set(C["satisfied_rows"]+C["conditional_rows"]+C["missing_rows"]))==C["row_count"])
check("one coupled action row","one_repository_owned_covariantly_coupled_gauge_matter_action" in C["satisfied_rows"])
check("interacting algebra row","interacting_Gauss_BRST_classical_BV_and_boundary_BFV_algebra" in C["satisfied_rows"])
check("nonlinear observable row","bounded_nonlinear_gauge_and_internal_G_invariant_scalar_observable" in C["satisfied_rows"])
check("linearized positivity conditional",any("vacuum_linearized" in row for row in C["conditional_rows"]))
check("nonlinear semantics conditional",any("without_source_observation_semantics" in row for row in C["conditional_rows"]))
check("source action missing",any("source_action" in row for row in C["missing_rows"]))
check("global Hilbert quotient missing",any("physical_Hilbert" in row for row in C["missing_rows"]))
check("source observation missing",any("source_owned_observed" in row for row in C["missing_rows"]))
check("one action decision",Q["prior_separate_controls_replaced_by_one_repository_interacting_action"])
check("gauge carrier boundary",Q["carrier_obstruction_to_classical_interacting_gauge_algebra_excluded_for_this_control"])
check("positive energy boundary",Q["carrier_obstruction_to_positive_constrained_classical_energy_excluded_for_this_control"])
check("map-class escape",Q["bounded_linear_scalar_no_go_bypassed_by_explicit_nonlinear_map_class"])
check("source complex absent",not Q["source_owned_interacting_gu_constraint_complex_constructed"])
check("global quotient absent",not Q["closed_global_nonlinear_physical_hilbert_quotient_constructed"])
check("GU cohomology absent",not Q["gu_physical_cohomology_constructed"])
check("GU observation absent",not Q["gu_observed_state_map_constructed"])
check("K1145 K1150 fixed",not Q["k1145_k1150_candidate_counts_move"])
check("protected fixed",not Q["protected_status_change"])
assert n==27; print("RESULT: PASS 27/27")
