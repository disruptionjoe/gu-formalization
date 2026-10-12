#!/usr/bin/env python3
"""Hostile mutations for K1703."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]


def valid(d):
    s,g,l,q=d.get("seed_family",{}),d.get("global_branch",{}),d.get("legendre",{}),d.get("decision",{})
    return all([d.get("claim_id")=="K1703","|X|<=B" in s.get("definition",""),"0<u_0" in s.get("definition",""),
        "weakly compact" in s.get("compactness",""),"O_(B,u_0)(q^(7/2))" in s.get("uniform_remainder",""),
        "E H_4(Y)" in g.get("score_moment_identity",""),"j_X(q)>=q^2" in g.get("coercive_bound",""),
        "every global minimizer" in g.get("consequence",""),"-(3/2)r^2" in l.get("expansion",""),
        "(27/4)r^3" in l.get("uniform_floor",""),q.get("uniform_global_small_branch") is True,
        q.get("uncontrolled_seed_escape_closed") is False])


def main():
    src=json.loads((ROOT/"lab/process/k1703-uniform-seed-family-legendre-bound.json").read_text())
    muts=[(('claim_id',),'K1702'),(('seed_family','definition'),'unbounded'),(('seed_family','compactness'),'none'),
        (('seed_family','uniform_remainder'),'pointwise'),(('global_branch','score_moment_identity'),'wrong Hermite'),
        (('global_branch','coercive_bound'),'none'),(('global_branch','consequence'),'local candidate only'),
        (('legendre','expansion'),'quadratic only'),(('legendre','uniform_floor'),'no floor'),
        (('decision','uniform_global_small_branch'),False),(('decision','uncontrolled_seed_escape_closed'),True)]
    assert valid(src)
    for n,(path,val) in enumerate(muts,1):
        d=copy.deepcopy(src); cur=d
        for key in path[:-1]: cur=cur[key]
        cur[path[-1]]=val; assert not valid(d),n; print(f"REJECT {n:02d}: hostile mutation")
    print(f"RESULT: REJECTED {len(muts)}/{len(muts)}")


if __name__=="__main__": main()
