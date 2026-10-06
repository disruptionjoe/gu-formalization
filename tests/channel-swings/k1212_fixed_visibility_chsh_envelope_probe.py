#!/usr/bin/env python3
from copy import deepcopy
from k1212_fixed_visibility_chsh_envelope import build,validate
def main():
    muts=[("theorem","range","S=2 sqrt(1+V^2)"),("decision","one_axis_visibility_identifies_optimized_chsh",True),("decision","bounds_are_sharp",False),("decision","every_positive_visibility_forces_violation",True),("release_test","upper_bound_exact",False),("controls",2,"low_S_squared_over_4","29/25"),("controls",2,"high_S_squared_over_4","4/25"),("ownership","gu_prediction",True)]
    n=0
    for m in muts:
        x=deepcopy(build())
        if m[0]=="controls":x["controls"][m[1]][m[2]]=m[3]
        else:x[m[0]][m[1]]=m[2]
        try:validate(x)
        except AssertionError:n+=1
    assert n==len(muts);print(f"K1212 hostile probes: {n}/{len(muts)}")
if __name__=="__main__":main()
