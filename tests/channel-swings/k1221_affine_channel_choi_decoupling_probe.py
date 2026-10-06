#!/usr/bin/env python3
"""Hostile mutations for K1221."""
import copy
import k1221_affine_channel_choi_decoupling as p
def main():
    edits=[(("theorem","correlation_tensor"),"T=M D+t"),(("theorem","first_local_bloch"),"0"),
      (("theorem","second_local_bloch"),"t"),(("decision","unitality_required_for_correlation_rule"),True),
      (("decision","affine_translation_changes_optimized_chsh"),True),
      (("decision","translation_is_visible_in_first_marginal"),False),
      (("release_test","all_correlation_identities"),False),(("release_test","all_marginal_splits"),False),
      (("ownership","gu_native_effect"),"prediction")]
    n=0
    for path,val in edits:
        x=copy.deepcopy(p.build());d=x
        for k in path[:-1]: d=d[k]
        d[path[-1]]=val
        try:p.validate(x)
        except AssertionError:n+=1
    assert n==len(edits);print(f"K1221 hostile probes: {n}/{len(edits)}")
if __name__=="__main__":main()
