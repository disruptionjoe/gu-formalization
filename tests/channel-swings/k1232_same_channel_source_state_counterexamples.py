#!/usr/bin/env python3
"""K1232: same channel and marginals do not determine the Bell holdout."""
from fractions import Fraction as F
import json
from pathlib import Path
from k1231_affine_local_channel_two_qubit_law import probabilities
OUT=Path(__file__).parents[2]/"lab/process/k1232-same-channel-source-state-counterexamples.json"

def validate(d):
    M=[[F(3,10),-F(2,5),0],[F(2,13),F(3,26),-F(3,13)],[F(24,65),F(18,65),F(5,52)]]
    t=[0,-F(9,13),F(15,52)];a=[F(3,5),0,F(4,5)];b=[0,F(4,5),F(3,5)];z=[F(0)]*3
    states={"Phi+":[1,-1,1],"Phi-":[-1,1,1],"Psi+":[1,1,-1],"Psi-":[-1,-1,-1],"mixed":[0,0,0]}
    got={}
    for name,s in states.items():
        T=[[F(s[i]) if i==j else F(0) for j in range(3)] for i in range(3)]
        A,B,C,p=probabilities(M,t,z,z,T,a,b); got[name]=(str(C),[str(q) for q in p])
        assert (A,B)==(F(3,13),F(0)) and sum(p)==1 and min(p)>0
    assert got["Phi+"]==(d["controls"]["Phi+"]["correlation"],d["controls"]["Phi+"]["probabilities"])
    assert len({v[0] for v in got.values()})==5
    assert all(d["controls"][k]["local_marginals"]==["0","0"] for k in states)
    assert d["decision"]["same_process_data_and_source_marginals_determine_holdout"] is False
    assert d["decision"]["phi_plus_is_independent_premise"] is True
    assert d["ownership"]["gu_native_effect"]=="none"

if __name__=="__main__":
    d=json.loads(OUT.read_text());validate(d);print("K1232 controls: 11/11")
