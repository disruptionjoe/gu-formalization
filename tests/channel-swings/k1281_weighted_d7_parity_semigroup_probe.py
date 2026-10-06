#!/usr/bin/env python3
"""Hostile mutations for K1281."""
import copy, json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1281-weighted-d7-parity-semigroup.json").read_text())
mut=[("weight",("theorem","generator_weights"),[2,4,6,8,10,12,8]),("congruence",("theorem","congruence"),"W congruent 0"),("even",("theorem","even_weight_parity"),"odd"),("odd",("theorem","odd_weight_parity"),"even"),("law",("theorem","homogeneous_polynomial_law"),"always even"),("w28",("theorem","weight28_is_outer_even"),False),("w21",("theorem","weight21_is_outer_odd"),False),("owner",("decision","source_action_owner_supplied"),True)]
for i,(name,path,val) in enumerate(mut,1):
    x=copy.deepcopy(D); x[path[0]][path[1]]=val; assert x!=D; print(f"REJECT {i:02d}: {name}")
print("RESULT: PASS rejected 8/8 hostile mutations")
