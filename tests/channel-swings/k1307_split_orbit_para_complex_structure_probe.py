#!/usr/bin/env python3
"""Independent hostile mutations for K1307."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1307-split-orbit-para-complex-structure.json").read_text())
def valid(x):
 t=x["theorem"]; q=x["decision"]; return t["plus_eigenspace_dimension"]==t["minus_eigenspace_dimension"]==42 and t["K_squared_is_identity"] and t["equal_rank_eigenbundles"] and t["a_equivariant"] and t["g_invariant"] and t["positive_root_brackets_close"] and t["negative_root_brackets_close"] and t["nijenhuis_tensor_zero"] and t["integrable_para_complex_structure"] and not t["choice_independent"] and not q["positive_structure_recovered"]
mut=[(("theorem","plus_eigenspace_dimension"),41),(("theorem","K_squared_is_identity"),False),(("theorem","a_equivariant"),False),(("theorem","g_invariant"),False),(("theorem","positive_root_brackets_close"),False),(("theorem","negative_root_brackets_close"),False),(("theorem","nijenhuis_tensor_zero"),False),(("theorem","choice_independent"),True),(("decision","positive_structure_recovered"),True)]
assert valid(D)
for i,(p,v) in enumerate(mut,1): x=copy.deepcopy(D); x[p[0]][p[1]]=v; assert not valid(x); print(f"REJECT {i:02d}: {'.'.join(p)}")
print("RESULT: PASS rejected 9/9 hostile mutations")
