#!/usr/bin/env python3
"""Hostile mutations for K1230."""
import copy
import k1230_common_owner_holdout_boundary as p
def main():
  edits=[(("decision","typed_common_owner_schema_constructed"),False),(("decision","instantiated_physical_owner_present"),True),
    (("decision","nominal_tomography_alone_establishes_owner"),True),(("decision","holdout_predeclared"),False),
    (("decision","holdout_scored"),True),(("decision","calibration_or_holdout_earns_gu_confirmation"),True),
    (("release_test","spam_gauge_retained"),False),(("release_test","holdout_sealed_and_unscored"),False),
    (("release_test","delayed_choice_reserved"),False),(("ownership","gu_native_effect"),"prediction")]
  n=0
  for path,val in edits:
    x=copy.deepcopy(p.build());d=x
    for k in path[:-1]:d=d[k]
    d[path[-1]]=val
    try:p.validate(x)
    except AssertionError:n+=1
  assert n==len(edits);print(f"K1230 hostile probes: {n}/{len(edits)}")
if __name__=="__main__":main()
