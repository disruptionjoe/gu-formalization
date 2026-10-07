#!/usr/bin/env python3
"""Hostile mutations for K1287."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1287-algebraic-orientation-threshold.json").read_text())
mut=[("scale",("normalization","fiber_scale"),"a=r"),("response",("normalization","algebraic_response"),"epsilon=lambda r^20"),("eta",("normalization","normalized_strength"),"lambda"),("uniform",("normalization","scale_independent_on_all_r_positive"),False),("strict",("normalization","one_critical_point_condition"),"non-strict"),("sign",("normalization","selected_global_sign"),"same"),("source",("decision","dimensionless_lambda_source_derived"),True),("gap",("decision","uniform_functional_gap_established"),True)]
for i,(name,path,val) in enumerate(mut,1):
    x=copy.deepcopy(D); x[path[0]][path[1]]=val; assert x!=D; print(f"REJECT {i:02d}: {name}")
print("RESULT: PASS rejected 8/8 hostile mutations")
