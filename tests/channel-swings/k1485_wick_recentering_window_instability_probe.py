#!/usr/bin/env python3
"""Hostile mutations for K1485."""
import copy,importlib.util
from pathlib import Path
P=Path(__file__).with_name("k1485_wick_recentering_window_instability.py");S=importlib.util.spec_from_file_location("k1485",P);M=importlib.util.module_from_spec(S);S.loader.exec_module(M)
mutations=[("claim_id","K0"),("recentering_window.necessary_upper_location","wrong"),("recentering_window.excluded_window","wrong"),("recentering_window.weak_trial","zero"),("recentering_window.mosco_failure","holds"),("recentering_window.projective_case","wrong"),("decision.uniform_semiboundedness_requires_subleading_negative_shift",False),("decision.necessary_negative_shift_leading_size","1"),("decision.fixed_fraction_under_recentered_window_excluded",False),("decision.excluded_window_mosco_liminf_holds",True),("decision.ground_energy_recentered_mosco_limit_excluded",True),("decision.boundary_window_is_two_sided_ground_energy_asymptotic",True),("decision.protected_status_change",True)]
for i,(path,value) in enumerate(mutations,1):
 d=copy.deepcopy(M.D);node=d;bits=path.split(".")
 for key in bits[:-1]:node=node[key]
 node[bits[-1]]=value;assert not all(M.validate(d)),path;print(f"PASS {i:02d}: rejected {path}")
print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")
