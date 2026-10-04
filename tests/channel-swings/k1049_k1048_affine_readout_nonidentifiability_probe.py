#!/usr/bin/env python3
"""Hostile mutations for K1049."""
from copy import deepcopy
from k1049_k1048_affine_readout_nonidentifiability import build,validate
def main():
    mutations=[("general_theorem","false"),("horn_map.source","other"),("horn_map.target","other"),("horn_map.gain_exact","0"),("horn_map.offset_exact","0"),("horn_map.gain_decimal","-1"),("horn_map.offset_decimal","100"),("horn_map.residuals.0","1"),("consequence","discriminates"),("reopener","none"),("scope","GU theorem"),("target_claim","CONFIRMED")]
    caught=0
    for path,value in mutations:
        d=deepcopy(build()); n=d; ps=path.split(".")
        for p in ps[:-1]: n=n[int(p)] if isinstance(n,list) else n[p]
        if isinstance(n,list): n[int(ps[-1])]=value
        else: n[ps[-1]]=value
        try: validate(d)
        except AssertionError: caught+=1
    assert caught==len(mutations); print(f"K1049 hostile probes: {caught}/{len(mutations)}")
if __name__=="__main__": main()
