#!/usr/bin/env python3
"""Hostile mutations for K1217."""
import copy
import k1217_directional_visibility_chsh_envelope as p
def main():
    edits=[(("theorem","range"),"2|V|=S"),(("theorem","squared_range"),"V^2<=1"),
      (("decision","single_direction_identifies_optimized_chsh"),True),
      (("decision","pauli_aligned_upper_bound_survives_without_alignment"),True),
      (("decision","bounds_sharp_for_every_V"),False),(("release_test","all_endpoints_attained"),False),
      (("release_test","zero_visibility_can_be_maximal"),False),(("ownership","gu_prediction"),True)]
    n=0
    for path,val in edits:
        x=copy.deepcopy(p.build());x[path[0]][path[1]]=val
        try:p.validate(x)
        except AssertionError:n+=1
    assert n==len(edits);print(f"K1217 hostile probes: {n}/{len(edits)}")
if __name__=="__main__":main()
