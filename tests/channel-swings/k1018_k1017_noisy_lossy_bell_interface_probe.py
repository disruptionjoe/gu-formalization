#!/usr/bin/env python3
"""Hostile mutations for K1018."""
from copy import deepcopy
from k1018_k1017_noisy_lossy_bell_interface import build, validate
def main():
    muts=[("domain","all reals"),("observed_chsh","S=2sqrt2"),("violation_iff","always"),("frozen_point.ideal_half_chsh","sqrt2"),("frozen_point.equal_efficiency_threshold","2/3"),("frozen_point.threshold",.8),("frozen_point.at_threshold_factor",1.1),("interpretation","loss irrelevant"),("claim_ceiling","GU theorem"),("ownership.gu_state_or_detector_constructed",True),("ownership.empirical_score",True),("target_claim","CONFIRMED")]
    caught=0
    for path,value in muts:
        d=deepcopy(build()); node=d; parts=path.split(".")
        for p in parts[:-1]: node=node[p]
        node[parts[-1]]=value
        try: validate(d)
        except AssertionError: caught+=1
    assert caught==len(muts); print(f"K1018 hostile probes: {caught}/{len(muts)}")
if __name__=="__main__": main()
