#!/usr/bin/env python3
"""Hostile mutations for K1697."""
import copy, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]


def valid(d):
    s, c = d.get("shape_space", {}), d.get("compactness", {})
    return all([
        d.get("claim_id") == "K1697",
        "degenerate faces adjoined" in s.get("parameterization", ""),
        "b_0(x)=|x|" in s.get("zero_profile", ""),
        "zero on every degenerate face" in s.get("boundary", ""),
        "g log(1/kappa_g)->1/(12pi)" in s.get("profile_rate", ""),
        "M=max_C R_0(C)>0" in c.get("leading_maximum", ""),
        "disjoint from the degenerate boundary" in c.get("maximizer_set", ""),
        "common compact interior" in c.get("near_minimizers", ""),
        "S_*>" in c.get("secondary_floor", ""),
        "does not cover arbitrary nonrectangular" in d.get("scope_guard", ""),
    ])


def main():
    src=json.loads((ROOT/"lab/process/k1697-rectangular-shape-compactness.json").read_text())
    muts=[
        (("claim_id",),"K1696"), (("shape_space","parameterization"),"open only"),
        (("shape_space","zero_profile"),"bounded"), (("shape_space","boundary"),"nonzero"),
        (("shape_space","profile_rate"),"unknown"), (("compactness","leading_maximum"),"zero"),
        (("compactness","maximizer_set"),"boundary"), (("compactness","near_minimizers"),"collapse"),
        (("compactness","secondary_floor"),"S_*=0"), (("scope_guard",),"all shapes"),
    ]
    assert valid(src)
    for i,(path,value) in enumerate(muts,1):
        d=copy.deepcopy(src); cur=d
        for key in path[:-1]: cur=cur[key]
        cur[path[-1]]=value
        assert not valid(d), i
        print(f"REJECT {i:02d}: hostile mutation")
    print(f"RESULT: REJECTED {len(muts)}/{len(muts)}")


if __name__=="__main__": main()
