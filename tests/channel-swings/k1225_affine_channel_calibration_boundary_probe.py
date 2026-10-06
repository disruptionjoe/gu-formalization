#!/usr/bin/env python3
"""Hostile mutations for K1225."""
import copy
import k1225_affine_channel_calibration_boundary as p
def main():
    edits=[(("decision","unitality_is_load_bearing_for_bell_chsh_rule"),True),
      (("decision","translation_must_be_measured_for_full_process"),False),
      (("decision","process_frame_supplies_physical_owner"),True),
      (("decision","calibration_anchor_earns_confirmation"),True),
      (("release_test","affine_decoupling_retained"),False),(("release_test","translation_blind_control_retained"),False),
      (("release_test","twelve_statistic_frame_retained"),False),(("release_test","linear_floor_retained"),False),
      (("release_test","holdout_unscored"),False),(("ownership","gu_native_effect"),"prediction")]
    n=0
    for path,val in edits:
        x=copy.deepcopy(p.build());d=x
        for k in path[:-1]:d=d[k]
        d[path[-1]]=val
        try:p.validate(x)
        except AssertionError:n+=1
    assert n==len(edits);print(f"K1225 hostile probes: {n}/{len(edits)}")
if __name__=="__main__":main()
