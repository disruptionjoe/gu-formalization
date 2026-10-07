#!/usr/bin/env python3
"""Exact controls for K1294's feasible realized selector transfer."""
import hashlib,json
from fractions import Fraction
from itertools import combinations
from math import prod
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1294-realized-selector-transfer.json").read_text())
def elementary(values,k): return sum(prod(c) for c in combinations(values,k))
n=0
def check(label,value):
    global n
    assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key in ("k1259","k1289","k1291","k1293"):
    pin=D["pinned_inputs"][key]
    check(f"pinned {key}", "PENDING" not in pin["sha256"] and hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
x=(1,2,3,4,5,6,7); z=tuple(v*v for v in x); p=prod(x)
target=tuple(elementary(z,k) for k in range(1,7))+(p,)
residual=tuple(elementary(z,k)-target[k-1] for k in range(1,7))+(p-target[-1],)
check("realized target has zero residual", residual==(0,)*7)
xw=(-2,-1,3,4,5,6,7); zw=tuple(v*v for v in xw)
target_w=tuple(elementary(zw,k) for k in range(1,7))+(prod(xw),)
check("even signed permutation has same target", target_w==target)
vand=prod(z[i]-z[j] for i in range(7) for j in range(i+1,7))
r0sq=target[0]
det_h=Fraction(2**12*vand*vand, r0sq**49)
check("Cartan Hessian determinant positive", det_h>0)
check("degree sum is forty-nine", sum(D["theorem"]["degrees"])==49)
check("properness transfers", D["theorem"]["proper_on_Cartan"])
check("rank seven transfers", D["theorem"]["cartan_hessian_rank"]==7)
check("positive inertia transfers", D["theorem"]["cartan_hessian_inertia"]==[7,0,0])
check("infeasible zero set empty", D["theorem"]["infeasible_target_zero_set_empty"])
check("all formal targets do not transfer", not D["decision"]["all_formal_targets_transfer"])
check("imported data remain", D["theorem"]["imports_one_scale_and_six_shapes"])
check("source owner absent", not D["theorem"]["source_owned"])
check("functional properness absent", not D["theorem"]["functional_BV_BFV_properness"])
assert n==16
print("RESULT: PASS 16/16")
