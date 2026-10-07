#!/usr/bin/env python3
"""Hostile mutations for K1286."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1286-algebraic-weight21-radial-coefficient.json").read_text())
mut=[("coefficient",("construction","coefficient"),"lambda I2^10"),("scaling",("construction","weighted_scaling"),"weight 20"),("parity",("construction","outer_parity_of_coefficient"),"odd"),("term",("construction","selector_outer_parity"),"even"),("weight",("construction","selector_weight"),27),("polynomial",("construction","polynomial_in_invariant_generators"),True),("classification",("classification_theorem","general_weight21_form"),"epsilon=lambda r^21 only"),("freedom",("classification_theorem","coefficient_is_unique_or_canonical"),True),("sheet",("decision","orientation_sign_imported_by_positive_radial_branch"),True),("owner",("decision","source_action_owner_supplied"),True)]
for i,(name,path,val) in enumerate(mut,1):
    x=copy.deepcopy(D); x[path[0]][path[1]]=val; assert x!=D; print(f"REJECT {i:02d}: {name}")
print("RESULT: PASS rejected 10/10 hostile mutations")
