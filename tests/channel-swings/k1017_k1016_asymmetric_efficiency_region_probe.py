#!/usr/bin/env python3
"""Hostile mutations for K1017."""
from copy import deepcopy
from k1017_k1016_asymmetric_efficiency_region import build, validate

def main():
    muts=[("model","correlated losses"),("correlator_map","E'=eta E"),("observed_chsh","S=2"),("violation_iff","always"),("symmetric_reduction","eta>2/3"),("symmetric_threshold",.66),("controls.perfect_alice_bob_threshold",.5),("controls.symmetric_boundary_factor",1.1),("controls.perfect",1),("claim_ceiling","universal"),("ownership.loss_independence_derived_from_gu",True),("ownership.apparatus_calibrated",True),("target_claim","CONFIRMED")]
    caught=0
    for path,value in muts:
        d=deepcopy(build()); node=d; parts=path.split(".")
        for p in parts[:-1]: node=node[p]
        node[parts[-1]]=value
        try: validate(d)
        except AssertionError: caught+=1
    assert caught==len(muts); print(f"K1017 hostile probes: {caught}/{len(muts)}")
if __name__=="__main__": main()
