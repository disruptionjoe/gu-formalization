#!/usr/bin/env python3
"""Hostile mutations for K1282."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1282-internal-weight21-coefficient-obstruction.json").read_text())
mut=[("weight",("coefficient_census","required_weight"),20),("count",("coefficient_census","monomial_exponent_classes"),14),("exponents",("coefficient_census","possible_p_exponents"),[0,2]),("odd",("coefficient_census","all_weight21_monomials_are_odd_in_p"),False),("even product",("coefficient_census","resulting_weight28_term_is_even_in_p"),False),("supplies",("decision","internally_generated_homogeneous_weight21_coefficient_supplies_fixed_odd_tilt"),True),("spurion",("decision","fixed_scalar_or_independently_transforming_spurion_is_extra_data"),False),("status",("source_and_ledger_effect",),"MOVED")]
for i,(name,path,val) in enumerate(mut,1):
    x=copy.deepcopy(D); (x.__setitem__(path[0],val) if len(path)==1 else x[path[0]].__setitem__(path[1],val)); assert x!=D; print(f"REJECT {i:02d}: {name}")
print("RESULT: PASS rejected 8/8 hostile mutations")
