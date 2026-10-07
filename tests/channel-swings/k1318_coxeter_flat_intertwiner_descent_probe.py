#!/usr/bin/env python3
"""Independent hostile mutations for K1318."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1318-coxeter-flat-intertwiner-descent.json").read_text())
def valid(x):
 c=x["coxeter_data"]; d=x["descent"]; q=x["decision"]; return c["type"]=="D7" and c["rank"]==7 and c["weyl_group_order"]==322560 and len(c["simple_edges"])==6 and d["all_coxeter_relations_required"] and d["path_independent_transport_follows"] and not d["analytic_normalized_intertwiners_constructed_here"] and q["finite_coherence_problem_reduces_to_simple_edges_and_relators"] and not q["checking_one_path_or_one_chamber_is_sufficient"] and not q["source_or_physical_status_moves"]
mut=[(("coxeter_data","type"),"A7"),(("coxeter_data","rank"),6),(("coxeter_data","weyl_group_order"),645120),(("coxeter_data","simple_edges"),[[1,2]]),(("descent","all_coxeter_relations_required"),False),(("descent","path_independent_transport_follows"),False),(("descent","analytic_normalized_intertwiners_constructed_here"),True),(("decision","checking_one_path_or_one_chamber_is_sufficient"),True),(("decision","source_or_physical_status_moves"),True)]
assert valid(D)
for i,(p,v) in enumerate(mut,1): x=copy.deepcopy(D); x[p[0]][p[1]]=v; assert not valid(x); print(f"REJECT {i:02d}: {'.'.join(p)}")
print("RESULT: PASS rejected 9/9 hostile mutations")
