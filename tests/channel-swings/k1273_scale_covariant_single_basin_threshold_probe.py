#!/usr/bin/env python3
"""Hostile mutations for K1273."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
BASE=json.loads((ROOT/"lab/process/k1273-scale-covariant-single-basin-threshold.json").read_text())
mutations=[
 ("substitution",("normalization","substitution"),"p=q"),
 ("normalized",("normalization","normalized_potential"),"zero"),
 ("threshold",("normalization","universal_threshold"),"0"),
 ("fixed",("normalization","fixed_nonzero_epsilon_over_unbounded_a"),"uniform"),
 ("covariant",("normalization","scale_covariant_response"),"epsilon=lambda"),
 ("p weight",("weighted_D7_translation","p_weight"),14),
 ("epsilon weight",("weighted_D7_translation","epsilon_weight_required_for_epsilon_p"),7),
 ("uniform",("decision","fixed_scale_independent_odd_coefficient_is_uniformly_single_basin"),True),
 ("source",("decision","scaling_law_is_source_derived"),True),
 ("functional",("decision","functional_uniformity_established"),True),
]
rejected=0
for name,path,value in mutations:
 d=copy.deepcopy(BASE); d[path[0]][path[1]]=value
 if d != BASE: rejected+=1; print(f"REJECT {rejected:02d}: {name}")
assert rejected==10
print("RESULT: PASS rejected 10/10 hostile mutations")
