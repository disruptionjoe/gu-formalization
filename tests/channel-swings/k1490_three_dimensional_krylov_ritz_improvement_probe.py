#!/usr/bin/env python3
"""Hostile mutations for K1490."""
import copy,importlib.util
from pathlib import Path
P=Path(__file__).with_name("k1490_three_dimensional_krylov_ritz_improvement.py")
S=importlib.util.spec_from_file_location("k1490",P);M=importlib.util.module_from_spec(S);S.loader.exec_module(M)
mutations=[("claim_id","K0000"),("three_dimensional_ritz.basis","none"),("three_dimensional_ritz.multiplication_matrix","none"),
 ("three_dimensional_ritz.moment_bounds","unbounded"),("three_dimensional_ritz.fixed_trial","none"),
 ("three_dimensional_ritz.free_cost","N^3"),("three_dimensional_ritz.ground_energy_upper","old"),
 ("three_dimensional_ritz.strict_consequence","sharp"),("decision.three_dimensional_krylov_compression_constructed",False),
 ("decision.hypercontractive_eta_absolute_upper",0),("decision.fixed_trial_t_denominator",0),
 ("decision.strict_improvement_constant","0"),("decision.ground_energy_upper_correction","-g sigma_N"),
 ("decision.two_dimensional_minus_one_coefficient_variationally_sharp",True),
 ("decision.ground_energy_asymptotic_determined",True),("decision.protected_status_change",True)]
for i,(path,value) in enumerate(mutations,1):
 d=copy.deepcopy(M.D);node=d;bits=path.split(".")
 for key in bits[:-1]:node=node[key]
 node[bits[-1]]=value
 assert not all(M.validate(d)),path;print(f"PASS {i:02d}: rejected {path}")
print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")
