#!/usr/bin/env python3
"""Hostile mutations for K1699."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]


def valid(d):
    c,x=d.get("comparison",{}),d.get("decision",{})
    return all([d.get("claim_id")=="K1699","4/15" in c.get("coefficient_difference",""),
        "(576/5)S_*g^3+o(g^3)" in c.get("envelope_difference",""),"S_*>0" in c.get("strictness",""),
        "h_g^(*-card-up)<h_g^(R-card-up)" in c.get("chain",""),x.get("fixed_shape_only_boundary_closed") is True,
        x.get("fully_rectangular_shape_optimized_strict") is True,x.get("all_seed_scalar_infimum_identified") is False,
        x.get("unrestricted_coefficient_identified") is False])


def main():
    src=json.loads((ROOT/"lab/process/k1699-global-three-point-rademacher-gap.json").read_text())
    muts=[(("claim_id",),"K1698"),(("comparison","coefficient_difference"),"zero"),
        (("comparison","envelope_difference"),"fixed shape"),(("comparison","strictness"),"S_*=0"),
        (("comparison","chain"),"equal"),(("decision","fixed_shape_only_boundary_closed"),False),
        (("decision","fully_rectangular_shape_optimized_strict"),False),
        (("decision","all_seed_scalar_infimum_identified"),True),
        (("decision","unrestricted_coefficient_identified"),True)]
    assert valid(src)
    for i,(path,val) in enumerate(muts,1):
        d=copy.deepcopy(src); cur=d
        for k in path[:-1]: cur=cur[k]
        cur[path[-1]]=val; assert not valid(d),i; print(f"REJECT {i:02d}: hostile mutation")
    print(f"RESULT: REJECTED {len(muts)}/{len(muts)}")


if __name__=="__main__": main()
