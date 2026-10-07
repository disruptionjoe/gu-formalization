#!/usr/bin/env python3
"""Independent hostile mutations for K1313."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1313-compact-picture-positive-hilbert-control.json").read_text())
def valid(x):
 c=x["construction"]; q=x["decision"]; return c["K_dimension"]==42 and c["M_dimension"]==0 and c["compact_picture_dimension"]==42 and c["positive_definite"] and c["normalized_principal_series_unitary"] and c["conserved_norm"] and c["tangent_para_kahler_signature"]==[42,42] and q["positive_mathematical_hilbert_control_exists"] and not q["physical_pairing_constructed"] and not q["source_or_physical_status_moves"]
mut=[(("construction","K_dimension"),56),(("construction","M_dimension"),7),(("construction","compact_picture_dimension"),35),(("construction","positive_definite"),False),(("construction","normalized_principal_series_unitary"),False),(("construction","conserved_norm"),False),(("construction","tangent_para_kahler_signature"),[84,0]),(("decision","physical_pairing_constructed"),True),(("decision","source_or_physical_status_moves"),True)]
assert valid(D)
for i,(p,v) in enumerate(mut,1): x=copy.deepcopy(D); x[p[0]][p[1]]=v; assert not valid(x); print(f"REJECT {i:02d}: {'.'.join(p)}")
print("RESULT: PASS rejected 9/9 hostile mutations")
