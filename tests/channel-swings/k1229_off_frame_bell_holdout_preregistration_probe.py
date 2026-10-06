#!/usr/bin/env python3
"""Hostile mutations for K1229."""
import copy
import k1229_off_frame_bell_holdout_preregistration as p
def main():
  edits=[(("exact_control","a_dot_t"),"0"),(("exact_control","correlation"),"0"),
    (("decision","holdout_is_predeclared"),False),(("decision","holdout_is_scored"),True),
    (("decision","calibration_refit_on_holdout_forbidden"),False),(("decision","holdout_validates_common_owner_model_not_GU"),False),
    (("decision","delayed_choice_entanglement_swapping_consumed"),True),(("release_test","probabilities_normalized"),False),
    (("release_test","no_refit"),False),(("ownership","gu_native_effect"),"confirmation")]
  n=0
  for path,val in edits:
    x=copy.deepcopy(p.build());d=x
    for k in path[:-1]:d=d[k]
    d[path[-1]]=val
    try:p.validate(x)
    except AssertionError:n+=1
  assert n==len(edits);print(f"K1229 hostile probes: {n}/{len(edits)}")
if __name__=="__main__":main()
