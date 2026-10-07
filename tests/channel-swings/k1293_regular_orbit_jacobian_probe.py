#!/usr/bin/env python3
"""Independent hostile mutations for K1293."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1293-regular-orbit-jacobian.json").read_text())
def valid(x):
    t=x["theorem"]; q=x["decision"]
    return (t["absolute_jacobian"].startswith("abs(det dF_x)=2^6") and
            t["matches_D7_regular_semisimple_locus"] and t["connected_quotient_local_diffeomorphism_on_regular_locus"] and
            t["outer_B7_branches_at_p_zero"] and not t["connected_D7_branches_at_p_zero"] and
            q["regular_selector_transfer_may_use_ordinary_inverse_function_theorem"] and
            not q["p_zero_is_a_D7_Weyl_wall"] and not q["functional_Fredholm_or_Green_result"])
mut=[(("theorem","absolute_jacobian"),"abs(det dF_x)=2^7"),(("theorem","matches_D7_regular_semisimple_locus"),False),(("theorem","connected_quotient_local_diffeomorphism_on_regular_locus"),False),(("theorem","outer_B7_branches_at_p_zero"),False),(("theorem","connected_D7_branches_at_p_zero"),True),(("decision","regular_selector_transfer_may_use_ordinary_inverse_function_theorem"),False),(("decision","p_zero_is_a_D7_Weyl_wall"),True),(("decision","functional_Fredholm_or_Green_result"),True)]
assert valid(D)
for i,(path,value) in enumerate(mut,1):
    x=copy.deepcopy(D); x[path[0]][path[1]]=value; assert not valid(x); print(f"REJECT {i:02d}: {'.'.join(path)}")
print("RESULT: PASS rejected 8/8 hostile mutations")
