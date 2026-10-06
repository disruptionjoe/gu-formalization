#!/usr/bin/env python3
from copy import deepcopy
from k1213_same_visibility_chsh_separator import build,validate
def main():
    muts=[(None,"same_visibility","1/2"),("low_channel","S_squared_over_4","29/25"),("low_channel","violates_CHSH",True),("high_channel","S_squared_over_4","4/25"),("high_channel","violates_CHSH",False),("decision","visibility_only_bell_inference_valid",True),("decision","k1004_law_is_general_pauli_law",True),("ownership","physical_shared_channel_identified",True)]
    n=0
    for s,k,v in muts:
        x=deepcopy(build())
        if s is None:x[k]=v
        else:x[s][k]=v
        try:validate(x)
        except AssertionError:n+=1
    assert n==len(muts);print(f"K1213 hostile probes: {n}/{len(muts)}")
if __name__=="__main__":main()
