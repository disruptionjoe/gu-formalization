#!/usr/bin/env python3
"""Composition controls for K1345's joint physical-admission boundary."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1345-physical-control-joint-admission-boundary.json").read_text()); n=0
def check(label,value):
 global n; assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
C=D["joint_control_census"]; Q=D["decision"]
check("twenty-one rows",C["row_count"]==21)
check("counts close",C["satisfied_count"]+C["conditional_count"]+C["missing_count"]==C["row_count"])
check("fifteen satisfied",C["satisfied_count"]==15 and len(C["satisfied_rows"])==15)
check("two conditional",C["conditional_count"]==2 and len(C["conditional_rows"])==2)
check("four missing",C["missing_count"]==4 and len(C["missing_rows"])==4)
check("Maxwell conditional ceiling",C["conditional_rows"][0].endswith("free_Maxwell_quotient_only"))
check("chosen export conditional","choosing_eta" in C["conditional_rows"][1])
check("gauge carrier obstruction excluded",Q["carrier_obstruction_to_nontrivial_free_gauge_reduction_excluded_for_this_control"])
check("nonlinear carrier obstruction excluded",Q["carrier_obstruction_to_defocusing_nonlinear_positive_evolution_excluded_for_this_control"])
check("invariant scalar export excluded",Q["full_G_invariant_bounded_scalar_export_excluded"])
check("separate actions not composed",not Q["separate_controls_compose_to_one_action"])
check("interacting GU complex absent",not Q["source_owned_interacting_gu_constraint_complex_constructed"])
check("GU cohomology absent",not Q["gu_physical_cohomology_constructed"])
check("GU export absent",not Q["gu_observed_state_map_constructed"])
check("candidate counts fixed",not Q["k1145_k1150_candidate_counts_move"])
check("protected fixed",not Q["protected_status_change"])
check("ledger fixed","LEDGER_UNCHANGED" in D["source_and_ledger_effect"])
assert n==21; print("RESULT: PASS 21/21")
