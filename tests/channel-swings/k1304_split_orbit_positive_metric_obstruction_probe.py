#!/usr/bin/env python3
"""Independent hostile mutations for K1304."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1304-split-orbit-positive-metric-obstruction.json").read_text())
def valid(x):
    t=x["theorem"]; q=x["decision"]
    return (t["positive_root_count"]==42 and t["orbit_dimension"]==84 and t["regular_split_stabilizer_dimension"]==7 and
            t["nontrivial_real_weights_present"] and not t["positive_inner_product_invariant_under_split_stabilizer"] and
            not t["g_invariant_riemannian_metric_exists"] and not t["g_invariant_positive_kahler_metric_from_kks_exists"] and
            t["kks_form_nondegenerate"] and not t["kks_form_alone_is_positive_pairing"] and
            not q["canonical_invariant_positive_state_metric_supplied"] and not q["SC_META_53_resolved"])
mut=[(("theorem","positive_root_count"),49),(("theorem","orbit_dimension"),91),
     (("theorem","nontrivial_real_weights_present"),False),(("theorem","positive_inner_product_invariant_under_split_stabilizer"),True),
     (("theorem","g_invariant_riemannian_metric_exists"),True),(("theorem","g_invariant_positive_kahler_metric_from_kks_exists"),True),
     (("theorem","kks_form_nondegenerate"),False),(("theorem","kks_form_alone_is_positive_pairing"),True),
     (("decision","SC_META_53_resolved"),True)]
assert valid(D)
for i,(path,value) in enumerate(mut,1):
    x=copy.deepcopy(D); x[path[0]][path[1]]=value; assert not valid(x); print(f"REJECT {i:02d}: {'.'.join(path)}")
print("RESULT: PASS rejected 9/9 hostile mutations")
