#!/usr/bin/env python3
"""Independent hostile mutations for K1303."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1303-nonzero-charge-bfv-complex.json").read_text())
def valid(x):
    c=x["construction"]; t=x["theorem"]; q=x["decision"]
    return (c["constraint_count"]==c["constraint_rank"]==c["minimal_ghost_count"]==91 and
            c["first_stage_reducibility"]==0 and t["regular_sequence_locally"] and t["koszul_tate_proper"] and
            t["master_equation_closes"] and t["degree_zero_reduced_observables"]=="C-infinity(O_mu)" and
            not t["degree_zero_reduced_observables_are_constants"] and not t["functional_local_bv_bfv_constructed"] and
            not t["physical_cohomology_identified"] and q["finite_nonzero_charge_properness_gap_closed"] and
            not q["seven_lock_obviated_as_selection_law"])
mut=[(("construction","constraint_rank"),84),(("construction","first_stage_reducibility"),7),
     (("construction","minimal_ghost_count"),7),(("theorem","regular_sequence_locally"),False),
     (("theorem","master_equation_closes"),False),(("theorem","degree_zero_reduced_observables"),"constants"),
     (("theorem","functional_local_bv_bfv_constructed"),True),(("theorem","physical_cohomology_identified"),True),
     (("decision","seven_lock_obviated_as_selection_law"),True)]
assert valid(D)
for i,(path,value) in enumerate(mut,1):
    x=copy.deepcopy(D); x[path[0]][path[1]]=value; assert not valid(x); print(f"REJECT {i:02d}: {'.'.join(path)}")
print("RESULT: PASS rejected 9/9 hostile mutations")
