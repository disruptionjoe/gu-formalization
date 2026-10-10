#!/usr/bin/env python3
"""Hostile mutations for K1698."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]


def valid(d):
    v,e=d.get("variational_data",{}),d.get("envelope",{})
    return all([d.get("claim_id")=="K1698","ell_0(C)^2/tau_0(C)" in v.get("leading_shape_functional",""),
        "argmax" in v.get("leading_maximizers",""),"S_*=min" in v.get("secondary_minimum",""),
        "inf_C" in e.get("definition",""),"-6g^2M" in e.get("expansion",""),
        "432c_Xg^3S_*" in e.get("expansion",""),e.get("optimizer_uniqueness_required") is False,
        "c_*=1/4" in e.get("named_seed_coefficients",""),
        "not the all-seed scalar infimum" in d.get("scope_guard","")])


def main():
    src=json.loads((ROOT/"lab/process/k1698-shape-optimized-cubic-envelope.json").read_text())
    muts=[(("claim_id",),"K1697"),(("variational_data","leading_shape_functional"),"unknown"),
        (("variational_data","leading_maximizers"),"none"),(("variational_data","secondary_minimum"),"zero"),
        (("envelope","definition"),"fixed C"),(("envelope","expansion"),"leading only"),
        (("envelope","optimizer_uniqueness_required"),True),(("envelope","named_seed_coefficients"),"equal"),
        (("scope_guard",),"all seeds")]
    assert valid(src)
    for i,(path,val) in enumerate(muts,1):
        d=copy.deepcopy(src); cur=d
        for k in path[:-1]: cur=cur[k]
        cur[path[-1]]=val; assert not valid(d),i; print(f"REJECT {i:02d}: hostile mutation")
    print(f"RESULT: REJECTED {len(muts)}/{len(muts)}")


if __name__=="__main__": main()
