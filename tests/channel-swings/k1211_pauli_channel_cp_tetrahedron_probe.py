#!/usr/bin/env python3
from copy import deepcopy
from k1211_pauli_channel_cp_tetrahedron import build,validate

def main():
    muts=[("release_test","four_probability_parameterization",False),("release_test","bell_tensor_signed_y",False),("channel","cp_iff","positivity assumed"),("bell_output","correlation_tensor","diag(lambda_x,lambda_y,lambda_z)"),("controls",2,"cp",False),("controls",3,"probabilities",["1","0","0","0"]),("ownership","channel_state_trace_pairing_and_axes_imported",False),("ownership","gu_channel_or_born_rule_constructed",True)]
    caught=0
    for mut in muts:
        x=deepcopy(build())
        if mut[0]=="controls": x["controls"][mut[1]][mut[2]]=mut[3]
        else: x[mut[0]][mut[1]]=mut[2]
        try: validate(x)
        except AssertionError: caught+=1
    assert caught==len(muts);print(f"K1211 hostile probes: {caught}/{len(muts)}")
if __name__=="__main__":main()
