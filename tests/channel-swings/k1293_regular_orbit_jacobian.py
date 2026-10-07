#!/usr/bin/env python3
"""Exact controls for K1293's split-D7 invariant Jacobian."""
import hashlib, json
from fractions import Fraction
from itertools import combinations
from math import prod
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1293-regular-orbit-jacobian.json").read_text())

def elementary(values,k): return sum(prod(c) for c in combinations(values,k))
def determinant(a):
    a=[[Fraction(v) for v in row] for row in a]; out=Fraction(1)
    for i in range(len(a)):
        pivot=next(j for j in range(i,len(a)) if a[j][i])
        if pivot!=i: a[i],a[pivot]=a[pivot],a[i]; out=-out
        p=a[i][i]; out*=p
        for k in range(i,len(a[i])): a[i][k]/=p
        for j in range(i+1,len(a)):
            f=a[j][i]
            for k in range(i,len(a[i])): a[j][k]-=f*a[i][k]
    return out

n=0
def check(label,value):
    global n
    assert value,label; n+=1; print(f"PASS {n:02d}: {label}")

for key in ("k1291","k1292"):
    pin=D["pinned_inputs"][key]
    check(f"pinned {key}", "PENDING" not in pin["sha256"] and hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
x=(1,2,3,4,5,6,7); z=tuple(v*v for v in x)
matrix=[]
for k in range(1,7):
    matrix.append([2*x[i]*elementary(z[:i]+z[i+1:],k-1) for i in range(7)])
matrix.append([prod(x[:i]+x[i+1:]) for i in range(7)])
det=determinant(matrix)
vand=prod(z[i]-z[j] for i in range(7) for j in range(i+1,7))
check("absolute Jacobian formula", abs(det)==2**6*abs(vand))
check("Jacobian square formula", det*det==2**12*vand*vand)
check("regular sample", len(set(z))==7 and det!=0)
x0=(0,1,2,3,4,5,6); z0=tuple(v*v for v in x0)
check("p zero regular witness", prod(x0)==0 and len(set(z0))==7)
check("D7 regularity match", D["theorem"]["matches_D7_regular_semisimple_locus"])
check("connected quotient local diffeomorphism", D["theorem"]["connected_quotient_local_diffeomorphism_on_regular_locus"])
check("outer derivative factor", D["theorem"]["outer_B7_jacobian_relation"].startswith("det d(e1,...,e6,p^2)=2p"))
check("outer quotient branches", D["theorem"]["outer_B7_branches_at_p_zero"])
check("connected quotient does not branch", not D["theorem"]["connected_D7_branches_at_p_zero"])
check("p zero not D7 wall", not D["decision"]["p_zero_is_a_D7_Weyl_wall"])
check("no functional conclusion", not D["decision"]["functional_Fredholm_or_Green_result"])
assert n==13
print("RESULT: PASS 13/13")
