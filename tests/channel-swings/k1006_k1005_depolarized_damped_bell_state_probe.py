#!/usr/bin/env python3
"""Hostile mutations for K1006."""
from copy import deepcopy
from k1006_k1005_depolarized_damped_bell_state import build, validate

def main():
    muts=[
        ("state", "bad"), ("correlation_tensor", "diag(lambda,-lambda,1)"),
        ("exact_control.p", "3/5"), ("exact_control.lambda", "1/5"),
        ("exact_control.spectrum", ["1","0","0","0"]), ("exact_control.trace", "2"),
        ("exact_control.correlation_diagonal", ["0","0","0"]),
        ("ownership.isotropic_contrast_is_repository_selected", False),
        ("ownership.gu_action_or_physical_quotient_constructed", True),
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
    print(f"K1006 hostile probes: {caught}/{len(muts)}")

if __name__=="__main__": main()
