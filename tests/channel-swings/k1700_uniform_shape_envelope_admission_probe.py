#!/usr/bin/env python3
"""Hostile mutations for K1700."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]


def valid(d):
    a,x=d.get("admission",{}),d.get("decision",{})
    return all([d.get("claim_id")=="K1700","fully channel-strength- and rectangular-shape-optimized" in a.get("quantum_result",""),
        "finite-strength all-seed scalar infimum" in a.get("remaining_quantum_gate",""),"K1145/K1150 remain 0/7" in a.get("physical_admission",""),
        "415 rows" in a.get("bridge_census",""),"SC-ACT-01/02/06 remain ASSERTS" in a.get("protected_state",""),
        "Do not promote" in a.get("scope_guard",""),x.get("uniform_shape_boundary_closed") is True,
        x.get("named_seed_global_gap_integrated") is True,x.get("true_unrestricted_coefficient_open") is True,
        x.get("source_status_changed") is False,x.get("physics_ledger_changed") is False,x.get("canon_or_public_status_changed") is False])


def main():
    src=json.loads((ROOT/"lab/process/k1700-uniform-shape-envelope-admission.json").read_text())
    muts=[(("claim_id",),"K1699"),(("admission","quantum_result"),"fixed shape only"),
        (("admission","remaining_quantum_gate"),"closed"),(("admission","physical_admission"),"physical"),
        (("admission","bridge_census"),"410 rows"),(("admission","protected_state"),"moved"),
        (("admission","scope_guard"),"promote"),(("decision","uniform_shape_boundary_closed"),False),
        (("decision","named_seed_global_gap_integrated"),False),(("decision","true_unrestricted_coefficient_open"),False),
        (("decision","source_status_changed"),True),(("decision","physics_ledger_changed"),True)]
    assert valid(src)
    for i,(path,val) in enumerate(muts,1):
        d=copy.deepcopy(src); cur=d
        for k in path[:-1]: cur=cur[k]
        cur[path[-1]]=val; assert not valid(d),i; print(f"REJECT {i:02d}: hostile mutation")
    print(f"RESULT: REJECTED {len(muts)}/{len(muts)}")


if __name__=="__main__": main()
