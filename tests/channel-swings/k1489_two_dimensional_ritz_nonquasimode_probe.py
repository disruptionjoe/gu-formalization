#!/usr/bin/env python3
"""Hostile mutations for K1489."""
import copy,importlib.util
from pathlib import Path
P=Path(__file__).with_name("k1489_two_dimensional_ritz_nonquasimode.py")
S=importlib.util.spec_from_file_location("k1489",P);M=importlib.util.module_from_spec(S);S.loader.exec_module(M)
mutations=[
 ("claim_id","K0000"),("nonquasimode_boundary.ritz_vector","none"),
 ("nonquasimode_boundary.higher_chaos_test","none"),("nonquasimode_boundary.interaction_residual","zero"),
 ("nonquasimode_boundary.free_residual","N^3"),("nonquasimode_boundary.residual_lower_bound","zero"),
 ("nonquasimode_boundary.consequence","quasimode"),("decision.higher_chaos_residual_constructed",False),
 ("decision.interaction_residual_scale","0"),("decision.free_residual_order_upper","N^3"),
 ("decision.ritz_residual_lower_fraction","0"),("decision.two_dimensional_ritz_vector_is_o_sigma_quasimode",True),
 ("decision.minus_one_is_full_ground_energy_leading_coefficient",True),
 ("decision.matching_ground_energy_lower_bound_proved",True),("decision.protected_status_change",True)]
for i,(path,value) in enumerate(mutations,1):
 d=copy.deepcopy(M.D);node=d;bits=path.split(".")
 for key in bits[:-1]:node=node[key]
 node[bits[-1]]=value
 assert not all(M.validate(d)),path
 print(f"PASS {i:02d}: rejected {path}")
print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")
