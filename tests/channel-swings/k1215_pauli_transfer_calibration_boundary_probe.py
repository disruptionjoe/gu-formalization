#!/usr/bin/env python3
from copy import deepcopy
from k1215_pauli_transfer_calibration_boundary import build,validate
def main():
    muts=[("identifiability","one_axis","identifies CHSH"),("identifiability","three_axis_magnitudes","insufficient"),("relation_to_prior","K1004","general law"),("relation_to_prior","delayed_choice_entanglement_swapping","scored confirmation"),("decision","visibility_only_prediction_allowed",True),("decision","calibration_anchor_earns_confirmation",True),("decision","full_transfer_is_gu_derived",True),("release_test","two_axis_residual_retained",False),("release_test","k1009_not_retracted",False),("ownership","gu_native_effect","prediction"),("ownership","prediction_or_confirmation",True)]
    n=0
    for s,k,v in muts:
        x=deepcopy(build());x[s][k]=v
        try:validate(x)
        except AssertionError:n+=1
    assert n==len(muts);print(f"K1215 hostile probes: {n}/{len(muts)}")
if __name__=="__main__":main()
