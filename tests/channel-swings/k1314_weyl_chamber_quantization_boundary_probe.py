#!/usr/bin/env python3
"""Independent hostile mutations for K1314."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1314-weyl-chamber-quantization-boundary.json").read_text())
def valid(x):
 c=x["classification_result"]; q=x["decision"]; return c["weyl_group_order"]==322560 and c["chamber_count"]==322560 and c["all_chambers_admit_positive_control"] and not c["single_chamber_canonical"] and not c["source_selected_chamber"] and c["finite_multichamber_sum_positive"] and c["finite_multichamber_multiplicity"]==322560 and not q["direct_sum_is_physical_sector"] and not q["source_or_physical_status_moves"]
mut=[(("classification_result","weyl_group_order"),645120),(("classification_result","chamber_count"),161280),(("classification_result","all_chambers_admit_positive_control"),False),(("classification_result","single_chamber_canonical"),True),(("classification_result","source_selected_chamber"),True),(("classification_result","finite_multichamber_sum_positive"),False),(("classification_result","finite_multichamber_multiplicity"),1),(("decision","direct_sum_is_physical_sector"),True),(("decision","source_or_physical_status_moves"),True)]
assert valid(D)
for i,(p,v) in enumerate(mut,1): x=copy.deepcopy(D); x[p[0]][p[1]]=v; assert not valid(x); print(f"REJECT {i:02d}: {'.'.join(p)}")
print("RESULT: PASS rejected 9/9 hostile mutations")
