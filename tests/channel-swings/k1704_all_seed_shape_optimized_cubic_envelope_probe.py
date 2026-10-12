#!/usr/bin/env python3
"""Hostile mutations for K1704."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]


def valid(d):
    i,e,q=d.get("inputs",{}),d.get("envelope",{}),d.get("decision",{})
    return all([d.get("claim_id")=="K1704","p_*^(-1/2)" in i.get("seed_family",""),"K1683 rectangles" in i.get("shape_space",""),
        "S_0(C)>0" in i.get("shape_data",""),"inf_(X in S)" in e.get("definition",""),
        "H_S(g)>=-6g^2M+108g^3S_*" in e.get("uniform_lower",""),"H_S(g)<=-6g^2M+108g^3S_*" in e.get("matching_upper",""),
        "(576/5)S_*g^3" in e.get("comparison",""),q.get("controlled_all_seed_cubic_envelope_identified") is True,
        q.get("exact_finite_strength_infimum_identified") is False,"not every bounded seed" in d.get("scope_guard","")])


def main():
    src=json.loads((ROOT/"lab/process/k1704-all-seed-shape-optimized-cubic-envelope.json").read_text())
    muts=[(('claim_id',),'K1703'),(('inputs','seed_family'),'excludes star'),(('inputs','shape_space'),'all shapes'),
        (('inputs','shape_data'),'S=0'),(('envelope','definition'),'fixed seed'),(('envelope','uniform_lower'),'no lower'),
        (('envelope','matching_upper'),'no upper'),(('envelope','comparison'),'no gap'),
        (('decision','controlled_all_seed_cubic_envelope_identified'),False),(('decision','exact_finite_strength_infimum_identified'),True)]
    assert valid(src)
    for n,(path,val) in enumerate(muts,1):
        d=copy.deepcopy(src); cur=d
        for key in path[:-1]: cur=cur[key]
        cur[path[-1]]=val; assert not valid(d),n; print(f"REJECT {n:02d}: hostile mutation")
    print(f"RESULT: REJECTED {len(muts)}/{len(muts)}")


if __name__=="__main__": main()
