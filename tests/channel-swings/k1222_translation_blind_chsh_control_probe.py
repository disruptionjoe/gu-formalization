#!/usr/bin/env python3
"""Hostile mutations for K1222."""
import copy
import k1222_translation_blind_chsh_control as p
def main():
    edits=[(("decision","same_M_different_t"),False),(("decision","same_bell_correlation"),False),
      (("decision","same_optimized_chsh"),False),(("decision","local_output_marginal_distinguishes_translation"),False),
      (("release_test","translations"),False),(("release_test","common_score"),False),
      (("controls",0,"cptp_by_kraus_family"),False),(("ownership","prediction_or_confirmation"),True)]
    n=0
    for path,val in edits:
        x=copy.deepcopy(p.build());d=x
        for k in path[:-1]:d=d[k]
        d[path[-1]]=val
        try:p.validate(x)
        except AssertionError:n+=1
    assert n==len(edits);print(f"K1222 hostile probes: {n}/{len(edits)}")
if __name__=="__main__":main()
