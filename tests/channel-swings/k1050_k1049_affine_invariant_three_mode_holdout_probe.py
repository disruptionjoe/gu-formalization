#!/usr/bin/env python3
"""Hostile mutations for K1050."""
from copy import deepcopy
from k1050_k1049_affine_invariant_three_mode_holdout import build,validate
def main():
    mutations=[("modes.0",0),("statistic","Q"),("affine_invariance","not invariant"),("horns.mass1.D","2"),("horns.mass4.frequencies.0","0"),("horns.mass4.D","1"),("horns.mass4.D_decimal","0"),("separation.exact_gap","0"),("separation.gap_decimal","0"),("separation.proof","none"),("sharp_additive_D_radius","1"),("requirements.0.candidate_grade","pass"),("requirements.1.gu_source_owned",True),("requirements.2.scorable",True),("route_comparison","same"),("score_gate","open"),("source_scope.SC-ACT-01","CONFIRMED"),("ledger_effect","advanced"),("target_claim","CONFIRMED")]
    caught=0
    for path,value in mutations:
        d=deepcopy(build()); n=d; ps=path.split(".")
        for p in ps[:-1]: n=n[int(p)] if isinstance(n,list) else n[p]
        if isinstance(n,list): n[int(ps[-1])]=value
        else: n[ps[-1]]=value
        try: validate(d)
        except AssertionError: caught+=1
    assert caught==len(mutations); print(f"K1050 hostile probes: {caught}/{len(mutations)}")
if __name__=="__main__": main()
