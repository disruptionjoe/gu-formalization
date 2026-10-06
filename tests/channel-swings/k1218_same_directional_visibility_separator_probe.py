#!/usr/bin/env python3
"""Hostile mutations for K1218."""
import copy
import k1218_same_directional_visibility_separator as p
def main():
    edits=[(("same_directional_visibility",),"1/2"),(("low_channel","S_squared_over_4"),"1"),
      (("low_channel","cp"),False),(("high_channel","S_squared_over_4"),"1"),(("high_channel","violates_CHSH"),False),
      (("decision","same_visibility_opposite_bell_disposition"),False),
      (("decision","k1212_upper_bound_requires_principal_axis_pauli_alignment"),False),
      (("ownership","prediction_or_confirmation"),True),(("release_test","score_gap"),"0")]
    n=0
    for path,val in edits:
        x=copy.deepcopy(p.build()); d=x
        for k in path[:-1]:d=d[k]
        d[path[-1]]=val
        try:p.validate(x)
        except AssertionError:n+=1
    assert n==len(edits);print(f"K1218 hostile probes: {n}/{len(edits)}")
if __name__=="__main__":main()
