#!/usr/bin/env python3
"""Composition controls for K1340's free-control physical boundary."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1340-free-control-physical-admission-boundary.json").read_text()); n=0
def check(label,value):
 global n; assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
C=D["free_control_census"]; Q=D["decision"]
check("fourteen rows",C["row_count"]==14)
check("counts close",C["satisfied_count"]+C["conditional_count"]+C["missing_count"]==C["row_count"])
check("nine satisfied",C["satisfied_count"]==9 and len(C["satisfied_rows"])==9)
check("one conditional",C["conditional_count"]==1 and len(C["conditional_rows"])==1)
check("four missing",C["missing_count"]==4 and len(C["missing_rows"])==4)
check("trivial-complex ceiling",C["conditional_rows"]==["positive_degree_zero_cohomology_for_the_trivial_constraint_complex_only"])
check("free package",Q["free_common_domain_positive_energy_causality_and_boundary_constructed"] and Q["principal_series_internal_equivariance_constructed"])
check("carrier-only obstruction excluded",Q["carrier_only_obstruction_to_free_causal_positive_dynamics_excluded_for_this_control"])
check("source ceiling",not Q["source_charge_or_chamber_selected"])
check("interaction ceiling",not Q["interacting_gu_constraint_complex_constructed"])
check("cohomology ceiling",not Q["nontrivial_gu_physical_cohomology_constructed"])
check("observation ceiling",not Q["observed_state_map_constructed"])
check("candidate counts fixed",not Q["k1145_k1150_candidate_counts_move"])
check("protected fixed",not Q["protected_status_change"])
check("ledger fixed","LEDGER_UNCHANGED" in D["source_and_ledger_effect"])
assert n==20; print("RESULT: PASS 20/20")
