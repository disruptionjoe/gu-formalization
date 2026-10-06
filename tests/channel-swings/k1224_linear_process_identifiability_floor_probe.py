#!/usr/bin/env python3
"""Hostile mutations for K1224."""
import copy
import k1224_linear_process_identifiability_floor as p
def main():
    edits=[(("release_test","full_dimension"),11),(("release_test","unital_dimension"),8),
      (("release_test","interior_perturbation_argument"),False),(("release_test","nonlinear_invariant_overclaim_rejected"),False),
      (("decision","twelve_statistic_frame_meets_linear_floor"),False),
      (("decision","nine_transfer_statistics_meet_unital_linear_floor"),False),
      (("decision","fewer_than_twelve_can_identify_full_affine_channel"),True),
      (("decision","fewer_than_nine_can_identify_full_unital_transfer"),True),
      (("ownership","prediction_or_confirmation"),True)]
    n=0
    for path,val in edits:
        x=copy.deepcopy(p.build());d=x
        for k in path[:-1]:d=d[k]
        d[path[-1]]=val
        try:p.validate(x)
        except AssertionError:n+=1
    assert n==len(edits);print(f"K1224 hostile probes: {n}/{len(edits)}")
if __name__=="__main__":main()
