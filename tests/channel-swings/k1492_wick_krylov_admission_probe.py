#!/usr/bin/env python3
"""Hostile mutations for K1492."""
import copy,importlib.util
from pathlib import Path
P=Path(__file__).with_name("k1492_wick_krylov_admission.py")
S=importlib.util.spec_from_file_location("k1492",P);M=importlib.util.module_from_spec(S);S.loader.exec_module(M)
mutations=[("claim_id","K0000"),("bridge_census.row_count",178),("bridge_census.satisfied_count",110),
 ("bridge_census.conditional_count",11),("bridge_census.excluded_count",53),("bridge_census.missing_count",3),
 ("bridge_census.new_satisfied_rows",[]),("bridge_census.new_excluded_rows",[]),("bridge_census.missing_rows",[]),
 ("decision.higher_chaos_krylov_direction_constructed",False),("decision.two_dimensional_ritz_quasimode_excluded",False),
 ("decision.strict_variational_improvement_proved",False),("decision.enlarged_scalar_and_brst_window_excluded",False),
 ("decision.matching_ground_energy_lower_asymptotic_constructed",True),("decision.ground_energy_recentered_limit_constructed",True),
 ("decision.full_spacetime_pde_repair_constructed",True),("decision.source_selected_reduction_constructed",True),
 ("decision.k1145_k1150_candidate_counts_move",True),("decision.protected_status_change",True),
 ("source_and_ledger_effect","LEDGER_MOVED")]
for i,(path,value) in enumerate(mutations,1):
 d=copy.deepcopy(M.D);node=d;bits=path.split(".")
 for key in bits[:-1]:node=node[key]
 node[bits[-1]]=value
 assert not all(M.validate(d)),path;print(f"PASS {i:02d}: rejected {path}")
print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")
