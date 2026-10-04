#!/usr/bin/env python3
"""Hostile mutations for K1047."""
from copy import deepcopy
from k1047_k1046_joint_ruler_frequency_certificate import build, validate
def main():
    mutations=[("measurement_model","exact"),("ratio_inflation","beta=1"),("separation_condition","always"),("sharp_surface","epsilon<1"),("recovery","none"),("fixture.delta","1"),("fixture.epsilon","1"),("fixture.R","1"),("fixture.beta_squared","2"),("fixture.measured_gap","-1"),("fixture.sharp_epsilon_decimal","0.5"),("systematics_boundary","measured"),("target_claim","CONFIRMED")]
    caught=0
    for path,value in mutations:
        data=deepcopy(build()); node=data; parts=path.split(".")
        for p in parts[:-1]: node=node[p]
        node[parts[-1]]=value
        try: validate(data)
        except AssertionError: caught+=1
    assert caught==len(mutations); print(f"K1047 hostile probes: {caught}/{len(mutations)}")
if __name__=="__main__": main()
