#!/usr/bin/env python3
"""Hostile mutations for K1048."""
from copy import deepcopy
from k1048_k1047_common_clock_cancellation import build,validate
def main():
    mutations=[("readout_model","y=omega"),("common_gain_theorem","gain required"),("differential_transfer","Q_hat=Q"),("offset_boundary","offset cancels"),("fixture.gain","1"),("fixture.true_Q","1"),("fixture.measured_Q","1"),("ownership_correction","absolute clock required"),("target_claim","CONFIRMED")]
    caught=0
    for path,value in mutations:
        d=deepcopy(build()); n=d; ps=path.split(".")
        for p in ps[:-1]: n=n[p]
        n[ps[-1]]=value
        try: validate(d)
        except AssertionError: caught+=1
    assert caught==len(mutations); print(f"K1048 hostile probes: {caught}/{len(mutations)}")
if __name__=="__main__": main()
