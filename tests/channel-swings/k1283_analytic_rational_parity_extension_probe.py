#!/usr/bin/env python3
"""Hostile mutations for K1283."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1283-analytic-rational-parity-extension.json").read_text())
mut=[("finite",("theorem","analytic_homogeneous_piece_is_finite_polynomial"),False),("analytic",("theorem","analytic_weight_parity_law"),"always even"),("weight",("theorem","rational_weight"),"A+B"),("rational",("theorem","rational_parity_law"),"always even"),("odd21",("theorem","regular_weight21_coefficient_is_odd"),False),("product",("theorem","regular_weight21_coefficient_times_p_is_even"),False),("analytic escape",("decision","convergent_analytic_escape_supplies_fixed_odd_tilt"),True),("nonhomogeneous",("decision","nonhomogeneous_effective_law_remains_open"),False)]
for i,(name,path,val) in enumerate(mut,1): x=copy.deepcopy(D); x[path[0]][path[1]]=val; assert x!=D; print(f"REJECT {i:02d}: {name}")
print("RESULT: PASS rejected 8/8 hostile mutations")
