#!/usr/bin/env python3
"""Independent hostile mutations for K1305."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1305-shifted-charge-admission-boundary.json").read_text())
def valid(x):
    c=x["certificate"]; q=x["decision"]
    return ((c["row_count"],c["satisfied_count"],c["satisfied_formal_count"],c["excluded_count"],c["missing_count"])==(12,3,2,1,6) and
            q["finite_nonzero_charge_bfv_feasible"] and not q["finite_properness_requires_source_owned_seven_lock"] and
            q["charge_selection_requires_source_owned_values_or_equivalent_law"] and not q["shifting_trick_selects_charge"] and
            not q["canonical_invariant_positive_metric_exists"] and not q["functional_physical_packet_constructed"] and
            not q["k1300_native_k1145_k1150_pass_counts_move"] and not q["protected_status_change"])
mut=[(("certificate","satisfied_count"),5),(("certificate","missing_count"),0),
     (("decision","finite_nonzero_charge_bfv_feasible"),False),(("decision","finite_properness_requires_source_owned_seven_lock"),True),
     (("decision","charge_selection_requires_source_owned_values_or_equivalent_law"),False),(("decision","shifting_trick_selects_charge"),True),
     (("decision","canonical_invariant_positive_metric_exists"),True),(("decision","functional_physical_packet_constructed"),True),
     (("decision","k1300_native_k1145_k1150_pass_counts_move"),True),(("decision","protected_status_change"),True)]
assert valid(D)
for i,(path,value) in enumerate(mut,1):
    x=copy.deepcopy(D); x[path[0]][path[1]]=value; assert not valid(x); print(f"REJECT {i:02d}: {'.'.join(path)}")
print("RESULT: PASS rejected 10/10 hostile mutations")
