#!/usr/bin/env python3
"""Hostile mutations for K1008."""
from copy import deepcopy
from k1008_k1007_entangled_bell_local_separator import build, validate

def main():
    muts=[
        ("optimized_chsh.formula", "S_max=2sqrt(1+lambda^2)"),
        ("optimized_chsh.violation_iff", "lambda>0"), ("threshold_order.strict_order_for_positive_lambda", "p_B<p_E"),
        ("exact_separator.entanglement_control", "p(1+2lambda)<1"), ("exact_separator.S_max_squared", "4"),
        ("exact_separator.optimized_CHSH_violates", True), ("exact_separator.S_fixed_squared", "4"),
        ("exact_separator.fixed_CHSH_violates", True), ("scope.optimized_chsh_local_only", False),
        ("scope.all_measurement_lhv_model_claimed", True), ("ownership.gu_state_or_measurement_owner_constructed", True),
    ]
    caught=0
    for path,value in muts:
        x=deepcopy(build()); cur=x; parts=path.split(".")
        for part in parts[:-1]: cur=cur[part]
        cur[parts[-1]]=value
        try: validate(x)
        except AssertionError: caught+=1
    assert caught==len(muts)
    print(f"K1008 hostile probes: {caught}/{len(muts)}")

if __name__=="__main__": main()
