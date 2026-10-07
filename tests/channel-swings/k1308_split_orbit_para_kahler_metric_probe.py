#!/usr/bin/env python3
"""Independent hostile mutations for K1308."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1308-split-orbit-para-kahler-metric.json").read_text())
def valid(x):
 t=x["theorem"]; q=x["decision"]; return t["metric_symmetric"] and t["metric_nondegenerate"] and t["metric_g_invariant"] and t["root_plane_count"]==42 and (t["positive_inertia"],t["negative_inertia"],t["zero_inertia"])==(42,42,0) and not t["metric_positive_definite"] and t["para_kahler"] and not t["kks_form_is_positive_pairing"] and not q["physical_hilbert_pairing_constructed"]
mut=[(("theorem","metric_symmetric"),False),(("theorem","metric_nondegenerate"),False),(("theorem","root_plane_count"),49),(("theorem","positive_inertia"),84),(("theorem","negative_inertia"),0),(("theorem","metric_positive_definite"),True),(("theorem","para_kahler"),False),(("theorem","kks_form_is_positive_pairing"),True),(("decision","physical_hilbert_pairing_constructed"),True)]
assert valid(D)
for i,(p,v) in enumerate(mut,1): x=copy.deepcopy(D); x[p[0]][p[1]]=v; assert not valid(x); print(f"REJECT {i:02d}: {'.'.join(p)}")
print("RESULT: PASS rejected 9/9 hostile mutations")
