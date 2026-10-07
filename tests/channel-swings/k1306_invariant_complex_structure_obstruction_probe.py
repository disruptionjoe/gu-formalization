#!/usr/bin/env python3
"""Independent hostile mutations for K1306."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1306-invariant-complex-structure-obstruction.json").read_text())
def valid(x):
 t=x["theorem"]; q=x["decision"]; return t["root_count"]==84 and t["positive_root_count"]==42 and t["root_space_real_dimension"]==1 and t["split_torus_characters_pairwise_distinct"] and t["invariant_endomorphism_preserves_each_root_space"] and not t["real_scalar_can_square_to_minus_one"] and not t["g_invariant_almost_complex_structure_exists"] and not t["g_invariant_kks_compatible_complex_structure_exists"] and not q["SC_META_53_resolved"]
mut=[(("theorem","root_count"),98),(("theorem","root_space_real_dimension"),2),(("theorem","split_torus_characters_pairwise_distinct"),False),(("theorem","invariant_endomorphism_preserves_each_root_space"),False),(("theorem","real_scalar_can_square_to_minus_one"),True),(("theorem","g_invariant_almost_complex_structure_exists"),True),(("theorem","g_invariant_kks_compatible_complex_structure_exists"),True),(("decision","SC_META_53_resolved"),True)]
assert valid(D)
for i,(p,v) in enumerate(mut,1): x=copy.deepcopy(D); x[p[0]][p[1]]=v; assert not valid(x); print(f"REJECT {i:02d}: {'.'.join(p)}")
print("RESULT: PASS rejected 8/8 hostile mutations")
