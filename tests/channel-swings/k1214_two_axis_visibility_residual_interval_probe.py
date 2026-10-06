#!/usr/bin/env python3
from copy import deepcopy
from k1214_two_axis_visibility_residual_interval import build,validate
def main():
    muts=[("theorem","third_axis_interval","lambda_z=1"),("theorem","two_axes_generally_sufficient",True),("control","lambda_z_interval",["0","1"]),("control","lower_endpoint_S_squared_over_4","32/25"),("control","upper_endpoint_S_squared_over_4","1"),("decision","third_axis_or_equivalent_calibration_needed",False),("ownership","gu_apparatus_or_prediction",True),("release_test","both_endpoints_cp",False)]
    n=0
    for s,k,v in muts:
        x=deepcopy(build());x[s][k]=v
        try:validate(x)
        except AssertionError:n+=1
    assert n==len(muts);print(f"K1214 hostile probes: {n}/{len(muts)}")
if __name__=="__main__":main()
