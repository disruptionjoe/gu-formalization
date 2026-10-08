#!/usr/bin/env python3
"""Hostile mutations for K1484."""
import copy, importlib.util
from pathlib import Path
P=Path(__file__).with_name("k1484_vacuum_fourth_chaos_ritz_asymptotic.py"); S=importlib.util.spec_from_file_location("k1484",P); M=importlib.util.module_from_spec(S); S.loader.exec_module(M)
mutations=[
 ("claim_id","K0"),("ritz_asymptotic.basis","wrong"),("ritz_asymptotic.centered_matrix","wrong"),("ritz_asymptotic.diagonal_order","wrong"),("ritz_asymptotic.lower_eigenvalue","wrong"),("ritz_asymptotic.leading_order","wrong"),("ritz_asymptotic.ground_energy_upper","wrong"),("ritz_asymptotic.eigenvector","wrong"),("ritz_asymptotic.weak_limit","zero"),("decision.exact_two_by_two_compression_constructed",False),("decision.ritz_lower_eigenvalue_ratio_limit",0),("decision.ground_energy_upper_leading_correction","+g sigma_N"),("decision.ritz_eigenvector_has_nonzero_weak_vacuum_limit",False),("decision.matching_ground_energy_lower_bound_proved",True),("decision.ground_energy_asymptotic_determined",True),("decision.ground_energy_recentered_limit_constructed",True),("decision.protected_status_change",True)]
for i,(path,value) in enumerate(mutations,1):
 d=copy.deepcopy(M.D); node=d; bits=path.split(".")
 for key in bits[:-1]: node=node[key]
 node[bits[-1]]=value; assert not all(M.validate(d)),path; print(f"PASS {i:02d}: rejected {path}")
print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")
