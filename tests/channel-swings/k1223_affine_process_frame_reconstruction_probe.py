#!/usr/bin/env python3
"""Hostile mutations for K1223."""
import copy
import k1223_affine_process_frame_reconstruction as p
def main():
    edits=[(("release_test","recovered_full_M"),False),(("release_test","all_three_translation_averages_agree"),False),
      (("release_test","raw_scalar_count"),12),(("release_test","independent_scalar_count"),9),
      (("release_test","consistency_relation_count"),3),
      (("decision","nine_centered_transfers_determine_bell_chsh"),False),
      (("decision","three_additional_marginal_statistics_determine_translation"),False),
      (("decision","full_affine_process_reconstructed"),False),
      (("decision","apparatus_frame_is_self_authenticating"),True),(("ownership","gu_native_effect"),"prediction")]
    n=0
    for path,val in edits:
        x=copy.deepcopy(p.build());d=x
        for k in path[:-1]:d=d[k]
        d[path[-1]]=val
        try:p.validate(x)
        except AssertionError:n+=1
    assert n==len(edits);print(f"K1223 hostile probes: {n}/{len(edits)}")
if __name__=="__main__":main()
