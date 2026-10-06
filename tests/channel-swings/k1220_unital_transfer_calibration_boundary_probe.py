#!/usr/bin/env python3
"""Hostile mutations for K1220."""
import copy
import k1220_unital_transfer_calibration_boundary as p
def main():
    edits=[(("identifiability","one_directional_read"),"identified"),
      (("decision","directional_visibility_only_prediction_allowed"),True),
      (("decision","three_aligned_axes_universally_sufficient"),True),
      (("decision","full_transfer_or_singular_spectrum_closes_imported_score"),False),
      (("decision","calibration_anchor_earns_confirmation"),True),
      (("decision","general_unital_result_is_gu_derived"),True),
      (("release_test","pauli_boundary_not_retracted"),False),(("release_test","holdout_unscored"),False),
      (("ownership","gu_native_effect"),"prediction"),(("ownership","prediction_or_confirmation"),True)]
    n=0
    for path,val in edits:
        x=copy.deepcopy(p.build());d=x
        for k in path[:-1]:d=d[k]
        d[path[-1]]=val
        try:p.validate(x)
        except AssertionError:n+=1
    assert n==len(edits);print(f"K1220 hostile probes: {n}/{len(edits)}")
if __name__=="__main__":main()
