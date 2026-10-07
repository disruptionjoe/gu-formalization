#!/usr/bin/env python3
"""Independent hostile mutations for K1317."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1317-chamber-average-equivariance-criterion.json").read_text())
def valid(x):
 c=x["criterion"]; q=x["decision"]; return c["necessity"] and c["sufficiency"] and not c["raw_fiber_unitarity_is_sufficient"] and not c["positive_direct_sum_is_sufficient"] and "independent of C" in c["diagonal_invariance_iff"] and q["K1316_average_can_be_G_descended_conditionally"] and not q["K1314_chamberwise_positivity_alone_proves_descent"] and q["normalized_intertwiner_data_still_required"] and not q["physical_sector_constructed"] and not q["source_or_physical_status_moves"]
mut=[(("criterion","necessity"),False),(("criterion","sufficiency"),False),(("criterion","raw_fiber_unitarity_is_sufficient"),True),(("criterion","positive_direct_sum_is_sufficient"),True),(("criterion","diagonal_invariance_iff"),"always"),(("decision","K1316_average_can_be_G_descended_conditionally"),False),(("decision","K1314_chamberwise_positivity_alone_proves_descent"),True),(("decision","normalized_intertwiner_data_still_required"),False),(("decision","source_or_physical_status_moves"),True)]
assert valid(D)
for i,(p,v) in enumerate(mut,1): x=copy.deepcopy(D); x[p[0]][p[1]]=v; assert not valid(x); print(f"REJECT {i:02d}: {'.'.join(p)}")
print("RESULT: PASS rejected 9/9 hostile mutations")
