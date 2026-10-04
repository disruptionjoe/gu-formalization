#!/usr/bin/env python3
"""Hostile mutations for K1073."""
from copy import deepcopy
from k1073_k1072_pairing_ratio_mass_selector import build, validate


def main():
    mutations=[("positive_solution_cone","S=I"),("selector","u=S_qq"),("uniqueness","many masses"),("scale_invariance","scale matters"),("controls.0.selected_mass_squared","2"),("circularity_guard","candidate pairing selects itself"),("ownership.source_action_pairing_owned",True),("claim_ceiling","GU mass theorem"),("target_claim","CONFIRMED")]
    caught=0
    for path,value in mutations:
        data=deepcopy(build()); node=data; parts=path.split(".")
        for part in parts[:-1]: node=node[int(part)] if part.isdigit() else node[part]
        node[parts[-1]]=value
        try: validate(data)
        except AssertionError: caught+=1
    assert caught==len(mutations); print(f"K1073 hostile probes: {caught}/{len(mutations)}")


if __name__=="__main__": main()
