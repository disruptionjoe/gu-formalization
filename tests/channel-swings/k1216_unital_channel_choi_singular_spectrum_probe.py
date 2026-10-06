#!/usr/bin/env python3
"""Hostile mutations for K1216."""
import copy
import k1216_unital_channel_choi_singular_spectrum as p

def main():
    muts=[]
    for path,value in [
      (("theorem","output_correlation"),"T=M"),(("theorem","gram_identity"),"open"),
      (("release_test","fixed_sign_matrix_orthogonal"),False),(("release_test","all_gram_identities"),False),
      (("ownership","gu_native_effect"),"prediction"),(("release_test","protected_status_unchanged"),False)]:
        x=copy.deepcopy(p.build()); x[path[0]][path[1]]=value; muts.append(x)
    x=copy.deepcopy(p.build()); x["controls"][0]["gram_equal"]=False; muts.append(x)
    x=copy.deepcopy(p.build()); x["controls"].pop(); muts.append(x)
    n=0
    for x in muts:
        try: p.validate(x)
        except AssertionError: n+=1
    assert n==len(muts); print(f"K1216 hostile probes: {n}/{len(muts)}")
if __name__=="__main__": main()
