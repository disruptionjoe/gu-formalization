#!/usr/bin/env python3
"""Hostile mutations for K1074."""
from copy import deepcopy
from k1074_k1073_multimode_affine_stiffness_law import build, validate


def main():
    mutations=[("law","arbitrary"),("affine_characterization","quadratic"),("two_mode_recovery","u=A1"),("controls.0.recovered_mass_squared","9"),("normalization_boundary","arbitrary scales identify u"),("source_boundary","source owns the Hessian"),("claim_ceiling","all actions"),("target_claim","CONFIRMED")]
    caught=0
    for path,value in mutations:
        data=deepcopy(build()); node=data; parts=path.split(".")
        for part in parts[:-1]: node=node[int(part)] if part.isdigit() else node[part]
        node[parts[-1]]=value
        try: validate(data)
        except AssertionError: caught+=1
    assert caught==len(mutations); print(f"K1074 hostile probes: {caught}/{len(mutations)}")


if __name__=="__main__": main()
