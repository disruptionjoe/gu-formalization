#!/usr/bin/env python3
"""Hostile mutations for K1010."""
from copy import deepcopy
from k1010_k1009_finite_shot_bell_certification import build, validate

def main():
    muts=[
        ("statistical_contract.penalty", "beta=0"), ("statistical_contract.certificate", "S_hat>2"),
        ("exact_example.n_per_correlator", 1710), ("exact_example.total_shots", 6840),
        ("exact_example.penalty_at_n", 1.0), ("exact_example.penalty_at_n_minus_one", 0.0),
        ("systematic_extension", "S_hat>2+beta"), ("unowned_assumptions", []),
        ("ownership.gu_physical_quotient_state_effect_locality_or_detector_constructed", True),
        ("ownership.prediction_or_confirmation", True),
    ]
    caught=0
    for path,value in muts:
        x=deepcopy(build()); cur=x; parts=path.split(".")
        for part in parts[:-1]: cur=cur[part]
        cur[parts[-1]]=value
        try: validate(x)
        except AssertionError: caught+=1
    assert caught==len(muts)
    print(f"K1010 hostile probes: {caught}/{len(muts)}")

if __name__=="__main__": main()
