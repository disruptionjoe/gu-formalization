#!/usr/bin/env python3
"""Hostile mutations for K1702."""
import copy, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]


def valid(d):
    f,c,q=d.get("family",{}),d.get("classification",{}),d.get("decision",{})
    return all([d.get("claim_id")=="K1702","p^(-1/2)" in f.get("law",""),"E X^6=1/p^2" in f.get("moments",""),
        "p>1/3" in f.get("negative_kurtosis",""),"y^2-15y+30=0" in c.get("root_equation",""),
        "p_*=(15+sqrt(105))/60" in c.get("admissible_root",""),"c_*=1/4" in c.get("consequence",""),
        q.get("three_point_negative_kurtosis_equality_unique") is True,q.get("all_distribution_equality_unique") is False,
        "Other bounded symmetric laws" in d.get("scope_guard","")])


def main():
    src=json.loads((ROOT/"lab/process/k1702-three-point-equality-classification.json").read_text())
    muts=[(('claim_id',),'K1701'),(('family','law'),'binary'),(('family','moments'),'wrong'),
        (('family','negative_kurtosis'),'all p'),(('classification','root_equation'),'linear'),
        (('classification','admissible_root'),'other root'),(('classification','consequence'),'c=0'),
        (('decision','three_point_negative_kurtosis_equality_unique'),False),(('decision','all_distribution_equality_unique'),True),
        (('scope_guard',),'unique globally')]
    assert valid(src)
    for n,(path,val) in enumerate(muts,1):
        d=copy.deepcopy(src); cur=d
        for key in path[:-1]: cur=cur[key]
        cur[path[-1]]=val; assert not valid(d),n; print(f"REJECT {n:02d}: hostile mutation")
    print(f"RESULT: REJECTED {len(muts)}/{len(muts)}")


if __name__=="__main__": main()
