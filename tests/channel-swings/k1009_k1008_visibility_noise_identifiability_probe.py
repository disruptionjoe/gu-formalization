#!/usr/bin/env python3
"""Hostile mutations for K1009."""
from copy import deepcopy
from k1009_k1008_visibility_noise_identifiability import build, validate

def main():
    muts=[
        ("shared_noise_model.visibility", "V=lambda"), ("shared_noise_model.optimized_relation", "S_max^2/4=1+V^2"),
        ("identifiability.visibility_alone_sufficient", True), ("identifiability.additional_calibration", "none"),
        ("same_visibility_controls.0.V", "1/5"), ("same_visibility_controls.1.V", "3/5"),
        ("same_visibility_controls.0.S_max_squared_over_4", "1"), ("same_visibility_controls.0.violates_CHSH", False),
        ("same_visibility_controls.1.S_max_squared_over_4", "1"), ("same_visibility_controls.1.violates_CHSH", True),
        ("ownership.shared_p_across_anchors_is_imported", False), ("ownership.gu_cross_anchor_law_constructed", True),
    ]
    caught=0
    for path,value in muts:
        x=deepcopy(build()); cur=x; parts=path.split(".")
        for part in parts[:-1]: cur=cur[int(part)] if isinstance(cur,list) else cur[part]
        last=parts[-1]
        if isinstance(cur,list): cur[int(last)]=value
        else: cur[last]=value
        try: validate(x)
        except AssertionError: caught+=1
    assert caught==len(muts)
    print(f"K1009 hostile probes: {caught}/{len(muts)}")

if __name__=="__main__": main()
