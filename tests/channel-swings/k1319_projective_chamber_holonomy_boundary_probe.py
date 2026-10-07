#!/usr/bin/env python3
"""Independent hostile mutations for K1319."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1319-projective-chamber-holonomy-boundary.json").read_text())
def valid(x):
 c=x["countercontrol"]; q=x["decision"]; return c["each_edge_transport_unitary"] and c["each_edge_transport_involutive"] and c["affected_relator"]=="m_56=3 braid" and c["relative_phase"]==-1 and not c["exact_braid_relation_holds"] and c["projective_braid_relation_holds"] and not c["path_independent_exact_transport"] and not q["edge_unitarity_and_positivity_imply_flatness"] and not q["projective_equivalence_is_exact_chamber_descent"] and not q["source_or_physical_status_moves"]
mut=[(("countercontrol","each_edge_transport_unitary"),False),(("countercontrol","each_edge_transport_involutive"),False),(("countercontrol","affected_relator"),"m_56=2"),(("countercontrol","relative_phase"),1),(("countercontrol","exact_braid_relation_holds"),True),(("countercontrol","projective_braid_relation_holds"),False),(("countercontrol","path_independent_exact_transport"),True),(("decision","projective_equivalence_is_exact_chamber_descent"),True),(("decision","source_or_physical_status_moves"),True)]
assert valid(D)
for i,(p,v) in enumerate(mut,1): x=copy.deepcopy(D); x[p[0]][p[1]]=v; assert not valid(x); print(f"REJECT {i:02d}: {'.'.join(p)}")
print("RESULT: PASS rejected 9/9 hostile mutations")
