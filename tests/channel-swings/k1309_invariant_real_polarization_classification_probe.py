#!/usr/bin/env python3
"""Independent hostile mutations for K1309."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1309-invariant-real-polarization-classification.json").read_text())
def valid(x):
 t=x["classification_theorem"]; q=x["quantization_boundary"]; return t["kks_pairs_root_spaces_only_with_opposites"] and t["each_eigenbundle_is_lagrangian"] and t["each_eigenbundle_dimension"]==42 and t["compatible_integrable_sign_sets_are_positive_root_systems"] and t["weyl_group_order"]==t["positive_root_system_count"]==t["invariant_integrable_real_polarization_count"]==322560 and t["weyl_action_transitive"] and not t["canonical_weyl_fixed_polarization_exists"] and q["real_lagrangian_polarization_constructed"] and not q["positive_complex_polarization_constructed"] and not q["positive_inner_product_constructed"]
mut=[(("classification_theorem","each_eigenbundle_is_lagrangian"),False),(("classification_theorem","each_eigenbundle_dimension"),84),(("classification_theorem","compatible_integrable_sign_sets_are_positive_root_systems"),False),(("classification_theorem","weyl_group_order"),645120),(("classification_theorem","invariant_integrable_real_polarization_count"),1),(("classification_theorem","weyl_action_transitive"),False),(("classification_theorem","canonical_weyl_fixed_polarization_exists"),True),(("quantization_boundary","positive_complex_polarization_constructed"),True),(("quantization_boundary","positive_inner_product_constructed"),True)]
assert valid(D)
for i,(p,v) in enumerate(mut,1): x=copy.deepcopy(D); x[p[0]][p[1]]=v; assert not valid(x); print(f"REJECT {i:02d}: {'.'.join(p)}")
print("RESULT: PASS rejected 9/9 hostile mutations")
