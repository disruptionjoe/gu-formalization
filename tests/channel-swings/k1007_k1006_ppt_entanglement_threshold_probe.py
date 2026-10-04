#!/usr/bin/env python3
"""Hostile mutations for K1007."""
from copy import deepcopy
from k1007_k1006_ppt_entanglement_threshold import build, validate

def main():
    muts=[
        ("partial_transpose_spectrum", ["0"]), ("entanglement.criterion", "p lambda>1"),
        ("entanglement.threshold", "p_E=1"), ("exact_control.threshold_at_lambda", "1/2"),
        ("exact_control.partial_transpose_spectrum", ["1","0","0","0"]),
        ("exact_control.negativity", "0"), ("exact_control.concurrence", "0"),
        ("exact_control.entangled", False), ("ownership.ppt_is_internal_state_classification", False),
        ("ownership.gu_physical_state_selected", True),
    ]
    caught=0
    for path,value in muts:
        x=deepcopy(build()); cur=x; parts=path.split(".")
        for part in parts[:-1]: cur=cur[part]
        cur[parts[-1]]=value
        try: validate(x)
        except AssertionError: caught+=1
    assert caught==len(muts)
    print(f"K1007 hostile probes: {caught}/{len(muts)}")

if __name__=="__main__": main()
